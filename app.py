from tkinter import *
from tkinter.ttk import Combobox
import tkinter.messagebox
from covid_india import states
import json
import threading



class Covid_India:
    def __init__(self,root):
        self.root=root
        self.root.title("Covid India")
        self.root.geometry("500x400")
        self.root.iconbitmap("logo620.ico")
        self.root.resizable(0,0)


        states_data=StringVar()



        def on_enter1(e):
            but_check['background']="black"
            but_check['foreground']="cyan"
            
            

        def on_leave1(e):
            but_check['background']="SystemButtonFace"
            but_check['foreground']="SystemButtonText"


        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




        def clear():
            states_data.set("Select Indian States")
            text.delete('1.0','end')

        def checks():
            try:
                text.delete('1.0','end')
                if states_data.get()!="Select Indian States":
                    with open("C:/TEMP/covid.json",'w') as f:
                        if states_data.get()=="All States":
                            fa=states.getdata()
                            ab=json.dumps(fa,indent=4)
                            f.write(ab)
                        
                        else:
                            ab=json.dumps(states.getdata(states_data.get()),indent=4)
                            f.write(ab)
                    with open('C:/TEMP/covid.json', encoding='utf-8') as data_file:
                        x=json.dumps(data_file.read(),indent=4, sort_keys=True)
                        data = json.loads(x)
                        ss=str(data)
                        text.insert("end",ss)

                else:
                    tkinter.messagebox.showerror("Error","Please Select Indian State")
            except Exception as e:
                print(e)

        

        def thread_check():
            t=threading.Thread(target=checks)
            t.start()


#====================frame=============================#
        
        mainframe=Frame(self.root,width=500,height=400,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=150,relief="ridge",bd=3,bg="#144e78")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=245,relief="ridge",bd=3)
        secondframe.place(x=0,y=150)


#==========================firstframe================================#
        
        select_state=['All States','Total','Andaman and Nicobar Islands','Andhra Pradesh',\
                      'Arunachal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh',\
                      'Dadra and Nagar Haveli and Daman and Diu','Delhi','Goa','Gujarat',\
                      'Haryana','Himachal Pradesh',\
                      'Jammu and Kashmir','Jharkhand','Karnataka','Kerala','Ladakh','Lakshadweep',\
                      'Madhya Pradesh','Maharashtra',\
                      'Manipur','Meghalaya','Mizoram','Nagaland','Odisha','Puducherry','Punjab',\
                      'Rajasthan','Sikkim','Tamil Nadu',\
                      'Telengana','Tripura','Uttarakhand','Uttar Pradesh','West Bengal']
        select_state_combo=Combobox(firstframe,values=select_state,font=('arial',14),width=23,state="readonly",textvariable=states_data)
        select_state_combo.set("Select Indian States")
        select_state_combo.place(x=100,y=30)

        but_check=Button(firstframe,width=17,text="Check",font=('times new roman',12),cursor="hand2",command=thread_check)
        but_check.place(x=50,y=90)
        but_check.bind("<Enter>",on_enter1)
        but_check.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,width=17,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=270,y=90)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)


#=======================secondframe==================================#
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
        






if __name__ == "__main__":
    root=Tk()
    Covid_India(root)
    root.mainloop()