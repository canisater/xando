'''
Created on 19 May 2014

@author: canisater
'''

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
        print ("    ",View.to_play[self.model.to_play], View.status[self.model.state])                
        print (ShellView.BOARD.format(*(View.to_play[i] for i in self.model.grid)))
        self.controller.reset()
        
    def notify(self, event):
        print ("    ",View.to_play[self.model.to_play], View.status[self.model.state])                
        print (ShellView.BOARD.format(*(View.to_play[i] for i in self.model.grid)))
      
 
class GUIView(View):
    '''
    classdocs
    '''
    def start(self):
        View.start(self)
