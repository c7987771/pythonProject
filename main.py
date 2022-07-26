import tkinter as tk
import time
import tkinter.messagebox



root = tk.Tk()
root.geometry("500x500+250+150")
root.title('文字遊戲')


clockcount = 5
testcount = 1
myscore = 10
b = tk.IntVar()
b.set(testcount)
a = tk.StringVar()
a.set(myscore)

def addscore():
    global myscore
    myscore = myscore + 10
    a.set(myscore)

def addtest():
    global testcount
    testcount = testcount + 1
    b.set(testcount)

def onYes():
    addscore()
    addtest()
    tkinter.messagebox.showinfo(title = '答對', # 視窗標題
                                message = "恭喜答對得10分")   # 訊息內容


def onNo():
    addtest()
    tkinter.messagebox.showinfo(title = '錯誤', # 視窗標題
                                message = "錯誤，下一題請加油")   # 訊息內容


def ontime():
    addtest()
    tkinter.messagebox.showinfo(title = '時間到', # 視窗標題
                                message = "時間到，下一題請加油")   # 訊息內容


def countdown():
    global clockcount
    global testcount
    testcount = testcount + 1
    clock =  button_clock.after(1000,countdown)
    clockcount = clockcount - 1

    if clockcount == -1:
        clockcount=5
        button_clock.after_cancel(clock)
        button_clock['state']='normal'
        ontime()

    else:
        button_clock['state']='disable'
        label_clock['text'] = str(clockcount)
        addtest()







label_clock = tk.Label(root)
label_score = tk.Label(root,textvariable=a)
label_score.pack()


button_clock = tk.Button(root,text='開始答題',command = lambda:countdown())


if testcount == 1:
    label_question = tk.Label(root, text='唐朝詩人杜牧詩「東風不與周郎便，銅雀春深鎖二喬」，寫的是哪一場戰役？')
    button_test1 = tk.Button(root, text='1.巨鹿之戰',command=lambda:onNo())
    button_test2 = tk.Button(root, text='2.官渡之戰',command=lambda:onYes())
    button_test3 = tk.Button(root, text='3.赤壁之戰',command=lambda:onNo())
    button_test4 = tk.Button(root, text='4.潼關之戰',command=lambda:onNo())

elif b == 2:
    label_question = tk.Label(root, text='「赤壁遺雄烈，青年有俊聲。弦歌知雅意，杯酒謝良朋。曾渴三千斛，常驅十萬兵，巴丘終命處，憑弔欲傷情。」這首詩寫的是誰？')
    button_test1 = tk.Button(root, text='1.周瑜')
    button_test2 = tk.Button(root, text='2.諸葛亮')
    button_test3 = tk.Button(root, text='3.曹操')
    button_test4 = tk.Button(root, text='4.劉備')

elif b == 3:
    label_question = tk.Label(root, text='「「大丈夫死於亂世，當帶三尺劍立於不世之功，與所世未遂夸何死乎，言訖而之！」請問這句話是誰說的？')
    button_test1 = tk.Button(root, text='1.周瑜')
    button_test2 = tk.Button(root, text='2.曹真')
    button_test3 = tk.Button(root, text='3.典韋')
    button_test4 = tk.Button(root, text='4.太史慈')

elif b == 4:
    label_question = tk.Label(root, text='劉備身邊的五虎上將何者為非？')
    button_test1 = tk.Button(root, text='1.諸葛亮')
    button_test2 = tk.Button(root, text='2.趙雲')
    button_test3 = tk.Button(root, text='3.關羽')
    button_test4 = tk.Button(root, text='4.張飛')

button_clock.pack()
label_clock.pack()
label_question.pack()
button_test1.pack()
button_test2.pack()
button_test3.pack()
button_test4.pack()

root.mainloop()