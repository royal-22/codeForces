n, k = input().split()
n, k = int(n), int(k)
while n > 0 and k > 0:
    if n%10 == 0:
        n //= 10
    else:
        n -= 1
    k -= 1

print(n)
