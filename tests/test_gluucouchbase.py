import pygluu.kubernetes.couchbase as module0


def test_couchbase_object():
    var0 = module0.Couchbase()


def test_set_memory_for_buckets():
    var0 = module0.Couchbase()
    assert var0 is not None
    var1 = module0.Couchbase()
    assert var1 is not None
    var2 = module0.Couchbase()
    assert var2 is not None
    var3 = False
    var4 = -3373
    var5 = None
    var6 = var0.create_couchbase_gluu_cert_pass_secrets(var3, var4, var5)


def test_exception():
    try:
        var0 = module0.Couchbase()
    except BaseException:
        pass


def test_uninstall_parameters():
    try:
        var0 = module0.Couchbase()
        assert var0 is not None
        var1 = module0.Couchbase()
        assert var1 is not None
        var2 = var1.uninstall()
    except BaseException:
        pass


def test_uninstall_pars():
    try:
        var0 = module0.Couchbase()
        assert var0 is not None
        var1 = module0.Couchbase()
        assert var1 is not None
        var2 = module0.Couchbase()
        assert var2 is not None
        var3 = module0.Couchbase()
        assert var3 is not None
        var4 = module0.Couchbase()
        var5 = var4.uninstall()
    except BaseException:
        pass


def test_uninstall_couchbase():
    try:
        var0 = module0.Couchbase()
        assert var0 is not None
        var1 = module0.Couchbase()
        var2 = var1.uninstall()
    except BaseException:
        pass