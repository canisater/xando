'''
Created on 19 May 2014

@author: canisater
'''

class Event():
    '''
    classdocs
    '''
    RESET = 0
    

class Model(object):
    '''
    classdocs
    '''
    (DRAW, XWIN, YWIN, TO_PLAY) = 0,1,2,3
    (X, Y) = 0,1  
    
    lines = ({0,1,2}, {3,4,5}, {6,7,8}, {0,3,6},
             {1,4,7}, {2,5,8}, {0,4,8}, {2,4,6})
    

    def set_square(self, square):
        event = Event()
        event.type = Event.SET_SQUARE
        event.square = square 
        self.grid[square] = self.state    
        self.change_state()
        self.notifyObservers(event)

    def reset(self):
        self.to_play = (self.to_play + 1) % 2
        self.xs = set()
        self.ys = set()
        self.grid = [2,2,2,2,2,2,2,2,2]
        event = Event()
        event.type = Event.RESET 
        self.notifyObservers(event)

    def register(self, observer):
        self.observers.append(observer)
 
    def notifyObservers(self, event):
        for o in self.observers:
            o.notify(event) 
         
    def __init__(self):
        '''
        Constructor
        '''
        print ("Created model")
        self.observers = []
        self.state = Model.TO_PLAY
        self.to_play = Model.X
        self.xs = set()
        self.ys = set()
        self.grid = [2,2,2,2,2,2,2,2,2]