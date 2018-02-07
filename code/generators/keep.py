def keeper(path):
    with open(path, encoding='UTF-8') as L:
        for n in L:
            print(n)
            k = input("Keep this line? ")
            if k == 'y' or k == 'yes':
                with open('clean_' + path, 'a') as f:
                    f.write(n)
            else:
                pass
