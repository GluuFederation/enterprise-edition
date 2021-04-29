import pytest

@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_images(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("installer-settings.images.edit", "")
    settings.set("installer-settings.images.edit", "")
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert settings.get("installer-settings.images.edit") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_casa(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("config.configmap.cnCasaEnabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("Casa", "casa") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_crrotate(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("global.cr-rotate.enabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("CR-rotate", "cr-rotate") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_keyauth(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("global.auth-server-key-rotation.enabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("Key rotate", "auth-server-key-rotation") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_ldap(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("config.configmap.cnCacheType", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("OpenDJ", "opendj") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_clientapi(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("global.client-api.enabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("CLIENT_API server", "client-api") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_oxpassport(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("config.configmap.cnPassportEnabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("oxPassport", "oxpassport") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_oxshiboleth(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("global.oxshibboleth.enabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("oxShibboleth", "oxshibboleth") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_radius(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("config.configmap.cnRadiusEnabled", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("Radius", "radius") == expected


@pytest.mark.parametrize("given, expected", [
    (True, True),
])
def test_testenv_prompt_test_edit_gluugw(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.images import PromptImages

    monkeypatch.setattr("click.prompt", lambda x: given)
    settings.set("installer-settings.images.edit", True)
    settings.set("installer-settings.gluuGateway.install", True)
    prompt = PromptImages(settings)
    prompt.prompt_image_name_tag()
    assert prompt_and_set_setting("Gluu-Gateway", "installer-settings.gluuGateway.kong") == expected
    assert prompt_and_set_setting("Gluu-Gateway-UI", "") == expected