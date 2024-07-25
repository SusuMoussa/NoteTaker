import function

menu = """
    1-) Create A New Note
    2-) Read A Note
    3-) List A Note
    4-) Delete A Note
    5-) Simulate Human Typing With A Note
    6-) Exit
"""

print (menu)

while True:
    option = input ("choose [1-6:]")
    #This function will list all the notes in the Notes folder




    if option == "1":
        function.MakeNote()

    elif option == "2":
        function.ReadNote()

    elif option == "3":
        function.ListNote()

    elif option == "4":
        function.RemoveNote()
 
    elif option == "5":
        function.HumanType()
    
    elif option == "6":
        exit()