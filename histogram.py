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

#input box
input_box_label = Label(app, text='Data Input')
input_box_label.place(x=20, y=5)
input_box = Entry(app, width=100)
input_box.place(x=20, y=30)





''' ################## def function zone################## '''
def callback():
    print 'Hello World.'



range_level = 5


def range_out(data):
    """print range"""
    min_range = min()
    max_range = min() + range_len(data, range_level)
    range_count = {}
    for i in xrange(5):
        range_count["range"+str(i+1)] = 0
        ans = "["+str(min_range)+" - "+str(max_range)+"] |"
        for j in data:
            if j >= min_range and j <= max_range:
                ans = ans + "-"
                range_count["range"+str(i+1)] += 1
        min_range = max_range
        max_range = max_range + range_len(data, range_level)
        print ans
    print range_count




def process_but():

    
    data = [int(i) for i in input_box.get().split(',')]
    print 'hello' 
    print data
    len_data.delete(1, last=None)
    len_data.insert(0, len(data))
    

''' ################## def function zone################## '''

'''#######################  process zone  #################'''



#process_button
process_button = Button(app, height=3, width=10, text='Process', command=process_but)
process_button.place(x=670, y=30)
'''#######################  process zone  #################'''



'''#######################  output zone  #################'''
#len_data
len_data_label = Label(app, text='len data')
len_data_label.place(x=170, y=520)
len_data = Listbox(app, height=1, width=10)
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
