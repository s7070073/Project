'''
PSIT Project
*************
Create by
PHONGNARET(57070073) and PHATTARAPON(57070086).
*************
'''
from Tkinter import *
app = Tk()
app.minsize(800, 615)
app.resizable(0, 0)
app.title("Histogram")
app.iconbitmap('favicon.ico')


def about():
    about = Toplevel(app)
    about.wm_title("About Us")
    about.iconbitmap('favicon.ico')
    about.minsize(300, 250)
    about.resizable(0, 0)
    Label(about, text='\nAbout Us',font=('times', 20, 'bold')).pack()
    Label(about, text='\nPONGNARAS  CHUTHONG\n57070073',font=('times', 10)).pack()
    Label(about, text='\nPHATTARAPON  KAEWKUSONWIWAT\n57070086',font=('times', 10)).pack()
    
def menu_help():
    menu_help = Toplevel(app)
    menu_help.wm_title("Help")
    menu_help.iconbitmap('favicon.ico')
    menu_help.minsize(300, 50)
    menu_help.resizable(0, 0)
    Label(menu_help, text='\nPlease open "Help.txt" to get information.').pack()
    
input_box_label = Label(app, text='Data Input')
input_box_label.place(x=26, y=22)
input_box = Entry(app, width=98)
input_box.place(x=30, y=47)

def callback():
    print 'Hello World.'

def conver_bar(cur, base):
    xxx = (cur * 330.0)/base
    return (330 - xxx) + 48

def range_out(data):
    """print range"""
    min_range = min(data)
    max_range = min(data) + ((max(data) - min(data))/4.0)
    range_count = {}
    count_data = []
    for i in xrange(5):
        range_count["range"+str(i+1)] = 0
        ans = "("+str(min_range)+","+str(max_range)+"]"
        for j in data:
            if j >= min_range and j < max_range:
                range_count["range"+str(i+1)] += 1
        min_range = max_range
        max_range = max_range + ((max(data) - min(data))/4.0)
        count_data.append([ans, range_count["range"+str(i+1)]])
    return range_count, count_data
