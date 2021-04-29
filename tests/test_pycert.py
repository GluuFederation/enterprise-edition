import pygluu.kubernetes.pycert as module0


def test_check_cert_with_private_key():
    var0 = '>_6<Z\\a~'
    var1 = '|\ntEaF}d5{T< 9'
    var2 = module0.check_cert_with_private_key(var0, var1)


def test_setup_crts():
    try:
        var0 = False
        var1 = 'FhZb9xG*,vw}\n"'
        var2 = 'X]/\x0b`VKKF=g'
        var3 = None
        var4 = b"\x10]\x8f\xccg\x9d\xa2,\x06\xd3\xda'\xeb\x9e"
        var5 = module0.setup_crts(var0, var1, var2, var3, var4, var0, var4)
    except BaseException:
        pass


def test_setup_crt():
    try:
        var0 = True
        var1 = 1737
        var2 = 'a\tOrd'
        var3 = ') X`zA\\5X`Hl$pVUjZS2'
        var4 = module0.setup_crts(var0, var1, var2, var0, var1, var3, var0)
    except BaseException:
        pass


def test_check_cert():
    try:
        var0 = False
        var1 = 2075
        var2 = module0.check_cert_with_private_key(var0, var1)
    except BaseException:
        pass


def test_check_cert_exception():
    try:
        var0 = False
        var1 = None
        var2 = module0.check_cert_with_private_key(var0, var1)
    except BaseException:
        pass

def test_check_cert_str():
    try:
        var0 = 2198.0
        var1 = b']\xa0I\xb5S'
        var2 = module0.check_cert_with_private_key(var0, var1)
    except BaseException:
        pass
