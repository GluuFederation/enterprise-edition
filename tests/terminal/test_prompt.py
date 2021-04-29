import pygluu.kubernetes.terminal.prompt as module0


def test_class_object():
    var0 = module0.Prompt()
    var1 = var0.load_settings()

def test_configuration():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.configuration()

def test_images():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.images()

def test_cache():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.cache()

def test_persistence_backend():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.persistence_backend()

def test_replicas():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.replicas()

def test_istio():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.istio()

def test_jackrabbit():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.jackrabbit()

def test_gluu_gateway():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.gluu_gateway()

def test_optional_services():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.optional_services()

def test_namespace():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.namespace()

def test_arch():
    var0 = module0.Prompt()
    var1 = var0.load_settings()
    var2 = var0.arch()

def test_base_exception_against_prompt():
    try:
        var0 = module0.Prompt()
    except BaseException:
        pass

