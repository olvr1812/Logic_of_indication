import re

regex = re.compile('\s+')
text = """123 nio su 
4456 nio breo
1323 nio planer"""
print(text)



#text = regex.split(text)
print(text)

regex = re.compile('\d+')

print(regex.search(text))
print(regex.findall(text))



