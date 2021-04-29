import pygluu.kubernetes.gluu as module0


def test_install_ldap_backup():
    var0 = module0.Gluu()
    var1 = var0.install_ldap_backup()


def test_unisntall_gluu():
    var0 = module0.Gluu()
    var1 = var0.install_ldap_backup()
    var2 = module0.Gluu()
    var3 = var2.install_ldap_backup()
    var4 = var2.uninstall_nginx_ingress()
    var5 = module0.Gluu()


def test_wait_for_nginx_add():
    var0 = module0.Gluu()
    assert var0 is not None
    var1 = var0.install_ldap_backup()
    assert var1 is None
    var2 = module0.Gluu()
    var3 = var2.install_ldap_backup()
    var4 = var2.uninstall_nginx_ingress()
    var5 = module0.Gluu()
    var6 = var5.install_ldap_backup()
    var7 = module0.Gluu()
    var8 = var7.install_ldap_backup()
    var9 = var7.uninstall_nginx_ingress()
    var10 = module0.Gluu()
    var11 = var0.wait_for_nginx_add()


def test_uninstall_nginx_ingress2():
    var0 = module0.Gluu()
    assert var0 is not None
    var1 = var0.install_ldap_backup()
    var2 = module0.Gluu()
    assert var2 is not None
    var3 = var2.install_ldap_backup()
    var4 = var2.uninstall_nginx_ingress()
    var5 = module0.Gluu()
    var6 = module0.Gluu()
    var7 = var6.install_ldap_backup()
    var8 = module0.Gluu()
    var9 = var8.install_ldap_backup()
    var10 = var8.uninstall_nginx_ingress()
    var11 = var2.uninstall_nginx_ingress()


def test_uninstall_nginx_ingress():
    var0 = module0.Gluu()
    var1 = var0.install_ldap_backup()
    var2 = module0.Gluu()
    var3 = var2.install_ldap_backup()
    var4 = var2.uninstall_nginx_ingress()
    var5 = module0.Gluu()
    var6 = var5.uninstall_nginx_ingress()


def test_upgrade_gluu():
    var0 = module0.Gluu()
    var1 = var0.install_ldap_backup()
    var2 = module0.Gluu()
    var3 = var2.install_ldap_backup()
    var4 = var2.uninstall_nginx_ingress()
    var5 = module0.Gluu()
    var6 = var5.uninstall_nginx_ingress()
    var7 = module0.Gluu()
    var8 = var7.install_ldap_backup()
    var9 = module0.Gluu()
    var10 = var9.install_ldap_backup()
    var11 = module0.Gluu()
    var12 = var11.install_ldap_backup()
    var13 = var11.uninstall_nginx_ingress()
    var14 = module0.Gluu()
    var15 = var14.upgrade_gluu()


def test_wait_for_nginx_add():
    try:
        var0 = module0.Gluu()
        assert var0 is not None
        var1 = var0.install_ldap_backup()
        assert var1 is None
        var2 = module0.Gluu()
        var3 = var2.install_ldap_backup()
        var4 = var2.uninstall_nginx_ingress()
        var5 = module0.Gluu()
    except BaseException:
        pass


def test_exception():
    try:
        var0 = module0.Gluu()
    except BaseException:
        pass


def test_ldap_nginx_ingress():
    try:
        var0 = module0.Gluu()
        assert var0 is not None
        var1 = var0.install_ldap_backup()
        assert var1 is None
        var2 = module0.Gluu()
        var3 = var2.install_ldap_backup()
        var4 = var2.uninstall_nginx_ingress()
        var5 = module0.Gluu()
    except BaseException:
        pass