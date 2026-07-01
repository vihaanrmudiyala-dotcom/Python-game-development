countryDb={}
while True:
    print('1.insert')
    print('2.display all coutries')
    print('3.display all capitals')
    print('4.get capital')
    print('5.delete')
    choice=int(input('enter your choice from 1-5'))
    if choice==1:
        country=input('enter country:').upper()
        capital=input('enter capital:').upper()
        countryDb[country]=capital
    elif choice==2:
        print(list(countryDb.keys()))
    elif choice==3:
        print(list(countryDb.values()))