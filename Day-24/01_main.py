with open("../../Downloads/Day_24/my_file.txt") as file:
    contents = file.read()
    print(contents)


# # Write
# with open("my_file.txt", mode = "w") as file:
#     file.write("NEW TEXT")

# #append
# with open("my_file.txt", mode = "a") as file:
#     file.write("\nNEW TEXT")
# #If you are going to open a file in a read mode and that file doesn't exits then it is 
# #going to create a new file from scatch.

# with open("new_file.txt", mode = "a") as file:
#     file.write("\nNEW TEXT")