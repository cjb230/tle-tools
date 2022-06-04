from math import pi

from tle_tools.keplerian_elements import KeplerianElements
from tle_tools import constants


class TwoLineElementSet:
    def __init__(
        self,
        satellite_name,
        satellite_catalog_number,
        classification,
        launch_year,
        year_launch_number,
        launch_piece,
        epoch_year,
        epoch_day,
        mean_motion_first_derivative,
        mean_motion_second_derivative,
        b_star,
        ephemeris_type,
        element_set_number,
        inclination,
        right_ascension_of_the_ascending_node,
        eccentricity,
        argument_of_perigee,
        mean_anomaly,
        mean_motion,
        revolution_number_at_epoch,
        checksum_l1=None,
        checksum_l2=None,
    ):
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
        return pow(
            (t * t * constants.earth_standard_gravitational_parameter) / (4 * pi * pi),
            (1 / 3),
        )

    def keplerian_elements(self) -> KeplerianElements:
        """
        Keplerian elements for this TLE

        NB Anomaly is not calculated!

        :return: KeplerianElements (tle_tools.keplerian_elements)
        """
        true_anomaly = -1
        result = KeplerianElements(
            semi_major_axis=self.semi_major_axis(),
            eccentricity=self.eccentricity,
            inclination=self.inclination,
            right_ascension_of_the_ascending_node=self.right_ascension_of_the_ascending_node,
            argument_of_perigee=self.argument_of_perigee,
            true_anomaly=true_anomaly,
        )
        return result
