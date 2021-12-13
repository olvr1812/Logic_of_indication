def create_array(test_string):
   test_string = test_string.split(',')
   test1 = []
   for i in test_string:
      test1.append(int(i))
   return test1

v_s = input('Введите тест валидности сигналов:\n')
p_s = input('Введите тест значений параметров сигнала:\n')

v_s = create_array(v_s)
p_s = create_array(p_s)

# Логика индикации
# БРУС крен
if v_s[0] == 1 or v_s[1] == 1 or v_s[2] == 1 or v_s[3] == 1:
   XKE_L = (p_s[0] * v_s[0] + p_s[1] * v_s[1] + p_s[2] * v_s[2] + p_s[3] * v_s[3]) / sum(v_s[:4])
   XKE_L_valid = 1
else:
   XKE_L_valid = 0
   XKE_L = 'Error'

# БРУС тангаж
if v_s[4] == 1 or v_s[5] == 1 or v_s[6] == 1 or v_s[7] == 1:
   XKV_L = (p_s[4] * v_s[4] + p_s[5] * v_s[5] + p_s[6] * v_s[6] + p_s[7] * v_s[7]) / sum(v_s[4:])
   XKV_L_valid = 1
else:
   XKV_L_valid = 0
   XKV_L = 'Error'

print('XKE_L = ', XKE_L, '\nXKE_L_valid = ', XKE_L_valid, '\nXKV_L = ', XKV_L, '\nXKV_L_valid = ', XKV_L_valid)