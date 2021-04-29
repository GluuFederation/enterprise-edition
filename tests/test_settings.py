import logging
import json
from pathlib import Path


def test_load_invalid_values(tmpdir, settings):
    p = Path(tmpdir) / 'test_settings.json'
    settings.values_file = p
    p.write_text('')
    settings.load()
    assert "Opps!" in settings.errors[0]


def test_store_data_exception(caplog, settings):
    # set collection to something that cannot be dumped as JSON
    settings.db = str

    with caplog.at_level(logging.INFO):
        assert settings.store_data() is False
        assert "Uncaught error" in caplog.text


def test_set_exception(caplog, settings):
    # set collection to something that cannot be dumped as JSON
    settings.dot = str

    with caplog.at_level(logging.INFO):
        assert settings.get("installer-settings.currentVersion", "5.0") is False
        assert "Uncaught error" in caplog.text


def test_get_exception(caplog, settings):
    with caplog.at_level(logging.INFO):
        assert settings.get("RANDOM_KEY") is False
        assert "No Value" in caplog.text


def test_update_exception(caplog, settings):
    # set collection to something that is not a collection
    collection = 1

    with caplog.at_level(logging.INFO):
        assert settings.update(collection) is False
        assert "Uncaught error" in caplog.text


def test_reset_data_exception(caplog, monkeypatch, settings):
    def fake_store_data():
        1 / 0

    monkeypatch.setattr(
        "pygluu.kubernetes.settings.ValuesHandler.store_data",
        fake_store_data,
    )

    with caplog.at_level(logging.INFO):
        assert settings.reset_data() is False
        assert "Uncaught error" in caplog.text


def test_settings_is_not_exist(settings, tmpdir):
    p = Path(tmpdir) / 'test_settings.json'
    settings.values_file = p

    assert settings.is_exist() is False


def test_settings_is_exist(settings, tmpdir):
    p = Path(tmpdir) / 'test_settings.json'
    p.write_text('{}')
    settings.values_file = p

    assert settings.is_exist() is True


def test_settings_validation_is_valid(settings, tmpdir):

    settings.db = str
    
    settings.set("installer-settings.acceptLicense", True)
    settings_object = json.dumps(settings.db)
    p = Path(tmpdir) / 'test_settings.json'
    p.write_text(settings_object)
    settings.values_file = p

    assert settings.validate() is True


def test_settings_validation_is_invalid(settings, tmpdir):

    settings.db = str
    
    settings.set("installer-settings.acceptLicense", "Y")
    settings.set("CN_ADMIN_PASSWORD", "123123123")
    settings.set("CN_INSTALL_GLUU_GATEWAY", "Y")
    settings_object = json.dumps(settings.db)
    p = Path(tmpdir) / 'test_settings.json'
    p.write_text(settings_object)
    settings.values_file = p

    assert settings.validate() is False


def test_settings_validation_not_exist_setting(settings, tmpdir):
    p = Path(tmpdir) / 'test_settings.json'
    settings.values_file = p
    assert settings.validate() is True


def test_settings_validation_not_valid_setting(settings, tmpdir):
    p = Path(tmpdir) / 'test_settings.json'
    settings.values_file = p
    p.write_text('')
    assert settings.validate() is False
