#Comments
print("Hello, Python!") #This prints hello python
print("Hii, # there") #This is considered as string 

#Numbers and Math
print("I will now count my chickens:")
print("Hens", 25 + 30 / 6)  #Here first the / (div) is performed and + (add) is performed

print("Roosters", 100 - 25 * 3 % 4) #25*3=75 75%4=3 result=97

print("Now I will count the eggs:")
print(3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6)  #first % , /, then + and - cal performed

print("Is it true that 3 + 2 < 5 - 7?")
print(3 + 2 < 5 - 7)

print("What is 3 + 2?", 3 + 2)

print("What is 5 - 7?", 5 - 7)

print("Oh, that's why it's False.")

print("How about some more.")

print("Is it greater?", 5 > -2)

print("Is it greater or equal?", 5 >= -2)

print("Is it less or equal?", 5 <= -2, end="\n\n")

# ex4
print("Variables and Names: ", end="\n\n")
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.", end="\n\n")

# ex5
print("More var and printing", end="\n\n")
my_name = 'Zed A. Shaw'
my_age = 35  
my_height = 74 
my_weight = 180  
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall.")
print(f"He's {my_weight} pounds heavy.")
print("Actually that's not too heavy.")
print(f"He's got {my_eyes} eyes and {my_hair} hair.")
print(f"His teeth are usually {my_teeth} depending on the coffee.")

total = my_age + my_height + my_weight
print(f"If I add {my_age}, {my_height}, and {my_weight} I get {total}.") # If I add 35, 74, 180 I get 289

# ex6
print("Strings and Text", end="\n\n")

types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# ex7
print("Excerise 7", end="\n\n")
print("Mary had a little lamb.")
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # what'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"

end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

print(end1 + end2 + end3 + end4 + end5 + end6, end=' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

# ex8
print("Excerise 8", end="\n\n")
formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4)) # replacing {} with 1 2 3 4
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))

# ex9
print("Excerise 9", end="\n\n")
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""", end="\n\n")

# ex10
print("ex10", end="\n\n")
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split on a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""
print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# ex11
# print("ex11", end="\n\n")
# print("which programming language you would like?", end=' ')
# prog_lang = input()
# print(f"what is the use of this {prog_lang} language ?", end=' ')
# use_case = input()
# print(f"which editor you use to code {prog_lang} language?", end=' ')
# editor = input()

# print(f"So, you like {prog_lang} language and the {prog_lang} language is used to {use_case} and you code this language in the {editor} editor.")

# ex12
# print("ex12", end="\n\n")

# prog_lang = input("which programming language you would like? ")

# use_case = input(f"what is the use of this {prog_lang} language ? ")

# editor = input(f"which editor you use to code {prog_lang} language? ")

# print(f"So, you like {prog_lang} language and the {prog_lang} language is used to {use_case} and you code this language in the {editor} editor.")


