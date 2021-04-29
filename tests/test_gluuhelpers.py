import pygluu.kubernetes.helpers as module0


def test_supported_version_func():
    var0 = module0.get_supported_versions()
    assert var0 is not None


def test_ssh_and_remove():
    var0 = None
    var1 = None
    var2 = None
    var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var4 = module0.ssh_and_remove(var0, var1, var2, var3)
    assert var4 is None


def test_update_settings_json_file():
    var0 = module0.get_supported_versions()
    assert var0 is not None
    var1 = None
    var2 = None
    var3 = None
    var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var5 = module0.ssh_and_remove(var1, var2, var3, var4)
    assert var5 is None
    var6 = -1349.004797
    var7 = module0.update_settings_json_file(var6)
    assert var7 is None


def test_get_supported_versions_value():
    var0 = module0.get_supported_versions()
    assert var0 is not None
    var1 = None
    var2 = None
    var3 = None
    var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var5 = module0.ssh_and_remove(var1, var2, var3, var4)
    assert var5 is None
    var6 = module0.get_supported_versions()
    assert var6 is not None


def test_get_logger():
    var0 = None
    var1 = None
    var2 = None
    var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var4 = module0.ssh_and_remove(var0, var1, var2, var3)
    assert var4 is None
    var5 = module0.get_logger(var1)
    assert var5 is not None


def test_update_settings_json():
    var0 = None
    var1 = None
    var2 = None
    var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var4 = module0.ssh_and_remove(var0, var1, var2, var3)
    assert var4 is None
    var5 = module0.get_logger(var1)
    assert var5 is not None
    var6 = module0.get_supported_versions()
    assert var6 is not None
    var7 = '+w#_Q,jvH#oUj&,{[f'
    var8 = module0.update_settings_json_file(var7)
    assert var8 is None


def test_check_microk8s_kube_config_file():
    var0 = module0.get_supported_versions()
    assert var0 is not None
    var1 = None
    var2 = None
    var3 = None
    var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var5 = module0.ssh_and_remove(var1, var2, var3, var4)
    assert var5 is None
    var6 = -1349.004797
    var7 = module0.update_settings_json_file(var6)
    assert var7 is None
    var8 = module0.check_microk8s_kube_config_file()
    assert var8 is None


def test_microk8s_kube_config_file():
    var0 = None
    var1 = None
    var2 = None
    var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var4 = module0.ssh_and_remove(var0, var1, var2, var3)
    assert var4 is None
    var5 = module0.get_logger(var1)
    assert var5 is not None
    var6 = module0.get_supported_versions()
    assert var6 is not None
    var7 = '+w#_Q,jvH#oUj&,{[f'
    var8 = module0.update_settings_json_file(var7)
    assert var8 is None
    var9 = module0.get_supported_versions()
    assert var9 is not None
    var10 = None
    var11 = None
    var12 = None
    var13 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var14 = module0.ssh_and_remove(var10, var11, var12, var13)
    assert var14 is None
    var15 = -1349.004797
    var16 = module0.update_settings_json_file(var15)
    assert var16 is None
    var17 = module0.check_microk8s_kube_config_file()
    assert var17 is None
    var18 = None
    var19 = None
    var20 = None
    var21 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var22 = module0.ssh_and_remove(var18, var19, var20, var21)
    assert var22 is None
    var23 = module0.get_supported_versions()
    assert var23 is not None
    var24 = module0.get_supported_versions()
    assert var24 is not None
    var25 = None
    var26 = None
    var27 = None
    var28 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var29 = module0.ssh_and_remove(var25, var26, var27, var28)
    assert var29 is None
    var30 = module0.get_supported_versions()
    assert var30 is not None
    var31 = None
    var32 = None
    var33 = None
    var34 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var35 = module0.ssh_and_remove(var31, var32, var33, var34)
    assert var35 is None
    var36 = module0.get_logger(var32)
    assert var36 is not None
    var37 = module0.check_microk8s_kube_config_file()
    assert var37 is None


def test_ssh_and_remove_process():
    var0 = None
    var1 = None
    var2 = None
    var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var4 = module0.ssh_and_remove(var0, var1, var2, var3)
    assert var4 is None
    var5 = module0.get_logger(var1)
    assert var5 is not None
    var6 = module0.get_supported_versions()
    assert var6 is not None
    var7 = '+w#_Q,jvH#oUj&,{[f'
    var8 = module0.update_settings_json_file(var7)
    assert var8 is None
    var9 = None
    var10 = 'oka/vXL2i^5=]'
    var11 = None
    var12 = module0.ssh_and_remove(var9, var10, var1, var11)
    assert var12 is None


def test_helpers_file():
    var0 = module0.get_supported_versions()
    assert var0 is not None
    var1 = None
    var2 = None
    var3 = None
    var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var5 = module0.ssh_and_remove(var1, var2, var3, var4)
    assert var5 is None
    var6 = -1349.004797
    var7 = module0.update_settings_json_file(var6)
    assert var7 is None
    var8 = module0.check_microk8s_kube_config_file()
    assert var8 is None
    var9 = None
    var10 = None
    var11 = None
    var12 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var13 = module0.ssh_and_remove(var9, var10, var11, var12)
    assert var13 is None
    var14 = module0.get_logger(var10)
    assert var14 is not None
    var15 = module0.get_supported_versions()
    assert var15 is not None
    var16 = '+w#_Q,jvH#oUj&,{[f'
    var17 = module0.update_settings_json_file(var16)
    assert var17 is None
    var18 = None
    var19 = None
    var20 = None
    var21 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var22 = module0.ssh_and_remove(var18, var19, var20, var21)
    assert var22 is None
    var23 = module0.get_logger(var19)
    assert var23 is not None
    var24 = module0.check_microk8s_kube_config_file()
    assert var24 is None


