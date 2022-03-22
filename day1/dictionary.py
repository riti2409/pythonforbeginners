#if we have the list of 5 values we use 3 to fetch the value at 3
#sometimes its better to have a key value pair
#we specify 2 things key(immutable,unique) , key
data = {1: 'navin', 2: 'kiran', 4: 'harsh'}
#when we want to fetch a particular value
print(data[4])
#o/p=harsh
data.get(1)
'navin'
print(data.get(3))
#o/p=none
# print(data[3])
#o/p=error
#if we dont have a key we can use
data.get(3, 'not found')
#creating dictionary with the help of list
keys = ['navin', 'kiran', 'harsh']
values = ['python', 'java', 'c++']
data1 = dict(zip(keys, values))
print(data1)
# {'navin': 'python', 'kiran': 'java', 'harsh': 'c++'}
#to assign a value to a key
data1['monika'] = 'cs'
#to del a key
del data['harsh']
prog = {'js': 'atom', 'cs': 'vs', 'python': ['python', 'sublime']}
print(prog['python'])
