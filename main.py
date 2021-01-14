from CPFTools.CPFgen import CPFgenerator
from CPFTools.CPFverify import CPFverifyier

something = True
while something:
    option = input("Hello! Digit 1 for GENERATE CPF, Digit 2 for VERIFY CPF or exit. \nOption: ")
    if option == 'exit':
        something = False
    elif option == '1':
        CPF = CPFgenerator()
        print(CPF)
    elif option ==  '2':
        CPFverifyier()
    else:
        print("Invalid Option!")