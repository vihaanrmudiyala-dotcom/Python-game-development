books = {'physics':180,'chemistry':220,'maths':250}
books['physics']=200
print('pyhsics book price has been updated to 200')
book1=input('\nEnter name of first new book:').lower()
cost1=int(input('enter cost of the book:'))
books[book1]=cost1
book2=input('\nEnter name of second new book:').lower()
cost2=int(input('enter cost of the book:'))
books[book2]=cost2
print('\nNew books added successfully')
search_book=input('\nEnter book name you want the price of')
if search_book in books:
    print('Cost of',search_book,'is:',books[search_book])
else:
    print('book not found!')
print("\nAll books and their cost:")
for book in books:
    print(book,':',books[book])