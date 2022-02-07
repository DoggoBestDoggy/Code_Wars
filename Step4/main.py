def shortcut(s):
    characters = "aeiou"
    word = ""
    for i in s:
        if not i in characters:
            word += i
    return word
