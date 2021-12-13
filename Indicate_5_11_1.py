def create_array(test_string):
   test_string = test_string.split(',')
   test1 = []
   for i in test_string:
      test1.append(int(i))
   return test1

v_s = input('Введите тест валидности сигналов:\n')
p_s = input('Введите тест значений параметров сигнала:\n')
T = float(input("Введите время:\n"))

v_s = create_array(v_s)
p_s = create_array(p_s)

if v_s[0] == 1 and v_s[1] == 1 and v_s[2] == 1:
   if abs(p_s[0] - p_s[1]) < 1 and T >= 0.5:
      if v_s[2] == 1 and p_s[2] != (5 or 6 or 7) and p_s[1] < -6 or p_s[1] > 2:
         print("OK")
      else:
         print("Not OK")