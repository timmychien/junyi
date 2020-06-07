#1-B
def reverse_only_word(sentence):
  sent_list=list(sentence)
  spaces=0
  temp=[]
  new_sentence=[]
  sentence=sentence.split()
  for words in sentence:
    temp.append([words])
    temp.append([' '])
  for w in range(len(temp)):
    for word in temp[w]:
      word=list(word)
      for i in range(len(word)):
        p=word.pop()
        print(p)
        new_sentence.append(p)
  new_sentence=''.join(new_sentence)
  return new_sentence