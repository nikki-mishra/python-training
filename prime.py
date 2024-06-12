def is_prime(n):
    # returns 0 if it is prime, else 1
    p = 0
    j = 2
    while j < n:
        if n % j == 0:
            p = 1
            break
        j = j + 1
    return p



i = 1
s = 0

while i < 50:
    x = is_prime(i)
    if x == 0:
        s = s + i
    i = i + 1

print(s)














