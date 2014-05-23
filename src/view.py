'''
Created on 19 May 2014

@author: canisater
'''
from model import State, Event
import tkinter as tk
import tkinter.font as tkFont
class View():
    '''
    classdocs
    '''
    status = ["Draw", "Win", "to play"]
    to_play = ["X", "Y", " "]
    
    
    def __init__(self, model, controller):
        '''
        Constructor
        '''
        print ("Created view")
        self.model = model
        self.controller = controller
    
    def start(self):
        self.model.register(self)    

class ShellView(View):
    '''
    classdocs
    '''
    BOARD = '''
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    ---+---+---
     {} | {} | {}
    '''
    def start(self):
        View.start(self)
        self.notify(None)
        while True:
            while True: 
                while (not self.controller.set_square(input("Enter square (0..8):"))):
                    pass
                
                if self.model.state != State.TO_PLAY:
                    break
                    
            if  'Y' not in input("Play again? (Y or N):"):
                break                        
            self.controller.reset()
            
        
    def notify(self, event):
        
        print (ShellView.BOARD.format(*(p.description() for p in self.model.grid)))
        
        if self.model.state == State.TO_PLAY:
            print(self.model.to_play.name, self.model.state.description())
        elif self.model.state == State.DRAW:
            print (self.model.state.description())
        else: 
            print (self.model.grid[event.square].description(), self.model.state.description())
 
class GUIView(View, tk.Frame):
    def __init__(self, model, controller):
        '''
        Constructor
        '''
        View.__init__(self, model, controller)
        tk.Frame.__init__(self, None)
        self.add_widgets()
        self.grid()
    
    def button_press(self,b):
        print("Button", str(b))
        self.controller.set_square(str(b))
        
    def add_widgets(self):
        self.buttons = tk.Frame(self)
        self.buttons.grid(row=0)
        self.button_map = {}
        courier = tkFont.Font(family="Courier",size=24,weight="bold")
        
        for b in range(9):
            self.button_map[b] = tk.Button(self.buttons,
                                      text=' ',font=courier,
                                      command=(lambda b = b: self.button_press(b)))
            self.button_map[b].grid(row=b//3, column=b%3)
            self.button_map[b].bind('<<Event>>',func=self.got_event)
        
        self.message = tk.Label(self,text="Some text")
        self.message.grid(row=1)  
       
           
    def start(self):
        View.start(self)
        self.mainloop()
        
    def notify(self, event):
        print (event)
        
        if event == Event.RESET:
            for b in range(9):
                self.button_map[b]['state'] = tk.NORMAL 
                self.button_map[b]['text'] = ' '
        else:
            square = event.square        
            self.button_map[square].event_generate('<<Event>>', when='tail',data=square)
        
             
        if self.model.state == State.TO_PLAY:
            self.message['text'] = '{} {}'.format(self.model.to_play.name, self.model.state.description())
        elif self.model.state == State.DRAW:
            self.message['text'] = '{}'.format(self.model.state.description())
        else: 
            self.message['text'] = '{} {}'.format(self.model.grid[event.square].description(), 
                                                  self.model.state.description())

    
    def got_event(self, tkevent):
        tkevent.widget.configure(text='X')
        print(dir(tkevent))
        print(type(tkevent))
        print(tkevent.send_event)
        print(tkevent.type) 
        print(tkevent.keycode)
        print(tkevent.num)
             
            
         
