
import numexpr as ne
import tkinter as tk

win = tk.Tk()
win.title('Радужный калькулятор')
win.geometry('371x541')
win.resizable(False, False)

maintext = '''0'''

label = tk.Entry(win, text = maintext,
bg = 'white',#свет фона
justify=tk.RIGHT,#закрепляет текст c лева
relief=tk.RAISED, # создаёт границу
bd = 2,font = ('Gothic', 12, 'bold') )
label.grid(row=0,column=0,stick='wesn',columnspan=3)
the_number = ''
win.config(bg='black')
precommacoun = 1; commacount = 1
label.insert(0,'0')



def labeltex():
    global label,  maintext
    if maintext != '':
        new = ''
        for i in maintext:
            if i in['-', ',', '+', '*', '/', ' ', '1', '2', '3', '4', '5','6','7','8','9','0','.']:
                new += i
        maintext = new
        if maintext[0] =='0' and len(maintext)>1:
            try:
                if int(maintext[1]) > -1: maintext = maintext[1:]
            except: print('')
        
    
    label.delete(0,tk.END)
    if len(maintext) > 29: label.insert(0, maintext[(len(maintext) - 29)::])


    else: label.insert(0,maintext)


def deleteCom():
    global maintext, label, labeltex,precommacoun, commacount
    maintext = label.get()
    if maintext != '':
        if maintext[-1] == '.': commacount = 0; precommacoun = 1
        maintext = maintext[0:-1]
        if maintext == '':maintext = '0'

    labeltex()
def solveCom():
    global maintext, label, labeltex,precommacoun, commacount
    maintext = label.get()
    try:
        for i in range(1,len(maintext)):
            if maintext[i-1] == ' ' and maintext[i] == 0 and maintext[i+1] != '.':
                maintext = maintext[:i] + maintext[i+1:]
    except: None
    if maintext[-4:] == ' / 0': maintext = f'({maintext[:-4]}+0)'
    if maintext[-3:] == ' /0': maintext = f'({maintext[:-3]}+0)'
    if maintext[-3:] in [' - ', ' -', '  -']: maintext = f'({maintext}0)/2'
    elif maintext[-3:] in [' + ', ' +', '  +']: maintext = f'({maintext}0)*2'
    elif maintext[-3:] in [' * ', ' *', '  *']: maintext = f'({maintext}1)**2'
    elif maintext[-3:] in [' / ', ' /', '  /']: maintext = f'({maintext}1)**0.5'
    if int(ne.evaluate(maintext)) == ne.evaluate(maintext):
        maintext = str(int(ne.evaluate(maintext)))
    elif round(float(ne.evaluate(maintext))) == float(ne.evaluate(maintext)) + 0.000001 or round(float(ne.evaluate(maintext))) == float(ne.evaluate(maintext)) - 0.000001: maintext = str(round(float(ne.evaluate(maintext))))
    else:
        maintext = str(round(round(float(ne.evaluate(maintext)),10),6))
    labeltex()
    commacount = 0
    precommacoun = 0
    
def one1():
    global maintext, label, labeltex,precommacoun, commacount, the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '1'
    the_number += '1'
    labeltex()
def two2():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '2'
    the_number += '1'
    labeltex()
def three3():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '3'
    the_number += '1'
    labeltex()
def four4():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '4'
    the_number += '1'
    labeltex()
def five5():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '5'
    the_number += '1'
    labeltex()
def six6():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '6'
    the_number += '1'
    labeltex()
def seven7():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '7'
    the_number += '1'
    labeltex()
def eight8():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '8'
    the_number += '1'
    labeltex()
def nine9():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '9'
    the_number += '1'
    labeltex()
def zero0():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    
    if precommacoun == 1: commacount = 0
    maintext = label.get()
    maintext += '0'
        
    labeltex()

def comma():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    maintext = label.get()
    if commacount == 0:
        maintext += '.'
        commacount = 1
        precommacoun = 0
        the_number += '1'
    labeltex()

def C():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    maintext = '0'
    commacount = 0
    precommacoun = 0
    labeltex()

