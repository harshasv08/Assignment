def avr(ar):
    n=0
    for i in ar:
        if isinstance(n, int):
            n+=i
    n=n/len(ar)
    return n



a = eval(input("Enter the array list:"))

result = avr(a)
print("avrage of array values:", result)
