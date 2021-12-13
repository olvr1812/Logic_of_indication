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

if v_s[0] == 1 and v_s[1] == 1 and v_s[2] == 1:
   if p_s[1] == 0 and p_s[2] == 0:
      if p_s[0] == 0:
         print("Вариант 1")
      else:
         if p_s[0] < -27:
            print("Вариант 3 | Индицируется минимальное значение (-27)")
         else:
            if p_s[0] < 0:
               print("Вариант 3 | Линейно пропорционально значению параметра ELEV_L_CONS")
            else:
               if p_s[0] > 22:
                  print("Вариант 2 | Индицируется максимальное значение (22)")
               else:
                  print("Вариант 2 | Линейно пропорционально значению параметра ELEV_L_CONS")
   else:
       if p_s[0] == 0:
           print("Вариант 4")
       else:
           if p_s[0] < -27:
               print("Вариант 6 | Индицируется минимальное значение (-27)")
           else:
               if p_s[0] < 0:
                   print("Вариант 6 | Линейно пропорционально значению параметра ELEV_L_CONS")
               else:
                   if p_s[0] > 22:
                       print("Вариант 5 | Индицируется максимальное значение (22)")
                   else:
                       print("Вариант 5 | Линейно пропорционально значению параметра ELEV_L_CONS")
else:
   print("Вариант 7")
