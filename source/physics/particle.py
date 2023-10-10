from __future__ import annotations

from abc import ABC, abstractmethod


class Particle(ABC):
    def __init__(self, mass: float, charge: int, spin: float) -> None:
        """
        Particle class: abstract class for inheritance and more exact implementations.

        mass : float
            mass of particle, more correctly rest energy of particle, MeV.

        charge : int
            charge of particle, in units of e, MeV * cm.

        spin : float
            spin of particle.
        """

        self.__mass = mass
        self.__charge = charge
        self.__spin = spin
        self.__energy = 0.0

    @property
    def mass(self) -> float:
        return self.__mass

    @property
    def charge(self) -> int:
        return self.__charge

    @property
    def spin(self) -> float:
        return self.__spin

    @property
    def total_energy(self) -> float:
        return self.__energy

    @abstractmethod
    def accelerate_to_energy(self) -> bool:
        pass


class Photon(Particle):
    def __init__(self, wavelength: float) -> None:
        """
        Class for representation of photon.

        wavelength : float
            wavelength of photon, cm.
        """
        super().__init__(0.0, 0, 1.0)
        self.__lambda = wavelength

    @property
    def wavelength(self) -> float:
        return self.__lambda

    def accelerate_to_energy(self) -> bool:
        pass


class Nuclon(Particle):
    def __init__(self, spin_direction: bool, isospin_z_dir: bool) -> None:
        """
        Class for representation of nuclon.
        Nuclon types: proton and neutron.

        spin_direction : bool
            Nuclon, cause of fermion, has spin = 1/2. Only direction maybe different.

        isospin_z : float
            Projection of isospin to z-axis.
        """
        spin = 1/2 if spin_direction else -1/2
        mass = 938.27 if isospin_z_dir else 939.57
        charge = 1 if isospin_z_dir else 0

        super().__init__(mass, charge, spin)
        self.__isospin_z = 1/2 if isospin_z_dir else -1/2

    @property
    def isospin_z(self) -> float:
        return self.__isospin_z

    def accelerate_to_energy(self) -> bool:
        pass


if __name__ == '__main__':
    pass
