from datetime import datetime

from freezegun import freeze_time

from army_days.core import compute_results, generate_default_configuration


@freeze_time("2024-08-05T13:00:00")
def test_compute_results_standard(standard_test_config):
    results = compute_results(standard_test_config)
    assert results is not None
    assert results[0].title == "Item 2"  # verify sorting works
    assert len(results) == 4  # verify past events are excluded
    assert results[2].days == 129.0  # verify that we're *not* using army butt days
    # switch settings...
    standard_test_config.config.use_army_butt_days = True
    standard_test_config.config.show_completed = True
    results = compute_results(standard_test_config)
    assert results is not None
    assert results[0].title == "Item 4"  # verify sorting and showcompleted
    assert len(results) == 6  # verify past events are included
    assert results[0].days == -840.0
    assert results[4].days == 128.5  # army butt days now in use


@freeze_time("2024-08-05T13:00:00")
def test_generate_default_configuration():
    config = generate_default_configuration()
    assert config is not None
    assert config.config.use_army_butt_days is False
    assert config.config.show_completed is False
    assert len(config.entries) == 1
    assert config.entries[0].date == datetime(2025, 8, 5)


@freeze_time("2024-02-29T13:00:00")  # LEAP DAY
def test_generate_default_configuration_leap_day():
    config = generate_default_configuration()
    assert config is not None
    assert config.config.use_army_butt_days is False
    assert config.config.show_completed is False
    assert len(config.entries) == 1
    assert config.entries[0].date == datetime(2025, 3, 1)
