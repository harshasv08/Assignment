def remove_element(arr, element):
    c=[]
    for i in arr:
        if element!=i:
            c+=[i]
    return c

a= [10, 20, 30, 40, 50]
remove = 30

ua = remove_element(a, remove)
print("Original array:", a)
print("Updated array:", ua)
