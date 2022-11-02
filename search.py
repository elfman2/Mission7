def get_words ( line ):
    r = []
    for c in line.strip(',').split():
        if c.isalpha():
            r.append(c.lower())
    return f"{r}"
print(get_words("The banana is yellow,"))
