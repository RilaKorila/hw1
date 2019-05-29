import sys

def load(file):
    try:
        with open(file) as fin:
            #ファイルを読み込む
            loadedWord = fin.read()
            #スペースや改行を除去
            loadedWord = loadedWord.strip()
            #改行があったら区切る
            loadedWord = loadedWord.split('\n')

            loadedWord = [x.lower() for x in loadedWord]
            return loadedWord

    except IOError as e:
        print("Error: {}",format(e))
        sys.exit(1)
