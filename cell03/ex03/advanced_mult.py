out = 0
while(out < 11):
    ins = 0
    print(f"Table de {out}: ", end="")
    inn = 0
    while inn < 11:
        print(out * inn, end=" ")
        inn+=1
    print()
    out+=1
