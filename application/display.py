
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


import numpy as np

from matplotlib.colors import LinearSegmentedColormap


import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib import colormaps


import tkinter.font

from tkinter import *

import csv



basepath = "C:/Users/cepag/Documents/School/Uni/Competitions/Engineering Competition/CEC 2024/CEC-2024-Programming-Competition/data/"
world_path = "world_array_data_day_"
algal_path = "algal_data_day_"



class Display:
    def __init__(self):
        # Class Constants
        



        # Initialize window
        self.root = Tk()
        self.root.wm_title("Hector Analysis")
    
        
        self.TITLE_FONT = tkinter.font.Font(size=20, weight="bold") #tkinter.font.Font(family="Arial", size=20, weight="bold")
        self.LABEL_FONT = tkinter.font.Font(size=16)

        self.preserve_selected = StringVar()
        self.preserve_selected.set("Algal")
        self.day_selected = IntVar()
        self.day_selected.set(1)
        self.rig_one_coords_text = StringVar()
        self.rig_one_coords_text.set("Rig 1: (_, _)")
        self.rig_two_coords_text = StringVar()
        self.rig_two_coords_text.set("Rig 2: (_, _)")

        self.rig_one_coords = (-1, -1)
        self.rig_two_coords = (-1, -1)

        self.rigCoordsList = [[(-1,-1),(-1,-1)],[(-1,-1),(-1,-1)]]

        



        self.collectedList = [[1,2,3,4],
                             [11,12,13,14],
                             [21,22,23,24]]
        self.compromisedList = [[31,32,33,34],
                                [41,42,43,44],
                                [51,52,53,54]]
        
        self.heliumCount = IntVar()
        self.metalCount = IntVar()
        self.oilCount = IntVar()
        self.compromisedCount = IntVar()

        # Initialize Canvas
        self.UpdateCanvas(forgetLast=False)

        # ----------------------- Initialize Interface -----------------------
        self.interface = Frame(master=self.root)
        self.interface.config(borderwidth=1)

        # ----------------------- Preserve Section -----------------------
        title = Label(master=self.interface, text="Preserve", font="bold")
        title.config(font=self.TITLE_FONT)
        title.pack(side=TOP, pady=(0, 0))

        btn = Radiobutton(master=self.interface, text="Algal", variable=self.preserve_selected, value="Algal", command=self._on_preserve_change)
        btn.pack(side=TOP)
        # btn.config(font=LABEL_FONT)
        Radiobutton(master=self.interface, text="Coral", variable=self.preserve_selected, value="Coral", command=self._on_preserve_change).pack(side=TOP)
        Radiobutton(master=self.interface, text="Species", variable=self.preserve_selected, value="Species", command=self._on_preserve_change).pack(side=TOP)

        # --------------------------- Day Select Section ---------------------------
        title = Label(master=self.interface, text="Day", font="bold")
        title.config(font=self.TITLE_FONT)
        title.pack(side=TOP, pady=(50, 0))
        scale = Scale(master=self.interface, from_=1, to=30, orient="horizontal", length=200, variable=self.day_selected)
        scale.bind("<ButtonRelease-1>", self._on_day_change)
        scale.pack()
        buttonGroup = Frame(master=self.interface)
        Button(master=buttonGroup, text="<", width=4, command=self._set_prev_day).pack(side=LEFT)
        Button(master=buttonGroup, text=">", width=4, command=self._set_next_day).pack(side=RIGHT)
        buttonGroup.pack()



        # --------------------------- Coordinates Section ---------------------------
        title = Label(master=self.interface, text="Coordinates", font="bold")
        title.config(font=self.TITLE_FONT)
        title.pack(pady=(50, 0))
        Label(self.interface, textvariable=self.rig_one_coords_text).pack()
        Label(self.interface, textvariable=self.rig_two_coords_text).pack()

        
        self.rig_one_coords_text.set(f"Rig 1: {self.rig_one_coords}")
        self.rig_two_coords_text.set(f"Rig 2: {self.rig_two_coords}")



        # ---------------------------- Metrics --------------------------
        self.metrics = tkinter.Frame(master=self.root)
        self.metrics.config(borderwidth=1)

        # --------------------- Collected ---------------------
        title = Label(master=self.metrics, text="Collected", font="bold")
        title.config(font=self.TITLE_FONT)
        title.pack(pady=(50,0))
        section = Frame(master=self.metrics)
        Label(section, text="Helium").pack(side=LEFT)
        Label(section, text=":").pack(side=LEFT)
        Label(section, textvariable=self.heliumCount).pack(side=RIGHT)
        section.pack()
        section = Frame(master=self.metrics)
        Label(section, text="Metal").pack(side=LEFT)
        Label(section, text=":").pack(side=LEFT)
        Label(section, textvariable=self.metalCount).pack(side=RIGHT)
        section.pack()
        section = Frame(master=self.metrics)
        Label(section, text="Oil").pack(side=LEFT)
        Label(section, text=":").pack(side=LEFT)
        Label(section, textvariable=self.oilCount).pack(side=RIGHT)
        section.pack()
        
        

        # --------------------- Compromised ---------------------
        title = Label(master=self.metrics, text="Compromised", font="bold")
        title.config(font=self.TITLE_FONT)
        title.pack(pady=(50,0))
        
        section = Frame(master=self.metrics)
        Label(section, textvariable=self.preserve_selected).pack(side=LEFT)
        Label(section, text=":").pack(side=LEFT)
        Label(section, textvariable=self.compromisedCount).pack(side=RIGHT)
        section.pack()
        

        # Resource destruction (just the selected resource)
        # Compromised





        self.metrics.pack(side=tkinter.RIGHT, expand=0, padx=10, pady=5)
        self.interface.pack(side=tkinter.RIGHT, expand=10, padx=10, pady=5)

    def UpdateCanvas(self, forgetLast = True):
        if forgetLast: self.canvas.get_tk_widget().pack_forget()
        
        self._update_coords()
        self._update_metrics()

        # UPDATE FUNCTION TO READ IN DATA FROM INPUT?
        data = simpleGetArray(basepath + world_path + str(self.day_selected.get()) + ".csv") # ----------- INSERT DATA
        
        fig, ax = plt.subplots()
        # ax.imshow(data, cmap=colormaps.get('cividis'))
        cmap = LinearSegmentedColormap.from_list('', [(0.1725,0.1725,0.6980), (0.8235,0.7804,0.5412)])
        ax.imshow(data, cmap=cmap)
        plt.tight_layout(pad=0)
        plt.axis('off')
        plt.margins(x=0)
        plt.plot(int(self.rig_one_coords[0]),int(self.rig_one_coords[1]),'ro') 
        plt.plot(int(self.rig_two_coords[0]),int(self.rig_one_coords[1]),'rx') 
        
        # self.rig_one_coords = (random.randint(1, 99), random.randint(1, 99))
        # self.rig_two_coords = (random.randint(1, 99), random.randint(1, 99))
        

        self.canvas = FigureCanvasTkAgg(fig, master=self.root)  # A tk.DrawingArea.
        # self.canvas.get_tk_widget().config()
        self.canvas.get_tk_widget().pack(side=LEFT, fill=BOTH, expand=0)

        


    def _on_preserve_change(self):
        print("YO PRESERVED " + self.preserve_selected.get())

        # update
        
        self.UpdateCanvas()

    def _on_day_change(self, e):
        # print("SELECTED DAY " + str(self.day_selected.get()))

        self.UpdateCanvas()

    def _set_next_day(self):
        if self.day_selected.get() < 30:
                self.day_selected.set(self.day_selected.get() + 1)
                self._on_day_change(None)
    def _set_prev_day(self):
        if self.day_selected.get() > 1:
            self.day_selected.set(self.day_selected.get() - 1)
            self._on_day_change(None)

    def _update_coords(self):
        day = self.day_selected.get()
        self.rig_one_coords = self.rigCoordsList[0][day-1]
        self.rig_two_coords = self.rigCoordsList[1][day-1]
        
        self.rig_one_coords_text.set(f"Rig 1: {self.rig_one_coords}")
        self.rig_two_coords_text.set(f"Rig 2: {self.rig_two_coords}")

    
    def _update_metrics(self):
        day = self.day_selected.get()
        
        # Update Collected
        self.heliumCount.set(self.collectedList[0][day-1])
        self.metalCount.set(self.collectedList[1][day-1])
        self.oilCount.set(self.collectedList[2][day-1])

        # Update Compromised
        if self.preserve_selected.get() == 'Algal':
            self.compromisedCount.set(self.compromisedList[0][day-1])
        elif self.preserve_selected.get() == 'Coral':
            self.compromisedCount.set(self.compromisedList[1][day-1])
        elif self.preserve_selected.get() == 'Species':
            self.compromisedCount.set(self.compromisedList[2][day-1])
        
    def show(self):
        self.UpdateCanvas()
        self.root.mainloop()

    # inputs one array for both rigs for 30 days of x,y tuples
    def setRigCoords(self, inputArr):
        self.rigCoordsList = inputArr
        self._update_coords()
        
    # Input arr (helium, metal, oil) by day
    def setCollected(self, inputArr):
        # self.heliumCount.set(inputArr[0])
        # self.metalCount.set(inputArr[1])
        # self.oilCount.set(inputArr[2])
        self.collectedList = inputArr
    
    # input value
    def setCompromised(self, inputArr):
        self.compromisedList = inputArr




def simpleGetArray(path):
    reader = csv.reader(open(path), delimiter=",")

    # data = np.array(x).astype = float
    data = np.zeros((100, 100))

    # Populate data array
    for i, row in enumerate(reader):
        if i != 0:
            # print(row)
            # y += int(row[1])
            if row[3] != "":
                data[int(row[2])][int(row[1])] = float(row[3])
            else:
                # data is empty
                data[int(row[2])][int(row[1])] = None
    return data







def test():
    app = Display()
    # list of rig1 list and rig2 list
    app.setRigCoords([[(1,1),(2,2),(3,3),(4,4)],
                      [(50,1),(50,2),(50,3),(50,4)]])
    
    # tuple list of collected by day (helium, metal, oil)
    app.setCollected([[1,2,3,4],
                      [11,12,13,14],
                      [21,22,23,24]])

    # list of compromised by day (algal, coral, species)
    app.setCompromised([[31,32,33,34],
                        [41,42,43,44],
                        [51,52,53,54]])

    # show app
    app.show()

test()


