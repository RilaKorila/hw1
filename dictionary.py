import sys

def load(file):
    try:
        with open(file) as fin:
            #ファイルを読み込む
            data = fin.read()
            #スペースや改行を除去
            stripped_data = data.strip()
            #改行があったら区切る
            words = stripped_data.split('\n')

            return [word.lower() for word in words]
    except IOError as e:
        print("Error: {}",format(e))
        sys.exit(1)
