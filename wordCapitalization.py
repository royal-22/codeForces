n = input()

if n[0].isupper():
    print(n)
else: 
    result = n[0].upper() + n[1:]
    print(result)
