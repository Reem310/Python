import xdrlib


class MathDojo:
    def __init__(self):
        self.result = 0
    def add(self, num, *nums):
        # your code here
        self.result=self.result+num
        if len(nums)>0:
            for a in nums:
                self.result=self.result+a
        return self

    def subtract(self, num, *nums):
        # your code here
        self.result=self.result-num
        if len(nums)>0:
            for a in nums:
                self.result=self.result-a
        return self
        
# create an instance:
ad = MathDojo()
bd = MathDojo()
cd = MathDojo()

# to test:
x = ad.add(2).add(2,5,1).subtract(3,2).result
print(x)	# should print 5
# run each of the methods a few more times and check the result!
b = bd.add(2).add(1,2).add(1,2,3).result
print(b)
c = cd.subtract(2).subtract(1,2).subtract(1,2,3).result
print(c)


