#کد اصلي
from Bookstore_Eng import Bookstore
from Book_Eng import Books
mybookstore = Bookstore()

print('''|---------------------------------------------------------------------|
|                < Welcome to "Nazanin Bookstore. >                   |
|                      ************************                       |
| Enter 'Commands' to see all of the command available.               |
|---------------------------------------------------------------------|''')
while True:
    Command = input("|What's your command? ")
    if Command.lower() == 'commands':   #valid command that user can enter
        print('''|---------------------------------------------------------------------|
| Here is the list of valid commands that you can enter:              |
|                      ************************                       |
|            About             ->         Regarding the bookstore.    |
|---------------------------------------------------------------------|
|            Menu              ->         Main menu of bookstore.     |
|---------------------------------------------------------------------|
|            Call              ->            Our phone number.        |
|---------------------------------------------------------------------|
|       Support / Guide        ->               Extra help.           |
|---------------------------------------------------------------------|
|         Quit / Exit          ->          Quiting the program.       |
|---------------------------------------------------------------------|''')
        continue

    elif Command.lower() == 'about':    #bookstore__repr__
        print('''/                                                                      \
|Welcome to Nazanin Bookstore. Thanks for visitng us for purchasing book|
\                                                                       /
|---------------------------------------------------------------------|''')
    
    elif Command.lower() == 'menu':   #showing the store menu
         print('''|---------------------------------------------------------------------|
|                                MENU                                 |
|                      ************************                       |
|             Cart                ->         Showing your cart.       |
|---------------------------------------------------------------------|
|           All Books             ->       All the books available.   |
|---------------------------------------------------------------------|
|           Book Info             ->        Description of a book     |
|---------------------------------------------------------------------|
|            Purchace             ->             Buy a book.          |
|---------------------------------------------------------------------|
|             Remove              ->       Remove a book from cart.   |
|---------------------------------------------------------------------|
|           Search Book           ->       Search title of a book.    |
|---------------------------------------------------------------------|
|          Search Author          ->      Search name of an author.   |
|---------------------------------------------------------------------|
|          Search Genre           ->      Search for specific genre.  |
|---------------------------------------------------------------------|
|             Factor              ->          list of purchace.       |
|---------------------------------------------------------------------|
|             Receipt             ->     receipt after your purchase. |
|---------------------------------------------------------------------|
|NOTE ->  Test your chances of winning a discount Enter "Get Discount"|
|---------------------------------------------------------------------|''')   

    elif Command.lower()== 'all books':
        print('Here is a list of Books that we have available: ')
        counter = 1
        for book in Books:
            print(f'{counter}- {book.title}')
            counter +=1
        print()
        
    elif Command.lower() == 'cart':    #cart
        try:
            print(mybookstore.See_cart(),'\n')
        except TypeError:
            print('Your cart is empty.\n')

    elif Command.lower() == 'search book':   #search book
        search_Book = input("Enter the name of the book that you're looking for: ")
        search_Book = search_Book.title()
        print(mybookstore.searchBook(search_Book),'\n')

    elif Command.lower() == 'search author':   #search author
        search_author = input("Enter the author that you're looking for: ")
        print(mybookstore.search_Author(search_author),'\n')

    elif Command.lower() == 'search genre':   #search genre
        search_genre = input("Enter the genre that you're looking for: ")
        print(mybookstore.search_Genre(search_genre),'\n')
         
    elif Command.lower() == 'purchace':   #buy  #############################################
        while True:
            print('Enter title of a book or enter "Back" to go back to the menu.')
            title = input('Enter the title of book that you want to purchace: ')
            if title.lower() == 'back':     #برگشت
                print('Your in menu panel now.')
                break
            title = title.title()
            found_book = False
            for book in Books:
                if book.title == title:
                    found_book = True
                    while True:
                        try:
                            number = int(input('How many copies of this book are intend to purchase? '))
                            break
                        except ValueError:
                            print('Enter a number.')
                    Add_Book = book
                    mybookstore.Add_cart(Add_Book, number), '\n'
            if not found_book:
                print('Unable to find the book.')
            
    elif Command.lower() == 'remove':  #remove
        while True:
            print(mybookstore.See_cart())
            print('NOTE: The book will be removed fro myour cart entirly.\nEnter "Back" to go back to main menu.')
            Remove_Book = input('Enter the name of the book that you want to remove from your cart: ')
            if Remove_Book.lower() == 'back':     #برگشت
                print('Your in menu panel now.')
                break
            Remove_Book = Remove_Book.title()
            mybookstore.Remove_cart(Remove_Book)      

    elif Command.lower() == 'book info':   #showbookinfo 
        print('''|---------------------------------------------------------------------|
|  Welcome to the *Book-Info* menu:\nTo see all commands enter menu  .|
|                      ************************                       |''')
        title = input('|First please enter title of the book: ')
        title = title.title()
        found_book = False
        for book in Books:
            if book.title == title:
                found_book = True   #اگه تو ليست بود
                print('''|---------------------------------------------------------------------|
|Valid commands that you can use here:                                |
|author - price - series - genre - publisher - description - summary')|
|For seeing all infos in one place you can enter "all info"           |
|---------------------------------------------------------------------|\n''')

                while True:
                    ShowBookInfo_command = input('|What do you want to know about this book?')
                    if ShowBookInfo_command.lower() == 'summary':   #خلاصه
                        summary = book.get_summary()
                        lengthLine = 69
                        line = ""                          #متن توي کادر جا بشه
                        for word in summary.split():
                            if len(line + " " + word) <= lengthLine:
                                line += (" " + word)   #کلمه شکسته نشه
                            else:
                                print('|',line,'|')
                                line = word
                        if line:
                            print('|',line,'|')
                        print('|---------------------------------------------------------------------|\n')
                    elif ShowBookInfo_command.lower() == 'author':   #نويسنده
                        print('|',book,'\n')
                    elif ShowBookInfo_command.lower() == 'price':   #قيمت
                        print('|',book.get_price(),' toman','\n')
                    elif ShowBookInfo_command.lower() == 'stock':   #موجودي
                        if book.available > 0:
                            print('|',book.get_available(),'\n')
                        else:    
                            print(f'''|{title} is out of stock.                                            |\n''')
                    elif ShowBookInfo_command.lower() == 'publisher':   #انتشارات
                        print('|',book.get_publisher(),'\n')
                    elif ShowBookInfo_command.lower() == 'series':   #مجموعه
                        if book.get_series() == '-':
                            print('''|This book doesn't belong to any series.                              |\n''')
                        else:    
                            print('|',book.get_series(),'\n')
                    elif ShowBookInfo_command.lower() == 'description':   #توضیحات کتاب
                        print('|',book.get_desc(),'\n')
                    elif ShowBookInfo_command.lower() == 'genre':   #ژانر
                        print('|',book.get_genre(),'\n')
                    elif ShowBookInfo_command.lower() == 'all info':   #توضیحات کامل
                        print('|',book.full_info(),'\n')
                    elif ShowBookInfo_command.lower() == 'quit':
                        print('''|Exiting from "Book-Info" menu.'                             |
|---------------------------------------------------------------------|\n''')
                        break
                    else:
                        print('''|Command was invalid. Check that there are no typos.                      |
|---------------------------------------------------------------------|\n''')
        if not found_book:  #اگه پيدا نشد
            print('''|Unable to find the book. Quiting the *Book-Info* menu.                               |
|---------------------------------------------------------------------|\n''')


            
    elif Command.lower() == 'factor':   #factor
        try:
            print(mybookstore.Show_Purchase(),'\n')
        except ValueError:
            print('Your cart is empty.')
            
    elif Command.lower() == 'get Discount':   #با بردن ميني گيم يوزر کد تخفيف ميگيره
        print("Let's play a minigame if you win you'll get a discount code.")
        print('Try to guess a number in range of 1 to 20. you have 4 chances to guess.')
        import random
        num = random.randint(1,20)
        userGuess = int(input('Enter your guess:'))
        counter = 0
        while counter <= 4:
            if userGuess == num:
                print('You won!')
                OFF_list = [10,15,20,25,30,35,40,45,50]  #درصد تخفيفي که يوزر ميتونه بگيره
                OFF_Chance = random.choices(OFF_list)   
                Code_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '@', '#', '!', '$', '%', '*']
                DiscountCode = ''.join(random.choices(Code_list, k=5))  #کد تخفيف
                print(f'You won *{OFF_Chance}%* discount.')
                print(f'To use your discount enter {DiscountCode} in "receipt" command.')
                break
            elif userGuess > num and userGuess < 20:
                counter += 1
                print(f'Guess lower.{4 - counter} chances left.')
                num = int(input('Enter your guess:'))
            elif userGuess < num and userGuess > 1:
                counter += 1
                print(f'guess higher.{4 - counter} chances left.')
                num = int(input('Enter your guess:'))
            else:
                counter += 1
                print(f'Enter a number in range of (1,20).{4 - counter} chances left.')
                num = int(input('Enter your guess:'))
        else:   #باخت يوزر
            print('Sorry you lost the minigame.')

    elif Command.lower() == 'receipt':   #receipt
        try:
            print(mybookstore.receipt(Bookstore))
            answer = input('Do you have any discount code? ')
            while True:
                if answer.lower == 'yes':
                    counter = 0 
                    while counter < 3:  
                        print(f'You have {3 - counter} chances. Check to enter your code correctly.')
                        Discount = input('Enter your discount code here: ')
                        if Discount == DiscountCode:
                            OFF = OFF_Chance // 100
                            print(mybookstore.receipt(OFF))
                            print('Thanks for your purchase.\nGoodbye')
                            break
                        else:
                            counter += 1
                            print(f'Invalid. {3 - counter} more chances')
                    else:
                        print('Discount code is expired.')
                        print(mybookstore.receipt())
                        print('Thanks for your purchase.\nGoodbye')
                elif answer.lower == 'no':
                    print(mybookstore.receipt())
                    print('Thanks for your purchase.\nGoodbye')
                    break
                else:
                    answer = input('Please answer with "yes" or "no": ')
            break
        except ValueError:
            print('Your cart is empty.')
    
    elif Command.lower() == 'support':  #پشتيباني
        print('For support text or call this number -> 987654\n')

    elif Command.lower() == 'call':  #تماس
        print('Our phone number -> 654321\n')
        
    elif Command.lower() == 'guide':   #راهنماي
        print('If you need help call this number for more help -> 123456\n')
        
    elif Command.lower() == 'quit' or Command.lower() == 'exit':   #quiting the shop
        answer = input('Are you sure you want to exit the program?')
        if answer.lower() == 'yes':
            print('Thanks for visiting our bookstore.\nGoodbye')
            break
        while True:
            if answer.lower() == 'no':
                print('program is still active.','\n')
                break
            elif answer.lower() != 'yes':
                print('Invalid input.')
                answer = input('Try answering again: ','\n')

    else:
        print("The command that you've entered is invalid. Check that there are no typos.",'\n')
        continue
