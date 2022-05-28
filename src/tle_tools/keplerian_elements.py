from math import pi, sqrt

from tle_tools import constants


class KeplerianElements:
    def __init__(
        self,
        semi_major_axis: int,
        eccentricity: float,
        inclination,
        right_ascension_of_the_ascending_node,
        argument_of_perigee,
        true_anomaly,
    ):
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
