import Tkinter
import math
TypeRadio=[("Inductor",1),("Capacitor",0)]
FrequencyRadio=[("Hz",1),("KHz",1e3),("MHz",1e6),("GHz",1e9),("THz",1e12)]
ValueRadio=[[("F",1),("mF",1e-3),("uF",1e-6),("nF",1e-9),("pF",1e-12)],
            [("H",1),("mH",1e-3),("uH",1e-6),("nH",1e-9),("pH",1e-12)]]
class ImpedanceCalc():

        
    #initialze window
    def __init__(self,master):
        frame=Tkinter.Frame(master)
        frame.grid()
        
        #class variables
        self.master=master
        self.type=Tkinter.IntVar()
        self.frequency=Tkinter.DoubleVar()
        self.value=Tkinter.DoubleVar()
        self.frequencymul=Tkinter.DoubleVar()
        self.valuemul=Tkinter.DoubleVar()
        
        #Create Labels
        self.TypeLabel = Tkinter.Label(master, text="Type")
        self.TypeLabel.grid(row=0, column=0, sticky=Tkinter.W)
        self.FrequencyLabel = Tkinter.Label(master, text="Frequency")
        self.FrequencyLabel.grid(row=1, column=0, sticky=Tkinter.W)
        self.ValueLabel = Tkinter.Label(master, text="Value")
        self.ValueLabel.grid(row=2, column=0, sticky=Tkinter.W)
        self.ImpedanceLabel = Tkinter.Label(master, text="Impedance")
        self.ImpedanceLabel.grid(row=4, column=0, sticky=Tkinter.W)
        self.OhmLabel = Tkinter.Label(master, text="Ohm")
        self.OhmLabel.grid(row=4, column=6, sticky=Tkinter.W)

        #Create Entries
        self.FrequencyEntry = Tkinter.Entry(master)
        self.FrequencyEntry.grid(row=1,column=1,columnspan=2,sticky=Tkinter.W)
        self.ValueEntry = Tkinter.Entry(master)
        self.ValueEntry.grid(row=2,column=1,columnspan=2,sticky=Tkinter.W)
        self.ImpedanceEntry = Tkinter.Entry(master,state="readonly",width=40)
        self.ImpedanceEntry.grid(row=4,column=1,columnspan=4,sticky=Tkinter.W)

        #Create Radio Buttons
        self.TypeRadioButton=[]
        
        for text,mode in TypeRadio:
            self.TypeRadioButton.append(Tkinter.Radiobutton(master, text=text, variable=self.type, value=mode, command=self.ChangeRadioValue))
            self.TypeRadioButton[len(self.TypeRadioButton)-1].grid(row=0,column=1+len(self.TypeRadioButton)-1,sticky=Tkinter.W)
            
        self.FrequencyRadioButton=[]
        for text,mode in FrequencyRadio:
            self.FrequencyRadioButton.append(Tkinter.Radiobutton(master, text=text, variable=self.frequencymul, value=mode))
            self.FrequencyRadioButton[len(self.FrequencyRadioButton)-1].grid(row=1,column=3+len(self.FrequencyRadioButton)-1,sticky=Tkinter.W)
            
        self.ValueRadioButton=[]
        for text,mode in ValueRadio[self.type.get()]:
            self.ValueRadioButton.append(Tkinter.Radiobutton(master, text=text, variable=self.valuemul, value=mode))
            self.ValueRadioButton[len(self.ValueRadioButton)-1].grid(row=2,column=3+len(self.ValueRadioButton)-1,sticky=Tkinter.W)

        #Create Calculation Button
        self.CalcButton=Tkinter.Button(master,text="Calculate",command=self.CalculateImp)
        self.CalcButton.grid(row=3,column=0,sticky=Tkinter.W)
        
    def CalculateImp(self):
        self.ImpedanceEntry.config(state=Tkinter.NORMAL)
        self.ImpedanceEntry.delete(0,Tkinter.END)
        try:
            if (self.type.get()==0):
                impedance=1.0/(2*math.pi*float(self.FrequencyEntry.get())*self.frequencymul.get()*float(self.ValueEntry.get())*self.valuemul.get())
            else:
                impedance=2*math.pi*float(self.FrequencyEntry.get())*self.frequencymul.get()*float(self.ValueEntry.get())*self.valuemul.get()
            self.ImpedanceEntry.insert(Tkinter.END,str(impedance))
        except ValueError as e:
            if (e.message != "could not convert string to float: "):
                raise
            else:
                self.ImpedanceEntry.insert(Tkinter.END,"Invalid Frequency or Value")
        self.ImpedanceEntry.config(state="readonly")
        
    def ChangeRadioValue(self):
        for i in range(len(self.ValueRadioButton)):
            self.ValueRadioButton[i].config(text=ValueRadio[self.type.get()][i][0])

    def eventreturn(self,event):
        self.CalculateImp()

    def eventescape(self,event):
        self.kill(self.master)
        
    def kill(self,master):
        master.destroy()
        
if __name__ == '__main__':
    root=Tkinter.Tk()
    root.title("Impedance Calculator")
    IC=ImpedanceCalc(root)
    root.bind("<Return>",IC.eventreturn)
    root.bind("<Escape>",IC.eventescape)
    root.mainloop()
    try:
        root.destroy()
    except Tkinter.TclError as e:
        if (e.message != "can't invoke \"destroy\" command:  application has been destroyed"):
            raise
        else:
            pass
                                        
    
