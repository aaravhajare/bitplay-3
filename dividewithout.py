import math as m

def divide(de,di) :

    sign = (-1 if ((de < 0) ^ di < 0) else 1)

    de = abs(de)
    di = abs(di)

    qn = 0
    tn = 0

    for i in range(31 , -1, -1) :

        if (tn + (di << i) <= de) :

            tn += di << i
             
            qn |= 1 << i

    if sign == -1 :
        qn = -qn

    return qn
    
a = int(input())
b = int(input())
print(divide(a,b))

# alternat

print(a/b)



