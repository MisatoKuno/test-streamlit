#**が歩きます
def walk(p):
    print("{}が歩きます".format(p))

a=walk("aさん")
b=walk("bさん")


"""
クラスの定義でやってみる
"""
class person:
    def __init__(self):
        self.name=""
    
    def walking(self):
        print("{}が歩きます".format(self.name))
    
p1=person()
p2=person()
p1.name="dさん"
p2.name="cさん"
p1.walking()
p2.walking()

"""
計算クラス
"""
class cul:
    def __init__(self):
        self.a=0
        self.b=0
    def SET(self,a,b):
        self.a=a
        self.b=b
    def tasu(self):
        return self.a+self.b
    def sa(self):
        return abs(self.a-self.b)
    def waru(self):
        if self.b!=0:
            return self.a/self.b
        else:
            return "0では割れません"

c=cul()
c.SET(8,3)
print(c.tasu())
print(c.sa())
c.SET(2,0)
print(c.waru())
c.SET(9,8)
print(c.waru())


"""
計算クラス２：引数つき
"""
class person2:
    def __init__(self,name):
        self.name=name
    def waaalk(self):
        print("{}さんが歩きます".format(self.name))

P=person2("misato")
P.waaalk()


"""
計算クラス3:継承したバージョン
"""
class newcul(cul):
    def kakeru(self):
        return self.a*self.b

n=newcul()
n.SET(5,4)
print(n.kakeru())