def multi():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    maintext = label.get()
    if maintext[-3:] in [' * ', ' / ',' + ', ' - ']: maintext = maintext[0:-3] + ' * '
    elif maintext[-1] == '.': maintext = maintext[0:-1] + ' * '
    else: maintext += ' * '
    precommacoun = 1
    the_number = ''
    labeltex()
 
def unmulti():
    
    global maintext, label, labeltex,precommacoun, commacount,the_number
    maintext = label.get()
    if maintext[-3:] in [' * ', ' / ',' + ', ' - ']: maintext = maintext[0:-3] + ' / '
    elif maintext[-1] == '.': maintext = maintext[0:-1] + ' / '
    else: maintext += ' / '
    labeltex()
    precommacoun = 1
    the_number = ''
def plus():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    maintext = label.get()
    if maintext[-3:] in [' * ', ' / ',' + ', ' - ']: maintext = maintext[0:-3] + ' + '
    elif maintext[-1] == '.': maintext = maintext[0:-1] + ' + '
    else: maintext += ' + '
    labeltex()
    the_number = ''
    precommacoun = 1
def minus():
    global maintext, label, labeltex,precommacoun, commacount,the_number
    maintext = label.get()
    if maintext[-3:] in [' * ', ' / ',' + ', ' - ']: maintext = maintext[0:-3] + ' - '
    elif maintext[-1] == '.': maintext = maintext[0:-1] + ' - '
    else: maintext += ' - '
    labeltex()
    the_number = ''
    precommacoun = 1

