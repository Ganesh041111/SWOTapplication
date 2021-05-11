import json
import tkinter
from tkinter import *
import random


from pandas import DataFrame
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# load questions and answer choices from json file instead of the file
with open('quiz_data.json', encoding="utf8") as f:
    data = json.load(f)

# convert the dictionary in lists of questions and answers_choice
questions = [v for v in data[0].values()]
answers_choice = [v for v in data[1].values()]

answers = [[0],[0,1,2,3],[1],[0,2],[0,1,2],[0,1,2,3],[0,1,2,3],[0,1,2],[0,1,2],[0,1,2]]

user_answer = []
communication = teamwork =risk_taking_ability = creativity = problem_solving = 0
indexes = []
Quality={}

def gen():
    global indexes
    while(len(indexes) < 10):
        x = random.randint(0,9)
        if x in indexes:
            continue
        else:
            indexes.append(x)

def showresult(score,communication,creativity,problem_solving,teamwork,risk_taking_ability):
    lblQuestion.destroy()
    r1.destroy()
    r2.destroy()
    r3.destroy()
    r4.destroy()

    labelimage = Label ( root, background = "#ffffff", border = 0 )
    labelimage.pack(pady=(50,30))

    #dict
    global Quality
    Quality["Communication"] = communication
    Quality["Creativity"] = creativity
    Quality["Prob_Solving"] = problem_solving
    Quality["Risk_taking"] = risk_taking_ability
    Quality["Teamwork"] = teamwork

    #sorting
    print(sorted(Quality.items(),key=lambda kv:(kv[1],kv[0])))
    
    Q_li=[]
    Q_li.append([communication,"Communication"])
    Q_li.append([creativity,"Creativity"])
    Q_li.append([problem_solving,"Problem solving"])
    Q_li.append([risk_taking_ability,"Risk taking ability"])
    Q_li.append([teamwork,"Teamwork"])
    Q_li.sort()
    print(Q_li)

    labelresulttext = Label(root, font=("Consolas", 16,"bold"),background="lightgreen", width=35, text="STRENGTH")
    labelresulttext.place(x=25, y=10)

    label01 = Label(root, font=("Consolas", 16,"bold","underline"),background="powderblue", width=35, text=" " + Q_li[4][1])
    label01.place(x=25, y=50)

    labelresulttext1 = Label(root, font=("Consolas", 16,"bold"), background="lightgreen", width=35, text="WEAKNESS")
    labelresulttext1.place(x=485, y=10)

    label02 = Label(root, font=("Consolas", 16,"bold","underline"),background="powderblue", width=35, text=" " + Q_li[0][1])
    label02.place(x=485, y=50)

    labelresulttext2 = Label(root, font=("Consolas", 16,"bold"), background="lightgreen", width=35, text="OPPORTUNITIES")
    labelresulttext2.place(x=25, y=250)

    labelresulttext3 = Label(root, font=("Consolas", 16,"bold"), background="lightgreen", width=35, text="THREATS")
    labelresulttext3.place(x=485, y=250)


    fh=open("Directory.txt","a")
    n1=2
    n2=len(Q_li[4][1])

    for i in range (0,25-n1):
        fh.write(" ")
    fh.write("----      ")
    fh.write("S: ")
    fh.write(Q_li[4][1])
    for i in range (0,25-n2):
        fh.write(" ")
    fh.write("----      ")
    fh.write("W: ")
    fh.write(Q_li[0][1])
    fh.write("\n")
    fh.close()

    #

    if Q_li[4][1] == "Communication":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="You're good at:\n - Presentation and Hosting.\n - Reporting and Interpretation.\n - Public Speaking. ",
        )
        labelresulttext4.place(x=65, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Opportunities for you:\n - Advertising/Sales Representative.\n - Public relation specialist.\n - Vlogger/Youtuber. ",
        )
        labelresulttext5.place(x=65, y=290)

    if Q_li[4][1] == "Creativity":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="You're good at:\n - Design and Craft.\n – Imagination skills.\n - Creative explanation or solutions. ",
        )
        labelresulttext4.place(x=65, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Opportunities for you:\n - Interior Designing and Architecture.\n – Sculptor, Painter, etc.\n - Movie/Video Animators. ",
        )
        labelresulttext5.place(x=65, y=290)

    if Q_li[4][1] == "Problem solving":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="You're good at:\n - Analyzing problems and finding logical solutions.\n – Mathematical Calculations.\n - Quizzes, Puzzles etc. ",
        )
        labelresulttext4.place(x=65, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Opportunities for you: \n - Mathematician, Programmer.\n – Strategic Thinker, Business analyst.\n - Event head, Organizer etc. ",
        )
        labelresulttext5.place(x=65, y=290)

    if Q_li[4][1] == "Teamwork":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="You're good at:\n - Multitasking and Coordination.\n – Group communication is better.\n - Team spirit.",
        )
        labelresulttext4.place(x=65, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Opportunities for you:\n - Sport Activities like Cricket ,Football etc.\n – Managing Big Events in Groups.\n - Dancing in cultural activities . ",
        )
        labelresulttext5.place(x=65, y=290)

    if Q_li[4][1] == "Risk taking ability":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="You’re good at:\n - Exploring things .\n-You’re confident \n-You stand out more" ,
        )
        labelresulttext4.place(x=65, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Opportunities for you:\n - You can be a good businessman. \n- You can be a good negotiator. \n- You can be good  decision maker. ",
        )
        labelresulttext5.place(x=65, y=290)



        #
    if Q_li[0][1] == "Communication":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Improvements:\n - Work on listening skills.\n - Try to speak more in public.\n - Work on your body language. ",
        )
        labelresulttext4.place(x=525, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Threats for you:\n - You could be separated from your community.\n - You will become introvert.\n - Experiancing difficulty in expressing your ideas. ",
        )
        labelresulttext5.place(x=525, y=290)

    if Q_li[0][1] == "Creativity":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Improvements:\n - You can discuss ideas with others to stimulate imagination skill. \n - Try reading creative books to improve your creativity. ",
        )
        labelresulttext4.place(x=525, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Threats for you:\n  - Creative Events.\n – Thinking of complex  and creative ideas.\n - You will not be able to innovative. ",
        )
        labelresulttext5.place(x=525, y=290)

    if Q_li[0][1] == "Teamwork":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Improvements:\n – You should try to believe or rely on other members.\n – You should respect your team members and their opinions.\n - Develop Team Spirit. ",
        )
        labelresulttext4.place(x=525, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Threats for you: \n - You will rely more on others.\n – You will prevent working solo or by yourself.\n You will not like to be supervise closely",
        )
        labelresulttext5.place(x=525, y=290)

    if Q_li[0][1] == "Risk taking ability":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Improvements:\n - You should try to be more confident.\n - Try to control your emotions.\n - Try to believe more in yourself. ",
        )
        labelresulttext4.place(x=525, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Threats for you: \n- You can miss opportunity if you stop taking risks. \n- You will become habitual to rely on others for any decision. ",
        )
        labelresulttext5.place(x=525, y=290)

    if Q_li[0][1] == "Problem solving":
        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Improvements:\n - You should try to see things in different manner.\n - Try to devlop logical thinking.\n - Solve puzzels, quizzes. ",
        )
        labelresulttext4.place(x=525, y=90)

        labelresulttext5 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="#ffffff",
            width=35,
            text="Threats for you:\n - Not being able to analyze problems.\n - Fields like Mathematics, logical thinking.\n - Problem solving approach. ",
        )
        labelresulttext5.place(x=525, y=290)

    def graph_but():
        labelresulttext.destroy()
        labelresulttext1.destroy()
        labelresulttext2.destroy()
        labelresulttext3.destroy()
        label02.destroy()
        label01.destroy()
        #labelresulttext4.destroy()
        root.config(background="white")

        labelresulttext4 = Label(
            root,
            font=("Consolas", 14),
            wraplength=(300),
            background="white",
            width=35,
            text="                                                                                                     \n ",
        )
        labelresulttext4.place(x=318,y=25)
        import matplotlib.pyplot as plt

        data1 = {'Quality': ['Communication','Teamwork','Risk Taking','Creativity','Problem Solving'],'Points': [communication,teamwork,risk_taking_ability,creativity,problem_solving] }
        df1 = DataFrame(data1,columns=['Quality','Points'])


        figure1 = plt.Figure(figsize=(60,160), dpi=100)
        ax1 = figure1.add_subplot(211)
        bar1 = FigureCanvasTkAgg(figure1, root)
        bar1.get_tk_widget().pack(side=tkinter.LEFT, fill=tkinter.BOTH)
        df1 = df1[['Quality','Points']].groupby('Quality').sum()
        df1.plot(kind='bar', legend=True, ax=ax1)
        ax1.set_title('Quality Vs. Points')
        root.mainloop()

    but_5 = Button(root, text="Graphical View", width=16, height=1, bg="light green", font=("Albertus 10 bold"),
                   command=graph_but)
    but_5.place(x=400, y=440)

