'''
Created on 19 May 2014

@author: canisater
'''

import sys
import model
import view
import controller

if __name__ == '__main__':

    if len(sys.argv) > 1:
        option = sys.argv[1].upper()
    else:
        option = 'CONSOLE'

    m = model.Model()
    c = controller.Controller(m)
    
    if option == 'CONSOLE':
        v = view.ShellView(m, c)
    else:
        v = view.GUIView(m, c)

    v.start()
