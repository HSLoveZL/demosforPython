from Tkinter import *


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.quitButton = Button(self, text='quit', command=self.quit)
        self.helloLabel = Label(self, text='Hello,World!')
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.helloLabel.pack()
        self.quitButton.pack()

app = Application()
app.master.title('Hello,World!')
app.mainloop()
