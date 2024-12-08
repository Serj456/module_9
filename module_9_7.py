def is_prime(func):
    def wrapper(*args):
        original_result = func(args)
        if original_result > 1:
            if original_result == 2:
                return f'{original_result} - простое число'
            if original_result % 2 == 0:
                return f'{original_result} - составное число'
            for i in range(3, int(original_result*0.5)+1,2):
                if original_result % i == 0:
                    return f'{original_result} - составное число'
                else:
                    return f'{original_result} - простое число'
    return wrapper


@is_prime
def sum_three(*args):
    for x in args:
        s = sum(x)
    return s

result = sum_three(2, 3, 6, 551)
print(result)