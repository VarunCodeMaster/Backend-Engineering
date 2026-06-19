# 📚 Day 1: Python Fundamentals

# 1. Getting Started with Python

## What is Python?

Python is a high-level, interpreted, general-purpose programming language.

### High-Level Language

Humans can read and write it easily:

```python
print("Hello World")
```

Compared to C:

```c
printf("Hello World");
```

---

## Why Learn Python?

Python is used in:

* Web Development
* Data Science
* AI and Machine Learning
* Automation
* Cybersecurity
* Game Development
* Desktop Applications

---

## Features of Python

### Easy to Learn

Simple syntax:

```python
name = "Varun"
age = 22
```

---

### Interpreted Language

Python executes code line by line.

**Compiler Languages:**

```
Source Code → Compiler → Machine Code → Execute
```

**Python:**

```
Source Code → Interpreter → Execute
```

This makes debugging easier.

---

### Dynamically Typed

You don't specify data types manually.

```python
age = 20
name = "Varun"
price = 99.5
```

Python automatically decides the type.

---

### Object-Oriented

Everything in Python is an object:

```python
x = 10
name = "Varun"
```

Both integers and strings are objects.

---

## Installing Python

Download from:

```text
https://python.org
```

Check installation:

```bash
python --version
```

or

```bash
python3 --version
```

---

## Running Python

### Interactive Mode (REPL)

Start Python:

```bash
python
```

Then:

```python
>>> 2+3
5
```

REPL = Read → Evaluate → Print → Loop

Useful for testing small pieces of code.

---

### Script Mode

Create:

```python
main.py
```

Code:

```python
print("Hello World")
```

Run:

```bash
python main.py
```

---

# 2. Python Syntax

Syntax means the rules for writing code.

---

## Indentation (Very Important)

Unlike many languages, Python uses indentation to define blocks.

Correct:

```python
if True:
    print("Hello")
```

Wrong:

```python
if True:
print("Hello")
```

Error:

```
IndentationError
```

Usually 4 spaces are used.

---

## Comments

### Single-line Comment

```python
# This is a comment
print("Hello")
```

Python ignores comments.

---

### Multi-line Comments

Python doesn't truly have multiline comments.

People use:

```python
"""
This is
multiple lines
"""
```

or

```python
'''
Multiple lines
'''
```

Technically these are multiline strings.

---

## Case Sensitivity

Python is case-sensitive.

```python
name = "Varun"

print(name)
```

Different variables:

```python
name
Name
NAME
```

All are different.

---

## Statements

Single statement:

```python
x = 10
```

Multiple statements:

```python
x = 10
y = 20
z = x + y
```

---

## Multiple Statements on One Line

Possible but not recommended:

```python
x = 10; y = 20; print(x+y)
```

---

## Line Continuation

### Using Backslash

```python
total = 10 + 20 + \
30 + 40
```

### Better Way

Inside brackets:

```python
total = (
    10 +
    20 +
    30 +
    40
)
```

---

# 3. Python Output

Output means displaying something to the screen.

---

## print()

```python
print("Hello")
```

Output:

```
Hello
```

---

## Printing Multiple Values

```python
name = "Varun"
age = 22

print(name, age)
```

Output:

```
Varun 22
```

Python automatically puts spaces.

---

## sep Parameter

Default separator:

```python
print("A", "B", "C")
```

Output:

```
A B C
```

Custom separator:

```python
print("A", "B", "C", sep="-")
```

Output:

```
A-B-C
```

---

## end Parameter

Default:

```python
print("Hello")
print("World")
```

Output:

```
Hello
World
```

Actually:

```python
end="\n"
```

Custom:

```python
print("Hello", end=" ")
print("World")
```

Output:

```
Hello World
```

---

## Escape Characters

### New Line

```python
print("Hello\nWorld")
```

Output:

```
Hello
World
```

---

### Tab

```python
print("Hello\tWorld")
```

