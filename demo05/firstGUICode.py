from Tkinter import *
import tkMessageBox


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        # self.quitButton = Button(self, text='Hello', command=self.hello)
        # self.helloLabel = Label(self, text='Hello,World!')
        self.nameInput = Entry(self)
        self.alertButton = Button(self, text='Hello', command=self.hello)
        self.pack()
        self.createwidgets()

    def createwidgets(self):
        self.nameInput.pack()
        self.alertButton.pack()

    def hello(self):
        name = self.nameInput.get()
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
# app.master.title('Hello,World!')
app.mainloop()
