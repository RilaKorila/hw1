def readNumber(line, index):
  number = 0
  while index < len(line) and line[index].isdigit():
    number = number * 10 + int(line[index])
    index += 1
  if index < len(line) and line[index] == '.':
    index += 1
    keta = 0.1
  while index < len(line) and line[index].isdigit():
      number += int(line[index]) * keta
      keta /= 10
      index += 1
  token = {'type': 'NUMBER', 'number': number}
  return token, index

def readPlus(line, index):
  token = {'type': 'PLUS'}
  return token, index + 1

def readMinus(line, index):
  token = {'type': 'MINUS'}
  return token, index + 1

def readMultiplied(ine, index):
  token = {'type': 'MULTIPLIED'}
  return token, index + 1

def readDivided(line, index):
  token = {'type': 'DIVIDED'}
  return token, index + 1

def tokenize(line):
  tokens = []
  index = 0
  while index < len(line):
      if line[index].isdigit():
          (token, index) = readNumber(line, index)
      elif line[index] == '+':
          (token, index) = readPlus(line, index)
      elif line[index] == '-':
          (token, index) = readMinus(line, index)
      elif line[index] == '*':
          (token, index) = readMultiplied(line, index)
      elif line[index] == '/':
          (token, index) = readDivided(line, index)
      else:
          print('Invalid character found: ' + line[index])
          exit(1)
      tokens.append(token)
  return tokens


def evaluate1(tokens):
# '''
# Calucurate only * and /
#     Argments: tokens
#     Return:   tokens
# '''
  new_tokens = []
  index = 0

  while index < len(tokens):
      if tokens[index]['type'] == 'MULTIPLIED':
          del new_tokens[-1]
          result = tokens[index-1]['number'] * tokens[index+1]['number']
          new_token = {'type': 'NUMBER', 'number': result}
          new_tokens.append(new_token)
          index += 1
      elif tokens[index]['type'] == 'DIVIDED':
          del new_tokens[-1]
          result = tokens[index-1]['number'] / tokens[index+1]['number']
          new_token = {'type': 'NUMBER', 'number': result}
          new_tokens.append(new_token)
          index += 1
      else:
          print(tokens[index])
          new_tokens.append(tokens[index])

      index += 1
  return new_tokens

def evaluate2(tokens):
  # '''
  #   Calucurate only + and -
  #       Argments: (array[string])tokens
  #       Return:   (float)answer
  # '''
  print(tokens)
  answer = 0
  tokens.insert(0, {'type': 'PLUS'}) # Insert a dummy '+' token
  index = 1
  while index < len(tokens):
      if tokens[index]['type'] == 'NUMBER':
          if tokens[index - 1]['type'] == 'PLUS':
              answer += tokens[index]['number']
          elif tokens[index - 1]['type'] == 'MINUS':
              answer -= tokens[index]['number']
          else:
              print('Invalid syntax')
              exit(1)

      index += 1
  return answer


def test(line):
  tokens = tokenize(line)
  actualAnswer = evaluate2(tokens)
  expectedAnswer = eval(line)
  if abs(actualAnswer - expectedAnswer) < 1e-8:
      print("PASS! (%s = %f)" % (line, expectedAnswer))
  else:
      print("FAIL! (%s should be %f but was %f)" % (line, expectedAnswer, actualAnswer))
# Add more tests to this function :)


def runTest():
    print("==== Test started! ====")
    test("1+2")
    test("1.0+2.1-3")
    print("==== Test finished! ====\n")
    runTest()


while True:
    print('> ', end="")
    line = input()
    tokens = tokenize(line)
    tokens = evaluate1(tokens)
    answer = evaluate2(tokens)
    print("answer = %f\n" % answer)
