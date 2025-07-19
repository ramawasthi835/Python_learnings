my_dict={"ram":100, "debu" : 99, "ketan" : 100}#Creating a dictionary
print(my_dict.items()) #prints all the items in the list
print(my_dict.keys()) #prints all the keys of the list
print(my_dict.values()) # prints all the values of the list
print(my_dict["ram"]) #Gets value of the key and returns error if not present
print(my_dict.get("keta"))#Gets the value of the key, returns none if not present
my_dict.update({"debu":100, "sushma":99})#updates the value of key if present or adds new key value pair if key is new
print(my_dict)