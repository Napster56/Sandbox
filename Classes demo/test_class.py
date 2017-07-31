

class Test:
    def __init__(self, param=''):
        self.string=''
        for char in param:
            if char.isalpha():
                self.string += char


    def __add__(self, param):
        if type(param) == Test:
            string = self.string + param.string
            return Test(string)
        else:
            return self

    def __str__(self):
        return "Value: {}".format(self.string)

inst1 =Test("abc")
inst2 =Test("123ijk")
sumInst1 = inst1 + inst2
sumInst2 = inst1 + "xyz"
print(inst1)
print(sumInst1)
print(sumInst2)
print(isinstance(sumInst2, Test))

