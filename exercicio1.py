codigo = int(input("Digite o código: "))

match codigo:
    case 1:
        print("Caneta - R$1.20")
    case 2:
        print("Lapis - R$0.80")
    case 3:
        print("Caderno - R$4.50")
    case 4:
        print("Borracha - R$1.00")
    case 5:
        print("Regua - R$1.50")
    case _:
        print("Codigo invalido!")