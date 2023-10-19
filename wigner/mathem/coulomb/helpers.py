import numpy


"""
#######################################################################
#                          Code by TheKoke                            #
#           Module that calculates Coulomb Wave Functions             #
#       All math description and explanations of analytical and       #
#        numerical calculations listed in description.txt file        #
#  That helper.py file needed to define Г(x), M(a, b, z), U(a, b, z)  #
#######################################################################
"""


def tricomi_function(a: int, b: int, z: complex) -> complex:
    return kummer_function(a, b, z) * gamma_function(1 - b) / gamma_function(a + 1 - b) + \
           kummer_function(a + 1 - b, 2 - b, z) * gamma_function(b - 1) / gamma_function(a)


def kummer_function(a: int, b: int, z: complex) -> complex:
    result = 1.0

    epsilon = 1e-10
    current = complex(1.0, 0.0)

    n = 1
    while (current * current.conjugate()).real > epsilon:
        constant = rising_factorial(a, n) / (rising_factorial(b, n) * gamma_function(n + 1).real)
        current = constant * (z ** n)

        result += current
        n += 1

    return result


def rising_factorial(a: int, n: int) -> int:
    if n == 0:
        return 1

    return numpy.arange(a, a + n).prod()


def gamma_function(z: complex) -> complex:
    lanczos_parameter = 7
    lanczos_coeffs = [
        0.99999999999980993,
        676.5203681218851,
        -1259.1392167224028,
        771.32342877765313,
        -176.61502916214059,
        12.507343278686905,
        -0.13857109526572012,
        9.9843695780195716e-6,
        1.5056327351493116e-7
    ]

    if z.real < 0.5:
        return numpy.pi / (numpy.sin(numpy.pi * z) * gamma_function(1 - z))  # Reflection formula
    else:
        z -= 1

        x = lanczos_coeffs[0]
        for i in range(1, len(lanczos_coeffs)):
            x += lanczos_coeffs[i] / (z + i)

        sqrt = numpy.sqrt(2 * numpy.pi)
        power = numpy.power(z + lanczos_parameter + 1/2, z + 1/2)
        exp = numpy.exp(-(z + lanczos_parameter + 1/2))

    return sqrt * power * exp * x


if __name__ == '__main__':
    print(kummer_function(-2.5, 1.5, complex(0, 1)))
