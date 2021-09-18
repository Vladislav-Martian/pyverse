__all__ = ["iterable", "nextable", "forable"]

from typing import overload


def instanceof(obj, *clss):
    "Clone of isinstance() default function, but with inline notation"
    return isinstance(obj, tuple(clss))


def iterable(elem):
    """
    Returns True if element is iterable and vice-versa
    """
    try:
        iter(elem)
    except:
        return False
    else:
        return True


def nextable(elem):
    """
    Returns True if element is iterable and vice-versa
    """
    try:
        next(elem)
    except:
        return False
    else:
        return True


def forable(elem):
    """
    Returns True if element is able to use in for..in and vice-versa
    """
    try:
        x = iter(elem)
        next(x)
    except:
        return False
    else:
        return True


def withable(elem):
    """
    Returns True if element is able to use <with elem as var:> and vice-versa
    """
    return hasattr(elem, "__enter__") and hasattr(elem, "__exit__")


def awithable(elem):
    """
    Returns True if element is able to use <async with elem as var:> and vice-versa
    """
    return hasattr(elem, "__aenter__") and hasattr(elem, "__aexit__")
