from urllib.request import urlopen
import xmltodict

def ask(input):
  question = f'https://api.wolframalpha.com/v2/query?appid=77R2HJ-V3H7WK2YUE&input={input}'
  file = urlopen(question)
  data = file.read()
  file.close()
  data = xmltodict.parse(data)
  return data
