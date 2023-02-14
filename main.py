int_series = 7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450


def multiples_of_3_or_5():
    result = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


def fibonacci(num: int):
    sum_result = 0
    left = 1
    right = 1
    other = 0

    while other <= num:
        if other % 2 == 0:
            sum_result += other
        left = right
        right = other
        other = left + right
    return sum_result


"""All prime numbers are odd except for 2"""


def larger_prime_factor(num: int):
    prime_counter = 2
    factor_num = num
    while prime_counter < factor_num:
        if factor_num % prime_counter == 0:
            factor_num = factor_num / prime_counter
        else:
            if prime_counter == 2:
                prime_counter += 1
            else:
                prime_counter += 2
    return prime_counter


""" Largest Palindrome two numbers and three digits """


def largest_palindrome():
    result = 0
    for num in range(100, 1000):
        for num2 in range(100, 1000):
            if is_palindrome(num * num2) and num * num2 > result:
                result = num * num2
    return result


def is_palindrome(num: int):
    num_holder = num
    num_reverse = 0
    while num_holder > 0:
        num_reverse = (num_reverse * 10) + (num_holder % 10)
        num_holder = num_holder // 10
    return num == num_reverse


# We know that 2520 and all it's multiples are divisible by 1-10
def smallest_multiple():
    starting_point = 2520
    is_num = False
    while not is_num:
        print(starting_point)
        check = True
        for num in range(20, 0, -1):
            print(num)
            test = starting_point % num
            if test != 0:
                check = False
                break
        if not check:
            starting_point += 2520
        else:
            is_num = True
    return starting_point


def sum_square_difference(range_num: int):
    sum_of_square = 0
    square_of_sum = 0
    for num in range(1, range_num + 1):
        sum_of_square += num ** 2
        square_of_sum += num
    return (square_of_sum ** 2) - sum_of_square


def find_prime_of_large_number(num: int):
    odd_or_prime = 2
    count = 0
    primes_list = []
    while count < num:
        if is_prime(odd_or_prime, primes_list):
            primes_list.append(odd_or_prime)
            count += 1
        if odd_or_prime == 2:
            odd_or_prime += 1
        else:
            odd_or_prime += 2

    return primes_list[-1]


def is_prime(num: int, prime_list: list):
    if num == 2:
        return True
    if not prime_list or num < 2:
        return False
    for prime in range(len(prime_list) - 1, -1, -1):
        if num % prime_list[prime] == 0:
            return False
    return True


""" Returns int list in reverse"""


def convert_to_list_of_ints(num: int):
    list_of_ints = []
    while num > 0:
        list_of_ints.append(num % 10)
        num = num // 10
    return list_of_ints


def product_series(int_list: list, counter: int):
    product = 0
    slow = 0
    size = len(int_list)
    while slow <= (size - counter):
        inner_product = int_list[slow]
        fast = slow + 1
        inner_counter = 0
        while inner_counter < counter - 1:
            inner_product *= int_list[fast]
            inner_counter += 1
            fast += 1
        if inner_product > product:
            product = inner_product
        slow += 1
    return product


""" a + b + c = sum
   c = sum -b -a
"""


def pythagorean_triple(sum: int):
    for a in range(1, sum):
        for b in range(a + 1, sum - a):
            c = sum - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return -1


""" n represents a limit. This is my naive approach and it is too slow"""


def summation_of_primes(n: int):
    odd_or_prime = 2
    prime_sum = 0
    prime_list = []
    while odd_or_prime < n:
        if is_prime(odd_or_prime, prime_list):
            prime_list.append(odd_or_prime)
            prime_sum += odd_or_prime
        if odd_or_prime == 2:
            odd_or_prime += 1
        else:
            odd_or_prime += 2
    return prime_sum


def summation_of_primes_fast(n: int):
    sum = 0
    for num in prime_generator(n):
        sum += num
    return sum


"""
For all natural numbers between 2 and the limit + 1
determine if prime by analyzing multiples of numbers
 
"""


def prime_generator(n):  # Sieve of Eratosthenes
    prime, composite = [], set()
    for num in range(2, n + 1):
        if num not in composite:
            prime.append(num)
            composite.update(range(num * num, n + 1, num))
    return prime


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(summation_of_primes(10))

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
