def strip_comments(strng, markers):
    splittStr = strng.split('\n')
    new = []
    for text in splittStr:
        for marker in markers:
            if marker in text:
                text = text[:text.find(marker)]
        new.append(text.rstrip())
    return '\n'.join(new)


print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))