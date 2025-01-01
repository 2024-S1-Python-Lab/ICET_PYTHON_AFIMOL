#list1=set(['Blue','Black', 'Green','Red','Orange'])
#list2=set(['Red','Brown','Orange','Pink'])
#print(list1.difference(list2))

#s1=input("Enter first string: ")
#s2=input("Enter second string: ")
#print(s2[0]+s1[1:]," ",s1[0]+s2[1:])

# Sample dictionary
#my_dict = {'banana': 3, 'apple': 1, 'cherry': 2, 'date': 4}
#print("Original list:", my_dict)
# Sort in ascending order based on keys
#asorted_dict = dict(sorted(my_dict.items()))
#print("Ascending order:", asorted_dict)
# Sort in descending order based on keys
#dsorted_dict = dict(sorted(my_dict.items(), reverse=True))
#print("Descending order:", dsorted_dict)

#dict1 = {"name": "Alice", "age": 25}
#dict2 = {"name":"ammu","occupation": "Software Engineer", "hobbies": ["reading", "writing", "coding"]}
# Merge dict2 into dict1
#dict1.update(dict2)
#print(dict1)

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
if num1 < num2:
    min = num1  # Find the minimum of the two numbers

else:
    min = num2

gcd = 1 # Initialize GCD to 1 (as GCD is always at least 1)
# Iterate from 1 to the minimum of the two numbers
for i in range(1, min + 1):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i


print(f"The GCD of {num1} and {num2} is {gcd}")
