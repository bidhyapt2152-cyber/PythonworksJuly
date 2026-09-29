#Given a list
l=[1,1,2,3,4,5,5,5,6,7]
#create a new dictionary where keys are numbers and values are count of each number
new={}
for i in l:
    new[i]=l.count(i)
print(new)

#Given list
l=[34,12,56,89,90,11]

#find the largest element
print("Maximum",max(l))


#find the smallest element
print("Minimum",min(l))


#find the second largest element
l.sort()
print("sorted",l)
print("second maximum",[l[-2]])


#find the second smallest element
l.sort()
print("sorted",l)
print("second minimum",[l[1]])



# Qn.
l=[["arun",23,40000],
    ["amal",24,50000],
    ["anu",27,30000]]

#create a new list of salary
# Given nested list
l = [
    ['arun', 23, 40000],
    ['amal', 24, 50000],
    ['anu', 27, 30000]
]

# 1. Create a new list of salaries
new= []
for i in l:
    new.append(i[2])  # Salary is at index 2

# Find the maximum salary
max_salary=max(i)



# 2. Create a new list of ages
new = []
for i in l:
    new.append(i[1])  # Age is at index 1

# Find the minimum age
min_age = min(new)













