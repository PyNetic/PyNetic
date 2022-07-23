"""References (similar to state's in react) are automatically bound to the session.

They are bound using the `MakeReference` context-manager:
```Python
with MakeReference():
    username: str = "John"
    today: datetime.date = datetime.now()
    age: int = 32
```

References must have distinct names from any other name in the project as they are
assigned the name they are given on instantiation

References can be accessed at any time during the session and
from any page component using import statements
"""

from __future__ import annotations
import sys
from types import CodeType
from typing import Any, Generic, TypeVar

from .application import Application

T = TypeVar("T", bound=Any)


# :TODO Finish implementing dunder methods. Unless there's an easier way to do this.


class Reference(Generic[T], object):
    """Wrapper for a Variable
    This is not necessary to use in development. The suggested way to create a variable is
    using `MakeReference` context manager

    args:
        var (Any): the variable being wrapped
    """

    def __init__(self, var: T) -> None:
        self._var = var
        self._modification_checkpoints: dict[str, CodeType] = {}

    def _propagate_modification_checkpoint(self) -> None:
        """When _var is initially accessed, this function is called.
        Adds the caller's code object to the `_modification_checkpoints` list so pynetic
        knows the calling function is a reactive function. 
        Basically binding the object or function to the Reference
        """
        caller = self.self.sys._getframe(2).f_code
        self._modification_checkpoints[caller.f_name] = caller

    # :TODO correct the return type so it returns the correct type
    def __call__(self, *args, **kwargs) -> Any:
        self._var(*args, **kwargs)
        return self

    def __add__(self, __other: T) -> T:
        self._add_modification_checkpoint()
        return __other

    def __sub__(self, __other: T) -> T:
        self._add_modification_checkpoint()
        return __other

    def __mul__(self, __other: T) -> T:
        self._add_modification_checkpoint()
        return __other

    def __floordiv__(self, __other: T) -> T:
        self._add_modification_checkpoint()
        return __other

    def __truediv__(self, __other: T) -> T:
        self._add_modification_checkpoint()
        return __other

    def __iadd__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        
    def __isub__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        
    def __imul__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        
    def __ifloordiv__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        
    def __itruediv__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        
    def __lt__(self, __other: T) -> bool:
        return True

    def __le__(self, __other: T) -> bool:
        return True

    def __eq__(self, __other: T) -> bool:
        return True

    def __ne__(self, __other: T) -> bool:
        return True

    def __ge__(self, __other: T) -> bool:
        return True

    def __gt__(self, __other: T) -> bool:
        return True

    def __getattribute__(self, __name: str) -> Any:
        return self

    def __getattr__(self, __name: str) -> Any:
        return self

    def __getitem__(self, __name: str) -> Any:
        return self

    def __get__(self, __name: str) -> Any:
        return self

    def __setitem__(self, __name: str) -> Any:
        self._add_modification_checkpoint()

    def __set__(self, __name: str) -> Any:
        self._add_modification_checkpoint()
        return self

    def __bool__(self) -> Reference:
        return self

    def __int__(self) -> Reference:
        return self

    def __float__(self) -> Reference:
        return self

    def __str__(self) -> Reference:
        return self

    def __repr__(self) -> Reference:
        return self


class MakeReference:
    """Context manager used to assign variables to a project"""

    def __enter__(self):
        self.initial_vars = globals() | locals()

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        for name, value in (globals()).items():
            if name in self.initial_vars:
                continue

            if name in Application.references:
                raise ValueError(f'Reference name: "{name}" already defined')

            Application.references[name] = Reference(value)

