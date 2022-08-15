import random
from enum import Enum
class Point:
    def __init__(self,Column_,Row_):
        self.Column=Column_
        self.Row=Row_ 

class Directions(Enum):
    Up = 1
    Down = 3
    Left = 4
    Right = 6
class ModelZmeika:
    def __init__(self):
        self.dimesionSetka=30
        self.CellsSetka=[]
        for i in range(self.dimesionSetka):
          for k in range(self.dimesionSetka):
             self.CellsSetka.append(Point(i,k))
        self.CellsZmeika=[Point(0,0),Point(1,0),Point(2,0)]
        self.Goal=Point(random.randint(0,self.dimesionSetka),
                        random.randint(0,self.dimesionSetka))
    def Keys(self,event):
        #проверка на разворот
        direction=self.findDirection(event)
        if direction.value%2!=options.currentdirection.value%2: 
           self.MainLoop(direction)
    def MovementBody(self):
        for i in range(count-2,-1,-1):
            self.CellsZmeika[i],Head=Head,self.CellsZmeika[i]
    def MainLoop(self,direction):
        while True:
            count=len(self.CellsSetka)
            Tail=self.CellsZmeika[0]
            Head=self.CellsZmeika[-1]
            if self.direction==Directions.Down: 
              if Head.Row==self.dimesionSetka -1:
                 Head.Row=0
              else:
                   Head.Row+=1
              self.MovementBody()
            if self.direction==Directions.Right: 
              if Head.Column==self.dimesionSetka-1:
                 Head.Column=0
              else:
                   Head.Column+=1
              self.MovementBody()
            if self.direction==Directions.Left: 
              if Head.Column==0:
                 Head.Column=self.dimesionSetka-1
              else:
                   Head.Column-=1
              self.MovementBody()
            if self.direction==Directions.Up: 
              if Head.Row==0:
                 Head.Row=self.dimesionSetka-1
              else:
                   Head.Row-=1
              self.MovementBody()
            
            if self.CellsZmeika[-1].Column+self.CellsZmeika[-1].Row-self.Goal.Column-self.Goal.Row==0:
               Goallast=self.Goal
               self.Goal=Point(random.randint(0,self.dimesionSetka),
                                random.randint(0,self.dimesionSetka))
               if self.CellsZmeika[0].Column==self.CellsZmeika[1].Column:
                   self.CellsZmeika.insert(0,Point(self.CellsZmeika[0].Column,self.CellsZmeika[0].Row+self.CellsZmeika[0].Row-self.CellsZmeika[1].Row))
               else:
                  self.CellsZmeika.insert(0,Point(CellsZmeika[0].Column+self.CellsZmeika[0].Column-self.CellsZmeika[1].Column,self.CellsZmeika[0].Row))
            
           
               




