import tkinter as tk

class TypewriterLabel(tk.Label):
    def __init__(self, master=None, **kwargs):
        super().__init__(master, **kwargs)
        self.text = self.cget('text')
        self.delay = 100 # in milliseconds
        self.idx = 0
        self.stop = len(self.text)
        self.display_text = tk.StringVar()
        self.config(textvariable=self.display_text)

    def start(self):
        if self.idx < self.stop:
            self.display_text.set(self.text[:self.idx])
            self.idx += 1
            self.after(self.delay, self.start)

root = tk.Tk()
label = TypewriterLabel(root, font=('Arial', 18), text='Hello, World!')
label.pack()
label.start()
root.mainloop()
