import pygluu.kubernetes.redis as module0

def test_redis_class_object():
    var0 = module0.Redis()


def test_base_exception():
    try:
        var0 = module0.Redis()
    except BaseException:
        pass


def test_redis_install_exception():
    try:
        var0 = module0.Redis()
        var1 = var0.install_redis()
    except BaseException:
        pass


def test_install_redis():
    try:
        var0 = module0.Redis()
        var1 = module0.Redis()
        var2 = var1.install_redis()
    except BaseException:
        pass