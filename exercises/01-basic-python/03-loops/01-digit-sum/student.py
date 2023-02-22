# Write your code here
def digit_sum(x):
    test = 0
    while x > 0:
        test += last_digit(x)
        x=remove_last_digit(x)
    return test


def last_digit(x):
    return x % 10


def remove_last_digit(x):
    return x//10
