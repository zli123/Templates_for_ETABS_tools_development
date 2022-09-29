class test():
    def __init__(self):
        self.__radius = 1.0

    def setRadius(self, x):
        self.__radius = x

    def setName(self, y):
        self.__name = y

    def getRadius(self):
        return self.__radius

a = test()
a.setRadius(3.0)
a.setName("Hello")

c = test()
c.setRadius(5.0)
c.setName("Goodbye")

e = test()
e.setRadius(10.0)

i = test()
i.setRadius(25.0)

o = test()
o.setRadius(100.0)

u = test()
u.setRadius(250.0)

li = [a, c, e, i, o, u]
liRadius = []
for k in li:
    liRadius.append(k.getRadius())


liDict = dict(zip(liRadius,li))
needToDelete = [a, e, u]

li = [x for x in li if x not in needToDelete]


c.setRadius(15.0)
li[1].setRadius(20.0)
a.setRadius(9.0)

li = [3, 5, 10]

#li = None