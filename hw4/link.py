def readData(file_name):
    try:
        file = open(file_name)
        lines = file.readlines()

        for line in lines:
            print(line)

    except Exception as e:
        print(e)

    finally:
        file.close()



while True:
    print('from > ', end = "")
    start = input()
    print('to > ', end = "")
    goal = input()

    readData('./.gitignore/links.txt')
    readData('./.gitignore/nicknames.txt')
    answer = 3
    print("from %s to %s -> %d steps" % (start, goal, answer))

    print('Do you continue? (yes/no) >', end = '')
    judgement = input()
    if judgement == 'yes':
        pass
    elif judgement == 'no':
        break
    else:
        print('please input yes or no')
        break
