from tkinter import*
class Point:
    def __init__(self,Column_,Row_):#координаты поинта (колонна,ряд)
        self.Column=Column_
        self.Row=Row_ 
class View:
    def __init__(self,model,controller):    
        self.mainwindow= Tk()
        self.canvas = Canvas(self.mainwindow,width = 600,height = 600)
        self.mainwindow.title("Snake")
        self.model=model
        self.controller=controller
        self.CellsSetka=[]
        self.controller.specialfunc=self.controllers
        #создание поля
        for i in range(30):
          for k in range(30):
             self.CellsSetka.append(Point(i,k))
        #отрисовка поля
        for point in self.CellsSetka:
            X0=(point.Column+2)*15
            Y0=(point.Row+2)*15
            X1=X0+15
            Y1=Y0+15
            self.PaintRectange(X0,Y0,X1,Y1,"Gray")                   
    def canvasupdate(self):
        self.canvas.update()
    #отрисовка поинта
    def PaintRectange(self,X0,Y0,X1,Y1,Color):
        self.canvas.create_rectangle(X0,Y0,X1,Y1,fill=Color)
    # управление
    def controllers(self):
        self.mainwindow.BindKey("<Right>",self.model.Keys)
        self.mainwindow.BindKey("<Left>",self.model.Keys)
        self.mainwindow.BindKey("<Up>",self.model.Keys)
        self.mainwindow.BindKey("<Down>",self.model.Keys)