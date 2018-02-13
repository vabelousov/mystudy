'''
This file is for trying python3 features
Vladimir Belousov
'''
import urllib.request
u = urllib.request.urlopen('http://www.avito.ru')

words = {}

for ln in u:
  
  line = str(ln).strip(' \n')
  for word in line.split(' '):
    if len(word) > 0:
      try:
        words[word] += 1
      except KeyError:
        words[word] = 1

pairs = words.items()
sorted_x=sorted(pairs, key=lambda x: x[1], reverse=True)
for p in sorted_x[:10]:
  print('Слово ['+p[0]+'] встречается '+str(p[1])+' раз.')
