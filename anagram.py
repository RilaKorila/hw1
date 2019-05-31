#coding: UTF-8

import itertools
import dictionary
import binarysearch

print("input character: ")
input_list = input('>> ') #get 16 characters

#リストの中身を小文字に変える
lowered_input_list = input_list.lower()

print(lowered_input_list)
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
sorted_list = sorted(lowered_input_list)
#newList.sort()

#アナグラムを組んだらここに格納
anagrams = []

#全部の組み合わせを考える　consider combination
permu_list = itertools.permutations(sorted_list)

#辞書を持ってくる
words = dictionary.load('dictionary.txt')
sorted_words = sorted(words)

for permu_word in permu_list:
    binarysearch.search(permu_word, sorted_words, anagrams)


print(anagrams)
