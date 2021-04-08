import requests
import json

word =input(str("enter the word "))
resp = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en_US/{word}/')

if resp.status_code == 200:
    data = (resp.content).decode('utf8')
    data = json.loads(data)
    print(data[0]['meanings'][1]['partOfSpeech'],data[0]['meanings'][1]['definitions'][0]['definition'])
    # for i in data[0]['meanings'][1]:
    #     # print(data)
    #     print('part of speech ---> ',i['partOfSpeech'])
    #     print('defination --> ',i['definitions'][0]['definition'])
    #     # for j in i['definitions']:
    #         # print(j['definition'])
    #     print('#'*10)
    #     # print(i['definitions'][0]['definition'])
else:
    print('matching details not found')
    