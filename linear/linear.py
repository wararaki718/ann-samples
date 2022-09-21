from typing import Tuple

import numpy as np


class Linear:
    def add(self, x: np.ndarray):
        self._x = x
    
    def search(self, query: np.ndarray, k: int=5) -> Tuple[np.ndarray, np.ndarray]:
        distances = np.linalg.norm(self._x - query, axis=1)
        indices = np.argsort(distances)[:k]
        return indices, distances[indices]
