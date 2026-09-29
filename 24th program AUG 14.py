
#1 .Given a list
l=[1,1,1,2,3,3,4,5]

#remove duplicates from list
l = [1, 1, 1, 2, 3, 3, 4, 5]
remove = list(set(l))
print(remove)



# 2.Given a list
l=[1,1,1,2,3,3,4,5]
#
# remove duplicates without set()

new = []
for i in l:
    if i not in new:
        new.append(i)
print(new)

#
# 3.Given two lists
#
l1=[23,45,78,90,12,74]
l2=[45,89,23,56,34]

# print common elelments
l1 = [23, 45, 78, 90, 12, 74]
l2 = [45, 89, 23, 56, 34]
comm= list(set(l1) & set(l2))
print(comm)

