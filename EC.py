

from tkinter import *

a = Tk()

width = 800
height = 600

def avg_score():
    _test1 = float(test1.get())
    _test2 = float(test2.get())
    _test3 = float(test3.get())

    average = (_test1+_test2+_test3)/3
    average_score.config(text=f"{average}")



frame = Frame(a)
frame.pack()


frame1 = Frame(a)
frame1.pack()

frame2 = Frame(a)
frame2.pack()



frame3 = Frame(a)
frame3.pack()


frame4 = Frame(a)
frame4.pack()


Label(frame, text="Enter score for test 1: ").pack(side=LEFT)
test1 = Entry(frame,width=10)
test1.pack(side=RIGHT)



Label(frame1, text="Enter score for test 2: ").pack(side=LEFT)
test2 = Entry(frame1,width=10)
test2.pack(side=RIGHT)


Label(frame2, text="Enter score for test 3: ").pack(side=LEFT)
test3 = Entry(frame2,width=10)
test3.pack(side=RIGHT)


Label(frame3, text="Average ").pack(side=LEFT)


average_score = Label(frame3)
average_score.pack(side=RIGHT)

Button(frame4, text="Average", width=15,
       command=avg_score).pack(side=LEFT)
Button(frame4, text="Exit", width=15,
       command=a.destroy).pack(side=RIGHT)



a.mainloop()