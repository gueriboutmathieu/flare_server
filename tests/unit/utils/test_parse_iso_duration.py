import pytest

from flare.utils.parse_iso_duration import parse_iso_duration


@pytest.mark.parametrize(
    ("iso_duration", "duration"),
    [
        ("P4DT4H56M37S", 363397),
        ("PT4H56M", 17760),
        ("PT4H", 14400),
        ("PT56M", 3360),
        ("PT37S", 37),
    ],
)
def test_parse_iso_duration(iso_duration: str, duration: int):
    assert parse_iso_duration(iso_duration) == duration


def test_parse_iso_duration_invalid():
    with pytest.raises(ValueError):
        parse_iso_duration("invalid")
