#Phonebook awnsers

1 = Phonebook = {"Jane Doe": "+27 555 5367", "John Smith": "+27 555 6254", "Bob Stone": "+27 555 5689"}

#printing a number without "" caused problems because of the + or et spaces im guessing

2 = Phonebook["Jane Doe"] = "+27 555 1024"

#can also ude += instead of =

3 = Phonebook["Anna Cooper"] = "+27 555 3237"

#can't use +=

4 = Phonebook["Bob Stone"]

5 = Phonebook.get("Bob Stone")

6 = Phonebook.keys()

7 = Phonebook.values()