def calc():
    global indexes,user_answer,answers,communication,teamwork,risk_taking_ability,creativity,problem_solving
    x = 0
    score = 0
    for i in indexes:
        if i==0:
            if user_answer[x] == answers[i][0]:
                communication = communication + 5

        if i==1:
            if user_answer[x] == answers[i][0]:
                communication = communication + 5
            elif user_answer[x] == answers[i][1]:
                problem_solving = problem_solving + 5
            elif user_answer[x] == answers[i][2]:
                creativity = creativity + 5
            elif user_answer[x] == answers[i][3]:
                creativity = creativity + 5

        if i==2:
            if user_answer[x] == answers[i][0]:
                risk_taking_ability = risk_taking_ability + 5

        if i==3:
            if user_answer[x] == answers[i][0]:
                problem_solving = problem_solving + 5
            elif user_answer[x] == answers[i][1]:
                teamwork = teamwork + 5

        if i==4:
            if user_answer[x] == answers[i][0]:
                communication = communication + 5
            elif user_answer[x] == answers[i][1]:
                problem_solving = problem_solving + 5
            elif user_answer[x] == answers[i][2]:
                teamwork = teamwork + 5

        if i==5:
            if user_answer[x] == answers[i][0]:
                creativity = creativity + 5
            elif user_answer[x] == answers[i][1]:
                problem_solving = problem_solving + 5
            elif user_answer[x] == answers[i][2]:
                risk_taking_ability = risk_taking_ability + 5
            elif user_answer[x] == answers[i][3]:
                teamwork = teamwork + 5

        if i==6:
            if user_answer[x] == answers[i][0]:
                creativity = creativity + 5
            elif user_answer[x] == answers[i][1]:
                problem_solving = problem_solving + 5
            elif user_answer[x] == answers[i][2]:
                communication = communication + 5
            elif user_answer[x] == answers[i][3]:
                risk_taking_ability = risk_taking_ability + 5

        if i==7:
            if user_answer[x] == answers[i][0]:
                teamwork = teamwork + 5
            elif user_answer[x] == answers[i][1]:
                teamwork = teamwork + 5
            elif user_answer[x] == answers[i][2]:
                risk_taking_ability = risk_taking_ability + 5

        if i==8:
            if user_answer[x] == answers[i][0]:
                problem_solving = problem_solving + 5
            elif user_answer[x] == answers[i][1]:
                risk_taking_ability = risk_taking_ability + 5
            elif user_answer[x] == answers[i][2]:
                creativity = creativity + 5

        if i==9:
            if user_answer[x] == answers[i][0]:
                creativity = creativity + 5
            elif user_answer[x] == answers[i][1]:
                communication = communication + 5
            elif user_answer[x] == answers[i][2]:
                teamwork = teamwork + 5

        if user_answer[x] == answers[i][0]:
            communication = communication + 5
        x += 1
    print(score)
    showresult(score,communication,creativity,problem_solving,teamwork,risk_taking_ability)

