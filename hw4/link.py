import networkx as nx
import matplotlib.pyplot as plt
import queue


def readData(file_name):
    try:
        file = open(file_name)
        lines = file.readlines()
        dataList = makeDataList(lines)

    except Exception as e:
        print(e)

    finally:
        file.close()

    return dataList

def makeDictionary(lines):
    dataDictionary = {}

    for line in lines:
        data = line.split('\t')
        key = data[0]
        value = data[1]
        dataDictionary[key] = value

    print(data)
    return dataDictionary

def makeDataList(lines):
    dataList = []

    for line in lines:
        data = line.split()
        dataList.append(data)

    return dataList


def makeGraph(nodes, edges):
    G = nx.DiGraph()

    for data in nodes: #make nodes from nicknameData
        G.add_node(data[0])

    for link in edges:
        G.add_edge(link[0], link[1])

    # nx.draw_networkx(G)
    # plt.show()
    return G

def searchStep(start, goal, G): #BFS
    nextData = queue.Queue()
    nextList = nx.shortest_path(G, source = start) #nextList: dict type

    return len(nextList[goal]) - 1




def searchNickname(name, lists): #search number which correspond with input nickname
    for line in lists:
        if line[1] == name:
            return line[0]
    return 'none'

while True:
    linksData = readData('./.gitignore/links.txt')
    nicknamesData = readData('./.gitignore/nicknames.txt')

    Graph = makeGraph(nicknamesData, linksData)

    print('from > ', end = "")
    start = input()
    print('to > ', end = "")
    goal = input()

    startNum = searchNickname(start, nicknamesData)
    goalNum = searchNickname(goal, nicknamesData)
    if startNum == 'none':
        print(start + " does not exist.")
        break
    if  goalNum == 'none':
        print(goal + " does not exist.")
        break

    answer = searchStep(startNum, goalNum, Graph)
    print("from [%s] to [%s]: %d steps" % (start, goal, answer))

    print('Do you continue? (yes/no) >', end = '')
    judgement = input()
    if judgement == 'yes':
        pass
    elif judgement == 'no':
        break
    else:
        print('please input yes or no')
        break
