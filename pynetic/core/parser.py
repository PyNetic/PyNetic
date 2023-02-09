from ast import parse as ast_parse


def parse(filename: str) -> None:
    with open(filename) as of:
        tree = ast_parse(of.read())
