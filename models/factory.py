"""This module contains functions implementing the factory methods design 
partern.
"""

from settings import GRAPH_LIB
from .views import View

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