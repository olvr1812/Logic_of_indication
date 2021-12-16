from openpyxl import load_workbook
wb = load_workbook(filename='logic.xlsx', read_only=True)
ws = wb['6_3_8']
list1 = []
list2 = []
list3 = []
for i in ws.rows:
    #break
    for k in i:
        if k == i[0]:
            list1.append(k.value)
        elif k == i[1]:
            list2.append(k.value)
        elif k == i[2]:
            list3.append(k.value)

print(list1, list2, list3, sep="\n")

