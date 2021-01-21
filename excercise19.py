the_count = [1,2,3,4,5]
fruits = ['apples','oranges','grapes','banana']
changes = [1,'staple',2,'pins',3,'tape']

for number in the_count:
    print(f"this is count: {number}")

for fruit in fruits:
    print(f"this is fruit: {fruit}")

for i in changes:
    print(f"I got {i}")

elements = []

for i in range(0,6):
    print(f"adding {i} to the list")
    elements.append(i)

for i in elements:
    print(f"element was: {i}")
