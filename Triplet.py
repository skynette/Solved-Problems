target = 1000

def is_triple(a,b,c):
    if a**2 + b**2 == c**2:
        return True
    else:
        return False
a=1
b=2
c=target-a-b
for b in range(2,c):
    for a in range(1,b):
        c=target-a-b
        if a+b+c == target:
            if is_triple(a,b,c):
                print("Flag",a,b,c)
                print(a*b*c)