delete = tk.Button(win, text = '⌫', command=deleteCom, font = ('Gothic', 30, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
delete.grid(row=0,stick='we',column=3)

solve = tk.Button(win, text = '=', command=solveCom,  font = ('Gothic', 35, 'bold'), fg='white', bg ='green',activebackground='green',activeforeground='black',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
solve.grid(row=1,stick='we',column=3)

one = tk.Button(win, text = '1', command=one1, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
one.grid(row=4,stick='we',column=0)

two = tk.Button(win, text = '2', command=two2, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
two.grid(row=4,stick='we',column=1)
three = tk.Button(win, text = '3', command=three3, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
three.grid(row=4,stick='we',column=2)
four = tk.Button(win, text = '4', command=four4, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
four.grid(row=3,stick='we',column=0)
five = tk.Button(win, text = '5', command=five5, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
five.grid(row=3,stick='we',column=1)
six = tk.Button(win, text = '6', command=six6, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
six.grid(row=3,stick='we',column=2)
seven = tk.Button(win, text = '7', command=seven7, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
seven.grid(row=2,stick='we',column=0)
eight = tk.Button(win, text = '8', command=eight8, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
eight.grid(row=2,stick='we',column=1)
nine = tk.Button(win, text = '9', command=nine9, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
nine.grid(row=2,stick='we',column=2)

zero = tk.Button(win, text = '0', command=zero0, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
zero.grid(row=5,stick='we',column=1)

Cbutton = tk.Button(win, text = 'C', command=C, font = ('Gothic', 35, 'bold'),fg = 'red' ,activebackground='red',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
Cbutton.grid(row=1,stick='we',column=2)

plusbutton = tk.Button(win, text = '+', command=plus, font = ('Gothic', 35, 'bold'),fg = 'green',activeforeground='blue',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
plusbutton.grid(row=5,stick='we',column=3)

minusbutton = tk.Button(win, text = '-', command=minus, font = ('Gothic', 35, 'bold'),fg = 'green',activeforeground='blue',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
minusbutton.grid(row=4,stick='we',column=3)

multibutton = tk.Button(win, text = '*', command=multi, font = ('Gothic', 35, 'bold'),fg = 'green',activeforeground='blue',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
multibutton.grid(row=3,stick='we',column=3)

unmultibutton = tk.Button(win, text = '/', command=unmulti, font = ('Gothic', 35, 'bold'),fg = 'green',activeforeground='blue',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
unmultibutton.grid(row=2,stick='we',column=3)

commabutton = tk.Button(win, text = ',', command=comma, font = ('Gothic', 35, 'bold'),#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
commabutton.grid(row=5,stick='we',column=2)

def black():
    global win, rainbutton, commabutton, unmultibutton,multibutton, minusbutton,plusbutton, Cbutton, one,two,three,four,five,six,seven,eight,nine
    delete['bg'] = '#F0F0F0'
    delete['fg'] = 'black'
    delete['activeforeground'] = 'red'
    delete['activebackground'] = '#F0F0F0'

    Cbutton['bg'] = '#F0F0F0'
    Cbutton['activeforeground'] = 'black'
    Cbutton['activebackground'] = 'red'

    unmultibutton['bg'] = '#F0F0F0'
    unmultibutton['fg'] = 'green'
    unmultibutton['activeforeground'] = 'blue'
    unmultibutton['activebackground'] = '#F0F0F0'

    multibutton['bg'] = '#F0F0F0'
    multibutton['fg'] = 'green'
    multibutton['activeforeground'] = 'blue'
    multibutton['activebackground'] = '#F0F0F0'

    nine['bg'] = '#F0F0F0'
    nine['fg'] = 'black'
    nine['activeforeground'] = 'black'
    nine['activebackground'] = '#F0F0F0'

    eight['bg'] = '#F0F0F0'
    eight['fg'] = 'black'
    eight['activeforeground'] = 'black'
    eight['activebackground'] = '#F0F0F0'

    six['bg'] = '#F0F0F0'
    six['fg'] = 'black'
    six['activeforeground'] = 'black'
    six['activebackground'] = '#F0F0F0'

    minusbutton['bg'] = '#F0F0F0'
    minusbutton['fg'] = 'green'
    minusbutton['activeforeground'] = 'blue'
    minusbutton['activebackground'] = '#F0F0F0'

    seven['bg'] = '#F0F0F0'
    seven['fg'] = 'black'
    seven['activeforeground'] = 'black'
    seven['activebackground'] = '#F0F0F0'

    five['bg'] = '#F0F0F0'
    five['fg'] = 'black'
    five['activeforeground'] = 'black'
    five['activebackground'] = '#F0F0F0'

    three['bg'] = '#F0F0F0'
    three['fg'] = 'black'
    three['activeforeground'] = 'black'
    three['activebackground'] = '#F0F0F0'

    plusbutton['bg'] = '#F0F0F0'
    plusbutton['fg'] = 'green'
    plusbutton['activeforeground'] = 'blue'
    plusbutton['activebackground'] = '#F0F0F0'

    four['bg'] = '#F0F0F0'
    four['fg'] = 'black'
    four['activeforeground'] = 'black'
    four['activebackground'] = '#F0F0F0'

    two['bg'] = '#F0F0F0'
    two['fg'] = 'black'
    two['activeforeground'] = 'black'
    two['activebackground'] = '#F0F0F0'

    commabutton['bg'] = '#F0F0F0'
    commabutton['fg'] = 'black'
    commabutton['activeforeground'] = 'black'
    commabutton['activebackground'] = '#F0F0F0'

    one['bg'] = '#F0F0F0'
    one['fg'] = 'black'
    one['activeforeground'] = 'black'
    one['activebackground'] = '#F0F0F0'

    zero['bg'] = '#F0F0F0'
    zero['fg'] = 'black'
    zero['activeforeground'] = 'black'
    zero['activebackground'] = '#F0F0F0'

    win.config(bg='black')
   
    rainbutton['bg'] = 'pink'
    rainbutton['fg'] = 'violet'
    rainbutton['activeforeground'] = 'red'
    rainbutton['activebackground'] = 'pink'
    rainbutton['command'] = rain


def gray():
    global win, rainbutton, commabutton, unmultibutton,multibutton, minusbutton,plusbutton, Cbutton, one,two,three,four,five,six,seven,eight,nine
    delete['bg'] = 'gray'
    delete['fg'] = 'black'
    delete['activeforeground'] = 'red'
    delete['activebackground'] = 'gray'

    Cbutton['bg'] = 'gray'
    Cbutton['activeforeground'] = 'orange'
    Cbutton['activebackground'] = 'gray'

    unmultibutton['bg'] = 'gray'
    unmultibutton['fg'] = 'red'
    unmultibutton['activeforeground'] = 'orange'
    unmultibutton['activebackground'] = 'gray'

    multibutton['bg'] = 'gray'
    multibutton['fg'] = 'orange'
    multibutton['activeforeground'] = '#00FFFF'
    multibutton['activebackground'] = 'gray'

    nine['bg'] = 'gray'
    nine['fg'] = 'orange'
    nine['activeforeground'] = '#00FFFF'
    nine['activebackground'] = 'gray'

    eight['bg'] = 'gray'
    eight['fg'] = '#00FFFF'
    eight['activeforeground'] = '#00FF00'
    eight['activebackground'] = 'gray'

    six['bg'] = 'gray'
    six['fg'] = '#00FFFF'
    six['activeforeground'] = '#00FF00'
    six['activebackground'] = 'gray'

    minusbutton['bg'] = 'gray'
    minusbutton['fg'] = '#00FFFF'
    minusbutton['activeforeground'] = '#00FF00'
    minusbutton['activebackground'] = 'gray'

    seven['bg'] = 'gray'
    seven['fg'] = '#00FF00'
    seven['activeforeground'] = 'blue'
    seven['activebackground'] = 'gray'

    five['bg'] = 'gray'
    five['fg'] = '#00FF00'
    five['activeforeground'] = 'blue'
    five['activebackground'] = 'gray'

    three['bg'] = 'gray'
    three['fg'] = '#00FF00'
    three['activeforeground'] = 'blue'
    three['activebackground'] = 'gray'

    plusbutton['bg'] = 'gray'
    plusbutton['fg'] = '#00FF00'
    plusbutton['activeforeground'] = 'blue'
    plusbutton['activebackground'] = 'gray'

    four['bg'] = 'gray'
    four['fg'] = 'blue'
    four['activeforeground'] = 'violet'
    four['activebackground'] = 'gray'

    two['bg'] = 'gray'
    two['fg'] = 'blue'
    two['activeforeground'] = 'violet'
    two['activebackground'] = 'gray'

    commabutton['bg'] = 'gray'
    commabutton['fg'] = 'blue'
    commabutton['activeforeground'] = 'violet'
    commabutton['activebackground'] = 'gray'

    one['bg'] = 'gray'
    one['fg'] = 'violet'
    one['activeforeground'] = 'pink'
    one['activebackground'] = 'gray'

    zero['bg'] = 'gray'
    zero['fg'] = 'violet'
    zero['activeforeground'] = 'pink'
    zero['activebackground'] = 'gray'

    win.config(bg='#00FFFF')
    
    rainbutton['bg'] = 'gray'
    rainbutton['fg'] = 'black'
    rainbutton['activeforeground'] = '#66CCFF'
    rainbutton['activebackground'] = 'gray'
    rainbutton['command'] = black
def rain():
    global win, rainbutton, commabutton, unmultibutton,multibutton, minusbutton,plusbutton, Cbutton, one,two,three,four,five,six,seven,eight,nine
    delete['activeforeground'] = 'red'
    delete['activebackground'] = 'black'
    delete['bg'] = 'red'
    delete['fg'] = 'black'
    Cbutton['bg'] = 'orange'
    Cbutton['activeforeground'] = 'orange'
    Cbutton['activebackground'] = 'yellow'

    unmultibutton['bg'] = 'orange'
    unmultibutton['fg'] = 'red'
    unmultibutton['activeforeground'] = 'orange'
    unmultibutton['activebackground'] = 'yellow'

    multibutton['bg'] = 'yellow'
    multibutton['fg'] = 'orange'
    multibutton['activeforeground'] = '#00FFFF'
    multibutton['activebackground'] = '#00FF00'

    nine['bg'] = 'yellow'
    nine['fg'] = 'orange'
    nine['activeforeground'] = '#00FFFF'
    nine['activebackground'] = '#00FF00'

    eight['bg'] = '#00FF00'
    eight['fg'] = '#00FFFF'
    eight['activeforeground'] = '#00FF00'
    eight['activebackground'] = 'blue'

    six['bg'] = '#00FF00'
    six['fg'] = '#00FFFF'
    six['activeforeground'] = '#00FF00'
    six['activebackground'] = 'blue'

    minusbutton['bg'] = '#00FF00'
    minusbutton['fg'] = '#00FFFF'
    minusbutton['activeforeground'] = '#00FF00'
    minusbutton['activebackground'] = 'blue'

    seven['bg'] = 'blue'
    seven['fg'] = '#00FF00'
    seven['activeforeground'] = 'blue'
    seven['activebackground'] = 'violet'

    five['bg'] = 'blue'
    five['fg'] = '#00FF00'
    five['activeforeground'] = 'blue'
    five['activebackground'] = 'violet'

    three['bg'] = 'blue'
    three['fg'] = '#00FF00'
    three['activeforeground'] = 'blue'
    three['activebackground'] = 'violet'

    plusbutton['bg'] = 'blue'
    plusbutton['fg'] = '#00FF00'
    plusbutton['activeforeground'] = 'blue'
    plusbutton['activebackground'] = 'violet'

    four['bg'] = 'violet'
    four['fg'] = 'blue'
    four['activeforeground'] = 'violet'
    four['activebackground'] = 'pink'

    two['bg'] = 'violet'
    two['fg'] = 'blue'
    two['activeforeground'] = 'violet'
    two['activebackground'] = 'pink'

    commabutton['bg'] = 'violet'
    commabutton['fg'] = 'blue'
    commabutton['activeforeground'] = 'violet'
    commabutton['activebackground'] = 'pink'

    one['bg'] = 'pink'
    one['fg'] = 'violet'
    one['activeforeground'] = 'pink'
    one['activebackground'] = '#66CCFF'

    zero['bg'] = 'pink'
    zero['fg'] = 'violet'
    zero['activeforeground'] = 'pink'
    zero['activebackground'] = '#66CCFF'

    win.config(bg='#00FFFF')
    
    rainbutton['bg'] = '#66CCFF'
    rainbutton['fg'] = 'gray'
    rainbutton['activeforeground'] = '#66CCFF'
    rainbutton['activebackground'] = 'gray'
    rainbutton['command'] = gray






rainbutton = tk.Button(win, text = '🪅',fg='violet', command=rain, font = ('Gothic', 35, 'bold'),bg='pink',activebackground='pink',activeforeground='red',#закрепляет текст север юг запад восток se - юго восток
relief=tk.RAISED, # создаёт границу
bd = 7,)
rainbutton.grid(row=5,stick='we',column=0)




win.grid_columnconfigure(0,minsize=90)#пареметры колонн и рядов
win.grid_columnconfigure(1,minsize=90)
win.grid_columnconfigure(2,minsize=90)
win.grid_columnconfigure(2,minsize=90)


def press(keyy):
    
    if keyy.char == '0':
        zero()
    elif keyy.char == '1':
        one1()
    elif keyy.char == '2':
        two2()
    elif keyy.char == '3':
        three3()
    elif keyy.char == '4':
        four4()
    elif keyy.char == '5':
        five5()
    elif keyy.char == '6':
        six6()
    elif keyy.char == '7':
        seven7()
    elif keyy.char == '8':
        eight8()
    elif keyy.char == '9':
        nine9()
    elif keyy.char == '\r':
        solveCom()
    elif keyy.char in ['/',':']:
        unmulti()
    elif keyy.char in ['*','X','x']:
        multi()
    elif keyy.char == '-':
        minus()
    elif keyy.char == '+':
        plus()
    elif keyy.char in ['r','R','р','Р']:
        rain()
    elif keyy.char == '\x08':
        deleteCom()
    elif keyy.char in ['c','C','О',"о"]:
        C()
    elif keyy.char in ['G','g','с',"С"]:
        gray()
    elif keyy.char in ['Ч','ч','B',"b"]:
        black()

win.bind('<Key>', press)


win.mainloop()