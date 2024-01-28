def generate_hashtag(s):
    if not s or len(s) > 140:
        return False
    new = '#'
    flag = True
    for symbol in s:
        if symbol == " ":
            flag = True
        else:
            new += symbol.title() if flag else symbol.lower()
            flag = False
    return new

print(generate_hashtag('Codewars Is Nice'))
