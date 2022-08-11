
first = "Nico"
last = "Hulkenberg"

# - Create a variable called "full_name" that combines first and last with a space between them.  
full_name = first + " " + last
# - Print it out
print(full_name)


# - Create an "initials" variable that holds the first character of first followed by the first character of last. 
inititals = first[0] + last[0]
# - Print it out
print(inititals)


# - Create an "initials_2" variable that holds the first character of first followed by the first character of last, with periods after each letter!
inititals_2 = first[0] + "." + last[0] + "."
# - Print it out
print(inititals_2)


# Create a "nickname" variable that holds the first 4 characters of "last" (use a slice)
nickname = last[0:4]
# Print it out 
print(nickname)
