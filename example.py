from pyverse.pipeline import *
from pyverse.core import reprint


funcs = []

@funcs.append
def func(cell, meta):
    print(1)


@funcs.append
def func(cell, meta):
    print(2)


@funcs.append
def func(cell, meta):
    print(3)

#=================================================
@router
def selector(cell, meta):
    if cell["i"] >= len(funcs):
        cell.stop()
        return
    result = funcs[cell["i"]]
    cell["i"] += 1
    return result


@selector.initalizer
def func(cell, meta):
    cell["i"] = 0
#=================================================

box = dcell()
selector.launch(box)