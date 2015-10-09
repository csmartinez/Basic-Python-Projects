def second_highest(n1, n2, n3):
    n1 = int(n1)
    n2 = int(n2)
    n3 = int(n3)
    number_list = [n1, n2, n3]
    highest_num = max(number_list)
    number_list.remove(highest_num)
    return max(number_list)
