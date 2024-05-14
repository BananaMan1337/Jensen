from L5_klass import Book, Customer, Student, Car
#imports from the class.py, the Book and Customer class


book1 = Book("The Stockholm City", "Samuel Khan", "2001")
print(book1.title)
print(book1.describe())

Person1 = Customer("Samuel","23")
print(Person1.Greeting())


student1 = Student("Lisa", "9")
print(student1.Introduction())


car1 = Car("Volvo","V70","1999",0)
print(car1.drive(30))
print(car1.stop(0))

car2 = Car("Toyota","Prius","2005",0)
print(car2.drive(40))
print(car2.stop(0))