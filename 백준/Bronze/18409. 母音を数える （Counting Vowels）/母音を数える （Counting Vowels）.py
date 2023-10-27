N = int(input())
S = input()

vowels = ['a','i','u','e','o']

answer = 0

for vowel in vowels:
    answer += S.count(vowel)
    
print(answer)