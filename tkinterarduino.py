# By Yahya Khaddam
# Program Your ARDUINO with Python 


import tkinter as tk 
import pyfirmata


class Application(tk.Frame) : 
    def __init__(self,led,master = None) :
       
        super().__init__(master)
        self.master = master 
        self.pack()            
        self.led=led
        self.create_quit()
        
        
    def create_widgets(self):
        
        self.hi_there = tk.Button(self)
        self.hi_there["text"] = f"LED{self.led} (click me)"
        self.hi_there["fg"]="blue"        
        self.hi_there["command"] = self.say_hi        
        self.hi_there.pack(side="top",expand=True)
        
        
   

        
      
    def create_quit(self) :
         self.quit =tk.Button(self,text="Quit", fg="red",
                             command=self.master.destroy)
         self.quit.pack(side="left")
              
    def say_hi(self):
      
        global state
        board.digital[self.led].write(state)
        state = not state
        
        
        

board = pyfirmata.Arduino('/dev/cu.usbmodemFD131')
print("Communication Successfully started")



state=True # The LED indicator 
root=tk.Tk()
root.geometry("300x100")

w = tk.Label(root, text="By Yahya Khaddam").pack()
# the first button
led1=7
LED=Application(led1,master=root)
LED.create_widgets()
# the second one
led2=13
LED2=Application(led2,master=root)
LED2.create_widgets()
# third
led3=10
LED3=Application(led3,master=root)
LED3.create_widgets()


LED.mainloop()
LED2.mainloop()
LED3.mainloop()
        
        
        
        
        
        
        
        
        
        
        
        
        
        