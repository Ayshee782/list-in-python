#Write a Python program to create a list with five numbers and print it.
a=[12,13,34,45,56]
print(a)
b = [int(x) for x in input("Enter numbers separated by space: ").split()]
print(b)
c=list(map(int,input("enter 5 number=").split()))
print(c)