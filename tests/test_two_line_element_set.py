import pytest

from tle_tools.two_line_element_set import TwoLineElementSet


@pytest.fixture
def iss_tle() -> TwoLineElementSet:
    """
    Took this from https://live.ariss.org/tle/
    ISS (ZARYA)
    1 25544U 98067A   22155.44817811  .00008247  00000-0  15303-3 0  9995
    2 25544  51.6451  39.6852 0004682 193.2393 341.0291 15.49862837343202
    """
    return TwoLineElementSet(
        satellite_name="ISS (ZARYA)",
        satellite_catalog_number=25544,
        classification="U",
        launch_year=98,
        year_launch_number=67,
        launch_piece="A",
        epoch_year=8,
        epoch_day=155.44817811,
        mean_motion_first_derivative=0.00008247,
        mean_motion_second_derivative=0.15303,
        b_star=0,
        ephemeris_type=0,
        element_set_number=9995,
        inclination=51.6451,
        right_ascension_of_the_ascending_node=39.6852,
        eccentricity=0.0004682,
        argument_of_perigee=193.2393,
        mean_anomaly=341.0291,
        mean_motion=15.49862837,
        revolution_number_at_epoch=343202,
    )


def test_keplerian_elements(iss_tle):
    result = iss_tle.keplerian_elements()
    assert result.semi_major_axis == 6795174.095898508
    assert result.eccentricity == 0.0004682
    assert result.inclination == 51.6451
    assert result.raan == 39.6852
    assert result.argument_of_perigee == 193.2393
    assert result.true_anomaly == -1
