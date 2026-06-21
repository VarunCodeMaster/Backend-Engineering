
# 1. Python Strings

# Theory

A string is a sequence of characters enclosed in quotes.

```python
name = "Varun"
```

Python treats strings as objects of type `str`.

```python
print(type(name))
```

Output:

```python
<class 'str'>
```

---

# Subtopics

## Creating Strings

Single quotes:

```python
name = 'Varun'
```

Double quotes:

```python
name = "Varun"
```

Triple quotes:

```python
paragraph = """This
is
multiple lines."""
```

---

## Strings are Immutable

Once created, characters cannot be changed.

```python
name = "Varun"
```

Trying:

```python
name[0] = "T"
```

❌ Not allowed.

Instead:

```python
name = "Tarun"
```

---

# Internal Concept

Strings are immutable objects stored in memory.

```python
a = "hello"
b = a
```

Both point to the same object.

```python
print(id(a))
print(id(b))
```

Same memory address.

Changing:

```python
a = "world"
```

creates a completely new string object.

---

## String Indexing

```python
word = "Python"
```

Positive indexing:

```python
P y t h o n
0 1 2 3 4 5
```

Negative indexing:

```python
P y t h o n
-6 -5 -4 -3 -2 -1
```

Example:

```python
word[0]
word[-1]
```

---

## String Slicing

Syntax:

```python
string[start:end:step]
```

```python
word = "Python"
```

```python
word[0:3]
```

Output:

```python
Pyt
```

Reverse:

```python
word[::-1]
```

Output:

```python
nohtyP
```

---

## String Length

```python
len("Python")
```

Output:

```python
6
```

---

## String Methods

### Uppercase

```python
name.upper()
```

### Lowercase

```python
name.lower()
```

### Title

```python
name.title()
```

### Replace

```python
text.replace("hello", "hi")
```

### Split

```python
"apple mango".split()
```

Output:

```python
['apple', 'mango']
```

### Join

```python
"-".join(["A", "B", "C"])
```

Output:

```python
A-B-C
```

### Find

```python
text.find("o")
```

Returns index.

### Count

```python
text.count("a")
```

### Strip

Removes spaces:

```python
text.strip()
```

---

## Membership Operators

```python
"Py" in "Python"
```

Returns:

```python
True
```

---

## String Formatting

### f-string

```python
name = "Varun"

print(f"Hello {name}")
```

### format()

```python
"Hello {}".format(name)
```

### Old style

```python
"Hello %s" % name
```

---

# Common Mistakes

### Forgetting strings are immutable

❌

```python
name[0] = "T"
```

---

### Wrong indexing

```python
word = "Python"

word[6]
```

There is no index 6.

---

### Confusing split() and join()

```python
split()
```

converts:

```python
String → List
```

```python
join()
```

converts:

```python
List → String
```

---

# Common Error Messages

### IndexError

```python
word[10]
```

Error:

```python
IndexError: string index out of range
```

---

### TypeError

```python
"Age: " + 20
```

Error:

```python
TypeError: can only concatenate str (not "int")
```

Correct:

```python
"Age: " + str(20)
```

or

```python
f"Age: {20}"
```

---

# Important Notes

✅ Strings are immutable.

✅ Slicing never causes errors if range exceeds length.

```python
word[0:100]
```

No error.

---

# 2. Python Operators

---

# Theory

Operators perform operations on values.

---

# Types of Operators

## Arithmetic Operators

| Operator | Meaning        |
| -------- | -------------- |
| +        | Addition       |
| -        | Subtraction    |
| *        | Multiplication |
| /        | Division       |
| //       | Floor division |
| %        | Modulus        |
| **       | Power          |

Example:

```python
10 // 3
```

Output:

```python
3
```

---

## Comparison Operators

```python
==
!=
>
<
>=
<=
```

Return True or False.

---

## Assignment Operators

```python
=
+=
-=
*=
/=
%=
```

Example:

```python
x += 5
```

Means:

```python
x = x + 5
```

---

## Logical Operators

### and

Both must be True.

```python
True and True
```

---

### or

At least one True.

---

### not

Reverses boolean.

---

## Membership Operators

```python
in
not in
```

Example:

```python
"a" in "apple"
```

---

## Identity Operators

```python
is
is not
```

Checks memory location.

```python
a = [1,2]
b = a

a is b
```

True.

---

## Bitwise Operators

```python
&
|
^
~
<<
>>
```

Operate on binary numbers.

Advanced topic; we'll revisit later.

---

# Internal Concept

### == vs is

```python
a = [1,2]
b = [1,2]
```

```python
a == b
```

True (same values)

```python
a is b
```

False (different objects)

---

# Common Mistakes

### Using = instead of ==

❌