canvas_area = Canvas(app, width=750, height=410)
canvas_area.place(x=20, y=100)
canvas_area.create_line(50, 15, 50, 378)
canvas_area.create_line(50, 378, 704, 378)
canvas_area.create_line(50, 345, 704, 345, dash=(4, 4))
canvas_area.create_line(50, 312, 704, 312, dash=(4, 4))
canvas_area.create_line(50, 279, 704, 279, dash=(4, 4))
canvas_area.create_line(50, 246, 704, 246, dash=(4, 4))
canvas_area.create_line(50, 213, 704, 213, dash=(4, 4))
canvas_area.create_line(50, 180, 704, 180, dash=(4, 4))
canvas_area.create_line(50, 147, 704, 147, dash=(4, 4))
canvas_area.create_line(50, 114, 704, 114, dash=(4, 4))
canvas_area.create_line(50, 81, 704, 81, dash=(4, 4))
canvas_area.create_line(50, 48, 704, 48, dash=(4, 4))
canvas_area.create_line(50, 15, 704, 15, dash=(4, 4))
def process_but():
    '''process function'''
    canvas_area = Canvas(app, width=750, height=410)
    canvas_area.place(x=20, y=100)
    canvas_area.create_line(50, 15, 50, 378)
    canvas_area.create_line(50, 378, 704, 378)
    canvas_area.create_line(50, 345, 704, 345, dash=(4, 4))
    canvas_area.create_line(50, 312, 704, 312, dash=(4, 4))
    canvas_area.create_line(50, 279, 704, 279, dash=(4, 4))
    canvas_area.create_line(50, 246, 704, 246, dash=(4, 4))
    canvas_area.create_line(50, 213, 704, 213, dash=(4, 4))
    canvas_area.create_line(50, 180, 704, 180, dash=(4, 4))
    canvas_area.create_line(50, 147, 704, 147, dash=(4, 4))
    canvas_area.create_line(50, 114, 704, 114, dash=(4, 4))
    canvas_area.create_line(50, 81, 704, 81, dash=(4, 4))
    canvas_area.create_line(50, 48, 704, 48, dash=(4, 4))
    canvas_area.create_line(50, 15, 704, 15, dash=(4, 4))    
    data = [float(i) for i in input_box.get().split(',')]    
    average =(sum(data))/float((len(data)))
    sigma = 0
    for i in xrange(len(data)):
        sigma = sigma + ((data[i]-average)**2)
    num_sd = (sigma/(len(data)-1))**0.5
    mode = {}
    mode2 = []
    for i in data:
        if i not in mode:
            mode[i] = 1
        else:
            mode[i] = mode[i] + 1
    for j in mode:
        if mode[j] == max(mode.values()):
            mode2.append(j)
    y_label = []
    cur = 0
    for _ in xrange(12):
        y_label.append('%.2f' % cur)
        cur += max(range_out(data)[0].values())/10.0
        
    Label(app, text=y_label[11]).place(x=28,y=105)
    Label(app, text=y_label[10]).place(x=28,y=138)
    Label(app, text=y_label[9]).place(x=28,y=171)
    Label(app, text=y_label[8]).place(x=28,y=204)
    Label(app, text=y_label[7]).place(x=28,y=237)
    Label(app, text=y_label[6]).place(x=28,y=270)
    Label(app, text=y_label[5]).place(x=28,y=303)
    Label(app, text=y_label[4]).place(x=28,y=336)
    Label(app, text=y_label[3]).place(x=28,y=369)
    Label(app, text=y_label[2]).place(x=28,y=402)
    Label(app, text=y_label[1]).place(x=28,y=435)
    Label(app, text='0.00').place(x=28,y=468)
    label0 = Label(app, text=range_out(data)[1][0][0])
    label0.place(x=130,y=480)
    label1 = Label(app, text=range_out(data)[1][1][0])
    label1.place(x=258,y=480)
    label2 = Label(app, text=range_out(data)[1][2][0])
    label2.place(x=386,y=480)
    label3 = Label(app, text=range_out(data)[1][3][0])
    label3.place(x=514,y=480)
    label4 = Label(app, text=range_out(data)[1][4][0])
    label4.place(x=642,y=480)    
    base = max(range_out(data)[0].values())
    canvas_area.create_rectangle(114, conver_bar(range_out(data)[1][0][1], base), 178, 378, fill='yellow')
    canvas_area.create_rectangle(242, conver_bar(range_out(data)[1][1][1], base), 306, 378, fill='orange')
    canvas_area.create_rectangle(370, conver_bar(range_out(data)[1][2][1], base), 434, 378, fill='red')
    canvas_area.create_rectangle(498, conver_bar(range_out(data)[1][3][1], base), 562, 378, fill='violet')
    canvas_area.create_rectangle(626, conver_bar(range_out(data)[1][4][1], base), 690, 378, fill='blue')        
    len_data.delete(1, last=None)
    len_data_mess = str(len(data))
    len_data.insert(0, len_data_mess.center(18))    
    max_data.delete(1, last=None)
    max_data_mess = str('%.2f' % max(data))
    max_data.insert(0, max_data_mess.center(18))    
    min_data.delete(1, last=None)
    min_data_mess = str('%.2f' % min(data))
    min_data.insert(0, min_data_mess.center(18))   
    range_data.delete(1, last=None)
    range_data_mess = str('%.2f' % (max(data) - min(data)))
    range_data.insert(0, range_data_mess.center(18))
    average_data.delete(1, last=None)
    average_data_mess = str('%.2f' % (sum(data)/float(len(data))))
    average_data.insert(0, average_data_mess.center(18))
    sd_data.delete(1, last=None)
    sd_data_mess = str('%.2f' % num_sd)
    sd_data.insert(0, sd_data_mess.center(18))
    mode_data.delete(1, last=None)
    mode_data.insert(0, mode2)
    class_interval_data.delete(1, last=None)
    class_interval_mess = str('%.2f' % ((max(data) - min(data))/float(6)))
    class_interval_data.insert(0, class_interval_mess.center(18))
    
process_button = Button(app, height=3, width=10, text='Process', command=process_but)
process_button.place(x=670, y=30)
len_data_label = Label(app, text='Length')
len_data_label.place(x=190, y=520)
len_data = Listbox(app, height=1, width=10)
len_data.place(x=270, y=520)
max_data_label = Label(app, text='Max')
max_data_label.place(x=40, y=520)
max_data = Listbox(app, height=1, width=10)
max_data.place(x=100, y=520)
min_data_label = Label(app, text='Min')
min_data_label.place(x=40, y=550)
min_data = Listbox(app, height=1, width=10)
min_data.place(x=100, y=550)
range_data_label = Label(app, text='Range')
range_data_label.place(x=190, y=550)
range_data = Listbox(app, height=1, width=10)
range_data.place(x=270, y=550)
average_data_label = Label(app, text='Average')
average_data_label.place(x=390, y=520)
average_data = Listbox(app, height=1, width=10)
average_data.place(x=450, y=520)
sd_data_label = Label(app, text='S.D.')
sd_data_label.place(x=390, y=550)
sd_data = Listbox(app, height=1, width=10)
sd_data.place(x=450, y=550)
mode_data_label = Label(app, text='Mode')
mode_data_label.place(x=570, y=520)
mode_data = Listbox(app, height=1, width=10)
mode_data.place(x=650, y=520)
class_interval_data_label = Label(app, text='Class Interval')
class_interval_data_label.place(x=570, y=550)
class_interval_data = Listbox(app, height=1, width=10)
class_interval_data.place(x=650, y=550)

