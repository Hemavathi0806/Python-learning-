	# 1.what is list in python?
#list means set of elements or collection of multiple elements stored in one variable
#2.Create a list of 5 fruits and print it.
fruits=["watermelon","mango","gauva","cherry","grapes"]
print(fruits)
#3.Create a list of numbers and print the first element.
nums=[10,8,11,22]
print(nums[0])
#4.How do you add an item to a list?
fruits=["watermelon","mango","gauva","cherry","grapes"]
fruits.append("strawberry")
print(fruits)
fruits.insert(0,"chikki")
print(fruits)
#5.Write a program to add "Mango" to a fruit list.
fruits=["watermelon","gauva","cherry","grapes"]
fruits.append("mango")
print(fruits)
#6.How do you remove an item from a list?
fruits=["watermelon","gauva","cherry","grapes"]
fruits.remove("cherry")
print(fruits)
#7.Create a student marks list and print all elements using a loop
marks_list = [100, 99, 98, 86, 65, 56]

for marks in marks_list:
    print(marks)
#8.What is the difference between append() and insert()?
#append()-adds an item to the end of the list.
#insert()-adds an item at a specific location or index
#9.Write a Python program to find the length of a list.
fruits=["watermelon","gauva","cherry","grapes"]
print(len(fruits))
#10.create a list
colors = ["Red", "Blue", "Green"]
#change blue to yellow

colors[1]="yellow"
print(colors)
#11.Write a program to sort a list of numbers.
numbers=[12,3,38,3668,1,65,23]
numbers.sort()
print(numbers)
#12.How do you reverse a list?
numbers = [10, 20, 30, 40, 50]
numbers.reverse()
print(numbers)
#13.How do you check whether an item exists in a list?
fruits = ["apple", "mango", "grapes"]
print("mango" in fruits)
   
      
      

