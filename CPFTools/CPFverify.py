def CPFverifyier():
    cpf = input("CPF:")
    separate = cpf.split("-")
    firstPart = separate[0].split(".")
    digit = separate[1]
    firstNumbers = firstPart[0] + firstPart[1] +firstPart[2]

    total = 0
    count = 10

    for number in firstNumbers:
        numb = int(number)
        total += numb * count
        count -= 1

    firstDigit = 0
    secondDigit = 0
    count = 11
    if 11 - (total % 11) > 9:
        if digit[0] == str(firstDigit):
            total = 0
            newCPF = firstNumbers + digit[0]
            for number in newCPF:
                numb = int(number)
                total += numb * count
                count -= 1
            if 11 - (total % 11) > 9:
                if digit[1] == 0:
                    print("CPF CORRECT")
                else:
                    print("INVALID CPF")
            else:
                secondDigit = 11 - (total % 11)
                if digit[1] == str(secondDigit):
                    print("CPF CORRECT")
                else:
                    print("INVALID CPF")
        else:
            print("INVALID CPF")
    else:
        firstDigit = 11 - (total % 11)
        total = 0
        newCPF = firstNumbers + str(firstDigit)
        for number in newCPF:
            numb = int(number)
            total += numb * count
            count -= 1
        if 11 - (total % 11) > 9:
            if digit[1] == '0':
                print("CPF CORRECT")
            else:
                print("INVALID CPF")
        else:
            secondDigit = 11 - (total % 11)
            if digit[1] == str(secondDigit):
                print("CPF CORRECT")
            else:
                print("INVALID CPF") 