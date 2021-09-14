words = ['Grapes','Mango','Tabel','Apple','Cricket','Republic','Elephant','College','Traveller','Achieve','Beleiver','America','Indi','Facebook','Birthday','Monsoon','Movies','Finished','Process','Untitled','Script','Project']


def labelSlider():
    global count,sliderWords
    text = 'Welcome to typing speed Increaser'
    if(count >= len(text)):
        count = 0
        sliderWords = ''
    sliderWords += text[count]
    count += 1
    fontLabel.configure(text=sliderWords)
    fontLabel.after(150,labelSlider)

def time():
    global timeleft,score,miss
    if(timeleft >=11):
        pass
    else:
        timeLableCount.configure(fg='red')

    if(timeleft>0):
        timeleft -= 1
        timeLableCount.configure(text=timeleft)
        timeLableCount.after(1000,time)
    else:
        gamePlayDetailLabel.configure(text='Hit = {} | Miss = {} | Total Score = {}'.format(score,miss,score-miss))
        rr= messagebox.askyesnocancel('Notification', 'For Play Agin Hit Try Button')
        if(rr==True):
            score = 0
            timeleft= 60
            miss = 0
            timeLableCount.configure(text=timeleft)
            worldLabel.configure(text=words[0])
            scoreLableount.configure(text=score)


def startGame(event):
    global score,miss
    if(timeleft == 60):
        time()

    gamePlayDetailLabel.configure(text='')
    if(worldEntry.get() == worldLabel['text']):
        score +=1
        scoreLableount.configure(text=score)

    else:
        miss +=1
    random.shuffle(words)
    worldLabel.configure(text=words[0])
    worldEntry.delete(0,END)


from tkinter import *
import random
from tkinter import messagebox

################################################## ROOT METHOD
from tkinter import Label
root = Tk()
root.geometry('800x500+400+100')
root.configure(bg='powder blue')
root.title('Typing game')
root.iconbitmap('img\Typing speed.png')
################################################# Variable
score = 0
timeleft = 60
count = 0
sliderwords = ''
miss = 0
################################################# LABEL METHOD
fontLabel = Label(root,text='Welcome to typing Speed Increase',font=('airal',25,'italic bold'),
                  bg='powder blue',fg='red',width=40)
fontLabel.place(x=10,y=10)

random.shuffle(words)



worldLabel = Label(root,text=words[0],font=('airal',40,'italic bold'),bg='powder blue')
worldLabel.place(x=370,y=200)

scoreLabel = Label(root,text='Your Score : ',font=('airal',25,'italic bold'),bg='powder blue')
scoreLabel.place(x=10,y=100)

scoreLableount = Label(root,text=score,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
scoreLableount.place(x=80,y=180)

timerLabel = Label(root,text='Time Left:',font=('airal',25,'italic bold'),bg='powder blue')
timerLabel.place(x=600,y=100)

timeLableCount = Label(root,text=60,font=('airal',25,'italic bold'),bg='powder blue',fg='blue')
timeLableCount.place(x=680,y=180)

gamePlayDetailLabel = Label(root,text='Type Word and Hit Enter Button',font=('arial',30,'italic bold'),
                            bg='powder blue',fg='dark grey')
gamePlayDetailLabel.place(x=150,y=400)
################################################### Entery Method
worldEntry = Entry(root,font=('airal',25,'italic bold'),bd=10,justify='center')
worldEntry.place(x=250,y=300)
worldEntry.focus_set()
#####################################################
root.bind('<Return>',startGame)
root.mainloop()