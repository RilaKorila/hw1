#coding: UTF-8
import itertools
import loadDictionary
import binary_search

print("input character: ")
list = input('>> ') #get 16 characters

#リストの中身を小文字に変える
list = list.lower()

print(list)
#newList = [] #ここに1文字ずつ格納　store the character one by one

# for chara in list:
#     if chara == 'Q': #Qはuとセット　make Q and u one group
#         newList.append('Qu')
#     elif chara == 'u':
#         #何もしない do nothing
#         pass
#     else:
#         newList.append(chara)


#アルファベット順に並べる
sortedList = sorted(list)
#newList.sort()

#アナグラムを組んだらここに格納
anagrams = []

#全部の組み合わせを考える　consider combination
permuList = itertools.permutations(sortedList)

#辞書を持ってくる
wordsDicList = loadDictionary.load('dictionary.txt')

for permuWord in permuList:
    binary_search.search(permuWord, wordsDicList, anagrams)


print(anagrams)
