XKE_L, XKE_R, XKV_L, XKV_R = int(input('Положение левой БРУ по крену:\n')), int(input('Положение правой БРУ по крену:\n')), int(input('Положение левой БРУ по тангажу:\n')), int(input('Положение правой БРУ по тангажу:\n'))

XKE = (XKE_L + XKE_R)
XKV = (XKV_L + XKV_R)

print('XKE = ', XKE, '\nXKV = ', XKV)