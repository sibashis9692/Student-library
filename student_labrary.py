class Library:
    def __init__(self,list_of_books) -> None:
        self.books=list_of_books
    
    def List_all_books(self):
        print(f"Books present in library: {self.books}")

    def Books_isue(self,isue_book_name):
        if isue_book_name in self.books:
            print(f"Congrats your {isue_book_name} book are now isue! Please the book is return in 30 days")
            self.books.remove(isue_book_name)
        else:
            print(f"Sorry your {isue_book_name} book is not present in Labrary Please isue another book")

    def return_book(self,return_book):
        print("Thanks for return the books!")
        self.books.append(return_book)

class student:
    def request_Books(self):
        isue_book_name=input("enter you book name which you want to isue: ")
        return(isue_book_name)
    
    def return_book(self):
        return_book=input("enter which book is return: ")
        return(return_book)

if __name__ == "__main__":
    sapta_shree_junior_science_college=Library(["Python","java","c","c++"])
    student=student()
    while(True):
        welcomeMsg=""" ======= Welcome to the sapta_shree_junior_science_college Library ======= 
                please select one of these:
                1.List all the books
                2.Request a book
                3.return Book
                4.exit Library """
        print(welcomeMsg)
        a=int(input("Chose a option: "))
        if(a==1):
            sapta_shree_junior_science_college.List_all_books()
        elif(a==2):
            sapta_shree_junior_science_college.Books_isue(student.request_Books())
        elif(a==3):
            sapta_shree_junior_science_college.return_book(student.return_book())
        elif(a==4):
            print("Thanks for using the sapta_shree_junior_science_college Library")
            exit()
        else:
            print("Invalid input")