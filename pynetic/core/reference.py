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
        return self._var

    def __add__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var + __other

    def __sub__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var - __other

    def __mul__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var * __other

    def __floordiv__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var // __other

    def __truediv__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var / __other

    def __iadd__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var + __other

    def __isub__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var - __other

    def __imul__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var * __other

    def __ifloordiv__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var // __other

    def __itruediv__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var / __other

    def __lt__(self, __other: T) -> bool:
        return self._var < __other

    def __le__(self, __other: T) -> bool:
        return self._var <= __other

    def __eq__(self, __other: T) -> bool:
        return self._var == __other

    def __ne__(self, __other: T) -> bool:
        return self._var != __other

    def __ge__(self, __other: T) -> bool:
        return self._var >= __other

    def __gt__(self, __other: T) -> bool:
        return self._var > __other

    # :TODO correct the return type so it returns the correct type
    def __getattribute__(self, __name: str) -> Any:
        return self._var.__getattribute__(__name)

    # :TODO correct the return type so it returns the correct type
    def __getattr__(self, __name: str) -> Any:
        return self._var.__getattr__(__name)

    # :TODO correct the return type so it returns the correct type
    def __getitem__(self, __name: str) -> Any:
        return self._var.__getitem__(__name)

    # :TODO correct the return type so it returns the correct type
    def __get__(self, __name: str) -> Any:
        return self._var.__get__(__name)

    # :TODO correct the return type so it returns the correct type
    def __setitem__(self, __name: str) -> Any:
        self._add_modification_checkpoint()
        return self._var.__setitem__(__name)

    # :TODO correct the return type so it returns the correct type
    def __set__(self, __name: str) -> Any:
        self._add_modification_checkpoint()
        return self._var.__set__(__name)

    def __bool__(self) -> bool:
        return bool(self._var)

    def __int__(self) -> str:
        return str(self._var)

    def __float__(self) -> str:
        return str(self._var)

    def __str__(self) -> str:
        return str(self._var)

    def __repr__(self) -> str:
        return f"<Reference({self._name}: {repr(self._var)})"  # type: ignore


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


reference_bundled = """class Reference(Generic[T], object):
    def __init__(self, var: T) -> None:
        self._var = var
        self._modification_checkpoints: dict[str, CodeType] = {}

    def _propagate_modification_checkpoint(self) -> None:
        """When _var is modified, this function is called.
        Adds the caller's code object to the `_modification_checkpoints` list so pynetic
        knows the calling function is a reactive function.
        """
        caller = self.self.sys._getframe(2).f_code
        self._modification_checkpoints[caller.f_name] = caller

    # :TODO correct the return type so it returns the correct type
    def __call__(self, *args, **kwargs) -> Any:
        self._var(*args, **kwargs)
        return self._var

    def __add__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var + __other

    def __sub__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var - __other

    def __mul__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var * __other

    def __floordiv__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var // __other

    def __truediv__(self, __other: T) -> None:
        self._add_modification_checkpoint()
        return self._var / __other

    def __iadd__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var + __other

    def __isub__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var - __other

    def __imul__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var * __other

    def __ifloordiv__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var // __other

    def __itruediv__(self, __other: T) -> "Reference":
        self._add_modification_checkpoint()
        return self._var / __other

    def __lt__(self, __other: T) -> bool:
        return self._var < __other

    def __le__(self, __other: T) -> bool:
        return self._var <= __other

    def __eq__(self, __other: T) -> bool:
        return self._var == __other

    def __ne__(self, __other: T) -> bool:
        return self._var != __other

    def __ge__(self, __other: T) -> bool:
        return self._var >= __other

    def __gt__(self, __other: T) -> bool:
        return self._var > __other

    # :TODO correct the return type so it returns the correct type
    def __getattribute__(self, __name: str) -> Any:
        return self._var.__getattribute__(__name)

    # :TODO correct the return type so it returns the correct type
    def __getattr__(self, __name: str) -> Any:
        return self._var.__getattr__(__name)

    # :TODO correct the return type so it returns the correct type
    def __getitem__(self, __name: str) -> Any:
        return self._var.__getitem__(__name)

    # :TODO correct the return type so it returns the correct type
    def __get__(self, __name: str) -> Any:
        return self._var.__get__(__name)

    # :TODO correct the return type so it returns the correct type
    def __setitem__(self, __name: str) -> Any:
        self._add_modification_checkpoint()
        return self._var.__setitem__(__name)

    # :TODO correct the return type so it returns the correct type
    def __set__(self, __name: str) -> Any:
        self._add_modification_checkpoint()
        return self._var.__set__(__name)

    def __bool__(self) -> bool:
        return bool(self._var)

    def __int__(self) -> str:
        return str(self._var)

    def __float__(self) -> str:
        return str(self._var)

    def __str__(self) -> str:
        return str(self._var)

    def __repr__(self) -> str:
        return f"<Reference({self._name}: {repr(self._var)})"  # type: ignore"""