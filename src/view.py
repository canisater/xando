'''
Created on 19 May 2014

@author: canisater
'''
from model import State, Event, Player
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
            
            # Bind some custom events to update the Button labels 
            self.button_map[b].bind('<<Set-X>>',func=(lambda event: self.got_event(event,'X')))
            self.button_map[b].bind('<<Set-O>>',func=(lambda event: self.got_event(event,'O')))
            self.button_map[b].bind('<<Clear>>',func=(lambda event: self.got_event(event,' ')))
            
        self.message = tk.Label(self, text="X to play")
        self.message.grid(row=1)  
        self.playbutton = tk.Button(self, text='Play', state=tk.DISABLED, command=(self.controller.reset()))
        self.playbutton.grid(row=2)
           
    def start(self):
        View.start(self)
        self.mainloop()
        
    def notify(self, event):
        '''
        '''
        if event == Event.RESET:
            for b in range(9):
                self.button_map[b]['state'] = tk.NORMAL 
                self.button_map[b]['text'] = ' '
        else:
            square = event.square
            if self.model.grid[square] ==  Player.X:  
                self.button_map[square].event_generate('<<Set-X>>', when='tail')
            else:    
                self.button_map[square].event_generate('<<Set-O>>', when='tail')
             
        if self.model.state == State.TO_PLAY:
            self.message['text'] = '{} {}'.format(self.model.to_play.name, self.model.state.description())
        elif self.model.state == State.DRAW:
            self.message['text'] = '{}'.format(self.model.state.description())
        else: 
            self.message['text'] = '{} {}'.format(self.model.grid[event.square].description(), 
                                                  self.model.state.description())

    
    def got_event(self, tkevent, v):
        tkevent.widget.configure(text=v, state=tk.DISABLED)
                     
            
         
