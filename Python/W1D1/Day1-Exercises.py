# Topic: Python Output
# Level: Beginner
# Problem 1: Print "Hello, Python!"

print("Hello, Python");

# Topic: Variables
# Level: Beginner
# Problem 2: Create a variable called name and store your name. Print the variable.

name = "Varun";
print(name);

# Topic: Variables
# Level: Beginner
# Problem 3: Create a variable age and store your age. Print: I am 21 years old

age = 21;
print("I am", age, "years old");

# Topic: Variables
# Level: Beginner
# Problem 4: Create variables: city = Chennai, country = India. Print both variables.

city = "Chennai";
country = "India";
print(f"I am living in {city}, {country}");

# Topic: Datatypes
# Level: Beginner
# Problem 5: Store these values: 25, 5.8, "Python", True. Print their types using type()

age, price, language_name, is_active = 25, 5.8, "Python", True; #tuple unpacking method of declaring variables

print(
  f"Value: {age} {type(age)}\n",
  f"Value: {price} {type(price)}\n",
  f"Value: {language_name} {type(language_name)}\n",
  f"Value: {is_active} {type(is_active)}\n",
  sep="" #to remove the extra space from second line.
)

# Topic: Output + Variables
# Level: Intermediate
# Problem 6: Create variables: name, age, city. Print: Hi I'm Varun. I am 21 years old. I live in Chennai. (In separate lines)

name, age, city = "Varun", 21, "Chennai";

print(
  f"Hi I'm {name}\n",
  f"I'm {age} years old\n",
  f"I live in {city}\n",
  sep=""
)

# Topic: Type Conversion
# Level: Intermediate
# Problem 7: Convert: age = 21, into a string and print its datatype.

age = 21;
print(f"Age is: {age}, Type: {type(age)}\n");

age = str(age);
print(f"Age is: {age}, Type: {type(age)}");

# Topic: Float Conversion
# Level: Intermediate
# Problem 8: Convert: marks = "89.5". into a float and print the value and datatype.

mark = "89.5";
print(f"Mark: {mark}, Type: {type(mark)}\n");

mark = float(mark);
print(f"Mark: {mark}, Type: {type(mark)}");

#Mini Challenge 1
#Create variables for:
#Name, Age, Height, Weight, Favorite Sport, Is Student
#Print:
#------ MY PROFILE ------
#Name:
#Age:
#Height:
#Weight:
#Favorite Sport:
#Student:
#------------------------

name, age, height, weight, favorite_sports, is_student = "Varun", 21, "182CM", "74KG", "Cricket", True;

print(
  f"------ MY PROFILE ------\n",
  f"Name: {name}\n",
  f"Age: {age}\n",
  f"Height: {height}\n",
  f"Weight: {weight}\n",
  f"Favorite Sport: {favorite_sports}\n",
  f"Student {is_student}",
  f"------------------------",
  sep=""
)