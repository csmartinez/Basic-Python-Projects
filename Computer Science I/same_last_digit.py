def same_last_digit(n1, n2, n3):
    #Take in numbers, convert to strings and reverse their order
    n1 = str(n1)
    n2 = str(n2)
    n3 = str(n3)
    n1 =  n1[::-1]
    n2 =  n2[::-1]
    n3 =  n3[::-1]

    #compare first digit, now same place for any size string
    if n1[0] == n2[0] == n3[0]:
        return "True"
    else:
        return "False"
