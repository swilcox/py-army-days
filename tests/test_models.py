from datetime import datetime

from army_days.models import ConfigModel, DaysModel, EntryModel


def test_config_model():
    blank_model = ConfigModel()
    assert blank_model is not None
    assert blank_model.use_army_butt_days is False
    assert blank_model.show_completed is False


def test_days_model():
    blank_model = DaysModel(config=ConfigModel(), entries=[])
    assert blank_model is not None


def test_entry_model():
    simple_model = EntryModel(title="nothing", date=datetime(1, 1, 1))
    assert simple_model is not None
