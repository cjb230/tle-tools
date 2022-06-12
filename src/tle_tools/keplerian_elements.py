from math import pi, sqrt
from typing import Union

from tle_tools import constants


class KeplerianElements:
    def __init__(
        self,
        semi_major_axis: float,
        eccentricity: float,
        inclination: float,
        right_ascension_of_the_ascending_node: float,
        argument_of_perigee: float,
        true_anomaly: Union[float, None],
    ) -> None:
        self.semi_major_axis = semi_major_axis
        self.eccentricity = eccentricity
        self.inclination = inclination
        self.raan = right_ascension_of_the_ascending_node
        self.argument_of_perigee = argument_of_perigee
        self.true_anomaly = true_anomaly

    def orbital_period(self) -> float:
        """
        Time to complete one orbit. Depends only on the semi-major axis.

        :return: orbital period in seconds
        """
        return (
            2
            * pi
            * sqrt(
                pow(self.semi_major_axis, 3)
                / constants.earth_standard_gravitational_parameter
            )
        )

    def semi_minor_axis(self) -> float:
        """
        Length of the shorter axis. Depends on the semi-major axis and the eccentricity.

        :return: semi-minor axis length, in metres
        """
        return self.semi_major_axis * sqrt(1 - pow(self.eccentricity, 2))

    def area_within_orbit(self) -> float:
        """
        Area within the orbit.

        A step to calculating the radius vector's "speed".
        Area of ellipse = pi * semi-major axis * semi-minor axis.

        :return: area within the orbit, in square metres.
        """
        return pi * self.semi_major_axis * self.semi_minor_axis()

    def radius_vector_speed(self) -> float:
        """
        Rate at which the radius vector sweeps out area.

        This is a constant, per Kepler 2.

        :return: area sweep rate, in square metres per second
        """
        return self.area_within_orbit() / self.orbital_period()
