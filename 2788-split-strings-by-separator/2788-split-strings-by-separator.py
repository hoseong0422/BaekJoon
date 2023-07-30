class Solution:
    def splitWordsBySeparator(self, words: List[str], separator: str) -> List[str]:
        answer = []
        for word in words:
            answer += word.split(separator)
        answer = [i for i in answer if i != '']
        return answer
        