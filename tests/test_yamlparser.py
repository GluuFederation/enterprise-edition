import pytest
import pygluu.kubernetes.yamlparser as module0


def test_setitem():
    var0 = False
    var1 = 784
    var2 = 'VUz;/a/dx#srz^'
    var3 = '%'
    var4 = 'u\rt1\r5A@[YK:z2+e'
    var5 = -3751.85
    var6 = module0.Parser(var2, var3, var4, var5)
    assert var6 is not None
    var7 = var6.__setitem__(var0, var1)
    assert var7 is None


def test_dump_it():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None


def test_parser():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None


def test_delitem():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = False
    var7 = 784
    var8 = 'VUz;/a/dx#srz^'
    var9 = '%'
    var10 = 'u\rt1\r5A@[YK:z2+e'
    var11 = -3751.85
    var12 = module0.Parser(var8, var9, var10, var11)
    assert var12 is not None
    var13 = var12.__setitem__(var6, var7)
    assert var13 is None
    var14 = '\t|'
    var15 = var4.__delitem__(var14)
    assert var15 is None


def test_analyze_ordered_dict_object():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = '^!&@-I\x0b91+IPf~a\tC"a'
    var7 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var8 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var9 = '80T\tI'
    var10 = module0.Parser(var6, var7, var8, var9)
    assert var10 is not None
    var11 = var10.dump_it()
    assert var11 is None
    var12 = b'\xe8\xb8\x8f`\x00'
    var13 = module0.Parser(var6, var10, var12, var10)
    assert var13 is not None
    var14 = '[tJIBjwy'
    var15 = var4.analyze_ordered_dict_object(var14)
    assert var15 == '[tJIBjwy'

def test_updates():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = '^!&@-I\x0b91+IPf~a\tC"a'
    var7 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var8 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var9 = '80T\tI'
    var10 = module0.Parser(var6, var7, var8, var9)
    assert var10 is not None
    var11 = var10.dump_it()
    assert var11 is None
    var12 = b'\xe8\xb8\x8f`\x00'
    var13 = module0.Parser(var6, var10, var12, var10)
    assert var13 is not None
    var14 = False
    var15 = 784
    var16 = 'VUz;/a/dx#srz^'
    var17 = '%'
    var18 = 'u\rt1\r5A@[YK:z2+e'
    var19 = -3751.85
    var20 = module0.Parser(var16, var17, var18, var19)
    assert var20 is not None
    var21 = var20.__setitem__(var14, var15)
    assert var21 is None
    var22 = None
    var23 = var10.update(var22)
    assert var23 is None


def test_delitems():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None
    var8 = '}xcf\n.SqIB['
    var9 = var7.__delitem__(var8)
    assert var9 is None


def test_pars_values():
    var0 = ';*\x0c.J^MU^%vt/xe0(/4L'
    var1 = -359
    var2 = None
    var3 = b'k\xb5\xd0\xb0\x08\xbb\x84\xcb9\x81\xd8\xc9]<q\x91\xa5'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None


def test_update_setitem():
    var0 = False
    var1 = 784
    var2 = 'VUz;/a/dx#srz^'
    var3 = '%'
    var4 = 'u\rt1\r5A@[YK:z2+e'
    var5 = -3751.85
    var6 = module0.Parser(var2, var3, var4, var5)
    assert var6 is not None
    var7 = var6.__setitem__(var0, var1)
    assert var7 is None
    var8 = ';*\x0c.J^MU^%vt/xe0(/4L'
    var9 = -359
    var10 = None
    var11 = b'k\xb5\xd0\xb0\x08\xbb\x84\xcb9\x81\xd8\xc9]<q\x91\xa5'
    var12 = module0.Parser(var8, var9, var10, var11)
    assert var12 is not None
    var13 = None
    var14 = var12.update(var13)
    assert var14 is None


