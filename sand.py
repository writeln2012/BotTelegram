from itertools import count

f = open('TOKEN')
TOKEN = str(f.read(90))
numb = 0
for i in TOKEN:
    numb +=1
print(numb)
print(TOKEN)
f.close()
