"""
Immutable.

Copyright (c) 2012 Isaac Muse <isaacmuse@gmail.com>
License: MIT
"""


class Immutable(object):
    """Make class immutable."""

    def __init__(self, *args, **kwargs):
        """Initialize."""

        if not hasattr(self, '_immutable'):
            self.__freeze__()

    def __freeze__(self):
        """Freeze the object."""

        super(Immutable, self).__setattr__("_immutable", True)

    def __thaw__(self):
        """Thaw the object."""

        super(Immutable, self).__setattr__("_immutable", False)

    def __setattr__(self, name, value):
        """Prevent set attributes when frozen."""

        if self._immutable:
            raise NotImplementedError
        super(Immutable, self).__setattr__(name, value)

    def __delattr__(self, name):
        """Prevent deleting of attributes when frozen."""

        if self._immutable:
            raise NotImplementedError
        super(Immutable, self).__delattr__(name)

    def __setitem__(self, index, value):
        """Prevent set items when frozen."""

        if self._immutable:
            raise NotImplementedError
        super(Immutable, self).__setitem__(index, value)

    def __delitem__(self, index):
        """Prevent deleting of items when frozen."""

        if self._immutable:
            raise NotImplementedError
        super(Immutable, self).__delitem__(index)


def mutable(fn):
    """Mutable decorator."""

    def thaw(self, *args, **kwargs):
        """Thaw."""

        self.__thaw__()
        obj = fn(self, *args, **kwargs)
        self.__freeze__()
        return obj

    def ensure_frozen(self, *args, **kwargs):
        """Ensure frozen."""

        call = thaw if isinstance(self, Immutable) else fn
        return call(self, *args, **kwargs)

    return ensure_frozen
