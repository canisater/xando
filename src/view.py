'''
Created on 19 May 2014

@author: canisater
'''

class View():
    '''
    classdocs
    '''
    status = ["DRAW", "WIN", "TO PLAY"]
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
    def start(self):
        View.start(self)
        print (View.status[self.model.state])
           
 
class GUIView(View):
    '''
    classdocs
    '''
    def start(self):
        View.start(self)
