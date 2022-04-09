#convert these objects!


#%%
#1
start_list = [[2, 3, 4], [6, 8, 9]]
#turn it into [1,    2,   3, 4   ]

#for loop ver
new_list=[]
for list_1 in start_list:
    for number in list_1:
        if number%2==0:
            new_list.append(int(number/2))     
print(new_list)

#list comprehension ver
new_list_2=[int(number/2) for list_1 in start_list for number in list_1 if number%2==0]
print(new_list_2)


#%%
#2
import datetimes
start_dict = {'noah': '2/23/1999',
              'sarah':'9/1/2001',
              'zach': '8/8/2005'}
#turn it into {'Noah': datetime(1999, 2, 23),
#              'Sarah':datetime(2001, 9, 1),
#              'Zach': datetime(2005, 8, 8)}

#for loop ver
for key,val in start_dict.items():
    start_dict[key] = datetime.datetime.strptime(val, "%m/%d/%Y").date()
    
print(start_dict)





#%%

