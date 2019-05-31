def search(word, dic_list, candidates):
    target = ''.join(word)
    result = None
    left = 0
    right = len(dic_list) - 1

    while left <= right:
        mid = int((left + right) / 2)
        #print("target: {}".format(target))

        if dic_list[mid] == target:
            result = dic_list[mid]
            break
        elif dic_list[mid] > target:
            right = mid - 1
        else:
            left = mid + 1

    if result == None:
        pass
    else:
        candidates.append(target)
