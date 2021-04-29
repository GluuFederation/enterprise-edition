import pytest

def test_prompt_redis_type(monkeypatch, settings):
    from pygluu.kubernetes.terminal.redis import PromptRedis

    monkeypatch.setattr("click.prompt", lambda x, default: "CLUSTER")

    settings.set("config.configmap.cnRedisType", "")
    prompt = PromptRedis(settings)
    prompt.prompt_redis()
    assert settings.get("config.configmap.cnRedisType") == "CLUSTER"

def test_prompt_redis_master_nodes(monkeypatch, settings):
    from pygluu.kubernetes.terminal.redis import PromptRedis

    monkeypatch.setattr("click.prompt", lambda x, default: 3)

    settings.set("installer-settings.redis.install", True)
    settings.set("installer-settings.redis.masterNodes", "")
    prompt = PromptRedis(settings)
    prompt.prompt_redis()
    assert settings.get("installer-settings.redis.masterNodes") == 3

def test_prompt_redis_nodes(monkeypatch, settings):
    from pygluu.kubernetes.terminal.redis import PromptRedis

    monkeypatch.setattr("click.prompt", lambda x, default: 2)

    settings.set("installer-settings.redis.install", True)
    settings.set("installer-settings.redis.nodesPerMaster", "")
    prompt = PromptRedis(settings)
    prompt.prompt_redis()
    assert settings.get("installer-settings.redis.nodesPerMaster") == 2

def test_prompt_redis_namepsace(monkeypatch, settings):
    from pygluu.kubernetes.terminal.redis import PromptRedis

    monkeypatch.setattr("click.prompt", lambda x, default: "gluu-redis-cluster")

    settings.set("installer-settings.redis.install", True)
    settings.set("installer-settings.redis.namespace", "")
    prompt = PromptRedis(settings)
    prompt.prompt_redis()
    assert settings.get("installer-settings.redis.namespace") == "gluu-redis-cluster"

@pytest.mark.parametrize("given, expected", [
(False, False),
(True, True),
])
def test_testenv_prompt_test_environment(monkeypatch, settings, given, expected):
    from pygluu.kubernetes.terminal.redis import PromptRedis

    monkeypatch.setattr("click.confirm", lambda x: given)
    settings.set("installer-settings.redis.install", False)
    settings.set("config.redisPassword", "")
    prompt = PromptRedis(settings)
    prompt.prompt_redis()
    assert settings.get("config.redisPassword") == expected

def test_redis_object_prompt():
    var0 = None
    var1 = module0.PromptRedis(var0)
    assert var1 is not None

def test_configmap_redis_prompt():
    var0 = None
    var1 = module0.PromptRedis(var0)
    assert var1 is not None
    var2 = module0.PromptRedis(var1)
    assert var2 is not None

def test_masternodes_prompt():
    var0 = None
    var1 = module0.PromptRedis(var0)
    assert var1 is not None
    var2 = module0.PromptRedis(var1)
    assert var2 is not None
    var3 = 1716
    var4 = module0.PromptRedis(var3)
    assert var4 is not None

def test_nodespermaster_prompt():
    var0 = None
    var1 = module0.PromptRedis(var0)
    assert var1 is not None
    var2 = module0.PromptRedis(var1)
    assert var2 is not None
    var3 = None
    var4 = module0.PromptRedis(var3)
    assert var4 is not None
    var5 = module0.PromptRedis(var4)
    assert var5 is not None
    var6 = 1716
    var7 = module0.PromptRedis(var6)
    assert var7 is not None
    var8 = module0.PromptRedis(var0)
    assert var8 is not None
