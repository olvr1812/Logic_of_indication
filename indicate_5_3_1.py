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

if v_s[0] == 1 and v_s[1] == 1:
    if p_s[1] == 0:
        if p_s[0] == 1:
            print("Вариант 1")
        else:
            print('Вариант 3')
    else:
        if p_s[0] == 1:
            print("Вариант 2")
        else:
            print("Вариант 4")
else:
    print("Вариант 5")