def main():
    StudentList = {}
    while True:
        choice = int(input("What would you like to do?\n 1. Add a new student \n 2. Remove a student \n 3. View list of students\n 4.Quit\n"))
        if choice == 1:
            Name = input("What is the students name?")
            Age = int(input("How old is the student?"))
            StudentList[Name] = Age
            print("Student added.")
            continue
        elif choice == 2:
            print(StudentList)
            Name = input("What student would you like to remove?").lower()
            if Name in StudentList:
                del StudentList[Name]
                print("Student removed")
                continue
        elif choice == 3:
            print(StudentList)
        elif choice == 4:
            break
        else:
            print("Error, try again.")
            continue
if __name__ == "__main__":
    main()

    #I managed to get it to work without the teachers code. However i struggled as i was trying to add Name and Age as two
    #separate keys and elements. However just assinging the key Name with the Age as the element
    #This way you can delete them easily.
    #Im still not 100% sure why we do if __name__ == "__main__": and have it all in a function called main()
    #Teachers code below
def main():
    elever = {}
    while True:
        print("Meny:")
        print("1. Lägg till en elev")
        print("2. Ta bort en elev")
        print("3. Visa alla elever")
        print("4. Avsluta")
        val = input("Ange ditt val: ")
        if val == "1":
            namn = input("Ange elevens namn: ")
            ålder = int(input("Ange elevens ålder: "))
            elever[namn] = ålder
            print(f"Eleven {namn} har lagts till.")
        elif val == "2":
            namn = input("Ange namn på eleven du vill ta bort: ")
            if namn in elever:
               del elever[namn]
               print(f"Eleven {namn} har tagits bort.")
            else:
                print(f"Kunde inte hitta eleven {namn}.")
        # Denna rad kontrollerar om variabeln elever är sann (inte tom eller False)
        elif val == "3":
            if elever:
                for namn, ålder in elever.items():
                    print(f"{namn} - {ålder} år")
            else:
                print("Det finns inga elever i klassen.")
        elif val == "4":
            break
        else:
            print("Felaktigt val. Försök igen.")
if __name__ == "__main__":
    main()
    #In this scenario idk why we use def main and call it at the end when its all already in a loop
    #For example, this code works just the same
elever = {}
while True:
    print("Meny:")
    print("1. Lägg till en elev")
    print("2. Ta bort en elev")
    print("3. Visa alla elever")
    print("4. Avsluta")
    val = input("Ange ditt val: ")
    if val == "1":
        namn = input("Ange elevens namn: ")
        ålder = int(input("Ange elevens ålder: "))
        elever[namn] = ålder
        print(f"Eleven {namn} har lagts till.")
    elif val == "2":
        namn = input("Ange namn på eleven du vill ta bort: ")
        if namn in elever:
           del elever[namn]
           print(f"Eleven {namn} har tagits bort.")
        else:
            print(f"Kunde inte hitta eleven {namn}.")
    # Denna rad kontrollerar om variabeln elever är sann (inte tom eller False)
    elif val == "3":
        if elever:
            for namn, ålder in elever.items():
                print(f"{namn} - {ålder} år")
        else:
            print("Det finns inga elever i klassen.")
    elif val == "4":
        break
    else:
        print("Felaktigt val. Försök igen.")



#New exercise
Bookshelf = {}
def AddBook():
        Bookname = input("Input book title: ")
        Author = (input("Input book author: "))
        Bookshelf[Bookname] = Author
        print(f"{Bookname} has been added.")
def EditBook():
    for Bookname, Author in Bookshelf.items():
        print(f"{Bookname} - {Author}")
    Bookname = input("Which book would you like to edit?")  
    if Bookname in Bookshelf:
        del Bookshelf[Bookname]
        Bookname = input("What would you like to change the title to?")
        Author = input("What would you like to change the author to?")
        Bookshelf[Bookname] = Author
    else:
        print(f"Could not find {Bookname}.")   
def DelBook():
    Bookname = input("What book would you like to delete?: ")
    if Bookname in Bookshelf:
       del Bookshelf[Bookname]
       print(f"{Bookname} has been removed.")
    else:
        print(f"Could not find {Bookname}.")
def ShowBooks():
    if Bookshelf:
        for Bookname, Author in Bookshelf.items():
            print(f"{Bookname} - {Author}")
    else:
        print("There are no books.")

while True:
    print("Menu:")
    print("1. Add a book")
    print("2. Edit a book")
    print("3. Delete a book")
    print("4. Show all books")
    print("5. Quit")
    val = input("Input your choice: ")
    if val == "1":
        AddBook()
        continue
    elif val == "2":
        EditBook()
        continue
    elif val == "3":
        DelBook()
        continue

    elif val == "4":
        ShowBooks()
    elif val == "5":
        break
    else:
        print("Incorrect input, please try again")
#My code, since the teacher wants us to only use one key it ends up being that the key name is the books name
#And the value of the name is the author
#This creates issues with editing as he wanted us to only make it edit the author.
#However what do you do if you need to edit the title? 
#So i made it just delete the whole book and make a new one, without the user knowing ofc.
#So its just the 3. delete a book and 1. Add a book in one option.

#Next exercise, now we have 2 values to the key
#N.2_L4
# Skapa ett tomt bibliotek (dictionary)
library = {}
# Funktion för att lägga till en bok i biblioteket
def add_book():
    title = input("Series name: ")
    Time = input("Runtime: ")
    rating = int(input("Rating:"))
    library[title] = [Time, rating]
    print(f"{title} with runtime {Time} and rating {rating} has been added.")

# Funktion för att ta bort en bok från biblioteket
def remove_book():
    title = input("What title would you like to remove?: ")
    if title in library:
        del library[title]
        print(f"{title} has been removed.")
    else:
        print(f"{title} does not exist")

# Funktion för att visa en lista över alla böcker i biblioteket
def print_library():
    print("Series:")
    for title, (Time, rating) in library.items():
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        # PARENTHESIS NEEDED FOR MORE THAN ONE VALUE!!!!!!!!!!!!!!!!!!
        #!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        print(f"{title} runtime: {Time} rating:{rating}")

# Huvudloop för programmet
while True:
    print("What would you like to do?:")
    print("1. Add series")
    print("2. Remove series")
    print("3. Show list")
    print("4. Quit")
    choice = input("Input: ")
    if choice == "1":
        add_book()
    elif choice == "2":
        remove_book()
    elif choice == "3":
        print_library()
    elif choice == "4":
        print("Program exited.")
        break
    else:
        print("Incorrect answer.")
    

#I think i just assigned two values to the one key
#But the teacher used a subdictionary. As in a dictionary assigned to the key in the origial dictionary
#Im not sure if i assigned two values or a list, cause a list is [] and i put the two values in those.