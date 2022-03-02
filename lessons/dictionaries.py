"""Demonstrating some capabilities of python dictionaries."""

# Note that most operations performed on a dictionary are carried out by its key
# Declaring the types of a dictionary
schools: dict[str, int]

# Initialize to an empty dictionary
schools = dict()

# Set a key value pairing in the dictionary
schools["UNC"] = 19400
schools["DUKE"] = 6717
schools["NCSU"] = 26150

# Print a dictionary literal representation
print(schools)

# Access a value by its key lookup
print(f"UNC has {schools['UNC']} students") 
# Use single quotes to enclose the dict key type because python will not permit the use of a double quote .e string type indicator within an f string

# Remove a key value pair from a dictionary - This done using its key. E.g to get rid of Duke
schools.pop("DUKE")

# Test for the existence of a key
is_duke_present: bool = "DUKE" in schools
print(f"Duke is present: {is_duke_present}")
# OR
if "DUKE" in schools:
    print("Found the key 'Duke' in schools")
else:
    print("No key 'Duke' in schools")

# Update/ reassign a key value pair
schools["UNC"] = 2000

# To increase the value type of a dictionary's key-value pair by a given integer value 
schools["NCSU"] += 200

# Demonstration of dictionary literals
# An example of the empty dictionary literal 
schools = {}  # same as dict()
print(schools)

# Alternatively initialize key-value pairs
schools = {"UNC": 19400, "DUKIE": 6717, "NCSU": 26150}
print(schools)

# Example looping over the keys of a dict
for school in schools:
    print(f"Key: {school} -> Value: {schools[school]}")