class Solution:
    def calPoints(self, operations: List[str]) -> int:
        sum = 0
        score = []
        for i in range(len(operations)):
            if operations[i] == "D":
                score.append(int(score[-1] * 2))
            elif operations[i] == "+":
                score.append(int(score[-1] + score[-2]))
            elif operations[i] == "C":
                score.pop()
            else:
                score.append(int(operations[i]))
        
        for j in range(len(score)):
            sum += score[j]
        
        return sum