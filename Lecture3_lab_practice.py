#### fix the following errors!

#%% Q1
#1 x should be an integer
x = 10
y = 20
print(x + y)

#%% Q2
#2 The position index starts from 0, hence the indexed length is out of range
my_list = [40, 50, 60, 70, 80, 100, 200, 400]
my_list_len = len(my_list)-1
print(my_list[my_list_len])
#alternative
print(my_list[-1])

#%% Q3
#3 Missed a pair of () at the end
my_string = 'hello world'
print(my_string.upper())

#%% Q4
#4 Appending should use the append funtion
z = ['a', 'b', 'c']
z.append('d')
print(z)
# String does not have append function , list and string can all simply use "+"
z += 'e'
print(z)
#%% Q5
#5 why does the x not display 10, followed by the 200?  Fix it so it does.
#  Use the print function
x = 10
print(x)
y = 20
print(x * y)

#%% Q6
#6 The format is not correct, should be consistent. blue should be a string

color = 'My favorite color is %s, what is yours?' %'blue'
print(color)


#%% Q7

#### answer the following questions without changing the code given

#7 make the entries in this list unique
#  converting the list to a set
schools = ['harris', 'booth', 'crown', 'harris', 'harris']
schools_unique = set(schools)
print(schools_unique)

#%% Q8
#8 change the 'dog' entry to 'cat'
#  change the tuple to list first and conduct the change
animals = tuple(['bird', 'horse', 'dog', 'fish'])
animals_new = list(animals)
animals_new[2] = 'cat'
print(animals_new)

#%% Q9
#9 make this string take a name based on a variable (you can modify the code on this one)
student_name = input("What's your name?")
welcome = f'Hello {student_name}, and welcome to Data and Programming!'
print(welcome)

#%% Q10
#10 separate the words in this string into entries in a list, with only lower-case
#letters, e.g. ['i', 'love', 'how', ...
#   use .lower() and .split()
my_sent = 'I LOVE how spring is super late this year and there are no flowers and it is cold and rainy.'

my_sent_1 = my_sent[:-1].lower().split(" ")
print(my_sent_1)