```python
if x = 10:
```

Correct:

```python
if x == 10:
```

---

### Confusing / and //

```python
10 / 3
```

3.333

```python
10 // 3
```

3

---

# Common Errors

### SyntaxError

```python
if x = 10:
```

---

### ZeroDivisionError

```python
10/0
```

---

# Important Notes

`is` compares identity.

`==` compares values.

Never use:

```python
x is 10
```

Use:

```python
x == 10
```

---

# 3. Python Lists

---

# Theory

Lists store multiple values and are mutable.

```python
numbers = [1,2,3]
```

---

# Internal Concept

Lists store references to objects.

Memory:

```text
numbers
 ↓
[ref][ref][ref]
 ↓    ↓    ↓
 1    2    3
```

---

# Subtopics

### Indexing

```python
numbers[0]
```

---

### Slicing

```python
numbers[1:4]
```

---

### Add Elements

```python
append()
insert()
extend()
```

---

### Remove Elements

```python
remove()
pop()
clear()
del
```

---

### Sorting

```python
sort()
sorted()
```

Difference:

```python
sort()
```

modifies original.

```python
sorted()
```

returns new list.

---

### Reverse

```python
reverse()
```

---

### Copy

```python
copy()
```

---

### Nested Lists

```python
matrix = [[1,2],[3,4]]
```

---

# Common Mistakes

### Using append instead of extend

```python
a=[1,2]
a.append([3,4])
```

Result:

```python
[1,2,[3,4]]
```

---

extend:

```python
a.extend([3,4])
```

Result:

```python
[1,2,3,4]
```

---

# Common Errors

### IndexError

```python
nums[100]
```

---

### ValueError

```python
nums.remove(99)
```

Error:

```python
ValueError: list.remove(x): x not in list
```

---

# Important Notes

Lists are mutable.

Can store mixed types:

```python
[1,"Hello",True]
```

---

# 4. Python Tuples

---

# Theory

Tuple is an immutable sequence.

```python
point = (10,20)
```

---

# Internal Concept

Tuples are stored similarly to lists but cannot be modified after creation.

Because of immutability:

* Faster
* Safer
* Hashable (usable as dictionary keys)

---

# Creating Tuples

```python
t = (1,2,3)
```

Single value tuple:

```python
t = (10,)
```

Without comma:

```python
t = (10)
```

This is int.

---

# Packing and Unpacking

Packing:

```python
person = ("Varun",22)
```

Unpacking:

```python
name, age = person
```

---

# Common Mistakes

### Forgetting comma

```python
(5)
```

Not tuple.

---

# Common Errors

### TypeError

```python
t[0]=100
```

Error:

```python
TypeError: 'tuple' object does not support item assignment
```

---

# Important Notes

Tuples are immutable but can contain mutable objects.

```python
t=([1,2],3)
```

List inside tuple can change.

---

# 5. Python Sets

---

# Theory

Set stores unique values.

```python
nums={1,2,3}
```

Unordered and mutable.

---

# Internal Concept

Sets use Hash Tables.

This gives very fast searching:

Average complexity:

```text
O(1)
```

Much faster than lists.

---

# Subtopics

## Add

```python
add()
```

---

## Remove

```python
remove()
discard()
pop()
```

Difference:

### remove()

Error if absent.

### discard()

No error.

---

## Set Operations

### Union

```python
a | b
```

---

### Intersection

```python
a & b
```

---

### Difference

```python
a - b
```

---

### Symmetric Difference

```python
a ^ b
```

---

### Subset

```python
issubset()
```

---

### Superset

```python
issuperset()
```

---

## Frozen Set

Immutable set.

```python
frozenset([1,2,3])
```

---

# Common Mistakes

### Creating empty set

❌

```python
s={}
```

This creates dictionary.

Correct:

```python
s=set()
```

---

### Expecting order

Sets don't preserve insertion order conceptually.

Never rely on index.

```python
nums[0]
```

Not possible.

---

# Common Errors

### KeyError

```python
nums.remove(10)
```

if 10 not found.

---

### TypeError

```python
nums.add([1,2])
```

List is unhashable.

Error:

```python
TypeError: unhashable type: 'list'
```

---

# Important Notes and Interview Points

### Mutable vs Immutable

| Type      | Mutable |
| --------- | ------- |
| String    | ❌       |
| List      | ✅       |
| Tuple     | ❌       |
| Set       | ✅       |
| Frozenset | ❌       |

---

### Which is Faster?

Access by index:

```text
Tuple ≈ List
```

Membership checking:

```text
Set > List
```

Memory efficiency:

```text
Tuple > List
```

---

### `is` vs `==`

```python
a=[1,2]
b=[1,2]

a==b
```

True

```python
a is b
```

False

---
