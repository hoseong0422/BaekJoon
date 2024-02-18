target = {'CU'	:'see you',
          ':-)'	:'I’m happy',
          ':-('	:'I’m unhappy',
          ';-)'	:'wink',
          ':-P'	:'stick out my tongue',
          '(~.~)'	:'sleepy',
          'TA'	:'totally awesome',
          'CCC'	:'Canadian Computing Competition',
          'CUZ'	:'because',
          'TY'	:'thank-you',
          'YW'	:'you’re welcome',
          'TTYL'	:'talk to you later'}

while True:
    data = input()
    if data in target:
        print(target[data])
    else:
        print(data)

    if data == 'TTYL':
        break