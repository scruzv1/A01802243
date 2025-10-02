
# E1

print("Excercise 1")

print("Temperaturas de la semana")
print("Ingresa la temperatura de cada día de la semana")

temperaturas=[]
total=0


for i in range(1,8):
    dia = int(input(f"Día{i}: "))
    temperaturas.append (dia)
    total = total + dia
#guardamos temperaturas


#sacamos el promedio

promedio = total / 7

print(f"Temoperatura promedio {promedio}")
#clasificamos las temperaturas
print("Temperaturas:")


for i in range(0,7):

    if (temperaturas [i] > promedio):
        print(f"{temperaturas[i]}  above average")
    elif (temperaturas[i]<promedio):
        print(f"{temperaturas[i]} below average")
    else:
        print(f"{temperaturas[i]} equal to average")


# E2

print("Excercise 2")

students = ["Juan", "Pedro", "Pepe", "Patricio", "Agripino", "Eustakio"]

grades = [85, 55, 72, 40, 91, 66]

#Group average
average = sum(grades) / len(grades)
print(f"Group average: {average:.2f}")

#Percentage of fail
failed = [grade for grade in grades if grade < 60]
fail_percentage = (len(failed) / len(grades)) * 100
print(f"Percentage of failed students: {fail_percentage:.2f}%")

#Students who passed
passed_students = [students[i] for i in range(len(students)) if grades[i] >= 60]
print("Students who passed:", passed_students)




# E3

print("Excercise 3")

#Shopping list
items = ["Milk", "Bread", "Eggs", "Apples", "Rice", "Coffee"]

#Purchased or not
purchased = [False, True, False, False, True, False]

#Items that arent purchased
print("Items not purchased yet:")
for i in range(len(items)):
    if not purchased[i]:
        print(f"{items[i]}")

#Ask if purchased
for i in range(len(items)):
    if not purchased[i]:
        answer = input(f"Have you purchased {items[i]}? (yes/no): ")
        #update the list
        if answer == "yes":
            purchased[i] = True 

# Final list
print("Updated shopping list:")
for i in range(len(items)):
    final = "Purchased" if purchased[i] else "Not purchased"
    print(f"{items[i]}  {final}")



# E4

print("Excercise 4")

#List
numbers = [42, 7, 19, 73, 4, 56, 88, 12]

#Max values
maxValue = max(numbers)
print(f"Max values: {maxValue}")

#Min values
minValue = min(numbers)
print(f"Min values: {minValue}")

#Ordered list
orderedList = sorted(numbers)
print(f"Numbers in order: {orderedList}")

# E5

print("Excercise 5")

#Integers
numbers = [12, 7, 25, 40, 33, 18, 9, 4]

# Separate into even and odd lists
evenNumbers = [num for num in numbers if num % 2 == 0]
oddNumbers = [num for num in numbers if num % 2 != 0]

# Show results
print("Integers:", numbers)
print("Even numbers:", evenNumbers)
print("Odd numbers:", oddNumbers)


# E6

print("Excercise 6")

#Usernames
userNames = ["alice", "bob", "charlie", "diana", "bob"]

#Check if duplicated
duplicates = {name for name in userNames if userNames.count(name) > 1}
if duplicates:
    print("Duplicated users", duplicates)

#Ask new usernames
while True:
    newUser = input("Enter a new username:")
    if newUser in userNames:
        print("That user already exists, choose another one")
    else:
        userNames.append(newUser)
        print(f"User '{newUser}' created")
        break

print("New users list:", userNames)