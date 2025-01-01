# Accept an integer n as input
#n = int(input("Enter an integer n: "))
#nn = n * 11 # Compute nn by multiplying n by 11
#nnn = n * 111 # Compute nnn by multiplying n by 111
#s = n + nn + nnn
#print(f"{n}+{nn} + {nnn} = {s}")

#n=int(input("Enter a number : "))
#s=(n+11*n+111*n)
#print(f"{n}+{nn} + {nnn} = {s}")

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"Original List :{list1}")
# Using a list comprehension to remove even numbers
list2 = [x for x in list1 if x % 2 != 0]
print(f"List of odd numbers :{list2}")
