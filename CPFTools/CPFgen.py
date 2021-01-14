def CPFgenerator():
    from random import randint
    number = randint(100000000, 999999999)
    digit = ['','']
    total = 0
    count = 10
    for n in str(number):
        numb = int(n)
        total += numb * count
        count -= 1
    if 11 - (total % 11) > 9:
        digit[0] = '0'
        count = 11
        total = 0
        for n in str(number):
            numb = int(n)
            total += numb * count
            count -= 1
        if 11 - (total % 11) > 9:
            digit[1] = '0'
            cpf = str(number) + digit[0] + digit[1]
        else:
            d = 11 - (total % 11)
            digit[1] = str(d)
            cpf = str(number) + digit[0] + digit[1]
    else:
        d = 11 - (total % 11)
        digit[0] = str(d)
        count = 11
        total = 0
        for n in str(number):
            numb = int(n)
            total += numb * count
            count -= 1
        total += count * d
        if 11 - (total % 11) > 9:
            digit[1] = '0'
            cpf = str(number) + digit[0] + digit[1]
        else:
            d = 11 - (total % 11)
            digit[1] = str(d)
            cpf = str(number) + digit[0] + digit[1]
    count = 0
    strCPF = ''
    for _ in cpf:
        strCPF += cpf[count]
        count += 1
        if count == 3 or count == 6:
            strCPF += "."
        elif  count == 9:
            strCPF += "-"
    return strCPF