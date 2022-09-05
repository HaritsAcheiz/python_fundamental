"""
This Program show how basic while loop is used
"""

books = 10
mastered_book = 0

while mastered_book < books:
    read_times = 0
    if mastered_book == 7:
        while read_times < 2 :
            print(f'i have read {mastered_book + 1} books {read_times+1} times')
            read_times += 1
        mastered_book +=1
    else:
        while read_times < 1:
            print(f'i have read {mastered_book + 1} books {read_times+1} times')
            read_times += 1
        mastered_book += 1
    print(f'i have mastered {mastered_book} books')