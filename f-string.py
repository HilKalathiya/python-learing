string = "Hey My Name is {} and My country is {}"
name = "Hil"
country = "India"
print(string.format(name, country))
# this is method to format a string for adding somthing in it
string = "Hey My Name is {1} and My country is {0}"
name = "Hil"
country = "India"
print(string.format(name, country))  # like this indexing pan kari shakvi apde

# but this is very confusing when we are dealing with long strings
# so for that here is a f-String
name = "Hil"
country = "India"
print(f"Hey My Name is {name} and My country is {country}")
# this very good method
# if you want to thake formate as it is
print(f"Hey My Name is {{name}} and My country is {{country}}")  # you see this
