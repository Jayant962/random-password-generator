import random
lower="abcdefghijklmnopqrstuvwxyz"
upper="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers="0123456789"
symbols="[]{}()*;/,._-"
all=numbers+upper+lower+symbols
length=8
password="".join(random.sample(all,length))
print(password)