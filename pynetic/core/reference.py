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


from typing import Any, Generic, TypeVar, ParamSpec, TypeVar

T = TypeVar("T", bound=Any)
R = TypeVar("R")


# :TODO: Finish implementing dunder methods. Unless there's an easier way to do this.
class Reference(Generic[T], object):
    """Wrapper for a Variable
    This is not necessary to use. The suggested way to create a variable is
    using `Context` context manager

    args:
        var (Any): the variable being wrapped
    """

    def __init__(self, var: T) -> None:
        self._var = var

    # :TODO: correct the return type so it returns the correct type
    def __call__(self, *args, **kwargs) -> Any:
        self._var(*args, **kwargs)
        return self._var

    def __add__(self, __other: T) -> None:
        return self._var + __other

    def __sub__(self, __other: T) -> None:
        return self._var - __other

    def __mul__(self, __other: T) -> None:
        return self._var * __other

    def __floordiv__(self, __other: T) -> None:
        return self._var // __other

    def __truediv__(self, __other: T) -> None:
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

    # :TODO: correct the return type so it returns the correct type
    def __getattribute__(self, __name: str) -> Any:
        return self._var.__getattribute__(__name)

    # :TODO: correct the return type so it returns the correct type
    def __getattr__(self, __name: str) -> Any:
        return self._var.__getattr__(__name)

    # :TODO: correct the return type so it returns the correct type
    def __getitem__(self, __name: str) -> Any:
        return self._var.__getitem__(__name)

    # :TODO: correct the return type so it returns the correct type
    def __get__(self, __name: str) -> Any:
        return self._var.__get__(__name)

    # :TODO: correct the return type so it returns the correct type
    def __setitem__(self, __name: str) -> Any:
        return self._var.__setitem__(__name)

    # :TODO: correct the return type so it returns the correct type
    def __set__(self, __name: str) -> Any:
        return self._var.__set__(__name)

    # :TODO: correct the return type so it returns the correct type
    def __delitem__(self, __name: str) -> Any:
        return self._var.__delitem__(__name)

    def __del__(self, __name: str) -> None:
        del self

    def __bool__(self) -> bool:
        return bool(self._var)

    def __repr__(self) -> str:
        return f"<Reference({self._name}: {self.__orig_class__.__args__[0]} = {repr(self._var)})"  # type: ignore

    def __str__(self) -> str:
        return str(self._var)


class MakeReference:
    """Context manager used to assign variables to a project"""

    def __enter__(self):
        self.initial_vars = globals() | locals()

    def __exit__(self, exception_type, exception_value, exception_traceback) -> None:
        for k, v in (globals()).items():
            if k not in self.initial_vars:
                # Add variable to Application
                pass
