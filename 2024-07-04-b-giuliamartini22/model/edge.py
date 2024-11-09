from dataclasses import dataclass

from model.sighting import Sighting
from model.state import State


@dataclass
class Edge:
    s1: int
    s2: int