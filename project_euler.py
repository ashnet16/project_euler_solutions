""" Solution to Project Euler Problem 1"""


def multiples_of_3_or_5():
    result = 0
    for num in range(1000):
        if num % 3 == 0 or num % 5 == 0:
            result += num
    return result


""" Solution to Project Euler Problem 2"""


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


""" Solution to Project Euler Problem 3

All prime numbers are odd except for 2

"""


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


""" Solution to Project Euler Problem 4

Largest Palindrome two numbers and three digits """


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


"""
Solution to Project Euler Problem 5
We know that 2520 and all it's multiples are divisible by 1-10

"""


def smallest_multiple():
    starting_point = 2520
    is_num = False
    while not is_num:
        check = True
        for num in range(20, 0, -1):
            test = starting_point % num
            if test != 0:
                check = False
                break
        if not check:
            starting_point += 2520
        else:
            is_num = True
    return starting_point


"""
Solution to Project Euler Problem 6
"""


def sum_square_difference(range_num: int):
    sum_of_square = 0
    square_of_sum = 0
    for num in range(1, range_num + 1):
        sum_of_square += num ** 2
        square_of_sum += num
    return (square_of_sum ** 2) - sum_of_square


""" Solution to Project Euler Problem 7 """


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


""" Solution to Project Euler Problem 8 """


def product_series(int_list: list, limit: int):
    product = 0
    slow = 0
    size = len(int_list)
    while slow <= (size - limit):
        inner_product = int_list[slow]
        fast = slow + 1
        inner_counter = 0
        while inner_counter < limit - 1:
            inner_product *= int_list[fast]
            inner_counter += 1
            fast += 1
        if inner_product > product:
            product = inner_product
        slow += 1
    return product


""" 

Solution to Project Euler Problem 9

a + b + c = sum
   c = sum -b -a
"""


def pythagorean_triple(sum_input: int):
    for a in range(1, sum_input):
        for b in range(a + 1, sum_input - a):
            c = sum_input - a - b
            if a ** 2 + b ** 2 == c ** 2:
                return a * b * c
    return -1


""" Solution to Project Euler Problem 10 n represents a limit. 
This is my naive approach and it is too slow.
"""


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


""" Solution to Project Euler Problem 10 Optimized"""


def summation_of_primes_fast(n: int):
    sum_int = 0
    for num in prime_generator(n):
        sum_int += num
    return sum_int


"""
For all natural numbers between 2 and the limit + 1
determine if prime by analyzing multiples of numbers.
Performing multiplication is much faster than division

"""


def prime_generator(n):  # Sieve of Eratosthenes
    prime, composite = [], set()
    for num in range(2, n + 1):
        if num not in composite:
            prime.append(num)
            composite.update(range(num * num, n + 1, num))
    return prime


def horizontal_product(grid: list, limit: int):
    largest_product = 0
    for row in range(len(grid) - limit):
        largest_product_of_row = product_series(grid[row], limit)
        if largest_product_of_row > largest_product:
            largest_product = largest_product_of_row
    return largest_product


def vertical_product_helper(grid: list, limit: int, col: int):
    a = 0
    max_product_of_col = 0
    while a <= 20 - limit:
        inner_product = grid[a][col]
        b = a + 1
        count = 0
        while count < limit - 1:
            inner_product *= grid[b][col]
            count += 1
            b += 1
        if inner_product > max_product_of_col:
            max_product_of_col = inner_product
        a += 1

    return max_product_of_col


def vertical_product(grid: list, limit: int):
    largest_product = 0
    column = 0
    while column < 20:
        max_of_col = vertical_product_helper(grid, limit, column)
        if max_of_col > largest_product:
            largest_product = max_of_col
        column += 1
    return largest_product


def int_grid_creator(num_block: list, length: int, width: int):
    grid = []
    for x in range(length):
        block = []
        position = width * x
        for y in range(position, position + width):
            block.append(num_block[y])
        grid.append(block)
    return grid


def adjacent_product_up_down(grid: list, limit: int):
    max_product = 0
    column = 0
    while column <= 20 - limit:
        max_of_adj = adjacent_product_helper_up_down(grid, limit, column)
        if max_of_adj > max_product:
            max_product = max_of_adj
        column += 1
    return max_product


def adjacent_product_helper_up_down(grid: list, limit: int, col: int):
    max_product = 0
    a = col
    while a <= 20 - limit:
        b = a + 1
        count = 0
        inner_product = grid[a][a]
        while count < limit - 1:
            inner_product *= grid[b][b]
            count += 1
            b += 1
        a += 1
        if inner_product > max_product:
            max_product = inner_product

    return max_product


def adjacent_product_helper_down_up(grid: list, limit: int, row: int):
    max_product = 0
    column = 0
    row_num = row
    while row_num >= row - (row - limit + 1):
        b_row = row_num - 1
        b_column = column + 1
        count = 0
        inner_product = grid[row_num][column]
        while count < limit - 1:
            inner_product *= grid[b_row][b_column]
            count += 1
            b_row -= 1
            b_column += 1
        row_num -= 1
        column += 1
        if inner_product > max_product:
            max_product = inner_product

    return max_product


def adjacent_product_down_up(grid: list, limit: int):
    max_product = 0
    for num in range(len(grid) - 1, -1, -1):
        max_of_adj = adjacent_product_helper_down_up(grid, limit, num)
        if max_of_adj > max_product:
            max_product = max_of_adj
    return max_product


""" Solution to Project Euler Problem 11:
    Largest product in a grid
"""


def largest_product_grid(grid: list, limit: int):
    return max([adjacent_product_up_down(grid, limit), vertical_product(grid, limit), horizontal_product(grid, limit),
                adjacent_product_down_up(grid, limit)])


""" Solution to Project Euler Problem 12 :
    Highly divisible triangular number
    The nth triangular number is n(n+1)/2
"""


def find_highly_div_tri_num(div_limit: int):
    num = 1
    divs = 0
    result = 0
    while divs < div_limit:
        result = find_nth_triangular_number(num)
        divs = len(find_div_of_number(result))
        num += 1
    return result


def find_div_of_number(num: int):
    divisors = set()
    divisors.add(1)
    divisors.add(num)
    for prime_num in prime_generator(num):
        if num % prime_num == 0:
            divisors.add(prime_num)
            divisors.add(num // prime_num)
    return divisors


def find_nth_triangular_number(n: int):
    return n * (n + 1) // 2
