print('-*-*-*-Movie Rating Manager-*-*-*-')
movies={}
while True:
    print("\nchoose an option:")
    print('1.add movie')
    print('2.view all movies')
    print('3.search movie')
    print('4.update rating')
    print('5.delete movie')
    print('6.exit')
    choice=input('enter your choice')
    if choice=='1':
        name=input('enter a movie name')
        rating=input('enter movie rating out of 10:')
        movies[name]=rating
        print(name,'added successfully')
    elif choice=='2':
            if len(movies)==0:
                print('no movies in collection')
            else:
                print('/nMovie collection:')
                for name,rating in movies.items():
                    print(name,':',rating)
    elif choice=='3':
        name=input('enter a movie name to search')
        if name in movies:
            print(name,'has a rating of',movies[name])
        else:
            print('movie not found')
    elif choice=='4':
        name=input('enter a movie to update')
        if name in movies:
             new_rating=float(input('enter a new rating'))
             movies[name]=new_rating
             print('rating updated successfully')
        else:
            print('movie not found')
    elif choice=='5':
        name=input('enter a movie to delete')
        if name in movies:
             del movies[name]
             print('movie deleted successfully')
        else:
            print('movie not found')
    elif choice=='6':
        print('Exiting moives rating manager....')
        break
    else:
        print('invald choice. Please try again')
    