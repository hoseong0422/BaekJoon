import re

S=input()

if S.find('A')!=-1:
    S=re.sub('[B-D,F]', 'A', S)
elif S.find('B')!=-1:
    S=re.sub('[C-D,F]', 'B', S)
elif S.find('C')!=-1:
    S=re.sub('[D,F]','C',S)
else:
    S=re.sub('[D-Z]','A',S)
    
print(S)