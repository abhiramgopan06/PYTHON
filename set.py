# s1 = {2,False,2,3,4,4,5,2,3,2,6,4,5,(1.2,3),'hello',True}
# print(s1)
# s2 = set([2, False, 2, 3, 4, 4, 5, 2, 3, 2, 6, 4, 5, (1.2, 3), 'hello', True])
# print(s2)
# l1 = ['red','blue','green']
# s1.add('world')
# s1.update(l1)

# # s1.pop()
# # s1.remove('world')
# # s1.remove('World')
# # s1.discard('world')
# s1.clear()
# print(s1)

developer_one_interesets = {"Python","PHP","JS","C++"}
developer_two_interesets = {"Python","C","Java",}

# new_set1 = developer_one_interesets.union(developer_two_interesets)
# print(new_set1)

# new_set2 = developer_one_interesets.intersection(developer_two_interesets)
# print(new_set2)

# new_set3 = developer_one_interesets.difference(developer_two_interesets)
# print(new_set3)

# new_set4 = developer_two_interesets.difference(developer_one_interesets)
# print(new_set4)

# print(new_set3.union(new_set4))

# new_set5 = developer_one_interesets.symmetric_difference(developer_two_interesets)
# print(new_set5)

# developer_one_interesets.intersection_update(developer_two_interesets)
# developer_one_interesets.difference_update(developer_two_interesets)
# developer_two_interesets.difference_update(developer_one_interesets)
# developer_one_interesets.symmetric_difference_update(developer_two_interesets)
# developer_one_interesets.update(developer_two_interesets)

print(developer_one_interesets)

print(developer_two_interesets.isdisjoint(developer_one_interesets))# return true if these are no common values

languages = {"Python","PHP","JS","C++","C","Java","C#","Assembly","Ruby"}

print(developer_one_interesets.issubset(languages))# return True if the first set contains only the value in second set 
print(languages.issuperset(developer_two_interesets))# return true if the first set contains all the values in second set

copy1 = developer_two_interesets.copy()
copy1.add('C#')
print(copy1)
print(developer_two_interesets)