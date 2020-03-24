"""This module contains functions implementing the factory method design
patern.
"""
from pygame.image import load
from pygame import error as pg_error

from settings import GRAPH_LIB, IMG_ERROR
from views.view import View


def create_view(map):
    """Create a view object.

    This function is a factory  method: its create a view object depending on
    GRAPH_LIB constant in settings.py.

    Args:
        map: a Map object reprensenting the labyrinth.

    Exceptions:
        ValueError if the value of GRAPH_LIB is not manage

    Returns:
        View object in charge of the display.
    """
    if GRAPH_LIB == "pygame":
        view = View(map)
    else:
        raise ValueError(f'Cannot create a view from {GRAPH_LIB}')

    return view


def create_item_representation(image):
    """Return a representation of an object.

    This function create a representation for the Item object. It's can be a
    image or just a string dépending on the GRAPH_LIB constant in settings.py.

    Args:
        image: String of the image or just a string representing the item

    Exceptions:
        ValueError if the value of GRAPH_LIB is not manage

    Returns:
        A Surface object or a string.
    """

    if GRAPH_LIB == "pygame":
        try:
            representation = load(image).convert()
        except pg_error as err:
            raise FileNotFoundError(IMG_ERROR + err.args[0])
    elif GRAPH_LIB == "text":
        representation = str(image)
    else:
        msg = f'Cannot create a Item representation from {GRAPH_LIB}'
        raise ValueError(msg)

    return representation
