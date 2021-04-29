import pytest

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_test_environment(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.gluugateway import PromptGluuGateway

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("installer-settings.gluuGateway.install", "")
    prompt = PromptGluuGateway(settings)
    prompt.prompt_gluu_gateway()
    assert settings.get("installer-settings.gluuGateway.install") == expected

def test_prompt_ui_namespace(monkeypatch, settings):
    from pygluu.kubernetes.terminal.gluugateway import PromptGluuGateway

    monkeypatch.setattr("click.prompt", lambda x, default: "gg-ui")

    settings.set("installer-settings.gluuGateway.install", True)
    settings.set("installer-settings.global.client-api.enabled", True)
    settings.set("installer-settings.gluuGateway.uI.namespace", "")
    prompt = PromptGluuGateway(settings)
    prompt.prompt_gluu_gateway()
    assert settings.get("installer-settings.gluuGateway.uI.namespace") == "gg-ui"

def test_prompt_kong_postgres_db_name(monkeypatch, settings):
    from pygluu.kubernetes.terminal.gluugateway import PromptGluuGateway

    monkeypatch.setattr("click.prompt", lambda x, default: "kong")

    settings.set("installer-settings.gluuGateway.install", True)
    settings.set("installer-settings.global.client-api.enabled", True)
    settings.set("installer-settings.gluuGateway.kong.postgresUser", "")
    prompt = PromptGluuGateway(settings)
    prompt.prompt_gluu_gateway()
    assert settings.get("installer-settings.gluuGateway.kong.postgresUser") == "kong"

def test_prompt_postgres_db_user(monkeypatch, settings):
    from pygluu.kubernetes.terminal.gluugateway import PromptGluuGateway

    monkeypatch.setattr("click.prompt", lambda x, default: "konga")

    settings.set("installer-settings.gluuGateway.install", True)
    settings.set("installer-settings.global.client-api.enabled", True)
    settings.set("installer-settings.gluuGateway.uI.postgresUser", "")
    prompt = PromptGluuGateway(settings)
    prompt.prompt_gluu_gateway()
    assert settings.get("installer-settings.gluuGateway.uI.postgresUser") == "konga"

def test_prompt_postgres_db_name(monkeypatch, settings):
    from pygluu.kubernetes.terminal.gluugateway import PromptGluuGateway

    monkeypatch.setattr("click.prompt", lambda x, default: "kong")

    settings.set("installer-settings.gluuGateway.install", True)
    settings.set("installer-settings.global.client-api.enabled", True)
    settings.set("installer-settings.gluuGateway.kong.postgresDatabaseName", "")
    prompt = PromptGluuGateway(settings)
    prompt.prompt_gluu_gateway()
    assert settings.get("installer-settings.gluuGateway.kong.postgresDatabaseName") == "kong"

def test_prompt_postgres_ui_db_name(monkeypatch, settings):
    from pygluu.kubernetes.terminal.gluugateway import PromptGluuGateway

    monkeypatch.setattr("click.prompt", lambda x, default: "konga")

    settings.set("installer-settings.gluuGateway.install", True)
    settings.set("installer-settings.global.client-api.enabled", True)
    settings.set("installer-settings.gluuGateway.uI.postgresDatabaseName", "")
    prompt = PromptGluuGateway(settings)
    prompt.prompt_gluu_gateway()
    assert settings.get("installer-settings.gluuGateway.uI.postgresDatabaseName") == "konga"
