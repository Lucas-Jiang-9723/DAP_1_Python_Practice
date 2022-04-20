#%%
#1. will the code run, and if so, what will be the data types and values of a and b?
a, b = [10, 11] #run
a, b = [10] #not run
a, b = [10, 11, 12] #not run
a, *b = [10, 11] #run a = 10, b = [11]
a, *b = [10] #run a = 10, b = []
a, *b = [10, 11, 12] #run a = 10, b = [11, 12]

#%%
#2. what data type is args and kwargs inside the function, what are the values,
#and how would you use them?
def base_function(*args, **kwargs):
    #kwargs dictionary
    #positioning arguments list/tuple
    pass

base_function()
base_function(['A', 'B'])
base_function('Hello', 'World', '!')
base_function(answer=True, question='No')
base_function('a', 'b', c='value', d=10)

#%%
#3. write a lambda function that is passed into my_func, and performs a valid
#operation on a and b, without editing the contents of my_func at all.

def my_func(a, b, func=lambda x,y: sum([x,y])/10):
    value = func(a, b)
    return value

print(my_func(10,20))


#%%

