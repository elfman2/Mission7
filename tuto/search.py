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

print(get_words("The bana.na i;s :  yellow,"))
