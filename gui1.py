from tkinter import *

class Main_window:
    def __init__(self, window):
        self.window = window
        self.window.title('Log into MARTA System')
        self.populate()

    def populate(self):
        self.unBox = Entry(self.window)
        self.unBox.grid(row = 1, column = 1, pady = (20,5))
        self.pwBox = Entry(self.window)
        self.pwBox.grid(row = 2, column = 1, pady = (0,20))
        unLabel = Label(self.window, text = 'Username').grid(row = 1, column = 0, ipadx = 15, pady = (20,5))
        pwLabel = Label(self.window, text = 'Password').grid(row = 2, column = 0, ipadx = 15, pady = (0,20))
        b_login = Button(self.window, text = 'Log in', command = self.login).grid(row = 3, columnspan = 2)
        b_register = Button(self.window, text = 'Register New Account', command = self.register).grid(row = 4, columnspan = 2, pady = 10)

        self.photo = PhotoImage(file = 'marta_logo.gif')
        lphoto = Label(self.window, image = self.photo).grid(row = 0, column = 0, columnspan = 2)

    def login(self):
        # Pop_Up(Toplevel(self.window),self.window,'Invalid Login')
        Admin_home(Toplevel(self.window),self.window)
        self.window.withdraw()
    def register(self):
        User_registration(Toplevel(self.window),self.window)
        self.window.withdraw()

class User_registration:
    def __init__(self,window,parent):
        self.window = window
        self.window.title('Create a MARTA Account')
        self.parent = parent
        self.populate()

    def populate(self):
        unLabel = Label(self.window, text = 'Username', anchor = W).grid( row = 1, column = 0,  padx = 15, pady = 5, sticky = E+W)
        emailLabel = Label(self.window, text = 'Email Adress', anchor = W).grid(row = 2, column = 0, padx = 15, pady = 5, sticky = E+W)
        unLabel = Label(self.window, text = 'Password', anchor = W).grid(row = 3, column = 0, padx = 15, pady = 5, sticky = E+W)
        pwLabel = Label(self.window, text = 'Confirm Password', anchor = W).grid(row = 4, column = 0, padx = 15, pady = 5, sticky = E+W)

        self.unBox = Entry(self.window)
        self.unBox.grid(row = 1, column = 1, padx = (0,15))
        self.emailBox = Entry(self.window)
        self.emailBox.grid(row = 2, column = 1, padx = (0,15))
        self.pwBox = Entry(self.window)
        self.pwBox.grid(row = 3, column = 1, padx = (0,15))
        self.confirmBox = Entry(self.window)
        self.confirmBox.grid(row = 4, column = 1, padx = (0,15))

        self.breezeLF = LabelFrame(self.window, text = 'Breeze Card', bd = 5, relief = RIDGE)
        self.breezeLF.grid(row = 5, columnspan = 2)
        v = IntVar()
        rb_existing = Radiobutton(self.breezeLF, text="Use my existing Breeze Card", variable=v, value=1,  anchor=W).grid(row = 0, columnspan = 2, pady = 5, padx = 5, sticky = W+E)
        rb_new = Radiobutton(self.breezeLF, text="Get new Breeze Card number", variable=v, value=2, anchor=W).grid(row = 2, columnspan = 2, pady = 5, padx = 5, sticky = W+E)
        cnLabel = Label(self.breezeLF, text = 'Card Number').grid(row = 1, column = 0, padx = 15)
        self.cnBox = Entry(self.breezeLF)
        self.cnBox.grid(row = 1, column = 1, padx = 10, pady = 5)

        b_register = Button(self.window, text = 'Create Account', command = self.register).grid(row = 6, column = 1, pady = 5)
        b_back = Button(self.window, text = 'Back', command = self.back).grid(row = 6, column = 0, pady = 5)

    def back(self):
        self.window.destroy()
        self.parent.deiconify()

    def register(self):
        pass

class Admin_home:
    def __init__(self,window,parent):
        self.window = window
        self.window.title('Administrator Home')
        self.parent = parent
        self.populate()

    def populate(self):
        b_suspended = Button(self.window, text = 'Station Management', command = self.s_management).grid(row = 0, pady = 5)
        b_suspended = Button(self.window, text = 'Suspended Cards', command = self.suspended).grid(row = 1, pady = 5)
        b_cardManagement = Button(self.window, text = 'Breeze Card Management', command = self.card_management).grid(row = 2, pady = 5,padx = 25)
        b_flow = Button(self.window, text = 'Passenger Flow Report', command = self.flow).grid(row = 3, pady = 5)
        b_back = Button(self.window, text = 'Log Out', command = self.back).grid(row = 4, pady = 10)

    def s_management(self):
        Station_list(Toplevel(self.window),self.window)
        self.window.withdraw()

    def suspended(self):
        self.window.withdraw()

    def card_management(self):
        self.window.withdraw()

    def flow(self):
        self.window.withdraw()

    def back(self):
        self.window.destroy()
        self.parent.deiconify()

class Station_list: #whatre these nifty little tables?
    def __init__(self,window,parent):
        self.window = window
        self.window.title('Station Listing')
        self.parent = parent
        self.populate()

    def populate(self):
        b_new = Button(self.window, text = 'Create New Station', command = self.new).grid()
        b_detail = Button(self.window, text = 'View Station Details', command = self.detail).grid()
        b_back = Button(self.window, text = 'Back', command = self.back).grid(row = 9, column = 0, pady = 5)

    def back(self):
        self.window.destroy()
        self.parent.deiconify()

    def new(self):
        Create_station(Toplevel(self.window),self.window)
        self.window.withdraw()

    def detail(self):
        Station_view(Toplevel(self.window),self.window,'North Avenue')
        self.window.withdraw()

