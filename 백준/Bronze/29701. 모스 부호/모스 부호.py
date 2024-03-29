hash_dict = {
    '.-':'A',
    '-...':'B',
    '-.-.':'C',
    '-..':'D',
    '.':'E',
    '..-.':'F',
    '--.':'G',
    '....':'H',
    '..':'I',
    '.---':'J',
    '-.-':'K',
    '.-..' : 'L',
    '--' : 'M',
    '-.' : 'N',
    '---' : 'O',
    '.--.' : 'P',
    '--.-' : 'Q',
    '.-.' : 'R',
    '...' : 'S',
    '-' : 'T',
    '..-' : 'U',
    '...-' : 'V',
    '.--' : 'W',
    '-..-' : 'X',
    '-.--' : 'Y',
    '--..' : 'Z',
    '.----' : '1',
    '..---' : '2',
    '...--' : '3',
    "....-" : '4',
    '.....' : '5',
    '-....' : '6',
    '--...' : '7',
    '---..' : '8',
    '----.' : '9',
    '-----' : '0',
    '--..--' : ',',
    '.-.-.-' : '.',
    '..--..' : '?',
    '---...' : ':',
    '-....-' : '-',
    '.--.-.' : '@'
    }

N = int(input())
data = list(map(str, input().split()))

answer = ''

for d in data:
    answer += hash_dict[d]

print(answer)