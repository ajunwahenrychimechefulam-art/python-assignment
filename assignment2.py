word1 = 'Hello'
word2 = 'Welcome'
word3 = """to Python class"""
print('hello', 'welcome', 'to python class')

sentence = "Python is fun to learn!"
print(sentence)

message = """Python is powerful.
It is easy to learn.
It is loved by developers."""
print(message)

text = "PYTHON"
print("First character:", text[0])
print("Third character:", text[2])
print("Last character:", text[-1])

language = "python"
for letter in language:
    print(letter)


fruit = "Banana"
print("length of the string:",)
word = "Learning python is cool"
if "python" in word:
    print("yes, 'python' is found!")

if "Java" not in word:
    print("'java' is not found in the sentence")

message = "coding is fun"
count = 0 
for char in  message:
    if char == 'n':
        count += 1
print ("The letter 'n' appears", count, "time.")

poem = """I love python for its grace,
Simple syntax, fast to embrace,
Coding feels like a warm embrace."""
print(poem.upper())