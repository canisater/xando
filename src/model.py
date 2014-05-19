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
    (DRAW, WIN, TO_PLAY) = 0,1,2
    (X, Y) = 0,1  
    
    lines = ((0,1,2), (3,4,5), (6,7,8), (0,3,6),
             (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    
    def check_line(self, square, a, b, c, ):
        return (self.grid[a] == self.grid[b] ==
                self.grid[c] == self.grid[square])
            
    def set_square(self, square):
        event = Event()
        event.type = Event.SET_SQUARE
        event.square = square 

        self.grid[square] = self.to_play    
        
        for line in lines:
            if self.check_line(square, line):
                self.state = Model.WIN    

        if self.grid.count('2') == 0:
            self.state = Model.DRAW 
                
        self.notifyObservers(event)

    def reset(self):
        self.to_play = (self.to_play + 1) % 2
        self.state = Model.TO_PLAY
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
        
        self.to_play = Model.X
        self.grid = [2,2,2,2,2,2,2,2,2]
