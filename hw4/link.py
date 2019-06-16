def readData(file_name):
    try:
        file = open(file_name)
        lines = file.readlines()

        print(lines[1])
        # for line in lines:
        #     print()

    except Exception as e:
        print(e)

    finally:
        file.close()

    return lines

while True:
    linksData = readData('./.gitignore/links.txt')
    nicknamesData = readData('./.gitignore/nicknames.txt')

    #makeGraph(linksData)
    print('from > ', end = "")
    start = input()
    print('to > ', end = "")
    goal = input()


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
