while (True):
    dec_num = int(input("введите число в десятичной системе: "))

    result = ""
    while dec_num > 0:
        result = str(dec_num % 2) + result
        dec_num = dec_num // 2

    print(result)