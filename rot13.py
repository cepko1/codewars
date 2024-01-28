def rot13(message):
    inp = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    new_message = ''
    for symbol in message:
        new_message += out[inp.index(symbol)] if symbol in inp else symbol
    return new_message


print(rot13('OKO'))
