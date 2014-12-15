'''
PSIT Project
*************
Create by
PHONGNARET(57070073) and PHATTARAPON(57070086).
*************
'''
from Tkinter import *
app = Tk()
app.minsize(800, 600)
app.resizable(0, 0)

def callback():
    print 'Hello World.'
"""form kim"""
"""project def code to tkinter"""
data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 15, 1, 20]
range_level = 5

def len_data():
    """find len of data"""
    return len(data)

def num_min():
    """find min number of data"""
    return min(data)

def num_max():
    """find max number of data"""
    return max(data)

def averange():
    """calculate averange from data"""
    return (sum(data))/float((len(data)))

def num_sd():
    """"""
    average =(sum(data))/float((len(data)))
    sigma = 0
    for i in xrange(len(data)):
        sigma = sigma + ((data[i]-average)**2)
    num_sd = (sigma/(len(data)-1))**0.5
    return num_sd
def mode():
    """find mode of data"""
    mode = {}
    mode2 = []
    for i in data:
        if i not in mode:
            mode[i] = 1
        else:
            mode[i] = mode[i] + 1
    for j in mode:
        if mode[j] == max(mode.values()):
            mode2.append('%.2f'%j)
    return mode2

def pisai():
    """"""
    return num_max() - num_min()

def range_len():
    """"""
    return pisai() / float(range_level)
    
def range_out():
    """print range"""
    min_range = num_min()
    max_range = num_min() + range_len()
    range_count = {}
    for i in xrange(5):
        range_count["range"+str(i+1)] = 0
        ans = "["+str(min_range)+" - "+str(max_range)+"] |"
        for j in data:
            if j >= min_range and j <= max_range:
                ans = ans + "-"
                range_count["range"+str(i+1)] += 1
        min_range = max_range
        max_range = max_range + range_len()
        print ans
    print range_count
        

print "data >>>", data
print "len_data >>>", '%.2f'%len_data()
print "num_min >>>", '%.2f'%num_min()
print "num_max >>>", '%.2f'%num_max()
print "averange >>>", '%.2f'%averange()
print "num_sd >>>", '%.2f'%num_sd()
print "mode >>>", mode()
print "pisai >>>", '%.2f'%pisai()
print "range_len >>>", '%.2f'%range_len()
print ""
range_out()



'''#######################  input zone  #################'''
#input box
input_box_label = Label(app, text='Data Input')
input_box_label.place(x=20, y=5)
input_box = Entry(app, width=100)
input_box.place(x=20, y=30)


#process_button
process_button = Button(app, text='Process',height=3, width=10)
process_button.place(x=670, y=30)
'''#######################  output zone  #################'''


'''#######################  output zone  #################'''
#len_data
len_data_label = Label(app, text='len data')
len_data_label.place(x=170, y=520)
len_data = Listbox(app, height=1, width=10)
len_data.insert(1, 321)
len_data.place(x=250, y=520)

#max_data
max_data_label = Label(app, text='max')
max_data_label.place(x=20, y=520)
max_data = Listbox(app, height=1, width=10)
max_data.place(x=80, y=520)

#min_data
min_data_label = Label(app, text='min')
min_data_label.place(x=20, y=550)
min_data = Listbox(app, height=1, width=10)
min_data.place(x=80, y=550)

#pisai_data
pisia_data_label = Label(app, text='pisia data')
pisia_data_label.place(x=170, y=550)
pisia_data = Listbox(app, height=1, width=10)
pisia_data.place(x=250, y=550)

#average_data
average_data_label = Label(app, text='average')
average_data_label.place(x=370, y=520)
average_data = Listbox(app, height=1, width=10)
average_data.place(x=430, y=520)


#sd_data
sd_data_label = Label(app, text='S.D.')
sd_data_label.place(x=370, y=550)
sd_data = Listbox(app, height=1, width=10)
sd_data.place(x=430, y=550)


#mode_data
mode_data_label = Label(app, text='mode')
mode_data_label.place(x=570, y=520)
mode_data = Listbox(app, height=1, width=10)
mode_data.place(x=630, y=520)


#range_data
range_data_label = Label(app, text='range')
range_data_label.place(x=570, y=550)
range_data = Listbox(app, height=1, width=10)
range_data.place(x=630, y=550)
'''#######################  output zone  #################'''



#histro
canvas_area = Canvas(app, width=750, height=410, background='pink')
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

canvas_area.create_rectangle(10, 10, 30, 30)



app.mainloop()
