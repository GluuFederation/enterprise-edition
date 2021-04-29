import pytest


@pytest.mark.parametrize("given, expected", [
    ("", "postgres"),  # default
    ("random", "random"),
])
def test_postgres_namespace(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.postgres import PromptPostgres

    monkeypatch.setattr("click.prompt", lambda x, default: given or expected)
    settings.set("installer-settings.postgres.install", "Y")
    settings.set("installer-settings.postgres.replicas", 3)
    settings.set("config.configmap.cnJackrabbitPostgresHost", "postgres.postgres.svc.cluster.local")
    settings.set("installer-settings.postgres.namespace", "")

    prompt = PromptPostgres(settings)
    prompt.prompt_postgres()
    assert settings.get("installer-settings.postgres.namespace") == expected


@pytest.mark.parametrize("given, expected", [
    ("", 3),  # default
    (2, 2),
])
def test_postgres_replicas(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.postgres import PromptPostgres

    monkeypatch.setattr("click.prompt", lambda x, default: given or expected)
    settings.set("installer-settings.postgres.install", "Y")
    settings.set("installer-settings.postgres.namespace", "postgres")
    settings.set("config.configmap.cnJackrabbitPostgresHost", "postgres.postgres.svc.cluster.local")
    settings.set("installer-settings.postgres.replicas", "")

    prompt = PromptPostgres(settings)
    prompt.prompt_postgres()
    assert settings.get("installer-settings.postgres.replicas") == expected


@pytest.mark.parametrize("given, expected", [
    ("", "postgres.postgres.svc.cluster.local"),  # default
    ("random", "random"),
])
def test_postgres_url(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.postgres import PromptPostgres

    monkeypatch.setattr("click.prompt", lambda x, default: given or expected)

    settings.set("installer-settings.postgres.namespace", "postgres")
    settings.set("installer-settings.postgres.replicas", 3)
    settings.set("config.configmap.cnJackrabbitPostgresHost", "")
    

    prompt = PromptPostgres(settings)
    prompt.prompt_postgres()
    assert settings.get("config.configmap.cnJackrabbitPostgresHost") == expected
