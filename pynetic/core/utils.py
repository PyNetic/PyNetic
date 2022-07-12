"""pynetic utilities module"""

from itertools import count, product
from string import ascii_lowercase, ascii_uppercase

all_letters = ascii_lowercase + ascii_uppercase

def short_names():
    """Generator over a-z ... A-Z ... aa-ZZ ..."""
    for i in count():
        for s in map("".join, product(all_letters, repeat=i)):
            yield s
