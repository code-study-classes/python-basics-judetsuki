check_between_numbers = lambda a, b, c: ((b > a) and (b < c)) or ((b < a) and (b > c))

check_odd_three = lambda num: (len(str(abs(num))) == 3) and (num % 2 != 0)


check_unique_digits =  lambda num: (len(set(str(abs(num)))) == 3)


def check_palindrome_number(num):
        num_str = str(abs(num))
        return num_str == num_str[::-1]

check_ascending_digits = lambda num: (len(str(abs(num)) == 3) and (abs(num) // 100 < (abs(num) // 10) % 10 < abs(num) % 10))