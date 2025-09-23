while (True):
    hours = int(input("текущий час:"))
    if(hours >= 24 or hours <0):
        print("неккоректное время")
        continue

    minutes = int(input("текущая минута:"))
    if(minutes >= 60 or minutes <0):
        print("неккоректное время")
        continue

    delivery_time = int(input("время доставки:"))
    if(delivery_time < 30 or delivery_time > 10 ** 9):
        print("неккоректное время")
        continue

    hours = (hours +(delivery_time + minutes) // 60) % 24
    minutes = (minutes + delivery_time % 60) % 60

    print(f"{hours}:{minutes}") 