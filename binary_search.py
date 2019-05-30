def search(word, dicList, list):
    target = ''.join(word)
    #target = word 
    result = None
    left = 0
    right = len(dicList) - 1

    while left <= right:
        mid = int((left + right) / 2)
        #print("target: {}".format(target))

        if dicList[mid] == target:
            result = dicList[mid]
            break

        elif dicList[mid] > target:
            right = mid - 1

        else:
            left = mid + 1

    if result == None:
        pass

    else:
        print(target)
        list.append(target)
