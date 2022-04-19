#fix the problems with each of these classes (1-3)

#%%
#1
class MyClass():
    def __init__(self):
        self.a = 10
        self.b = 20
        self.x = self.a + self.b
my_instance = MyClass()
print(my_instance.x)

#%%
#2
class MyClass():
    def __init__(self):
        a = 10
        b = 20
        self.x = a + b
my_instance = MyClass()
print(my_instance.x)

#%%
#3
class MyClass(): 
    def __init__(self,a, b):
        self.x = a + b
my_instance = MyClass(10, 20)
my_instance.x

#%%
#4 A Fibonacci sequence is a list of values where each is the sum of the previous
#  two, e.g. [0, 1, 1, 2, 3].
#      - First write a function that takes in a list of any two values, then
#        calculates the rest of the sequence starting from that point.  It
#        should have two arguments; the starting list, and the number to
#        calculate.
#      - Second, turn this into a class that takes the same list at start,
#        but has a method that takes N as an argument and then calculates
#        the sequence.
#  Note that technically the Fibonacci sequence starts at 0, but for our
#  coding practice we can calculate it from any two starting values.

# Ver1 - function
def fibonacci_calc(start_list, num_calc):
    result_list = start_list
    for i in range(1, num_calc-1):
        #new_number = start_list[-1] + start_list[-2]
        new_number = sum(start_list[-2:])
        result_list.append(new_number)
    return result_list

series_1 = fibonacci_calc([1,2],30)
print(series_1)


# Ver 2 - Class
class FibonacciCalc():
    def __init__(self,start_list, N):
        self.N = N
        self.start_list = start_list
    
    def generate(self):
        for i in range(1, self.N-1):
            self.start_list.append(self.start_list[-1] + self.start_list[-2])
        print(self.start_list)

series_2 = FibonacciCalc([0,1],10)
series_2.generate()
            


#%%
