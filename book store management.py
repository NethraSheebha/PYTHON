import mysql.connector
con = mysql.connector.connect(host = 'localhost', user = 'root', password = 'arhten', database = 'BOOK_STORE')
cur = con.cursor()

def viewbooks():
    cur.execute("SELECT * FROM BOOK")
    print('','Bno', 'Bname', 'Author', 'Price in rupees  |', sep = '  |  ')
    data = cur.fetchall()
    for i in data:
        print('',i[0],i[1],i[2],i[3], sep = ' |  ',end = '  |  ')
        print()

def search():
    try:
        book_to_search = input('Enter book name or author name to search: ')
        query = "SELECT * FROM BOOK WHERE bname = '{}' or author = '{}'".format(book_to_search,book_to_search)
        cur.execute(query)
        data = cur.fetchall()
        if not data :
            print("Book not found")
        else:
            print()
            print('','Bno', 'Bname', 'Author', 'Price in rupees  |', sep = '  |  ')
            for i in data:
                print('',i[0],i[1],i[2],i[3], sep = '  |  ',end = '  |  ')
                print()

    except ValueError:
        print('Enter only strings')

def bdetails():
    book_no = int(input("Enter book number to view details: "))
    query = "SELECT * FROM BOOK NATURAL JOIN BOOK_DETAILS WHERE BNO = {}".format(book_no)
    cur.execute(query)
    data = cur.fetchone()
    global bn,bp
    bn, bp = data[1], data[3]
    if data:
        print('\nBook name -',data[1])
        print('Author -',data[2])
        print('Price in rupees -',data[3])
        print('Genre -',data[4])
        print('Rating -',data[5])
        print('Reader review -',data[6],'\n')
    else:
        print("Book not found")

def addbooks():
    try:
        while True:
            no = int(input("Enter book number: "))
            name = input("Enter book name: ").title()
            author = input("Enter author name: " ).title()
            price = int(input("Enter price: "))
            genre = input("Enter genre: ").title()
            rating = input("Enter goodreads rating: ").title()
            review = input("Enter reader's review: ").title()
            query1 = "INSERT INTO BOOK VALUES ({},'{}','{}',{})".format(no,name,author,price)
            query2 = "INSERT INTO BOOK_DETAILS VALUES ({},'{}','{}','{}')".format(no,genre,rating,review)
            cur.execute(query1)
            con.commit()
            cur.execute(query2)
            con.commit()
            print("Added successfully")
            ch = input("Add another book? (y/n): ")
            if ch in 'Yy':
                pass
            elif ch in 'Nn':
                break
            else:
                print('Invalid. Enter only y/n.')
    except ValueError:
            print("Enter only integers for book no and price; strings for name of book and author")

def updatebook():
    no = int(input("Enter book number to update: "))
    field = input("Enter field to update - book name/author/price/genre/rating/reader review : ").lower()
    if field == 'book name':
        new = input("Enter new book name: ").title()
        cur.execute("UPDATE BOOK SET bname = '{}' WHERE bno = {}".format(new,no))
        con.commit()
    elif field == 'author':
        new = input("Enter new author name: ").title()
        cur.execute("UPDATE BOOK SET author = '{}' WHERE bno = {}".format(new,no))
        con.commit()
    elif field == 'price':
        new = int(input("Enter new price: "))
        cur.execute("UPDATE BOOK SET price = {} WHERE bno = {}".format(new,no))
        con.commit()
    elif field == 'genre':
        new = input("Enter new genre: ")
        cur.execute("UPDATE BOOK_DETAILS SET genre = '{}' WHERE bno = {}".format(new,no))
        con.commit()
    elif field == 'rating':
        new = input("Enter new rating: ")
        cur.execute("UPDATE BOOK_DETAILS SET rating = '{}' WHERE bno = {}".format(new,no))
        con.commit()
    elif field == 'reader review':
        new = input("Enter new review: ")
        cur.execute("UPDATE BOOK_DETAILS SET reader_review = '{}' WHERE bno = {}".format(new,no))
        con.commit()
    print("Updated successfully")

def deletebook():
    while True:
        no = int(input("Enter book number to delete: "))
        query = "SELECT * FROM BOOK NATURAL JOIN BOOK_DETAILS WHERE BNO = {}".format(book_no)
        cur.execute(query)
        data = cur.fetchone()
        if data:
            print('\nBook name -',data[1])
            print('Author -',data[2])
            print('Price in rupees -',data[3])
            print('Genre -',data[4])
            print('Rating -',data[5])
            print('Reader review -',data[6],'\n')
        else:
            print("Book not found")
        ans = input("Delete book? (y/n): ").lower()
        if ans == 'y':
            query1 = "DELETE FROM BOOK WHERE bno = {}".format(no)
            query2 = "DELETE FROM BOOK_DETAILS WHERE bno = {}".format(no)
            cur.execute(query1)
            con.commit()
            cur.execute(query2)
            con.commit()
            print("Deleted successfully")
            break
        elif ans == 'n':
            break
        else:
            print("Invalid. Enter only y/n")

def buybook():
    name = input("Enter your name: ").title()
    mob_no = input("Enter mobile no: ")
    email = input("Enter email id: ")
    ID = name[0:3] + mob_no[7:]
    query = "INSERT INTO CUSTOMER VALUES ('{}','{}','{}',{},{},'{}')".format(ID,name,bn,bp,mob_no,email)
    cur.execute(query)
    con.commit()
    print("Thank you for buying. Visit again!")

def custrec():
    query = "SELECT * FROM CUSTOMER"
    cur.execute(query)
    data = cur.fetchall()
    print('','Cust_ID', 'Cname', 'Book', 'amount', 'mob_no','email_id |', sep = '  |  ')
    for i in data:
         print('',i[0],i[1],i[2],i[3],i[4],i[5],sep = ' | ',end = ' | ')
         print()
    
print("WELCOME TO THE BOOKSTORE\n")

print("You are:\n1-Admin\n2-Customer")
person = int(input("Enter choice: "))
while True:
    if person == 1:
        print("1 - Work on Books record")
        print("2 - View customer record")
        print("3 - Exit")
        choice = int(input("Enter choice: "))
        if choice == 1:
            print("1 - View all books")
            print("2 - Add books")
            print("3 - Update books")
            print("4 - Delete books")
            opt = int(input("Enter operation to perform: "))
            if opt == 1:
                viewbooks()
            elif opt == 2:
                addbooks()
            elif opt == 3:
                bdetails()
                updatebook()
            elif opt == 4:
                deletebook()
        elif choice == 2:
           custrec()
        elif choice == 3:
            break
    elif person == 2:
        print('1 - View available books')
        print('2 - Search book')
        print('3 - View details of a book')
        print('4 - exit')
        ch = int(input('Enter choice: '))
        if ch == 1:
            viewbooks()
        elif ch == 2:
            search()
        elif ch == 3:
            bdetails()
            cart = input("Do you want to buy this book? y/n: ")
            if cart in 'Yy':
                buybook()
            elif cart in 'Nn':
                pass
            else:
                print('Please enter only y/n.')
        elif ch == 4:
            break
        else:
            print('Invalid option')
