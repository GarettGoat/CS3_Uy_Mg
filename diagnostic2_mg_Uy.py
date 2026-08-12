def calculate_total(topping_count):
    if topping_count < 0:
        print("error")
        return 0
    elif topping_count == 0:
        return 10.00
    else:
        return 10.00 + (topping_count * 1.50)
