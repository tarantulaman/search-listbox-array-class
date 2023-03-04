from tkinter import ttk
from tkinter import *



class Ventana:

    def __init__(self, window):


        self.wind = window
        self.wind.title('Student Application')
        


        entry_lb = Entry(window)
        entry_lb.grid(row = 1, column = 0)
        entry_lb.bind('<KeyRelease>', self.scankey_lb)

        self.listbox = Listbox(window)
        self.listbox.grid(row = 2, column = 0)
        


        self.get_languages_lb()





    

    





    # Funciones ListBox


    def get_languages_lb(self):

        list = ('C','C++','Java',
                'Python','Perl',
                'PHP','ASP','JS' )

        self.listbox.delete(0, 'end')

        # put new data
        for item in list:
            self.listbox.insert('end', item)

    


    def get_search_lb(self, data):

        self.listbox.delete(0, 'end')

        # put new data
        for item in data:
            self.listbox.insert('end', item)

        
        

    def scankey_lb(self, event):
	
        val = event.widget.get()
        print(val)

        list = ('C','C++','Java',
                'Python','Perl',
                'PHP','ASP','JS' )

        if val == '':
            self.get_languages_lb()
        else:
            data = []
            for item in list:
                if val.lower() in item.lower():
                    data.append(item)
                    print(data)	

            self.get_search_lb(data)	


    
   








if __name__ == '__main__':
    window = Tk()
    application = Ventana(window)
    window.mainloop()
