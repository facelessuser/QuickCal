"""
Enum.

Copyright (c) 2012 - 2016 Isaac Muse <isaacmuse@gmail.com>
License: MIT
"""
# pylint: disable=protected-access

from collections import namedtuple, OrderedDict
import operator
from .immutable import Immutable

_ENUM_VALUE = 0
_ENUM_SET = 1


def isenumvalue(obj):
    """Check if object is an enum value."""

    return hasattr(obj, "_enumtype") and obj._enumtype == _ENUM_VALUE


def isenumset(obj):
    """Check if object is an enum set."""

    return hasattr(obj, "_enumtype") and obj._enumtype == _ENUM_SET


def _comparator_value(fn):
    """Special method used as a decorator for comparisons of values."""

    def compare(self, other):
        """Compare the values."""

        if isenumvalue(other) and self._enumsetid == other._enumsetid:
            return fn(self.value, other.value)
        return NotImplemented
    return compare


def _comparator_set(fn):
    """Special method used as a decorator for comparisons of sets."""

    def compare(self, other):
        """Compare the sets."""

        if isenumset(other) and self._enumsetid == other._enumsetid:
            return fn(self._enumsetid, other._enumsetid)
        return NotImplemented
    return compare


def _enumvalue_factory(symbol, value, enumset, enumsetid):
    """Create an immutable enum value."""

    classname = "%s.%s" % (enumset, symbol)
    properties = {"_enumset": enumset, "_enumsetid": enumsetid, "_enumtype": _ENUM_VALUE}

    class EnumValue(namedtuple('enumvalue', ("name", "value")), Immutable):
        """EnumValue class."""

        def __str__(self):
            """Convert as a string."""

            return self.name

        def __int__(self):
            """Convert as an int."""

            return self.value

        def __hex__(self):
            """Convert as a hex."""

            return hex(self.value)

        def __oct__(self):
            """Convert as an octal."""

            return oct(self.value)

        def __float__(self):
            """Converted as a float."""

            return float(self.value)

        def __repr__(self):
            """Return a string representation of the class."""

            return "EnumValue: %s(name=%s, value=%d)" % (self.__class__.__name__, self.name, self.value)

        def __hash__(self):
            """Immutable, so we can hash it."""

            return hash((self.name, self.value))

        def _make(self, iterable):
            """Make not implemented."""

            raise NotImplementedError

        def _replace(self, **kwargs):
            """Replace not implemented."""

            raise NotImplementedError

        def __reduce__(self):
            """Reduce for pickling."""

            return (_enumvalue_factory, (self.name, self.value, self._enumset, self._enumsetid))

        @_comparator_value
        def __eq__(self, other):
            """Equal comparison."""

            return self == other

        @_comparator_value
        def __ne__(self, other):
            """Not equal comparison."""

            return self != other

        def __lt__(self, other):
            """Less than comparisons should not be done directly."""

            raise NotImplementedError(
                "Cannot compare enumvalue differences directly!"
                " Use enumvalue.value or int(enumvalue) instead."
            )

        __le__ = __lt__
        __gt__ = __lt__
        __ge__ = __lt__

    return type(classname, (EnumValue,), properties)(symbol, value)


def _enum_factory(symbols, start, name):
    """Generate an enum."""

    properties = {"_enumtype": _ENUM_SET}

    def sequence_enumerate(sequence, start=0):
        """Enumerate the sequence."""

        if isinstance(sequence, dict):
            assert len(sequence) == len(set(sequence.values()))
            for k, v in sorted(sequence.items(), key=operator.itemgetter(1)):
                yield k, v
        else:
            n = start
            for i in sequence:
                yield i, n
                n += 1

    def generate_enums(symbols, start, setname):
        """Construct the actual enum."""

        enums = tuple((k, v) for k, v in sequence_enumerate(symbols, start))
        enumsetid = hash((setname, enums))
        return [_enumvalue_factory(e[0], e[1], setname, enumsetid) for e in enums]

    class EnumSet(namedtuple('enum', symbols), Immutable):
        """EnumSet class."""

        def __reduce__(self):
            """Reduce for when pickling."""

            d = OrderedDict(zip(self._fields, self))
            e = d[self._fields[0]]
            for k, v in d.items():
                d[k] = v.value
            return (_enum_factory, (d, e.value, self._name))

        @property
        def _enumsetid(self):
            """Enum set id property."""

            return self.__hash__()

        @property
        def _name(self):
            """The class name property."""

            return self.__class__.__name__

        def __repr__(self):
            """Representation of the class."""

            d = self._asdict()
            return "EnumSet: %s(%s)" % (self._name, ', '.join("%s=%d" % (k, v) for k, v in d.items()))

        def __call__(self, index):
            """Executed when using the call syntax."""

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
            """Check for if the item contains the index."""

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
            """Hash return."""

            return hash((self.__class__.__name__, tuple(self)))

        @_comparator_set
        def __eq__(self, other):
            """Equal comparison."""

            return self == other

        @_comparator_set
        def __ne__(self, other):
            """Not equal comparison."""

            return self != other

        def __lt__(self, other):
            """Comparison for less than are not implemented."""

            raise NotImplementedError

        __le__ = __lt__
        __gt__ = __lt__
        __ge__ = __lt__

    return type(name, (EnumSet,), properties)(*generate_enums(symbols, start, name))


def enum(sequence, **kwargs):
    """Creat an enum."""

    symbols = sequence.split() if isinstance(sequence, str) else sequence
    start = int(kwargs.get("start", 0))
    name = str(kwargs.get("name", "enum"))
    if start < 0:
        start = 0
    return _enum_factory(symbols, start, name)
