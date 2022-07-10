"""Variables (similar to state's in react) 

Automatically bound to the session. They are bound using `Context` context-manager:

```Python
with Context():
    username: str = "John"
    today: datetime.date = datetime.now()
    age: int = 32
```

Variables must have distinct names from any other name in the project as they are
assigned the name they are given on instantiation

Variables be accessed at any time during the session and
from any page component using import statements
"""


class Variable(type):
    pass


class Context:
    """Context manager used to assign variables to a project"""

    __slots__ = "initial_vars", "vars"

    def __enter__(self):
        self.initial_vars = globals() | locals()

    def __exit__(self) -> None:
        self.vars = {k: v for k, v in globals() | locals() if k not in self.initial_vars}
