"""pynetic utilities module"""

from dataclasses import dataclass
from itertools import count, product
from string import ascii_lowercase, ascii_uppercase
from types import FunctionType
from typing import Any, Callable, Iterable, TypeVar

all_letters = ascii_lowercase + ascii_uppercase

def For(self, each: Iterable, condition: Callable, /, *statements: Any) -> None:
    """Replacement for builtin for loop to use inline with DOM elements
    
    Args:
        each (Iterable): The iterable to loop over
        condition (Callable): The function to use as a condition in the for loop
    
    Usage:
        ```Python
        my_list = ["Button 1", "Button 2", "Button 3"]
        Div(
            For(
                my_list,
                lambda x: x != 2,
                lambda name: Button(name)
            )
                
        )
    """
    self.each = each
    self.condition = condition
    self.statements = statements
        
    

def iter_short_names():
    """Generator over a-z ... A-Z ... aa-ZZ ..."""
    for i in count():
        for s in map("".join, product(all_letters, repeat=i)):
            yield s