def test_set_delitem():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = False
    var7 = 784
    var8 = 'VUz;/a/dx#srz^'
    var9 = '%'
    var10 = 'u\rt1\r5A@[YK:z2+e'
    var11 = -3751.85
    var12 = module0.Parser(var8, var9, var10, var11)
    assert var12 is not None
    var13 = var12.__setitem__(var6, var7)
    assert var13 is None
    var14 = var12.__delitem__(var6)
    assert var14 is None


def test_update_parser():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None
    var8 = None
    var9 = var4.update(var8)
    assert var9 is None


def test_analyze_ordered_dict_objects():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = '^!&@-I\x0b91+IPf~a\tC"a'
    var7 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var8 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var9 = '80T\tI'
    var10 = module0.Parser(var6, var7, var8, var9)
    assert var10 is not None
    var11 = var10.dump_it()
    assert var11 is None
    var12 = b'\xe8\xb8\x8f`\x00'
    var13 = module0.Parser(var6, var10, var12, var10)
    assert var13 is not None
    var14 = 1517
    var15 = var13.analyze_ordered_dict_object(var14)
    assert var15 == 1517


def test_dict_object():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None
    var8 = var7.dump_it()
    assert var8 is None
    var9 = ';*\x0c.J^MU^%vt/xe0(/4L'
    var10 = -359
    var11 = None
    var12 = b'k\xb5\xd0\xb0\x08\xbb\x84\xcb9\x81\xd8\xc9]<q\x91\xa5'
    var13 = module0.Parser(var9, var10, var11, var12)
    assert var13 is not None
    var14 = 'fwW\n[\x0cMzJ'
    var15 = var4.analyze_ordered_dict_object(var14)
    assert var15 == 'fwW\n[\x0cMzJ'


def test_ordered_dict_object():
    var0 = ';*\x0c.J^MU^%vt/xe0(/4L'
    var1 = -359
    var2 = None
    var3 = b'k\xb5\xd0\xb0\x08\xbb\x84\xcb9\x81\xd8\xc9]<q\x91\xa5'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = '^!&@-I\x0b91+IPf~a\tC"a'
    var6 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var7 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var8 = '80T\tI'
    var9 = module0.Parser(var5, var6, var7, var8)
    assert var9 is not None
    var10 = var9.dump_it()
    assert var10 is None
    var11 = b'\xe8\xb8\x8f`\x00'
    var12 = module0.Parser(var5, var9, var11, var9)
    assert var12 is not None
    var13 = var12.dump_it()
    assert var13 is None
    var14 = False
    var15 = 784
    var16 = 'VUz;/a/dx#srz^'
    var17 = '%'
    var18 = 'u\rt1\r5A@[YK:z2+e'
    var19 = -3751.85
    var20 = module0.Parser(var16, var17, var18, var19)
    assert var20 is not None
    var21 = var20.__setitem__(var14, var15)
    assert var21 is None
    var22 = '^!&@-I\x0b91+IPf~a\tC"a'
    var23 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var24 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var25 = '80T\tI'
    var26 = module0.Parser(var22, var23, var24, var25)
    assert var26 is not None
    var27 = var26.dump_it()
    assert var27 is None
    var28 = var12.analyze_ordered_dict_object(var17)
    assert var28 == '%'


def test_del_dumpit():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None
    var8 = ';*\x0c.J^MU^%vt/xe0(/4L'
    var9 = -359
    var10 = None
    var11 = b'k\xb5\xd0\xb0\x08\xbb\x84\xcb9\x81\xd8\xc9]<q\x91\xa5'
    var12 = module0.Parser(var8, var9, var10, var11)
    assert var12 is not None
    var13 = '^!&@-I\x0b91+IPf~a\tC"a'
    var14 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var15 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var16 = '80T\tI'
    var17 = module0.Parser(var13, var14, var15, var16)
    assert var17 is not None
    var18 = var17.dump_it()
    assert var18 is None
    var19 = b'\xe8\xb8\x8f`\x00'
    var20 = module0.Parser(var13, var17, var19, var17)
    assert var20 is not None
    var21 = var20.dump_it()
    assert var21 is None
    var22 = '^!&@-I\x0b91+IPf~a\tC"a'
    var23 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var24 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var25 = '80T\tI'
    var26 = module0.Parser(var22, var23, var24, var25)
    assert var26 is not None
    var27 = var26.dump_it()
    assert var27 is None
    var28 = False
    var29 = 784
    var30 = 'VUz;/a/dx#srz^'
    var31 = '%'
    var32 = 'u\rt1\r5A@[YK:z2+e'
    var33 = -3751.85
    var34 = module0.Parser(var30, var31, var32, var33)
    assert var34 is not None
    var35 = var34.__setitem__(var28, var29)
    assert var35 is None
    var36 = var4.update(var34)
    assert var36 is None


