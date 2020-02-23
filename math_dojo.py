class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        total = 0
        for x in nums:
            total = total + x
        self.result = total + num
        return self
    def subtract(self, num, *nums):
        total = 0
        for x in nums:
            total = total + x
        self.result = total
        return self

md = MathDojo()
x = md.add(2).add(2,5,1).subtract(3,2).result
print(x)	