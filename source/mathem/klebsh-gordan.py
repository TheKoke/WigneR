import math


class KlebschGordan:

    @staticmethod
    def coefficient(j1: int, m1: int, j2: int, m2: int, J: int, M: int) -> float:
        KlebschGordan.__handle_incorrect(j1, m1, j2, m2, J, M)

        if abs(j1 - j2) > J or j1 + j2 < J:
            return 0.0

        if m1 + m2 != M:
            return 0.0

        return 0.0

    @staticmethod
    def __handle_incorrect(j1: int, m1: int, j2: int, m2: int, J: int, M: int) -> None:
        if j1 % 1 != 0 or j2 % 1 != 0 or J % 1 != 0:
            raise ValueError('Total momentum must be integer number.')

        if j1 < 0 or j2 < 0 or J < 0:
            raise ValueError('Momentum cant be negative.')

        if abs(m1) % 1 != 0 or abs(m2) % 1 != 0 or abs(M) % 1 != 0 or \
                abs(m1) % 1 != 0.5 or abs(m2) % 1 != 0.5 or abs(M) % 1 != 0.5:
            raise ValueError('Projection of momentum must be integer or half-integer.')

        if abs(m1) > j1 or abs(m2) > j2 or abs(M) > J:
            raise ValueError('Projection of momentum cant be greater than momentum')

        if (j1 + m1) % 1 != 0 or (j1 + m1) % 1 < 0:
            raise ValueError('Value of j1 + m1 must be non-negative integer.')

        if (j2 + m2) % 1 != 0 or (j2 + m2) % 1 < 0:
            raise ValueError('Value of j2 + m2 must be non-negative integer.')

        if (J + M) % 1 != 0 or (J + M) % 1 < 0:
            raise ValueError('Value of J + M must be non-negative integer.')

        if (j1 + j2 + J) % 1 != 0 or (j1 + j2 + J) % 1 < 0:
            raise ValueError('Value of j1 + j2 + J must be non-negative integer.')

    @staticmethod
    def wigner_3j_symbol(j1: int, m1: int, j2: int, m2: int, j3: int, m3: int) -> float:
        sign = (-1) ** (j3 + m3 + 2*j1)
        sqrt = 1 / (2*j3 + 1) ** (1/2)

        return sign * sqrt * KlebschGordan.coefficient(j1, -m1, j2, -m2, j3, m3)

    @staticmethod
    def delta_symbol(a: int, b: int, c: int) -> float:
        helper = [a, b, c]

        delta = 1
        for i in helper:
            delta *= math.factorial(sum(helper) - 2*i)

        return math.pow(delta / math.factorial(sum(helper) + 1), 1/2)

    @staticmethod
    def kronecker(i: float, j: float) -> float:
        if i == j:
            return 1.0

        return 0.0


if __name__ == '__main__':
    pass
