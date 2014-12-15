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
len_data_label.place(x=170, y=500)
len_data = Listbox(app, height=1, width=10)
len_data.insert(1, 321)
len_data.place(x=250, y=500)

#max_data
max_data_label = Label(app, text='max')
max_data_label.place(x=20, y=500)
max_data = Listbox(app, height=1, width=10)
max_data.place(x=80, y=500)

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
average_data_label.place(x=370, y=500)
average_data = Listbox(app, height=1, width=10)
average_data.place(x=430, y=500)


#sd_data
sd_data_label = Label(app, text='S.D.')
sd_data_label.place(x=370, y=550)
sd_data = Listbox(app, height=1, width=10)
sd_data.place(x=430, y=550)


#mode_data
mode_data_label = Label(app, text='mode')
mode_data_label.place(x=570, y=500)
mode_data = Listbox(app, height=1, width=10)
mode_data.place(x=630, y=500)


#range_data
range_data_label = Label(app, text='range')
range_data_label.place(x=570, y=550)
range_data = Listbox(app, height=1, width=10)
range_data.place(x=630, y=550)
'''#######################  output zone  #################'''



#histro
canvas_area = Canvas(app, width=750, height=350, background='green')
canvas_area.place(x=20, y=100)

canvas_area.create_rectangle(10, 10, 30, 30)



app.mainloop()
