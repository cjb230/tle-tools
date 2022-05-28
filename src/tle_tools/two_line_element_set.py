from collections import namedtuple


class TwoLineElementSet:
    def __init__(self, satellite_name, satellite_catalog_number, classification, launch_year, year_launch_number,
                 launch_piece, epoch_year, epoch_day, mean_motion_first_derivative, mean_motion_second_derivative,
                 b_star, ephemeris_type, element_set_number, checksum_l1, inclination,
                 right_ascension_of_the_ascending_node, eccentricity, argument_of_perigee, mean_anomaly, mean_motion,
                 revolution_number_at_epoch, checksum_l2):
        self.satellite_name = satellite_name
        self.satellite_catalog_number = satellite_catalog_number
