import csv

class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a {self.age} year old {self.breed}"

animal_type = input("What type of animal are you interested in? ")
if animal_type.lower() == "dogs":
    with open("data/dogs.csv", "r") as file:
    # file = open("data/dogs.csv")
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(Animal(row[0],row[1],row[2])) 
    # file.close()

elif animal_type.lower() == "cats":
    with open("data/cats.csv", "r") as file:
    # file = open("data/cats.csv")
        reader = csv.reader(file)
        next(reader)
        for row in reader:
            print(Animal(row[0],row[1],row[2]))
    # file.close()

else:
    print(f"Sorry, we don't have any {animal_type} here")




