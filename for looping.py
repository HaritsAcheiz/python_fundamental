"""
This Program give an explanation of how for looping is used
"""

books = 10

print(f'Budi, please read {books} books for next test')

for books_have_been_read in range(1,books+1):
    print(f'i have read {books_have_been_read} books')
    books_have_been_read += 1

