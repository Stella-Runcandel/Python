#magic methods (use __)
#__init__, __str__, __eq__, etc...
#automatically called, let's dev defien and or customize bheaviour of objects

class Book:

    def __init__(self,title, author,num_pages):
        self.title = title
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f'{self.title} by {self.author}' #now calling print(book1 now gives us this insteed of memory adress)
            
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    def __lt__(self,other):
        return self.num_pages < other.num_pages
    
    def __gt__ (self,other): #makes x > y work
        return self.num_pages > other.num_pages
    def __add__ (self,other): #makes x + y work
        return f'{self.num_pages + other.num_pages} pages'
    def __contains__ (self,keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__ (self,key):
        if key == "title":
            return self.title        
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"Key: {key} was not found"

Book1 = Book("The Hobbit","J.R.R Tolkien",310)
Book2 = Book("Harry Potter and The Philosopher's Stone","J.k Rowling",223)
Book3 = Book("The lion, the Which and the Wardrobe","C.S Lewis",172)
Book4 = Book("The lion, the Which and the Wardrobe","C.S Lewis",170)



print(Book1,Book2,Book3,sep="\n")
print(Book1==Book2)
print(Book3==Book4) #false but why? def __eq #now upon runing again we get equal
print(Book1 + Book2) 
#we can search for keywords in the titles?
print("Lion" in Book3) #error if contains not define

#now let's try searching for key given object -> book one, search title?
print(Book1["title"])
print(Book1["author"])
print(Book1["num_pages"])
print(Book1["audio"])