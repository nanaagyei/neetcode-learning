class Solution:
    def calPoints(self, operations: List[str]) -> int:
        output = []

        for item in operations:
            if item == "+":
                output.append(output[-1] + output[-2])
            elif item == "D":
                output.append(2 * output[-1])
            elif item == "C":
                output.pop()
            else:
                output.append(int(item))
        
        return sum(output)