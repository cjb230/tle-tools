from math import pi

from tle_tools import constants
from tle_tools.keplerian_elements import KeplerianElements


class TwoLineElementSet:
    def __init__(
        self,
        satellite_name: str,
        satellite_catalog_number: int,
        classification: str,
        launch_year: int,
        year_launch_number: int,
        launch_piece: str,
        epoch_year: int,
        epoch_day: float,
        mean_motion_first_derivative: float,
        mean_motion_second_derivative: float,
        b_star: float,
        ephemeris_type: int,
        element_set_number: int,
        inclination: float,
        right_ascension_of_the_ascending_node: float,
        eccentricity: float,
        argument_of_perigee: float,
        mean_anomaly: float,
        mean_motion: float,
        revolution_number_at_epoch: int,
        checksum_l1: int = None,
        checksum_l2: int = None,
    ) -> None:
        assert mean_motion > 0
        self.satellite_name = satellite_name
        self.satellite_catalog_number = satellite_catalog_number
        self.classification = classification
        self.launch_year = launch_year
        self.year_launch_number = year_launch_number
        self.launch_piece = launch_piece
        self.epoch_year = epoch_year
        self.epoch_day = epoch_day
        self.mean_motion_first_derivative = mean_motion_first_derivative
        self.mean_motion_second_derivative = mean_motion_second_derivative
        self.b_star = b_star
        self.ephemeris_type = ephemeris_type
        self.element_set_number = element_set_number
        self.checksum_l1 = checksum_l1
        self.inclination = inclination
        self.right_ascension_of_the_ascending_node = (
            right_ascension_of_the_ascending_node
        )
        self.eccentricity = eccentricity
        self.argument_of_perigee = argument_of_perigee
        self.mean_anomaly = mean_anomaly
        self.mean_motion = mean_motion
        self.revolution_number_at_epoch = revolution_number_at_epoch
        self.checksum_l2 = checksum_l2

    def orbital_period(self) -> float:
        """
         Duration of one orbit. Calculated from the mean motion.

        :return: Duration of one orbit, in seconds
        """
        return 86400 / self.mean_motion

    def semi_major_axis(self) -> float:
        """
        Length of the semi-major axis. Calculated from the mean motion.

        :return: semi-major axis length in metres
        """
        t = self.orbital_period()
        return float(
            pow(
                (t * t * constants.earth_standard_gravitational_parameter)
                / (4 * pi * pi),
                (1 / 3),
            )
        )

    def keplerian_elements(self) -> KeplerianElements:
        """
        Keplerian elements for this TLE

        NB Anomaly is not calculated!

        :return: KeplerianElements (tle_tools.keplerian_elements)
        """
        result = KeplerianElements(
            semi_major_axis=self.semi_major_axis(),
            eccentricity=self.eccentricity,
            inclination=self.inclination,
            right_ascension_of_the_ascending_node=self.right_ascension_of_the_ascending_node,
            argument_of_perigee=self.argument_of_perigee,
            true_anomaly=None,
        )
        return result
