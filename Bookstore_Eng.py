#Bookstore eng
from Book_Eng import Book
from Book_Eng import Books
from Book_Eng import books

class Bookstore:
    def __init__(self, cart):
        self.cart = cart  #نمايش سبد خريد   'name' -> [price,copies]

    def __init__(self):
        self.cart = {}

    def __repr__(self):
        return 'Welcome to Nazanin Bookstore. Thanks for visitng us for purchasing book.'
    
    def searchBook(self, search_Book):  #جستجوي کتاب
        while True:
            search_Book_set = set(search_Book)
            for Book in Books:
                book_set = set(Book)
                if book_set.issupperset(search_Book_set) or search_Book_set.issuperset(book_set):
                    answer = input(f'Are you searching for {Book}?')
                    if answer == 'Yes':
                        print('Continue.')
                        break
                    else:
                        print('Then please try writing the name of the book carefuly')
        else:
            print('Invalid input. please answer again.')

    def searchAuthor(self, search_Author):  #جستجوي نويسنده
        while True:
            search_Author_set = set(search_Author)
            for Author in books.author:
                author = set(Author)
                if author.issupperset(search_Author_set) or search_Author_set.issuperset(author):
                    answer = input(f'Are you searching for {Author}?')
                    if answer == 'Yes':
                        print('Continue.')
                        break
                    else:
                        print('Then please try writing the name of the author carefuly')
        else:
            print('Invalid input. please answer again.')

    def searchGenre(self, search_genre):  #جستجوي ژانر
        while True:
            search_genre_set = set(search_genre)
            for genres in books.genre:
                for Genre in genres:
                    genre = set(Genre)
                    if genre.issupperset(search_genre_set):
                        answer = input(f'Are you searching for {Genre}?')
                        if answer == 'Yes':
                            print('Continue.')
                            break
                        else:
                            print('Then please try writing the name of the genre carefuly')
        else:
            print('Invalid input. please answer again.')

    def See_cart(self):  #نشان دادن سبد خريد
        return self.cart

    def Show_cart(self):    #تابع براي نشان دادن سبد خريد در اخر توابع ديگر
        answer = input('Show cart? ')
        if answer.lower() == 'yes':
            return self.cart
        else:
            print('Continue.')

   
    def Add_cart(self, Add_Book, number):
        Book_available = Add_Book.available
        Book_price = Add_Book.price
        Book_price = int(Book_price)*number
        if (Add_Book in self.cart) and ( int(Book_available) >= number ):                #کتاب تکراري / بيشتر کردن تعداد درخواست کتاب 
            new_number = number  
            number = self.cart[Add_Book.title].pop(number)
            number = number + new_number
            self.cart[Add_Book.title] = [Book_price,number]
        elif int(Book_available) >= number:                         #کتاب جديد
            self.cart.setdefault(Add_Book.title,[Book_price,number])
            Add_Book.available -= number
            print('Book added to your cart.')
            print(self.cart)
        elif Book_available == 0:   #چک کردن موجودي
            print(f'{Add_Book} is out of stock.')
        else:
            print(f'We only have {Book_available} copies of {Add_Book} left.')

    def Remove_cart(self, Remove_Book):  #حذف از سبد خريد
            for book in self.cart.copy():
                if book == Remove_Book:
                    self.cart.pop(book)
                    print(f'{Remove_Book} has been successfully removed from your cart.')
                    self.Show_cart()
            print(f'{Remove_Book} is not in your cart.')

    def Show_Purchase(self):    #نمايش فاکتور
        cart = self.cart
        with open('Report.txt','a') as report:
            text = '''|{"-"*69}|
|{"Purchase Invoice":^69}|
|{"-"*69}|'''
            report.write(text)
            price_cost = 0
            for title, price, copies in cart.keys(), cart.values():
                price = int(price)
                price_cost = price_cost + price
                text = f'''|{title:^35}->{price:^34}|'''
                report.write(text)
            else: 
                text = '''
|{"-"*69}|
|{"Total Cost":^35}:{price_cost:^34}|
|{"-"*69}|'''
                report.write(text)
        print('Report file created. you can check your factor there.')
        
    def receipt(self, cls):    #رسيد پرداخت
        cls.Show_Purchase(self)
        with open('Report.txt','a') as report:
            text = '''|{"Thanks for your purchase":^69}|
|{"-"*69}|'''
            report.write(text)
        print('Report file created. you can check your receipt there.')
        
    def OFF(self, OFF):    #کد تخفيف
        cart = self.cart
        with open('Report.txt','a') as report:
            text = '''|{"-"*69}|
|{"Purchase Invoice":^69}|
|{"-"*69}|'''
            report.write(text)
            price_cost = 0
            for title, price, copies in cart.keys(), cart.values():
                price = int(price)
                Before_Off_Price = price
                price = price * OFF
                text = f'''|{title:^35}->{price:^34}|'''
                print(text)
                Before_Off_Price_cost = Before_Off_Price_cost + Before_Off_Price
                price_cost = price_cost + price 
            else: 
                text = '''
|{"-"*69}|
|{"Total Cost":^35}:{price_cost:^34}|
|{"-"*69}|
|{"Cost difftence":^35}:{Before_Off_Price_cost - price_cost:^34}|
|{"-"*69}|'''
                report.write(text)
        print('Report file created. you can check your print receipt there.')
        




