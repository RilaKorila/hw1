#coding: UTF-8
import itertools
import loadDictionary
import binary_search

print("input character: ")
list = input('>> ') #get 16 characters

#リストの中身を小文字に変える
list = list.lower()

print(list)


#アルファベット順に並べる
sortedList = sorted(list)
#newList.sort()
print("\nsort")
print(sortedList)


#アナグラムを組んだらここに格納
anagrams = []

#全部の組み合わせを考える　consider combination
permuList = itertools.permutations(sortedList)

#重複を削除
uniquePermuList = set(permuList)

#辞書を持ってくる
wordsDicList = loadDictionary.load('dictionary.txt')
wordsDicList = sorted(wordsDicList)
wordsNewDicList = []
for word in wordsDicList:
    if len(word) >= 4:
        wordsNewDicList.append(word)


#辞書の中に一致するものを探す
for permuWord in uniquePermuList:
    check = ''
    for x in permuWord: #一文字づつみていく
        check += x
        binary_search.search(check, wordsNewDicList, anagrams)


# print("\nanagrams:")
# print(anagrams)

uniqueAnagrams = set(anagrams)
print(uniqueAnagrams)
top = ''

for word in uniqueAnagrams:
    if len(top) <= len(word):
        top = word

print('\nthe longest anagram: ')
print(top)
