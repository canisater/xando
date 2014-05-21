'''
Created on 19 May 2014

@author: canisater
'''
from enum import Enum

class Event(Enum):
    '''
    classdocs
    '''
    (RESET, SET_SQUARE) = (0, 1)

class State(Enum):
    '''
    classdocs
    '''    
    (DRAW, WIN, TO_PLAY) = 0,1,2
   
    def description(self, 
                    desc={DRAW: 'Draw', 
                          WIN: 'Win', 
                          TO_PLAY: 'To play'}):
        return desc[self.value]

 
class Player(Enum):
    '''
    classdocs
    '''    
    (X, O, NO_PLAYER) = 0,1,2
    
    def description(self, 
                    desc={X: 'X', 
                          O: 'O', 
                          NO_PLAYER: ' '}):
        return desc[self.value]
   
    
class Model(object):
    '''
    classdocs
    '''
    INITIAL_GRID = [Player.NO_PLAYER, Player.NO_PLAYER, Player.NO_PLAYER,
                    Player.NO_PLAYER, Player.NO_PLAYER, Player.NO_PLAYER,
                    Player.NO_PLAYER, Player.NO_PLAYER, Player.NO_PLAYER,]  
    
    LINES = ((0,1,2), (3,4,5), (6,7,8), (0,3,6),
             (1,4,7), (2,5,8), (0,4,8), (2,4,6))
    
    def check_line(self, square, a, b, c, ):
        return (self.grid[a] == self.grid[b] ==
                self.grid[c] == self.grid[square])
            
    def set_square(self, square):
        if self.grid[square] != Player.NO_PLAYER:
            return False
        
        event = Event.SET_SQUARE
        event.square = square 

        self.grid[square] = self.to_play    
        
        for line in Model.LINES:
            if self.check_line(square, *line):
                self.state = State.WIN    

        if self.state != State.WIN and self.grid.count(Player.NO_PLAYER) == 0:
            self.state = State.DRAW 
        
        # Toggle player    
        self.to_play = Player((self.to_play.value + 1) % 2)        
        self.notifyObservers(event)
        return True

    def reset(self):
        
        self.state = State.TO_PLAY
        self.grid = Model.INITIAL_GRID[:]

        self.notifyObservers(Event.RESET)

    def register(self, observer):
        self.observers.add(observer)
 
    def notifyObservers(self, event):
        for o in self.observers:
            o.notify(event) 
         
    def __init__(self):
        '''
        Constructor
        '''
        print ("Created model")
        self.observers = set()
        
        self.state = State.TO_PLAY 
        self.to_play = Player.X
        self.grid = Model.INITIAL_GRID[:]
