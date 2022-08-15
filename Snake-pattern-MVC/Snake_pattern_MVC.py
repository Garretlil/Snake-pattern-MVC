import  Model
import module2
import module3
from tkinter import*

model = Model.ModelZmeika()
controller=module2.Controller(model);
view = module3.View(model,controller)
view.canvas.pack()
view.mainwindow.mainloop()









