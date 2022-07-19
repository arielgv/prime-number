def is_prime(number: int) -> bool:
    n = 0
    for num in range(1, number + 1):   
        if number % num == 0:
            n += 1
    return n == 2

#The function returns True or False if the number is or isnt prime

def run():
    print(is_prime(10))


if __name__ == '__main__':
    run()