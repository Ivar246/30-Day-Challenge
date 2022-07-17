word = 'EXACTLY'
length = len(word)

new = ''.join([s.lower() if word.index(s) == (len(word)/2)-1  else s for  s in word])

print(new)