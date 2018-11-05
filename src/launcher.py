'''
Created on 19 May 2014

@author: canisater
'''

import sys
import model
import view
import controller
import argparse

if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='"X" and "O" game')
    parser.add_argument('-g','--gui', help='Use Tk inter GUI',
                        action='store_true') 

    args = parser.parse_args()
    
    m = model.Model()
    c = controller.Controller(m)
    
    if args.gui:
        x = view.ShellView(m, c)
        m.register(x)
        v = view.GUIView(m, c)
        
    else:
        v = view.ShellView(m, c)

    v.start()
