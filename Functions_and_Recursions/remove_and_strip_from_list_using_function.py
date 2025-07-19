# FUNCTION TO REMOVE A NAME FROM THE LIST IF IT EXISTS

def edit(l1, name):
    for i in range(len(l1)):
        if name == l1[i]:
            # FIXED: Added parentheses to actually call strip()
            temp = l1[i].strip()  
            l1.remove(name)  # Remove the matched name from list
            print(l1, temp)  # Print updated list and the cleaned name

# Initial list of names
lst = ['ram', 'shyam', 'ravi', 'saint']

# Call the function with the list and the name to remove
edit(lst, 'saint')

