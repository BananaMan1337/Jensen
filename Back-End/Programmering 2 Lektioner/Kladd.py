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