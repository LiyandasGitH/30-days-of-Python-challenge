def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
        
def find_nth_prime(limit):
    prime_num = []
    for number in range(2, limit + 1):
        if is_prime(number):
            prime_num.append(number)
    return prime_num