def histogram_help():
    """
    ****************************************************************
    ####################### Help ###################################
    ****************************************************************
    *** How to use Histograme ***
    *****************************
    |
    | Step1.
    | -> input(int, float)
    |            Example1. -> 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
    |            Example2. -> 1.2, 1, 3, 4, 1.11, 2, 3, 6, 4, 5
    |
    | Step2.
    | -> Click -> [Process] Button
    |
    | Step3.
    | -> The Program running and process to output
    |
    ******************
    ***   input    ***
    ******************
    |
    |you can put number in int, float, mix(int and float)
    |---> int
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |
    |---> float
    |    Example.
    |           -> input = 1.4, 0.0, 10.0, 3.0, 15.0, 3.0, 6.0, 1.6
    |
    |---> Mix int and float
    |    Example.
    |           -> input = 1.4, 0, 10.0, 3.0, 1.5, 3, 6.3, 16, 17, 1.5, 15
    |
    ******************
    ***   output   ***
    ******************
    |
    |output will show values
    |
    |---[Max]---
    |
    |    in Max list box ->>> show max values form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |           -> output [Max] -> [ 9.00 ]
    |    Example.
    |           -> input = 0, 10, 3, 15, 3, 6, 16, 17, 15, 15
    |           -> output [Max] -> [ 17.00 ]
    |    Example.
    |           -> input = 0, 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output [Max] -> [ 17.00 ]
    |
    |---[Min]---
    |
    |    in Min list box ->>> show min values form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |           -> output [Min] -> [ 0.00 ]
    |    Example.
    |           -> input = 0, 10, 3, 15, 3, 6, 16, 17, 15, 15
    |           -> output [Min] -> [ 0.00 ]
    |    Example.
    |           -> input = 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output [Min] -> [ 1.50 ]
    |
    |---[Length]---
    |
    |   in Length list box ->>> show number form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |           -> output [Length] -> [ 10 ]
    |    Example.
    |           -> input = 0, 6, 16, 17, 15, 15
    |           -> output [Length] -> [ 5 ]
    |    Example.
    |           -> input = 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output [Length] -> [ 8 ]
    |
    |---[Range]---
    |
    |   in Range list box ->>> show [Max] - [Min] form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |               [Max] = 9.00, [Min] = 0.00
    |               [Max] - [Min] = 9.00
    |           -> output [Range] -> [ 9.00 ]
    |    Example.
    |           -> input = 0,6,16,17,15,15
    |               [Max] = 17.00, [Min] = 0.00
    |               [Max] - [Min] = 17.00
    |           -> output [Range] -> [ 17.00]
    |    Example.
    |           -> input = 10.0,3.0,1.5,3,6,16,17,1.5,15
    |               [Max] = 17.00, [Min] = 1.50
    |               [Max] - [Min] = 15.50
    |           -> output [Range] -> [ 15.50 ]
    |
    |---[Average]---
    |
    |   in Average list box ->>> show Anverage valuse form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |           -> output [Average] -> [ 4.50 ]
    |    Example.
    |           -> input = 0, 6, 16, 17, 15, 15
    |           -> output [Average] -> [ 11.50]
    |    Example.
    |           -> input = 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output  [Average] -> [ 8.11 ]
    |
    |---[S.D.]---
    |
    |   in S.D. list box ->>> show S.D. valuse form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0
    |           -> output [S.D.] -> [ 3.30 ]
    |    Example.
    |           -> input = 0, 6, 16, 17, 15, 15
    |           -> output [S.D.] -> [ 6.89]
    |    Example.
    |           -> input = 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output  [S.D.] -> [ 6.48 ]
    |
    |---[Mode]---
    |
    |   in Mode list box ->>> show number is max repeatedly form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0
    |           -> output [Mode] -> [ [0.0] ]
    |    Example.
    |           -> input = 0, 6, 16, 17, 15, 15
    |           -> output [Mode] -> [ [15.0]]
    |    Example.
    |           -> input = 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output  [Mode] -> [ [1.5, 3.0] ]
    |
    |---[Class Interval]---
    |
    |   in Class Interval list box ->>> show how for graph(n) to graph(n+1)
    |   form data input
    |
    |    Example.
    |           -> input = 1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 0
    |           -> output [Class Interval] -> [ 1.50 ]
    |    Example.
    |           -> input = 0, 6, 16, 17, 15, 15
    |           -> output [Class Interval] -> [ 2.83 ]
    |    Example.
    |           -> input = 10.0, 3.0, 1.5, 3, 6, 16, 17, 1.5, 15
    |           -> output  [Class Interval] -> [ 2.58 ]
    """
menubar = Menu(app)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Exit", command=app.destroy)
menubar.add_cascade(label="File", menu=filemenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=about)
helpmenu.add_command(label="Help", command=menu_help)
menubar.add_cascade(label="Help", menu=helpmenu)
app.config(menu=menubar)
app.mainloop()
