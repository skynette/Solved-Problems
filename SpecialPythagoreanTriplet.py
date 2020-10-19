flag = 1000
target = 100000000
target_list = list(range(1,target))
index = 0

# for i in target_list:
a=target_list[index]
b=target_list[index+1]
c=target_list[index+2]

for i in range(target):
    if c==target_list[-1]:
        print("end")
        break
    a=target_list[index]
    b=target_list[index+1]
    c=target_list[index+2]
    aa = pow(a,2)
    bb = pow(b,2)
    cc = pow(c,2)
    # if aa+bb == cc:
    #     print("Triple found",a,b,c)
    #     print("Sum is",a+b+c)
    #     if a+b+c == flag:
    #         print("Flag",a,b,c)
    res = a+b+c
    print("Sum is",res)
    if res>flag:
        print("end")
        break
    index+=1

