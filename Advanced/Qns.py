# # #write a program to read a text file and displays the number of lines in a file
f = open("k.txt", "r")
s = f.readlines()
c=len(s)
print(c)

f.close()

# # #write a program to display the number of words in a file


f = open("k.txt", "r")
s = f.read()
words =s.split()
num =len(words)


f.close()
print("number of words",num)

             ####################################

# # #write a program to update the second line in a file

# Step 1: Read all lines from the file
f = open("k.txt", "r")
s = f.readlines()

# Step 2: Modify the second line (Index 1)
# Note: Keep the '\n' at the end to preserve the line break
s[1]="Far more piranhas are eaten by people than people are eaten by piranhas. If the fish are well-fed, they won’t bite humans."
print(s)
f.close()



# Step 3: Write the modified lines back to the file
f= open("k.txt", "w")
f.writelines(s)
f.close()

                                    #######################################3

# # #write a program to display the last 5 lines in a file

f = open("k.txt", "r")
s = f.readlines()
five_lines=s[-5:]
print(five_lines,end="")

f.close()


                      ###################################

# #program to search a particular word in a file
file = open("k.txt", "r")
#file.readlines()

# n=input("enter the word")
#
# for i in file:
#     if n in i:
#         print("present")
#         break
#     else:
#         print("not present")
#         break
#
#
# f.close()


f = open("k.txt", "r")

n = input("Enter the word: ")

for i in f:
    if n in i:
        print("present")
        break  # Skips the else block below completely
    else:
    # This runs ONLY if the loop finishes checking every line without breaking
       print("not present")

f.close()
