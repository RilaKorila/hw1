import networkx as nx
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


def makeGraph(nodes, edges): # make a graph from data
    G = nx.DiGraph()

    for data in nodes: #make nodes from pagesData
        G.add_node(data[0])

    for link in edges:
        G.add_edge(link[0], link[1])

    # nx.draw_networkx(G)
    # plt.show()
    return G

def searchStep(start, goal, G): # research how many step it costs
    nextData = queue.Queue()
    nextList = nx.shortest_path(G, source = start) #nextList: dict type

    if goal in nextList:
        return len(nextList[goal]) - 1
    else:
        return -1




def searchPage(name, lists): #search number which correspond with input nickname
    for line in lists:
        if line[1] == name:
            return line[0]
    return 'none'



linksData = readData('./.gitignore/wikipedia_links/links.txt')
pagesData = readData('./.gitignore/wikipedia_links/pages.txt')
Graph = makeGraph(pagesData, linksData)

while True:
    print('from > ', end = "")
    start = input()
    print('to > ', end = "")
    goal = input()

    startNum = searchPage(start, pagesData)
    goalNum = searchPage(goal, pagesData)
    if startNum == 'none':
        print(start + " does not exist.")
        break
    if  goalNum == 'none':
        print(goal + " does not exist.")
        break

    answer = searchStep(startNum, goalNum, Graph)
    if answer != -1:
        print("from [%s] to [%s]: %d steps" % (start, goal, answer))
    else:
        print("[%s] is not connected to [%s]" % (start, goal))

    print('Do you continue? (yes/no) >', end = '')
    judgement = input()
    if judgement == 'yes':
        pass
    elif judgement == 'no':
        break
    else:
        print('please input yes or no')
        break
