from abc import ABC, abstractmethod

import numpy as np


class Initializer(ABC):
    @abstractmethod
    def new_matrix(self, shape):
        pass


class Zeros(Initializer):
    def new_matrix(self, shape):
        return np.zeros(shape, dtype=float)


class CenteredNormal(Initializer):
    def __init__(self, std):
        self.std = std

    def new_matrix(self, shape):
        return np.random.normal(0, self.std, shape)


class PositiveNormal(CenteredNormal):
    def new_matrix(self, shape):
        return np.abs(super().new_matrix(shape))


class Xavier(Initializer):
    def new_matrix(self, shape):
        # standard dev = sqrt (1/(input size + output size))
        var = 2 / (shape[0] + shape[1])
        return np.random.normal(0, np.sqrt(var), shape)


class PositiveXavier(Xavier):
    def new_matrix(self, shape):
        return np.abs(super().new_matrix(shape))


if __name__ == '__main__':
    print(Zeros().new_matrix((2, 4)))
    print(CenteredNormal(1).new_matrix((2, 4)))
    print(PositiveNormal(2).new_matrix((2, 4)))
    print(Xavier().new_matrix((2, 4)))
    print(PositiveXavier().new_matrix((2, 4)))
