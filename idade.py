maior = 0
menor = 0
i1 = int(input('Insira a idade da irma'))
i2 = int(input('Insira a idade da irma'))
i3 = int(input('Insira a idade da irma'))
if(4 < i1 and i1 < 101 and 4 < i2 and i2 < 101 and 4 < i3 and i3 < 101):
    # encontrando o menor
    if(i1 < i2):
        if(i1 < i3):
            menor = i1
        else:
            menor = i3
    else:
        if(i2 < i3):
            menor = i2
        else:
            menor = i3

    # encontrando o maior
    if(i1 > i2):
        if(i1 > i3):
            maior = i1
        else:
            maior = i3
    else:
        if(i2 > i3):
            maior = i2
        else:
            maior = i3
    # encontrando o valor do meio
    if(i1 != maior and i1 != menor):
        print(i1)

    elif(i2 != maior and i2 != menor):
        print(i2)

    else:
        print(i3)
else:
    print('Numeros invalidos')
