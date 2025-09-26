print("Варианты действий:")
print("1) [+] [-] [*] [/] [^] [%]", "2) [извлечь корень]","3) [решить квадратное уравнение]", sep="\n")
choice = input("выберите действие ")


match choice:
        case "1":
            num_1 = float(input("первое число "))
            operator = input("операция ")
            num_2 = float(input("второе число "))

            match operator:
                case "+":
                    print(num_1 + num_2)
                case "-":
                    print(num_1 - num_2)
                case "*":
                    print(num_1 * num_2)
                case "/":
                    if num_2 != 0:
                        print(num_1 / num_2)
                    else:
                        print("ошибка")
                case "^":
                    print(num_1 ** num_2)
                case "%":
                    print(num_1 % num_2)
        case "2":
            num_koren = float(input("число для выведения корня: "))
            if num_koren >= 0:
                print(num_koren ** 1/2)
            else:
                print("ошибка")
        case "3":
            a = float(input("коэф 'a': "))
            b = float(input("коэф 'b': "))
            c = float(input("коэф 'c': "))
            if a != 0:
                D = b ** 2 - 4 * a * c
                if D > 0:
                    x_1 = (-b - pow(D,0.5)) / (2 * a)
                    x_2 = (-b + pow(D,0.5)) / (2 * a)
                    print("корни равны: ", x_1, x_2)
                elif D == 0:
                    x = -b / (2 * a)
                    print(x)
                else:
                    print("нет действительных корней")
            else:
                print("коэф a не может быть 0 (ОШИБКА)")
        case _:
            print("ошибка")