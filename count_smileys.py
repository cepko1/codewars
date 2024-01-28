def count_smileys(arr):
    def valid(smile):
        flag = False
        if len(smile) == 2:
            flag = True if (smile[0] == ':' or smile[0] == ';') and (smile[-1] == ')' or smile[-1] == 'D') else False
        if len(smile) == 3:
            flag = True if (smile[0] == ':' or smile[0] == ';') and (smile[-1] == ')' or smile[-1] == 'D') and (smile[1] == '-' or smile[1] == '~') else False
        return flag
    smiles = 0
    for smile in arr:
        if valid(smile):
            smiles += 1
    return smiles


# print(count_smileys([':D',':~)',';~D',':)']))

