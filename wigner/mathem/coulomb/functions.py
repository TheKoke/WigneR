import numpy

from helpers import tricomi_function, kummer_function, gamma_function


"""
#######################################################################
#                          Code by TheKoke                            #
#           Module that calculates Coulomb Wave Functions             #
#       All math description and explanations of analytical and       #
#        numerical calculations listed in description.txt file        #
#######################################################################
"""


class WaveFunction:
    def __init__(self, w: bool, l: int) -> None:
        self.w = w
        self.l = l

    def __call__(self, etha: float, ro: float) -> complex:
        phase_shift = gamma_function(self.l + 1 + complex(0, etha))

        constant = complex(0, -2) if self.w else complex(0, 2)
        constant *= -2 ** self.l
        constant *= numpy.exp(numpy.pi * etha / 2)
        constant *= numpy.exp(complex(0, phase_shift) if self.w else complex(0, -phase_shift))
        constant *= ro ** (self.l + 1)
        constant *= numpy.exp(complex(0, ro) if self.w else complex(0, -ro))

        first_argument = self.l + 1 + complex(complex(0, phase_shift) if self.w else complex(0, -phase_shift))
        second_argument = 2 * self.l + 2
        third_argument = complex(0, -2 * ro) if self.w else complex(0, 2 * ro)

        return constant * tricomi_function(first_argument, second_argument, third_argument)


class Regular:
    def __init__(self, l: int) -> None:
        self.l = l

    def __call__(self, etha: float, ro: float) -> complex:
        h_plus = WaveFunction(w=True, l=self.l)
        h_minus = WaveFunction(w=False, l=self.l)

        return (h_plus(etha, ro) - h_minus) / complex(0, 2)
    

class Irregular:
    def __init__(self, l: int) -> None:
        self.l = l

    def __call__(self, etha: float, ro: float) -> complex:
        h_plus = WaveFunction(w=True, l=self.l)
        h_minus = WaveFunction(W=False, l=self.l)

        return (h_plus + h_minus) / 2


if __name__ == '__main__':
    pass
