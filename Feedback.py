from tkinter import *
from tkinter import ttk


class Feedback:
    def __init__(self, master):
        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.logo = PhotoImage(file='python.gif')
        ttk.Label(self.frame_header, image=self.logo).grid(row=0, column=0, rowspan=2)
        ttk.Label(self.frame_header, text='Thanks for Exploring!').grid(row=0, column=1)
        ttk.Label(self.frame_header, text="We're glad you chose Pao&Zen travel corporation!").grid(row=1, column=1)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text='Name: ')
        ttk.Label(self.frame_content, text='Email: ')
        ttk.Label(self.frame_content, text='Comments: ')

        self.entry_name = ttk.Entry(self.frame_content, width=24)
        self.entry_email = ttk.Entry(self.frame_content, width=24)

        self.text_comments = Text(self.frame_content, width=50, height=10)

        ttk.Button(self.frame_content, text='Submit')
        ttk.Button(self.frame_content, text='Clear')


def main():
    root = Tk()
    feedback = Feedback(root)
    root.mainloop()


if __name__ == '__main__':
    main()
