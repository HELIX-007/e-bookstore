print('         *********************************')
print('          Hello,Welcome to AMA ebookstore')
print('         *********************************')
print('please select your desired genres\nscifi,horror,mystery,novel,selfhelp')


scifi=['The Martian','Frankenstei','I,Robot','Ready Player One','the time machine'] 
horror=['The Shinny','Haunting Of Hill House','The Silence The Lambs','The Exorcist','American Psyco']
mystery=['Sharp Objects','Double Cross','Angels and Demons','Battle Ground','The Da Vinci Code']
novel=['To Kill a Mockingbird','The Great Gasby','Pride and prejudice','The Lord Of The Rings','War and Peace']
selfhelp=['Think and grow rich','The subtle art of not giving a fuck','The power of habit','12 rules for life','the 48 laws of power']
genre=[scifi,horror,mystery,novel,selfhelp]

g=input('type your desired genre')

if genre[0]==g:
    print(genre[0])
