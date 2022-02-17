def create_array(test_string):
   test_string = test_string.split(',')
   test1 = []
   for i in test_string:
      test1.append(int(i))
   return test1

# Input value

v_s = input('Введите тест валидности сигналов:\n')
p_s = input('Введите тест значений параметров сигнала:\n')

v_s = create_array(v_s)
p_s = create_array(p_s)

# Логика

if (v_s[1] == 1 or v_s[2] == 1) and (v_s[3] == 1 or v_s[4] == 1) and v_s[0] == 1 and v_s[5] == 1:
   if (p_s[1] == 0 or p_s[2] == 0) and (p_s[3] == 0 or p_s[4] == 0) and p_s[5] == 0:
      if p_s[0] == 0:
         print("Вариант 1")
      else:
         if p_s[0] > 35:
            print("Вариант 2 | Индицируется максимальное значение (+35)")
         else:
            if p_s[0] > 0:
               print("Вариант 2 | Пропорционально значению параметра TRIM_KE")
            else:
               if p_s[0] < -35:
                  print("Вариант 3 | Индицируется минимальное значение (-35)")
               else:
                  print("Вариант 3 | Пропорционально значению параметра TRIM_KE")
   else:
      if p_s[0] == 0:
         print("Вариант 6")
      else:
         if p_s[0] > 35:
            print("Вариант 4 | Индицируется максимальное значение (+35)")
         else:
            if p_s[0] > 0:
               print("Вариант 4 | Пропорционально значению параметра TRIM_KE")
            else:
               if p_s[0] < -35:
                  print("Вариант 5 | Индицируется минимальное значение (-35)")
               else:
                  print("Вариант 5 | Пропорционально значению параметра TRIM_KE")
else:
   print("Вариант 7")
