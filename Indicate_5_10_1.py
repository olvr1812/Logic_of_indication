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

if v_s[0] == 1:
   L11V = 1
   if p_s[0] == 1 or p_s[8] == 1:
      L11F = 1
   else:
      L11F = 0
else:
   L11V = 0

if v_s[1] == 1:
   L12V = 1
   if p_s[1] == 1 or p_s[9] == 1:
      L12F = 1
   else:
      L12F = 0
else:
   L12V = 0

if v_s[2] == 1:
   L21V = 1
   if p_s[2] == 1 or p_s[10] == 1:
      L21F = 1
   else:
      L21F = 0
else:
   L21V = 0

if v_s[3] == 1:
   L22V = 1
   if p_s[3] == 1 or p_s[11] == 1:
      L22F = 1
   else:
      L22F = 0
else:
   L22V = 0

if v_s[4] == 1:
   R11V = 1
   if p_s[4] == 1 or p_s[12] == 1:
      R11F = 1
   else:
      R11F = 0
else:
   R11V = 0

if v_s[5] == 1:
   R12V = 1
   if p_s[5] == 1 or p_s[13] == 1:
      R12F = 1
   else:
      R12F = 0
else:
   R12V = 0

if v_s[6] == 1:
   R21V = 1
   if p_s[6] == 1 or p_s[14] == 1:
      R21F = 1
   else:
      R21F = 0
else:
   R21V = 0

if v_s[7] == 1:
   R22V = 1
   if p_s[7] == 1 or p_s[15] == 1:
      R22F = 1
   else:
      R22F = 0
else:
   R22V = 0

if p_s[16] == 1:
   ans = "Вариант 3"
else:
   if (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) > 6 and (L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 3:
      ans = "Вариант 2"

   elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 7 and (L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 2:
      ans = "Вариант 2"

   elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 5 and (L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 1:
      ans = "Вариант 2"

   elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 3 and (L11F + L12F + L21F + L22F + R11F + R12F + R21F + R22F) > 0:
      ans = "Вариант 2"

   elif (L11V + L12V + L21V + L22V + R11V + R12V + R21V + R22V) < 2:
      ans = "Вариант 3"
   else:
      ans = "Вариант 1"

print(ans)






