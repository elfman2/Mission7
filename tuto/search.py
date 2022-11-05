from functools import reduce

def readfile(filename):
  with open(filename,'r') as f:
    return f.readlines()

def get_words ( line ):
    word_list = []
    for w in line.split():
      word=''
      for c in w:
        if c.isalpha():
          word = word+c.lower()
      if len(word)>0:
        word_list.append(word)
    return word_list

def create_index(filename):
 index={}
 lines= readfile(filename)
 for i,line in enumerate(lines):
  for w in get_words(line):
     index.setdefault(w,[])
     if i not in index[w]:
       index[w].append(i)
 return index


def get_lines ( words, index ):
  return sorted(reduce(lambda x,y:x&y,[set(index[w]) for w in words]))


print(get_words("The bana.na i;s :  yellow,"))
index=create_index('test.txt')


print(get_lines(['the','of'],index))
