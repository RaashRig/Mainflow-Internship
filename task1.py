
my_list=[1,2,3,4,5]

my_list.append(8)
my_list.remove(3)
my_list[2]=15

print("updated list: ",my_list)

#dictionary
my_dict = {'name': 'samad', 'Age': 21, 'city' : 'Hyderabad'}

my_dict['gender'] = 'male'
del my_dict['city']
my_dict['age'] = 23

print("Updated dictionary: ", my_dict)

#sets
my_set={1,2,3,4,5}

my_set.add(6)
my_set.remove(3)
my_set.discard(7)

print("Updated set: ",my_set)


