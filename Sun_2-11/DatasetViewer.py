from tkinter import *
from tkinter import ttk
import pandas as pd

class DatasetViewer:
    def __int__(self):
        pass
    def create_ui(self):
        self.root=Tk()
        self.root.title('Dataset viewer - House Price Prediction')
        self.root.geometry('800x600')
        main_panel=PanedWindow(self.root)
        main_panel['bg']='yellow'
        main_panel.pack(fill=BOTH,expand=True)

        #Columns
        columns=('Avg. Area Income', 'Avg. Area House Age', 'Avg. Area Number of Rooms',
                'Avg. Area Number of Bedrooms', 'Area Population', 'Price')
        self.tree=ttk.Treeview(main_panel,columns=columns, show='headings')

        #Headings
        self.tree.heading('Avg. Area Income',text='Avg. Area Income')
        self.tree.heading('Avg. Area House Age',text='Avg. Area House Age')
        self.tree.heading('Avg. Area Number of Rooms',text='Avg. Area Number of Rooms')
        self.tree.heading('Avg. Area Number of Bedrooms',text='Avg. Area Number of Bedrooms')
        self.tree.heading('Area Population',text='Area Population')
        self.tree.heading('Price',text='Price')

        #Self.tree.grid(row=0,column=0,sticky='nsew')
        self.tree.pack(side=LEFT,fill=BOTH,expand=True)
        scrollbar=ttk.Scrollbar(main_panel,orient=VERTICAL,command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)

        #Scrollbar.grid(row=0,column=1,sticky='ns')
        scrollbar.pack(side=RIGHT,fill=BOTH,expand=True)

    def show_ui(self):
        self.root.mainloop()

    def show_data_listview(self,filename):
        df=pd.read_csv(filename)
        for i in range(0,len(df)):
            values=[df.iloc[i][0],df.iloc[i][1],df.iloc[i][2],df.iloc[i][3],df.iloc[i][4],df.iloc[i][5]]
            print(values)
            self.tree.insert('',END,values=values)