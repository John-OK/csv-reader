import csv
# establish animal class and output template
class Animal:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def __str__(self):
        return f"{self.name} is a{self.age} year old{self.breed}"
# declare function to take in user input and establish animal type
def show_animals():
    animal_type = input("What type of animal are you interested in? ")
    animal = animal_type.lower()
# with string interpolation, attempt to open file with animal type and return information
    try: 
        with open(f"data/{animal}.csv", "r") as file:
            reader = csv.reader(file)
            next(reader)
            for row in reader:
                print(Animal(row[0],row[1],row[2])) 

    # catch error if animal type is not found
    except:
        print(f"Sorry, we don't have any {animal} here")

show_animals()