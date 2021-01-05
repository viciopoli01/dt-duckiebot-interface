import time
import dataclasses
import numpy as np

from .roi import DisplayROI


@dataclasses.dataclass
class DisplayFragment:
    data: np.ndarray
    roi: DisplayROI
    screen: int
    z: int
    _time: float
    _ttl: int

    def ttl(self):
        if self._ttl < 0:
            # infinite ttl
            return 1
        elapsed = time.time() - self._time
        ttl = self._ttl - elapsed
        return ttl
