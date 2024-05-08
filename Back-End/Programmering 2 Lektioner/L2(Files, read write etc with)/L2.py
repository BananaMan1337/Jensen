#Create, read, update, remove files with function
#       open()
#Open has two parameters, filename and mode
# "r" read, opens a file for reading (error if no file exists)
# "a" append, opens a file to add more to the end of the file (error if no file exists)
# "w" write, opens a file to write on (error if no file exists)
# "x" create, makes a file (Error if file already exists)

#There is also parameters for if you want the file to be handled in text or binary.
#Text is the normal parameter
#Binary is for images and such

#"t" text, is standard
#"b" binary, is for images and others

#open("test.txt", "rt")
#would open the file and read it
#r is for read, however we dont actually need the t at the end as text is the standard way of opening it

#            read()
#read(size)
# this above would read the amount of the file that you specify, if you leave it empty as read() it would read the whole file
#readline(size) reads a certain line in a file, size helps you pick what part you read
#readlines(hint) reads all lines in a file and returns them as a list, hint is used to limit the read for an appoximate amount

#Not sure about this so far but you seem to add a file to a variable. So you would do 
#examplefile = open("test.txt")
#and now examplefile is the file???


#examplefile = open("text.txt", "r")
#print(examplefile.read(5))
#This would return the 5 first characters of the file

#If the file is in another directory you need to specify where it is like so
#examplefile = open("C:\\Python\examplefile.txt", "r")
#print(examplefile.read())


#the function write is used to write something to a file
#examplefile.write("Now we are adding this to the file")

#You close files as such
#examplefile.close()


examplefile = open("Back-End\Programmering 2 Lektioner\L2(Files, read write etc with)\Examplefile.txt", "w")
#note, W to write
examplefile.write("Test")
examplefile.close()
#This opens our file, writes Test and then closes it

#This opens our file, reads it and prints out the contents, then closes it
examplefile = open("Back-End\Programmering 2 Lektioner\L2(Files, read write etc with)\Examplefile.txt", "r")
#Note R to read
print(examplefile.read())
examplefile.close()

examplefile = open("Back-End\Programmering 2 Lektioner\L2(Files, read write etc with)\Examplefile.txt", "a")
#Note A to append
examplefile.write("\n Helloooo this is on a new line")
examplefile.close()
#This appends the new line at the end of the file

examplefile = open("Back-End\Programmering 2 Lektioner\L2(Files, read write etc with)\Examplefile.txt", "r")
print(examplefile.read())
examplefile.close()
#Now we read it again and see both of them with one being on a new line due to \n
#Since we are writing over it with the first code on line 47-50, it wont keep adding to the file as it overwrites everything each time its run
#If we instead had append on that line it would keep adding to the file

#       import os
#This module allows you to use the operative systems built in functions. Such as removing or changing folders and files
#You then use the prefix os to use it, example
import os
os.rmdir("blablatest")
#This would try to remove the directory (folder) called blablatest

import os
if os.path.exists("c:\exampleblabla.txt"):
    os.remove("c:\exampleblabla.txt")
    print("File has been removed")
else:
    print("File does not exist")

    #This imports os, checks if a path exists, if it does it removes it, if it cant find the path it says it cannot find it.



#          with
# When using "with", the program will autmatically handle the resource and make sure it gets closed when its no longer needed.
with open("Back-End\Programmering 2 Lektioner\L2(Files, read write etc with)\Examplefile.txt", "r") as examplefile:
    #with simplifies it so we dont have to close files or assign it a variable as we do that within with
    #open("path","r") as examplefile
    #This makes the file already be the variable examplefile
    content = examplefile.read()
    #Now we assign the read into a variable so that we can easily print it
print("The contents of examplefile.txt is",content)
#Here we use the variable content instead of reading it


with open("Back-End\Programmering 2 Lektioner\L2(Files, read write etc with)\Examplefile.txt", "a") as examplefile:
    #Same as above but with append
    examplefile.write("\n This is another thing being appended")
    examplefile.write("\n You can write several lines with text.\n Since we overwrite all of this in the first program it will not continuisly add to this file.")
    #Several writes work.
    print("Text has been added to the file")
    #Tells user that it has indeed added to the file


#      strip()
#Strip is used to remove spaces in a string
text = "     example   text    "
print(text.strip())
#this will output "Example text"

#      split()
#Split uses to separate a string into a list of smaller strings based on a certain separating character
text = "Example, text, banana, cheese"
print(text.split(","))
#This would split everything after commas.



#Exercise 1
#Skriv ett program som utför följande:

# Lägg till 3 textrader till filen 'd:\exempel.txt'.
# Läs filen och skriv ut dess innehåll.
# Lägg till en text till filen och läs den igen.


exercisefile = open("exempel.txt","w")
exercisefile.write("exercise1")
exercisefile.write("exercise2")
exercisefile.write("exercise3")
exercisefile.close()
exercisefile = open("exempel.txt", "r")
print(examplefile)
exercisefile.close()
exercisefile = open("exempel.txt","a")
exercisefile.write("exercise4")
exercisefile.close()
exercisefile = open("exempel.txt", "r")
print(examplefile)
exercisefile.close()

#I dont get why we were supposed to do this? Why not use with like this?
with open("exempel.txt", "w") as exercisefile:
    exercisefile.write("exercise1\n exercise2 \n exercise3")
with open("exempel.txt","r") as exercisefile:
    content= exercisefile.read()
    print(content)
with open("exempel.txt","a"):
    exercisefile.write("exercise4")
with open("exempel.txt", "r") as exercisefile:
    content= exercisefile.read()
    print(content)


#exercise 2
#Anta att du har filen 'kompisar.txt' som innehåller namnen på några dina vänner :
#Namn1
#Namn2
#Namn3

#Skriv ett program för att skriva ut ett välkomstmeddelande, ’Hej, xxxxxx ,Trevlig helg', på
#skärmen för varje väns namn.

with open("namelist.txt","r") as exercisefile:
    for line in exercisefile:
        #for every line in the file, print this below
        print("Hello", line, "have a good weekend")
        #line here being their name


#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#!!!!!Im tired so gonna copy paste and add comments!!!!!!
#!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

#Skriv ett program som skapar en mapp med namnet "my_friends" på D:\ om den inte redan
#finns. Programmet ska sedan skapa en textfil med namnet "exempel.txt" inuti denna mapp.
#I textfilen ska programmet skriva en hälsning till varje deltagare i listan
#['Samer', 'Olivia', 'Ove', 'Sara'], där varje hälsning är på en egen rad i formatet "Hej [Namn]!".


import os
#need to import os
deltagarna = ['Samer', 'Olivia', 'Ove', 'Sara']
#makes a variable with the list of friends

if not os.path.exists('d:\my_friends'):
#if the path does not exist
os.makedirs('d:\my_friends')
#make the path
# Skriv till filen 'exempel.txt' inuti mappen 'my_friends'
with open('d:\my_friends\exempel.txt', 'w') as fil:
    #open the file however there is no file?
    #Think teacher made a mistake, this would return an error as the file doesnt exist even if we make the directory, we have to make the file too

for y in deltagarna:
#For every deltagare write the below
fil.write('Hej ' + y + '!\n') 
