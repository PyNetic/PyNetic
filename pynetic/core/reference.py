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


class Reference(Generic[T], object):
    """Wrapper for a Variable
    This is not necessary to use. The suggested way to create a variable is
    using `Context` context manager

    args:
        var (Any): the variable being wrapped
    """

    def __init__(self, name: str, var: T) -> None:
        self._name = name
        self._var = var

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

    def __repr__(self) -> str:
        return f"<Reference({self._name}: {T} = {repr(self._var)})"

    def __str__(self) -> str:
        return str(self._var)


class MakeReference:
    """Context manager used to assign variables to a project"""

    __slots__ = "initial_vars", "vars"

    def __enter__(self):
        self.initial_vars = globals() | locals()

    def __exit__(self) -> None:
        self.vars = {k: v for k, v in globals() | locals() if k not in self.initial_vars}
