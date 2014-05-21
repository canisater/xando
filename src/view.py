'''
Created on 19 May 2014

@author: canisater
'''
from model import State
import tkinter as tk
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
                   
        

            
   
 
class GUIView(View):
    '''
    classdocs
    '''
    def start(self):
        View.start(self)
