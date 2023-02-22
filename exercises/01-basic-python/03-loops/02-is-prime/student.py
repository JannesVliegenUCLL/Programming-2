# Write your code here
def is_prime(n):
    teller = 0
    for x in range(2, n):
        if n % x == 0 and x != n:
            teller += 1
    if teller == 0 and n!=0 and n!=1:
        return True
    else:
        return False
