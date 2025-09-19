age = int(input("What is your age?"))

if age >= 18:
    print("Muy bien, ya estás grandecito")
else:
    print("Váyase a jugar niño")


if age >= 13 and age <= 19:
    print("Eres teenager")
elif age <= 12:
    print("Váyase a jugar niño")
else:
    print("Sáquese de aquí")

birthYear = int(input("What is your birth year?"))
birthdayCheck=input(f"You have {2025-birthYear}?")

if birthdayCheck == "Yes" or "Si" or "Ei":
    print("So your birthday already passed!")
elif birthdayCheck == "No" or "no" or "Noooo":
    print(f"So you have{2025-birthYear+1}")
else:
    print("Invalid, type Yes, Si, Ei, No, no or Noooo")