ques = 1
def selected():
    global radiovar,user_answer
    global lblQuestion,r1,r2,r3,r4
    global ques
    x = radiovar.get()
    user_answer.append(x)
    radiovar.set(-1)
    if ques < 10:
        lblQuestion.config(text= questions[indexes[ques]])
        r1['text'] = answers_choice[indexes[ques]][0]
        r2['text'] = answers_choice[indexes[ques]][1]
        r3['text'] = answers_choice[indexes[ques]][2]
        r4['text'] = answers_choice[indexes[ques]][3]
        ques += 1
    else:
        calc()

def startquiz():

    global lblQuestion,r1,r2,r3,r4

    lblQuestion = Label(root,text = questions[indexes[0]],font = ("Consolas", 18,"bold"),width = 500,wraplength = 800,background = "lightgreen")
    lblQuestion.pack(pady=(75,30))

    global radiovar
    radiovar = IntVar()
    radiovar.set(-1)

    r1 = Radiobutton(root,text = answers_choice[indexes[0]][0] ,wraplength = 950,font = ("Consolas", 16,"bold"),value = 0,variable = radiovar,command = selected,background = "powderblue")
    r1.place(x = 80, y = 180)

    r2 = Radiobutton(root,text = answers_choice[indexes[0]][1], wraplength = 950,font = ("Consolas", 16,"bold"),value = 1,variable = radiovar,command = selected,background = "powderblue")
    r2.place(x = 80, y = 240)

    r3 = Radiobutton(root,text = answers_choice[indexes[0]][2],wraplength = 950,font = ("Consolas", 16,"bold"),value = 2,variable = radiovar,command = selected,background = "powderblue")
    r3.place(x = 80, y = 300)

    r4 = Radiobutton(root,text = answers_choice[indexes[0]][3],wraplength = 950,font = ("Consolas", 16,"bold"),value = 3,variable = radiovar,command = selected,background = "powderblue")
    r4.place(x = 80, y = 360)

    


