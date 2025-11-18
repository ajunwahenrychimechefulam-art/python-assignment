#print(name_class)

# print(name_name)
 
# name = ["Rahl", "Mike", "innocent", Daniel"]
# X, Y, Z =name

 # print(x)
 # print(y)
 # print(z)

 # month = ["jan", "mar", "aug", "june"]
 # print(x)
 # print(y)
 # print(z)

month = ["jan", "mar", "aug", "june"]
a, b, c, d = month
print(a)
print(b)
print(c)
print(d)

name = 'Rahl'
age = 25
print(f"Myname is {name}\n'{age}years old!")
print(f"my name is Rahl\nl'n and I am 25 years old\nAm a software developer")     

# name _class = 'Rahl'

name = 'RAHL '

def myfunc():
    print("My name is" + name)

def RAHL():
        global x
        x = "fantastic"

RAHL()
print("python is " + x)

print("It's alright'")
print("He is called 'Henry'")
print('Heis called "johnny"')

# people()

a = "Hello world"
print(a[6])

for x in "apple":
      print(x)

# a = "Hello, World"
# print(len(a))
a =['mango', 'apple', 'cashew']  
print(a[2])      
txt ="The best things in life are free!"
print("faviour" in txt)

name ="Ada"
age = 19
school = "Bright Future Academy"

print(f"My name is Rahl/nl'n and i am 19 years old, and i attend Bright Future Academy")


txt = "The best in life are Free"
if "expenisive" not in txt:
    print("expensive not in txt")

    b = "  Hello, world"
    print(b[6])
    print(name.upper())
    print(name.replace("H", "j"))
    print(name.split(","))

    name ='Rahl'
    career = 'software Developer'
    nationality = 'Nigeria'
    Bio = name + " " +  career  + " " + nationality
    print(Bio)


    price = 30
    print(f"I need {price: .2f} money")
    print(price)

    txt = "we are the so-called \"Vikings\" from the north."
    print(txt)
    txt = "we are coming \'school' from school"

    txt = "looking at them \\girls." 
    print(txt)

    txt = "good morning\nworld!"
    print(txt)

    txt = "hi\rWorld!"
    print(txt)

    txt = "mango\t world!"
    print(txt)

    txt = "promis\b to henry!"
    print(txt)

    txt = "trees\f i love!"
    print(txt)

    txt = "\mango\ tree\ world\ henry\ love\ "
    print(txt)

    txt = "\ xmango\ xtree\ xworld\ xhenry\ xlove\ "
    print(txt)


    motors = ["Lexus", "Tayota", "Camry", "Benz"]
    motors[0]= 'GLK'
    motors[2]= 'Lexus'
    motors.append('Jeep')
    motors.sort(reverse=True)


    motors = []
    motors.append('LEZUX')
    motors.append('CAMRY')
    motors.append('GLK')
    motors.append('GLK')
    motors.append('TOYOTA')
    motors.append('BUGATTI')
    motors.append('BMW')
    motors.append('HYUNDAI')
    motors.append('NISSAN')
    motors.append('CHEVROLET')
    motors.append('FERRI')
    motors.append('PORSCHE')
    motors.append('FORD')
    motors.append('KIA')
    motors.append('GMC')
    print(motors)


    friuts = ["apple", "apple", "banna", "cherry"]
    friuts.pop(3)
    friuts.remove('apple')
    print(friuts)


    friuts = ["apple", "orange", "banna", "cherry"]
    for fruit in range (len(friuts)):
          print(friuts[fruit])


    fruit = ["apple", "orange", "banna", "cherry"]
    myfriuts = friuts[2:3]
    print(fruit)

    thisset ={"apple", "banana", "cherry"}
    print(thisset)

    thisset = {"apple", "banana", "cherry", "apple"}
    (print(thisset))

    thisset = {"apple", "banana", "cherry", True, 1, 2}
    print(thisset)

    thisset = {"apple", "banana", "cherry"}

    thisset.remove("banana")
    print(thisset)

    thisset = {"apple", "banana", "cherry"}
    x = thisset.pop()
    print(x)
    print(thisset)

    thisset = {"apple", "banana", "cherry"}
    thisset.clear()
    print(thisset)

    set1 = {"a", "b", "c"}
    set2 = {1, 2,3}
    set3 = set1.union(set2)
    print(set3)

    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "microsoft", "apple", "banana"}

    set3 = (set1) & (set2)
    print(set3)


    set1 = {"apple", 1, "banana", 0, "cherry"}
    set2 = {"false", "google", 1, "apple", 2, "True"}

    set3 = set1&(set2)
    print(set3)


    set1 = {"apple", "banana", "cherry"}
    set2 = {"google", "mircosoft", "apple"}

    set3 = (set2) - set1
    print(set3)

    x = ("apple", "banana", "cherry")
    y = list(x)
    y[1] = "kiwi"
    x = tuple(y)
    
    print(x)


    thistuple = ("apple", "banana", "cherry")
    y = list(thisset)
    y.append("organge")
    thistuple = tuple(y)
    print(thistuple)


    thistuple = ("apple", "banana", "cherry")
    y = list(thistuple)
    y.append("coconut")
    thistuple = tuple(y)
    print(thistuple)


    #how to access tuple items
    friuts = ("paw paw", "cucumber", "cashew")
    even_num = (2, 4, 6, 8, 10)
    multiple_dt = ("str",10, 0.1, ["tayota", "Honda"], False, {"key": "value"})
    print(type(friuts))
    print(fruit[-1])

    #slicing a tuple
    print(even_num[2:6])

    #tuple length (this shows the number of items)
    print(len(friuts))


    person = ("pleasant", 13, "bende")
    name, age, place = person
    print(f"My name is {name} and i am {age} years old and  i am from {place}")

    food = ("spagetti" "Rice" "Beans")
    print(food[0])
    print(food[1])
    print(food[3])
    z = list(food)
    z= tuple(z)
    print(z)
#this is note on how to change  items in a list and convert back to tuple


#back to the lessons
#Dictionaries
student = {
      "name" : "Pleasant",
      "age" :13, 
      "location" :"Bende",
      "class" : "100L"
}
#accessing value in dictionaries 
print(student["name"])
print(student.get("name"))

#changing value in a dictionary
student["age"] = 100 
print(student["age"])

#to add keys and value to an already existing dictionary
student["school"] ="UNICAL"
print(student)

#to delete a key value from a dictionary 
student.pop("class")
print(student)

#pop iteam remove the last iteam in a dictionary without the key
student.popitem()

#print the keys in a dictionary without the values for key in student:
for key in student:
      ...
      print(key)

#.value() gets the value assigned to the key as typing without 
# it will print only the keys 
for value in student.values():
    ...
    print (key)
#.value s)() gets the values assigned to the key as typing without 
# it will print only the keys
for value in student.values ():
    ...
    print(value)
#to get all the keys and their values together in a loop
for key, value in student.items():        
         ...
         print(value)
#to get all the keys and their value together in a loop 
for key, value in student.items():
         ...
         print(f"{key} : {value}")
for value in student.values():
    ...
    print(f"{key} : {value}")

#to get all they keys and their value togther in a loop
for key, value in student.items():
         ...
         print(f"{key} : {value}")

#creting nested dictionaries in dictionary
student = {
"s1" : {"name": "pleasant", "age": 13},
"s2" : {"name": "Mrs. Blessing", "age": 31},
"s3" : {"name": "anionted prof", "age": 53},
}      
# getting the key and value of name only 
print(student["s1"]["name"])
for key, value in student.items():
     for i, j in student.items():
           print(key,i,j)                    