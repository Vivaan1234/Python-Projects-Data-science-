name = input("What is ur name? ")
print("Welcome to band name generator, " + name)

nickname = input("What nickname would u add to ur band generator? ")
print("Nickname set to: " + nickname)

animal = input("What is ur spirit animal? ")
print("Cool spirit animal !!")

birthday=input("What is ur birthdate?")
print("Cool Swaggy Birthday!!")

# This combines the nickname and spirit animal to create the band name
print("Congrats ur band name is: "  nickname + " " + animal+" "+ birthday)

#Yes, exactly. You can put an input() function inside a print() function, but you cannot put it inside the quotation marks of a string.
#in simple terms it means print("welcome" + input(hgt)),no input function in double quotes!
