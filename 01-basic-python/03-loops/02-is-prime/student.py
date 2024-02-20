def is_prime(number):
    div = 2
    while div < number:
        if number % div == 0:
            return False
        div += 1
    if number < div:
        return False
    else:
        return True
