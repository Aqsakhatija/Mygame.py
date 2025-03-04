class livingthing:
    def isAlive(self):
        self.breath=True
class plants(livingthing):
    def smells(self,s):
        super().isAlive()
        self.smells=s
    def moves(self,m):
        super().isAlive()
        self.motion=False
class animals(livingthing):
    def smells(self,s):
        super().isAlive()
        self.smells=s
    def moves(self,m):
        super().isAlive()
        self.motion=m
p1=plants(); p1.smells("Lavender") ; print(p1.breath) ; print (p1.smells)
a1=animals(); a1.moves("swim"); print (a1.isAlive) ; print(a1.motion )



