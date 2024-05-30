#FileNotFound
with open("a_file.txt") as file:
    file.read()

#KeyError
a_dictionary = {"key" : "value"}
value = a_dictionary["non_existent_key"]

#IndexError
fruit_list = ["Apple", "Banana", "Pear"]
fruit = fruit_list[3]

#TypeError
text = 'abc'
print(text + 5)

#Catching exception
try:
    file = open("a_file.txt") #trying to open file which doesn't exist
except FileNotFoundError:
    file = open("a_file.txt", "w") #we ask to create the file in case it is not found

#To get a message from the exception:
except KeyError as error_message:
    print(f"The key {error_message} doesn't exist.")

#Raising exception:
raise KeyError("This is an Error i made up")