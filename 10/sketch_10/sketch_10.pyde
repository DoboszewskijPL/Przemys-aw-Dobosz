import unittest # wystarczy jeden import

class Library():
    availableBooks = list()
    def __init__(self, listOfBooks):
        self.availableBooks = listOfBooks
    def lendBook(self, requestedBook):
        if requestedBook in self.availableBooks:
            print("Customer have borrowed the book.")
            self.availableBooks.remove(requestedBook)
        else:
            print("Sorry, the book client want to boorow is not available in our list.")
    def displayAvailableBooks(self):
        clear()
        for number, book in enumerate(self.availableBooks):
            text(book, 20, 20+number*20)
    def addBook(self, returnedBook):
        if returnedBook:
            self.availableBooks.append(returnedBook)
            print("Client have returned the book. Thank You for using our service :)")

class Customer():
    book = ""
    haveBook = False
    def requestBook(self, book):
        print("Book You want to borrow is choosen.")
        self.book = book
        self.haveBook
        return self.book
    def returnBook(self):
        print("Book which you returning is {}".format(self.book))
        if self.haveBook:
            self.haveBook = False
            return self.book
        else:
            self.book = ""
            return False

def setup():
    size(220,100)
    global library, Przemek
    books = ["Naocznosc", "Sens Sztuki", "Harry Potter", "Duma I Uprzedzenie"]
    library = Library(books) # bo biblioteka bez książek, to nie biblioteka
    Madzia = Customer()
    Przemek = Customer()
    
def draw():
    library.displayAvailableBooks()
    fill(150)
    rect(100,10,100,20) # do wypożyczania
    rect(100,40,100,20) # do zwracania
    fill(250)
    text('wypozycz', 120,25)
    text('zwroc', 130, 55)

def mouseClicked(): # poklikajcie kilkakrotnie w przyciski: wypożyczneie dwa razy tej samej książki, próba zwrócenia bez posiadania żadnej? Kto podejmuje działanie? 
    if mouseX >100 and mouseX<200:
        if mouseY >10 and mouseY <30:
            library.lendBook(Przemek.requestBook("Duma I Uprzedzenie")) # cała interakcja między biblioteką a klientem łączy się dopiero tutaj, obiekty są oddzielne i każdy ma swoją odpowiedzialność: biblioteka za przechowywane książki, klient za wypożyczoną i to tej odpowiedzialności dotyczą metody, nie używają wzajemnie swoich pól, jest porządek
        if mouseY >40 and mouseY <60:
            library.addBook(Przemek.returnBook())

class Test(unittest.TestCase):
    
    def test_kolejnosci(self):
        ksiazki = ["Harry Potter", "Dzungla", "Pinokio"]
        result = sorted(ksiazki) # ten test sprawdza wbudowaną metodę sortującą, a powinien klasy i metody znajdujące się w kodzie
        self.assertEqual(result, ["Dzungla", "Harry Potter", "Pinokio"])
        
    def test_ilosci(self):
        ksiazki = ['Harry Potter', 'Ksiega Dzungli', 'Pinokio']
        result = len(ksiazki) # ponownie, sprawdza metodę wbudowaną len
        self.assertNotEqual(result, 5)
        
    def test_przykladny_wypozyczenia_z_biblioteki(self):
        lib = Library(["Harry Potter", "Dzungla", "Pinokio"])
        lib.lendBook("Harry Potter")
        self.assertEqual(lib.availableBooks, ["Dzungla", "Pinokio"])

if __name__ == '__main__':
    unittest.main()
    
#1,5pkt
