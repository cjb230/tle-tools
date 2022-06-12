"""All pytest tests for tle_tools.keplerian_elements."""
import pytest

from tle_tools.keplerian_elements import KeplerianElements


@pytest.fixture
def iss_set() -> KeplerianElements:
    """Example elements for the ISS. Outdated when you read this."""
    return KeplerianElements(
        semi_major_axis=6_600_000,
        eccentricity=0.00050,
        inclination=51.6431,
        right_ascension_of_the_ascending_node=0,
        argument_of_perigee=0,
        true_anomaly=0,
    )


@pytest.fixture
def molniya_set() -> KeplerianElements:
    """Example elements for a Molniya orbit.

    See https://en.wikipedia.org/wiki/Molniya_orbit#Properties
    """
    return KeplerianElements(
        semi_major_axis=26_600_000,
        eccentricity=0.74,
        inclination=63.4,
        right_ascension_of_the_ascending_node=0,
        argument_of_perigee=270,
        true_anomaly=0,
    )


def test_orbital_period(
    iss_set: KeplerianElements, molniya_set: KeplerianElements
) -> None:
    """Orbital period is calculated from semi-major axis."""
    result = iss_set.orbital_period()
    expected_value = 5336.241781322555
    assert result == expected_value, "Bad orbital period for ISS orbit"
    result = molniya_set.orbital_period()
    expected_value = 43175.96475741748
    assert result == expected_value, "Bad orbital period for Molniya orbit"


def test_semi_minor_axis(
    iss_set: KeplerianElements, molniya_set: KeplerianElements
) -> None:
    """Semi-minor axis is calculated from semi-major axis and eccentricity."""
    result = iss_set.semi_minor_axis()
    expected_value = 6599999.174999949
    assert result == expected_value
    result = molniya_set.semi_minor_axis()
    expected_value = 17891342.710931454
    assert result == expected_value


def test_area_within_orbit(
    iss_set: KeplerianElements, molniya_set: KeplerianElements
) -> None:
    """Orbital area is calculated from semi-major and semi-minor axes."""
    result = iss_set.area_within_orbit()
    expected_value = 136847758884398.33
    assert result == expected_value
    result = molniya_set.area_within_orbit()
    expected_value = 1495114467905620.0
    assert result == expected_value


def test_radius_vector_speed(
    iss_set: KeplerianElements, molniya_set: KeplerianElements
) -> None:
    """Radius vector speed calculated from orbital area and period."""
    result = iss_set.radius_vector_speed()
    expected_value = 25644969716.960884
    assert result == expected_value
    result = molniya_set.radius_vector_speed()
    expected_value = 34628397449.96699
    assert result == expected_value