class Station_view:
    def __init__(self,window,parent,station):
        self.window = window
        self.window.title('Station Detail - {}'.format(station))
        self.parent = parent
        self.station = station
        self.populate()

    def populate(self):
        # 6 labels, 1 checkbox, 1 entrybox, 1 button, back button
        stationLabel = Label(self.window, text = self.station, font = ('Arial', 16)).grid(row = 0, column = 0)
        stopLabel = Label(self.window, text = 'STATION NUM').grid(row = 0, column = 3) #station num
        fareLabel = Label(self.window, text = 'Fare',anchor = E).grid(row = 1, column = 0, sticky = E+W, padx = 10)
        intersectionLabel = Label(self.window, text = 'Nearest Intersection',anchor = E).grid(row = 2, column = 0, sticky = E+W, padx = 10)
        locLabel = Label(self.window, text = 'LOCATION', anchor = S).grid(row = 2, column = 1, columnspan = 2, sticky = E+W)
        
        statusLF = LabelFrame(self.window, text = 'When checked, passengers can enter at this station', bd = 0, labelanchor = S, font = ('Arial',8))
        statusLF.grid(row = 3, column = 0,columnspan = 3,padx = 10, sticky = E+W)
        status = IntVar()
        cb_status = Checkbutton(statusLF, text='Open Station', variable=status).grid(row = 0, column = 0)
        # openLabel = Label(self.window, text = 'When checked, passengers can enter at this station', font = ('Arial',8), anchor = E).grid(row = 4,columnspan=2, padx = 40)

        fareBox = Entry(self.window)
        fareBox.grid(row = 1, column = 1)

        b_price = Button(self.window, text = 'Update Price', command = self.price_update).grid(row=1, column = 2)
        b_back = Button(self.window, text = 'Back', command = self.back).grid(row = 4, column = 3)

    def back(self):
        self.window.destroy()
        self.parent.deiconify()

    def price_update(self):
        pass

class Create_station:
    def __init__(self,window,parent):
        self.window = window
        self.window.title('Create New Station')
        self.parent = parent
        self.populate()

    def populate(self):
        nameLabel = Label(self.window, text = 'Station Name', anchor = W).grid( row = 1, column = 0,  padx = 15, pady = 5, sticky = E+W)
        IDLabel = Label(self.window, text = 'Stop ID', anchor = W).grid(row = 2, column = 0, padx = 15, pady = 5, sticky = E+W)
        priceLabel = Label(self.window, text = 'Entry Fare', anchor = W).grid(row = 3, column = 0, padx = 15, pady = 5, sticky = E+W)
        typeLabel = Label(self.window, text = 'Station Type', anchor = W).grid(row = 4, column = 0, padx = 15, pady = 5, sticky = E+W)

        self.nameBox = Entry(self.window)
        self.nameBox.grid(row = 1, column = 1, padx = (0,15))
        self.IDBox = Entry(self.window)
        self.IDBox.grid(row = 2, column = 1, padx = (0,15))
        self.priceBox = Entry(self.window)
        self.priceBox.grid(row = 3, column = 1, padx = (0,15))
        
        self.intersectionLF = LabelFrame(self.window, text = 'Nearest Insersection', bd = 0, font = ('Arial',8))
        self.intersectionLF.grid(row = 7, column = 1, padx = (25,10))
        self.intersectionBox = Entry(self.intersectionLF)
        self.intersectionBox.grid(row = 0)

        v = IntVar()
        rb_train = Radiobutton(self.window, text='Train Station', variable=v, value=1,  anchor=W).grid(row = 5, column =1, pady = 5, padx = 5, sticky = W+E)
        rb_bus = Radiobutton(self.window, text='Bus Station', variable=v, value=2, anchor=W).grid(row =6, column = 1, pady = (0,5), padx = 5, sticky = W+E)
        
        status = IntVar()
        cb_status = Checkbutton(self.window, text='Open Station', variable=status).grid(row = 8)
        openLabel = Label(self.window, text = 'When checked, passengers can enter at this station', font = ('Arial',8), anchor = E).grid(row = 9,columnspan=2,ipadx = 10, padx = 10)

        b_new = Button(self.window, text = 'Create Station', command = self.new_station).grid(row = 10, column = 1, pady = 5)
        b_back = Button(self.window, text = 'Back', command = self.back).grid(row = 10, column = 0, pady = 5)


    def back(self):
        self.window.destroy()
        self.parent.deiconify()

    def new_station(self):
        #clear all entries, add to DB
        #popup station successfully added
        pass

class Suspended_cards: 
    #1 table, 2 buttons, 1 label

class Card_management_admin: 
    #6 entry boxes, 6 labels, 4 buttons, 1 checkbox, 1 table

class Passenger_flow: 
    #2 entry, 2 label, 2 buttons, 1 table

class Passenger_home:
    #6 Labels, 4 buttons, 3 drop down menus

class Card_management_passenger: 
    #3 Label, 1LabelFrame, 3 entry, 2 buttons, 1 table

class Trip_history: 
    #2 Label, 2 Entry, 2 buttons, 1 table

class Pop_Up:
    def __init__(self,window,parent,text,title = 'Error'):
        self.window = window
        self.window.title(title)
        self.parent = parent
        l1 = Label(self.window, text = text).grid(row = 0, ipadx = 25, sticky = E+W)
        b1 = Button(self.window, text = 'Ok', command = self.back).grid(row = 1)

    def back(self):
        self.window.destroy()



if __name__ == '__main__':
    root = Tk()
    Main_window(root)
    root.mainloop()
