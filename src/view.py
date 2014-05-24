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
  
    def add_widgets(self):
        self.buttons = tk.Frame(self)
        self.buttons.grid(row=0)
        self.button_map = {}
        courier = tkFont.Font(family="Courier",size=24,weight="bold")
        
        for b in range(9):
            self.button_map[b] = tk.Button(self.buttons,
                                      text=' ',font=courier,
                                      command=(lambda b = b: self.controller.set_square(str(b))))
            self.button_map[b].grid(row=b//3, column=b%3)
            
            # Bind some custom events to update the Button labels 
            self.button_map[b].bind('<<Set-X>>',func=(lambda event: event.widget.configure(text='X', state=tk.DISABLED)))
            self.button_map[b].bind('<<Set-O>>',func=(lambda event: event.widget.configure(text='O', state=tk.DISABLED)))
            self.button_map[b].bind('<<Clear>>',func=(lambda event: event.widget.configure(text=' ', state=tk.NORMAL)))
            self.button_map[b].bind('<<Disable>>',func=(lambda event: event.widget.configure(state=tk.DISABLED)))
            
        self.message = tk.Label(self, text="X to play")
        self.message.grid(row=1) 
        self.message.bind('<<Draw-Msg>>',func=(lambda event: event.widget.configure(text='Draw')))
        self.message.bind('<<XWin-Msg>>',func=(lambda event: event.widget.configure(text='X win')))
        self.message.bind('<<OWin-Msg>>',func=(lambda event: event.widget.configure(text='O win')))
        self.message.bind('<<XTurn-Msg>>',func=(lambda event: event.widget.configure(text='X to play')))
        self.message.bind('<<OTurn-Msg>>',func=(lambda event: event.widget.configure(text='O to play')))
         
        self.playbutton = tk.Button(self, text='Play', state=tk.DISABLED, command=(lambda: self.controller.reset()))
        self.playbutton.grid(row=2)
        self.playbutton.bind('<<Disable-Play>>',func=(lambda event: event.widget.configure(state=tk.DISABLED)))
        self.playbutton.bind('<<Enable-Play>>',func=(lambda event: event.widget.configure(state=tk.NORMAL)))
           
    def start(self):
        View.start(self)
        self.mainloop()
        
    def notify(self, event):
        '''
        '''
        if event == Event.RESET:
            for b in range(9):
                self.button_map[b].event_generate('<<Clear>>', when='tail') 
        
            self.playbutton.event_generate('<<Disable-Play>>',when='tail')
        
        else:
            square = event.square
            if self.model.grid[square] ==  Player.X:  
                self.button_map[square].event_generate('<<Set-X>>', when='tail')
            else:    
                self.button_map[square].event_generate('<<Set-O>>', when='tail')
             
        if self.model.state == State.TO_PLAY:
            if self.model.to_play == Player.X:
                self.message.event_generate('<<XTurn-Msg>>', when='tail')
            else:
                self.message.event_generate('<<OTurn-Msg>>', when='tail')    
        else:
            self.playbutton.event_generate('<<Enable-Play>>',when='tail')
            for b in range(9):
                self.button_map[b].event_generate('<<Disable>>', when='tail') 
                
            if self.model.state == State.DRAW:
                self.message.event_generate('<<Draw-Msg>>', when='tail')
            else: 
                if self.model.grid[square] == Player.X:
                    self.message.event_generate('<<XWin-Msg>>', when='tail')
                else:
                    self.message.event_generate('<<OWin-Msg>>', when='tail')    

            
    
                     
            
         
