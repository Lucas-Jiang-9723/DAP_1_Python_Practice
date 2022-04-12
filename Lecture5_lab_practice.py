
#%%
#1: this code does not run!  try it and examine the errors, then figure out what needs to
#be changed to make it work

#identification: Re-arrangement and spacing

a = 10

def first_func(b=20):
    c = 30
    value = second_func(b, c)
    return value

def second_func(b, c, d=40):
    e = 50
    return a + b + c + d + e

result = first_func()
print(result)



#%%
#2: take this code from Thursday's lab and write a function so that the form of
#the final answer is:
#answer = {key_func(k):val_func(v) for k, v in start_dict.items()}

import datetime
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

def cap_key(key):
    key = key.capitalize()
    return key

def rearrange_val(val):
    val = datetime.datetime.strptime(val, "%m/%d/%Y").date()
    return val

result_dict = {cap_key(key):rearrange_val(val) for key,val in start_dict.items()}
print(result_dict)
    

#%%
