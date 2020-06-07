def reverse_word(word):
  word=list(word)
  new_word=[]
  for i in range(len(word)):
    p=word.pop()
    print(p)
    new_word.append(p)
  new_word=''.join(new_word)
  return new_word