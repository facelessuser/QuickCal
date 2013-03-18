"""
Enum

Copyright (c) 2012 Isaac Muse <isaacmuse@gmail.com>
License: MIT
"""

from collections import namedtuple
import operator
from .immutable import Immutable

_ENUM_VALUE = 0
_ENUM_SET = 1


def isenumvalue(obj):
    return hasattr(obj, "_enumtype") and obj._enumtype == _ENUM_VALUE


def isenumset(obj):
    return hasattr(obj, "_enumtype") and obj._enumtype == _ENUM_SET


def _comparator_value(fn):
    def compare(self, other):
        if isenumvalue(other) and self._enumsetid == other._enumsetid:
            return fn(self.value, other.value)
        return NotImplemented
    return compare


def _comparator_set(fn):
    def compare(self, other):
        if isenumset(other) and self._enumsetid == other._enumsetid:
            return fn(self._enumsetid, other._enumsetid)
        return NotImplemented
    return compare


def _enumvalue_factory(symbol, value, enumset, enumsetid):
    classname = "%s.%s" % (enumset, symbol)
    properties = {"_enumset": enumset, "_enumsetid": enumsetid, "_enumtype": _ENUM_VALUE}

    class EnumValue(namedtuple('enumvalue', ("name", "value")), Immutable):
        def __str__(self):
            return self.name

        def __int__(self):
            return self.value

        def __hex__(self):
            return hex(self.value)

        def __oct__(self):
            return oct(self.value)

        def __float__(self):
            return float(self.value)

        def __repr__(self):
            return "EnumValue: %s(name=%s, value=%d)" % (self.__class__.__name__, self.name, self.value)

        def __hash__(self):
            return hash((self.name, self.value))

        def _make(self, iterable):
            raise NotImplementedError

        def _replace(self, **kwargs):
            raise NotImplementedError

        def __reduce__(self):
            return (_enumvalue_factory, (self.name, self.value, self._enumset, self._enumsetid))

        @_comparator_value
        def __eq__(self, other):
            return self == other

        @_comparator_value
        def __ne__(self, other):
            return self != other

        def __lt__(self, other):
            raise NotImplementedError("Cannot compare enumvalue differences directly! use enumvalue.value or int(enumvalue) instead.")

        __le__ = __lt__
        __gt__ = __lt__
        __ge__ = __lt__

    return type(classname, (EnumValue,), properties)(symbol, value)


def _enum_factory(symbols, start, name):
    properties = {"_enumtype": _ENUM_SET}

    def sequence_enumerate(sequence, start=0):
        if isinstance(sequence, dict):
            assert len(sequence) == len(set(sequence.values()))
            for k, v in sorted(sequence.iteritems(), key=operator.itemgetter(1)):
                yield k, v
        else:
            n = start
            for i in sequence:
                yield i, n
                n += 1

    def generate_enums(symbols, start, setname):
        enums = tuple((k, v) for k, v in sequence_enumerate(symbols, start))
        enumsetid = hash((setname, enums))
        return [_enumvalue_factory(e[0], e[1], setname, enumsetid) for e in enums]

    class EnumSet(namedtuple('enum', symbols), Immutable):
        def __reduce__(self):
            d = self._asdict()
            e = d[self._fields[0]]
            for k, v in d.items():
                d[k] = v.value
            return (_enum_factory, (d, e.value, self._name))

        @property
        def _enumsetid(self):
            return self.__hash__()

        @property
        def _name(self):
            return self.__class__.__name__

        def __repr__(self):
            d = self._asdict()
            return "EnumSet: %s(%s)" % (self._name, ', '.join("%s=%d" % (k, v) for k, v in d.items()))

        def __call__(self, index):
            item = None
            compare_idx = 1
            value = index

            if isenumvalue(index):
                value = index.value
            elif isinstance(index, str):
                compare_idx = 0
            elif not isinstance(index, int):
                raise TypeError("An enum set can only translate types(int, str, EnumValue)!")

            for i in self.__iter__():
                if i[compare_idx] == value:
                    item = i
                    break

            return item

        def __contains__(self, index):
            item = None
            if isenumvalue(index):
                for i in self.__iter__():
                    if i is index:
                        item = i
                        break
            else:
                item = self.__call__(index)
            return item is not None

        def __hash__(self):
            return hash(tuple(self))

        @_comparator_set
        def __eq__(self, other):
            return self == other

        @_comparator_set
        def __ne__(self, other):
            return self != other

        def __lt__(self, other):
            raise NotImplementedError

        __le__ = __lt__
        __gt__ = __lt__
        __ge__ = __lt__

    return type(name, (EnumSet,), properties)(*generate_enums(symbols, start, name))


def enum(sequence, **kwargs):
    symbols = sequence.split() if isinstance(sequence, str) else sequence
    start = int(kwargs.get("start", 0))
    name = str(kwargs.get("name", "enum"))
    if start < 0:
        start = 0
    return _enum_factory(symbols, start, name)
