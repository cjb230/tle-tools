import pytest
from tle_tools.keplerian_elements import KeplerianElements

@pytest.fixture
def iss_set():
    return KeplerianElements(semi_major_axis=6.6e6,  eccentricity=0.00050, inclination=51.6431,
                             right_ascension_of_the_ascending_node=0, argument_of_perigee=0, true_anomaly=0)

def test_orbital_period(iss_set):
    result = iss_set.orbital_period()
    expected_value = 5336.241781322555
    assert result == expected_value
