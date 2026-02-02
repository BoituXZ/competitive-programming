try:
    n = int(input())
except EOFError:
    n = 0

phone_book = {}
for i in range(n):
    name, number = input().split()
    phone_book[name] = number

while True:
    try:
        quer = input().strip()
        
        if not quer:
            continue
            
        if quer in phone_book:
            print(f"{quer}={phone_book[quer]}")
        else:
            print("Not found")
            
    except EOFError:
        break
