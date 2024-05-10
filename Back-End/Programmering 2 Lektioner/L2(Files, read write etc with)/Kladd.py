with open("d:\kompisar.txt", "r") as file:
    line = file.read()
    names = line.strip().split(",")
    for name in names:
        print("Hej," + name.strip() + "! Trevlig helg.")