Output:

```
Hello    World
```

---

### Quotes

```python
print("I'm Varun")
```

or

```python
print('I\'m Varun')
```

---

### Backslash

```python
print("C:\\Users\\Varun")
```

---

## Formatted Strings (f-strings)

Best method:

```python
name = "Varun"
age = 22

print(f"My name is {name} and I am {age} years old.")
```

Output:

```
My name is Varun and I am 22 years old.
```

Python evaluates expressions:

```python
x = 10

print(f"x squared = {x*x}")
```

Output:

```
x squared = 100
```

---

# 4. Python Variables

Variables store values in memory.

```python
name = "Varun"
```

Think:

```
Variable Name ----> Value
name -----------> "Varun"
```

---

## Naming Rules

✅ Valid:

```python
age = 20
my_name = "Varun"
_marks = 90
name123 = "A"
```

❌ Invalid:

```python
1name = "Varun"
my-name = "Varun"
class = 5
```

---

## Naming Conventions

Python uses snake_case:

```python
first_name = "Varun"
student_marks = 95
```

Not:

```python
firstName
StudentMarks
```

---

## Multiple Assignment

```python
a, b, c = 10, 20, 30
```

---

## Same Value

```python
x = y = z = 100
```

---

## Variable Reassignment

```python
x = 10
x = 20
```

Latest value wins.

---

## Dynamic Typing

```python
x = 10
x = "Hello"
x = 3.14
```

Allowed because Python is dynamically typed.

---

## Memory References

```python
a = 10
b = a
```

Both refer to the same object.

```python
print(id(a))
print(id(b))
```

Same memory address.

---

# 5. Python Data Types

Everything in Python is an object.

Check type:

```python
x = 10

print(type(x))
```

Output:

```
<class 'int'>
```

---

# Numeric Types

## int

Whole numbers

```python
age = 22
```

---

## float

Decimal numbers

```python
price = 99.99
```

---

## complex

```python
z = 3+4j
```

Real part:

```python
z.real
```

Imaginary part:

```python
z.imag
```

---

# Boolean Type

```python
is_logged_in = True
```

Values:

```python
True
False
```

Notice capital T and F.

---

# String

```python
name = "Varun"
```

Strings are sequences of characters.

```python
print(name[0])
```

Output:

```
V
```

---

# Sequence Types

## List

Mutable (changeable)

```python
numbers = [1,2,3]
```

Can modify:

```python
numbers[0] = 100
```

---

## Tuple

Immutable

```python
point = (10,20)
```

Cannot change:

```python
point[0] = 50
```

Error.

---

## Range

```python
r = range(5)
```

Produces:

```
0 1 2 3 4
```

---

# Set Types

## set

Unordered and unique.

```python
nums = {1,2,3}
```

Duplicates removed:

```python
{1,1,2,2}
```

becomes

```python
{1,2}
```

---

## frozenset

Immutable set.

```python
f = frozenset([1,2,3])
```

---

# Dictionary

Stores key-value pairs.

```python
student = {
    "name": "Varun",
    "age": 22
}
```

Access:

```python
print(student["name"])
```

Output:

```
Varun
```

---

# None Type

Represents absence of value.

```python
x = None
```

Similar to:

* null (JavaScript)
* NULL (SQL)

---

# Type Conversion

Implicit:

```python
x = 10 + 5.5
```

Result:

```python
15.5
```

Python converts automatically.

---

Explicit:

```python
int("10")
float("10")
str(100)
bool(1)
```

---

# Summary Table

| Type     | Example          |
| -------- | ---------------- |
| int      | 10               |
| float    | 3.14             |
| complex  | 2+3j             |
| bool     | True             |
| str      | "Hello"          |
| list     | [1,2,3]          |
| tuple    | (1,2,3)          |
| set      | {1,2,3}          |
| dict     | {"name":"Varun"} |
| range    | range(5)         |
| NoneType | None             |

---