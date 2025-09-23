while (True):
    input_number = int(input("введите число в двоичной системе: "))

    result = 0
    position = len(str(input_number)) - 1

    for i in str(input_number):
        result += int(i) * (2 ** position)                               
        position -= 1

    print(result) 