def test_analyze_ordered():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None
    var8 = 'mvTUWEE6l4\x0c'
    var9 = var7.analyze_ordered_dict_object(var8)
    assert var9 == 'mvTUWEE6l4\x0c'


def test_dump():
    var0 = '^!&@-I\x0b91+IPf~a\tC"a'
    var1 = b'\xe6`k\xb6\x84\x96\x8e\n\xd6\x90\xd4'
    var2 = b'\x12gu\xf5\x9f\xde^#\xfdA\xf2eF\xefH\xae\xbe+'
    var3 = '80T\tI'
    var4 = module0.Parser(var0, var1, var2, var3)
    assert var4 is not None
    var5 = var4.dump_it()
    assert var5 is None
    var6 = b'\xe8\xb8\x8f`\x00'
    var7 = module0.Parser(var0, var4, var6, var4)
    assert var7 is not None
    var8 = var7.dump_it()
    assert var8 is None
    var9 = var7.dump_it()
    assert var9 is None


def test_update_value():
    var0 = False
    var1 = 784
    var2 = 'VUz;/a/dx#srz^'
    var3 = '%'
    var4 = 'u\rt1\r5A@[YK:z2+e'
    var5 = -3751.85
    var6 = module0.Parser(var2, var3, var4, var5)
    assert var6 is not None
    var7 = var6.__setitem__(var0, var1)
    assert var7 is None
    var8 = None
    var9 = var6.update(var8)
    assert var9 is None


def test_parser_exception():
    try:
        var0 = b'/"\xb6\xd1\xdd#cu\xd7V\x8fIB'
        var1 = 562
        var2 = b'-E~\x0c\xd0\xcee\x91\x19\xc7\x85\x1b'
        var3 = True
        var4 = "5!`Ak3_$^+:_;*gNa`/'"
        var5 = module0.Parser(var1, var2, var3, var4)
    except BaseException:
        pass


def test_bool_exception():
    try:
        var0 = True
        var1 = -834.313
        var2 = 2756.11
        var3 = b'\x1fQ\x0e\xd5n\x93'
        var4 = -558
        var5 = module0.Parser(var1, var2, var3, var4)
    except BaseException:
        pass


def test_none_exception():
    try:
        var0 = None
        var1 = 2616
        var2 = '1\x0c'
        var3 = '>lK}nh'
        var4 = module0.Parser(var1, var2, var3, var3)
    except BaseException:
        pass


def test_float_exception():
    try:
        var0 = None
        var1 = False
        var2 = None
        var3 = 6030.779011
        var4 = module0.Parser(var0, var1, var2, var3)
    except BaseException:
        pass


def test_int_exception():
    try:
        var0 = -1685
        var1 = 343
        var2 = module0.Parser(var0, var0, var0, var1)
    except BaseException:
        pass


def test_empty_parse():
    try:
        var0 = 2573.167904
        var1 = 915.58
        var2 = -672
        var3 = -877
        var4 = 'Me5]dIm;ff.U,'
        var5 = (
            b'\x0e\xaa\x12\xc0\x9f\xe8\xc3\x87\xabS\xda\xde\x91i\xb7\xf2\x87\xb0'
            )
        var6 = module0.Parser(var4, var5, var2, var5)
        assert var6 is not None
        var7 = module0.Parser(var1, var2, var3, var6)
    except BaseException:
        pass



