'''
Created on 19 May 2014

@author: canisater
'''

class Controller(object):
    '''
    classdocs
    '''


    def __init__(self, model):
        '''
        Constructor
        '''
        print ("Created controller")
        self.model = model
    
    def reset(self):
        self.model.reset()   
    
    def set_square(self, square):
        if square not in '012345678':
            return False
        
        return self.model.set_square(int(square))       