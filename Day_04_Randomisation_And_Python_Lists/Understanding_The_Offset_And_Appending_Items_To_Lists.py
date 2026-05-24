
## PYTHON LIST CONCEPT (Check python documentation for Data Structures)
# The list is what you call a Data Structure. DATA STRUCTURE is a way of organizing and storing data in python.
# The list is a set of square brackets with many items stored insde, and those items can be any data type. They can even have mixed data types like you could store strings together with numbers of a set of Booleans.
## e.g fruits = [item1, item2]

## STORING THE NAMES OF ALL THE STATES IN THE U.S

states_of_america =["Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", "Connecticut", "Delaware", "Florida", "Georgia", "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota", "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", "West Virginia", "Wisconsin", "Wyoming"]
print(states_of_america[1]) # Generates Alaska as Alabama starts with [0] in computing terms. Alabama is not [1]. 
print(states_of_america[-1]) # Generates Wyoming as negative [-] starts counting from right to the left.

# append() adds a single item to the end of the list.
states_of_america.append("Adekunle")
print(states_of_america)

# extend() adds multiple items to the end of the list.
states_of_america.extend(["Taye", "Adetolani", "Adedoyinsola", "Adenike"])
print(states_of_america)