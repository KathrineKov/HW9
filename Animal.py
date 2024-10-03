#1st task
class Animal:
    def __init__(self, genus, name, year_of_birth, color=None, weight=None):
        self.genus = genus
        self.name = name
        self.year_of_birth = year_of_birth
        self.color = color
        self.weight = weight

    def get_age(self, year):
        return year - self.year_of_birth

    def get_info(self):
        return "{} is a {}".format(self.name, self.genus)

    def get_detailed_info(self):
        info = self.get_info()
        if self.color:
            info += " and is {} in color".format(self.color)
        if self.weight:
            info += " weighing {} kg".format(self.weight)
        return info

#2nd task    
animals = [
    Animal(genus="dog", name="Mars", year_of_birth=2015, color="black", weight=30),
    Animal(genus="elephant", name="Dumbo", year_of_birth=2000, color="gray", weight=5000),
    Animal(genus="python", name="Kaa", year_of_birth=2010, color="brown", weight=50),
    Animal(genus="cat", name="Bosya", year_of_birth=2018, color="white", weight=5),
    Animal(genus="fox", name="Rony", year_of_birth=2017, color="red", weight=8)
]

current_year = 2024

for animal in animals:
    print(animal.get_info())
    print("Age in {}: {}".format(current_year, animal.get_age(current_year)))
    print(animal.get_detailed_info())

#3rd task    
def find_oldest_animal(animals, current_year):
    oldest_animal = animals[0]
    
    for animal in animals:
        age = animal.get_age(current_year)
        if age > oldest_animal.get_age(current_year):
            oldest_animal = animal
    return oldest_animal

oldest_animal = find_oldest_animal(animals, current_year)

print("The oldest animal is {} the {}, and is {} years old.".format(
    oldest_animal.name,
    oldest_animal.genus,
    oldest_animal.get_age(current_year)
))

#4th task
my_file = "animals_info.txt"
file = open(my_file, 'w')

for animal in animals:
    file.write("Name: {}, Genus: {}\n".format(animal.name, animal.genus))
file.close()

file = open(my_file, 'r')
text = file.read()
file.close()
print(text)