def startIspressed():

    textName=text_box1.get()
    textAge=text_box2.get()
    root.clipboard_append(textName)
    root.clipboard_append(textAge)

    fh=open("Directory.txt","a")
    fh.write(textName)
    n=len(textName)

    for i in range (0,25-n):
        fh.write(" ")
    fh.write("----      ")
    fh.write(textAge)
    fh.close()
    text_box1.delete(0,END)
    text_box2.delete(0,END)

    labelimage.destroy()
    labeltext.destroy()
    label0.destroy()
    label1.destroy()
    label2.destroy()
    text_box1.destroy()
    text_box2.destroy()
    label3.destroy()
    label4.destroy()
    label5.destroy()
    label6.destroy()
    label7.destroy()
    label8.destroy()
    btnStart.destroy()
    gen()
    startquiz()

root = tkinter.Tk()
root.title("S.W.O.T. Analysis")
root.geometry("1000x480")
root.config(background="powderblue")
root.resizable(0,0)

labelimage = Label(root,background = "#ffffff")
labelimage.pack(pady=(40,0))

labeltext = Label(root,text = "S.W.O.T. ANALYSIS ",font = ("Arial",30,"bold"),background = "powderblue")
labeltext.place(x=318,y=25)

label0 = Label(root, text = "ENTER YOUR DETAILS ", fg = "black", bg = "powderblue",font = ("Arial",18,"bold","underline"))
label0.place(x=60, y=117)

label1 = Label(root, text = "NAME : ", fg = "black", bg = "powderblue",font = ("Helvetica",18,"bold"))
label1.place(x=60, y=185)

text_box1 = Entry(root, width=23,  relief="solid", bg = "white", font = ("arial",18,"bold"))
text_box1.place(x=160, y=185)



label2 = Label(root, text = "AGE : ", fg = "black", bg = "powderblue",font = ("Helvetica",18,"bold"))
label2.place(x=600, y=185)

text_box2 = Entry(root, width=5, relief="solid", font = ("arial",18,"bold"))
text_box2.place(x=675, y=185)

label3 = Label(root, text = "Terms and conditions", fg = "black", bg = "powderblue",font = ("Helvetica",16,"bold","italic","underline"))
label3.place(x=45, y=250)

label4 = Label(root, text = "1. The result generated through this test is purely based on answers selected.", fg = "black", bg = "powderblue",font = ("Arial",12,"bold"))
label4.place(x=45, y=290)

label5 = Label(root, text = "2. Accuracy of the test depends on the honest answer selected by the the user.", fg = "black", bg = "powderblue",font = ("Arial",12,"bold"))
label5.place(x=45, y=315)

label6 = Label(root, text = "3. Test comprises of total 10 Questions with multiple choices of answers.", fg = "black", bg = "powderblue",font = ("Arial",12,"bold"))
label6.place(x=45, y=340)

label7 = Label(root, text = "4. Only one answer should be selected for any given question.", fg = "black", bg = "powderblue",font = ("Arial",12,"bold"))
label7.place(x=45, y=365)

label8 = Label(root,
         text = "5. After completion of the test, 'S.W.O.T.' analysis of the user will be presented along with the areas of improvement.",
         fg = "black", bg = "powderblue",font = ("Arial",12,"bold"))
label8.place(x=45, y=390)

btnStart = Button(root, width=10, text="Proceed", relief="ridge", fg="black", bg="lightgreen",font = ("arial",12,"bold"),command = startIspressed)
btnStart.place(x=875, y=433)


root.mainloop()