def test_update_settings_json():
    var0 = module0.get_supported_versions()
    assert var0 is not None
    var1 = module0.get_supported_versions()
    assert var1 is not None
    var2 = None
    var3 = None
    var4 = None
    var5 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var6 = module0.ssh_and_remove(var2, var3, var4, var5)
    assert var6 is None
    var7 = -1349.004797
    var8 = module0.update_settings_json_file(var7)
    assert var8 is None
    var9 = module0.get_supported_versions()
    assert var9 is not None
    var10 = None
    var11 = None
    var12 = None
    var13 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var14 = module0.ssh_and_remove(var10, var11, var12, var13)
    assert var14 is None
    var15 = module0.get_supported_versions()
    assert var15 is not None
    var16 = None
    var17 = module0.update_settings_json_file(var16)
    assert var17 is None


def test_e2e_get_version():
    var0 = module0.get_supported_versions()
    assert var0 is not None
    var1 = None
    var2 = None
    var3 = None
    var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var5 = module0.ssh_and_remove(var1, var2, var3, var4)
    assert var5 is None
    var6 = -1349.004797
    var7 = module0.update_settings_json_file(var6)
    assert var7 is None
    var8 = None
    var9 = None
    var10 = None
    var11 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var12 = module0.ssh_and_remove(var8, var9, var10, var11)
    assert var12 is None
    var13 = module0.get_supported_versions()
    assert var13 is not None
    var14 = module0.get_supported_versions()
    assert var14 is not None
    var15 = None
    var16 = None
    var17 = None
    var18 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var19 = module0.ssh_and_remove(var15, var16, var17, var18)
    assert var19 is None
    var20 = module0.get_supported_versions()
    assert var20 is not None
    var21 = module0.get_supported_versions()
    assert var21 is not None


def test_copy():
    var0 = None
    var1 = None
    var2 = None
    var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
    var4 = module0.ssh_and_remove(var0, var1, var2, var3)
    assert var4 is None
    var5 = module0.get_logger(var1)
    assert var5 is not None
    var6 = 'M]e<8>#arT\r'
    var7 = None
    var8 = module0.copy(var6, var7)
    assert var8 is None


def test_check_port_exception():
    try:
        var0 = b'T'
        var1 = module0.check_port(var0, var0)
    except BaseException:
        pass


def test_empty_port_exception():
    try:
        var0 = None
        var1 = 'REp3Ft/*Ups%!'
        var2 = module0.check_port(var0, var1)
    except BaseException:
        pass


def test_check_port():
    try:
        var0 = None
        var1 = None
        var2 = None
        var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
        var4 = module0.ssh_and_remove(var0, var1, var2, var3)
        assert var4 is None
        var5 = None
        var6 = None
        var7 = module0.check_port(var5, var6)
    except BaseException:
        pass


def test_analyze_storage_class():
    try:
        var0 = module0.get_supported_versions()
        assert var0 is not None
        var1 = None
        var2 = b'\xf2'
        var3 = module0.analyze_storage_class(var1, var2)
    except BaseException:
        pass


def test_prompt_password():
    try:
        var0 = module0.get_supported_versions()
        assert var0 is not None
        var1 = False
        var2 = None
        var3 = module0.prompt_password(var1, var2)
    except BaseException:
        pass


def test_exec_cmd():
    try:
        var0 = None
        var1 = None
        var2 = None
        var3 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
        var4 = module0.ssh_and_remove(var0, var1, var2, var3)
        assert var4 is None
        var5 = module0.get_supported_versions()
        assert var5 is not None
        var6 = 2097.0
        var7 = -2280.1758
        var8 = module0.exec_cmd(var6, var0, var7)
    except BaseException:
        pass


def test_analyze_storage():
    try:
        var0 = module0.get_supported_versions()
        assert var0 is not None
        var1 = None
        var2 = None
        var3 = None
        var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
        var5 = module0.ssh_and_remove(var1, var2, var3, var4)
        assert var5 is None
        var6 = b'\x1d\x85'
        var7 = module0.analyze_storage_class(var1, var6)
    except BaseException:
        pass


def test_analyze_storage_exception():
    try:
        var0 = module0.get_supported_versions()
        assert var0 is not None
        var1 = -2130.0
        var2 = None
        var3 = module0.analyze_storage_class(var1, var2)
    except BaseException:
        pass


def test_none_password_execption():
    try:
        var0 = module0.get_supported_versions()
        assert var0 is not None
        var1 = None
        var2 = None
        var3 = None
        var4 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
        var5 = module0.ssh_and_remove(var1, var2, var3, var4)
        assert var5 is None
        var6 = -1349.004797
        var7 = module0.update_settings_json_file(var6)
        assert var7 is None
        var8 = module0.check_microk8s_kube_config_file()
        assert var8 is None
        var9 = module0.get_supported_versions()
        assert var9 is not None
        var10 = None
        var11 = None
        var12 = None
        var13 = b'\xb1\xb0\xb13\xad\xaa\xa5\x97\x93:\xd9\xfe\x96\xa1'
        var14 = module0.ssh_and_remove(var10, var11, var12, var13)
        assert var14 is None
        var15 = -1349.004797
        var16 = module0.update_settings_json_file(var15)
        assert var16 is None
        var17 = None
        var18 = module0.prompt_password(var17, var17)
    except BaseException:
        pass
