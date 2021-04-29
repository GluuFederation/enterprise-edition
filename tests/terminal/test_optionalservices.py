import pytest

def test_prompt_key_rotation(monkeypatch, settings):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.prompt", lambda x, default: 48)

    settings.set("global.auth-server-key-rotation.enabled", True)
    settings.set("auth-server-key-rotation.keysLife", False)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("auth-server-key-rotation.keysLife") == 48

def test_prompt_app_cert(monkeypatch, settings):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.prompt", lambda x, default: "client-api")

    settings.set("global.client-api.enabled", True)
    settings.set("config.configmap.cnClientApiApplicationCertCn", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("config.configmap.cnClientApiApplicationCertCn") == "client-api"

def test_prompt_admin_cert(monkeypatch, settings):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.prompt", lambda x, default: "client-api")

    settings.set("global.client-api.enabled", True)
    settings.set("config.configmap.cnClientApiAdminCertCn", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("config.configmap.cnClientApiAdminCertCn") == "client-api"

def test_prompt_casa(settings):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    settings.set("config.configmap.cnCasaEnabled", True)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.client-api.enabled") == True

@pytest.mark.parametrize("given, expected", [
    (False, False),
    (True, True),
])
def test_testenv_prompt_crrotate(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.cr-rotate.enabled", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.cr-rotate.enabled") == expected

@pytest.mark.parametrize("given, expected", [
    (False, False),
    (True, True),
])
def test_testenv_kyerotation(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.auth-server-key-rotation.enabled", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.auth-server-key-rotation.enabled") == expected

@pytest.mark.parametrize("given, expected", [
    (False, False),
    (True, True),
])
def test_testenv_prompt_radius(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("config.configmap.cnRadiusEnabled", False)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("config.configmap.cnRadiusEnabled") == expected

@pytest.mark.parametrize("given, expected", [
    (False, False),
    (True, True),
])
def test_testenv_prompt_passport(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("config.configmap.cnPassportEnabled", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("config.configmap.cnPassportEnabled") == expected

@pytest.mark.parametrize("given, expected", [
    (False, False),
    (True, True),
])
def test_testenv_prompt_cncasat(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("config.configmap.cnCasaEnabled", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("config.configmap.cnCasaEnabled") == expected

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_oxshibboleth(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.oxshibboleth.enabled", "")
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.oxshibboleth.enabled") == expected

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_fido2(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.fido2.enabled", False)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.fido2.enabled") == expected

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_configapit(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.config-api.enabled", False)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.config-api.enabled") == expected

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_scim(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.scim.enabled", False)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.scim.enabled") == expected

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_clientapi(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.optionalservices import PromptOptionalServices

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("global.client-api.enabled", False)
    prompt = PromptOptionalServices(settings)
    prompt.prompt_optional_services()
    assert settings.get("global.client-api.enabled") == expected