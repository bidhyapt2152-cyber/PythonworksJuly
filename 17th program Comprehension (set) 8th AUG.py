#Set comprehension


# Given
s="python coding  is easy and fun"
# Qn. create a new set with only vowels
new=set()
for i in s:
    if i in "AEIOUaeiou":
        new.add(i)
print(new)


           #OR

new={i for i in s if i in 'AEIOUaeiou'}
print(new)



         ################################################

# create a new set                #Normal method
# l=[1,2,3,4]
# new=set()
# for i in l:
#     new.add(i)
# print(new)
#
#      #OR
#
# l=[1,2,3,4]                      #Comprehension
# new={i for i in l}
# print(new)