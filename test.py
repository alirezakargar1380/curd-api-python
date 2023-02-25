# this is the way that we can comment in python
test = "hello i'm a test variable"
print(test)

# print each item of array
test_array_str = [
    'item 1',
    'item 2',
    'item 3',
    'item 4'
]
for item in test_array_str:
    print(item)


# duble number
test_array_int = [3, 6, 9]


def printArrayItems(item):
    return item+item


result = map(printArrayItems, test_array_int)
print(list(result))

# print each char of the word varable
word = "anaconda"
for letter in word:
    print(letter)

# Object
obj = {
    "username": "alireza",
    "password": "12345678"
}
print(obj)
print(obj["username"])
