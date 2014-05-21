'''
Created on 19 May 2014

@author: canisater
'''

import unittest
from unittest.mock import Mock
import model

class Test(unittest.TestCase):


    def setUp(self):
        self.m = model.Model()


    def tearDown(self):
        pass


    def test_initialisation(self):
        # Assert initial state 
        self.assertEqual(self.m.grid, model.Model.INITIAL_GRID, "Invalid initial grid")
        self.assertEqual(self.m.state, model.State.TO_PLAY, "Invalid initial state")
        self.assertEqual(self.m.to_play, model.Player.X, "Invalid initial 'to play'")

    def test_register_notify(self): 
        # Set up some mock observers
        mock_observer_1 = Mock()
        mock_observer_2 = Mock()
        
        # Assert there none registered 
        self.assertEqual(self.m.observers, set(), "Invalid initial observer list")
       
        # Add observers and assert they are there
        self.m.register(mock_observer_1)
        self.assertSetEqual(self.m.observers, {mock_observer_1}, "Observer not added correctly")
        
        self.m.register(mock_observer_2)
        self.assertSetEqual(self.m.observers, {mock_observer_1, mock_observer_2}, "Observer not added correctly")
       
        # Try and add the same one twice
        self.m.register(mock_observer_2)
        self.assertSetEqual(self.m.observers, {mock_observer_1, mock_observer_2}, "Same observers added twice")
        
        # Call reset
        self.m.reset()
        
        # Make sure the right calls were made
        # 'method_calls' is a list of 'call' objects
        mo1_calls = mock_observer_1.method_calls
        mo2_calls = mock_observer_2.method_calls
        self.assertListEqual(mo1_calls, mo2_calls, "Not all observers got notified")
        
        self.assertEqual(len(mo1_calls), 1, "Invalid number of notify calls made")
        name, args, kwargs = mo1_calls[0]
        
        self.assertEqual(name, 'notify', 'Wrong notify method called')
        self.assertEqual(len(args),1,'Wrong number of args passed to notify method')
        self.assertEqual(len(kwargs),0,'Too many args passed to notify method')
        
        self.assertTrue(isinstance(args[0], model.Event), 'Wrong argument type')
               
    def test_check_line(self):
        self.m.grid = [model.Player(p) for p in [1,1,1,1,2,2,0,0,0]]
        lines = ((0,0,1,2,True), (3,3,4,5,False), (6,6,7,8,True), (3,0,3,6,False),
                 (4,1,4,7,False), (8,2,5,8,False), (4,0,4,8,False), (6,2,4,6,False))
        for line in lines:
            s,a,b,c,r = line
            self.assertEqual(self.m.check_line(s, a, b, c), r, "Check line failed {}{}{}{}{}".format(*line))
         
    def test_reset(self):
        # Call 'reset()' and check results 
        self.m.reset()
        self.assertEqual(self.m.grid, model.Model.INITIAL_GRID, "Invalid initial grid")
        self.assertEqual(self.m.state, model.State.TO_PLAY, "Invalid initial state")
        self.assertEqual(self.m.to_play, model.Player.X, "Invalid initial 'to play' not toggled")
     
    def test_set_square_Xwin(self):
        self.assertTrue(self.m.set_square(0), "Set square failed")
        self.assertEqual(self.m.to_play, model.Player.O , "Set square failed - invalid next player") 
        self.assertFalse(self.m.set_square(0), "Set square failed - duplicate not rejected")
        self.m.set_square(3)
        self.m.set_square(1)
        self.m.set_square(4)
        self.m.set_square(2)
        self.assertEqual(self.m.state, model.State.WIN, "Set square failed - invalid state")

    def test_set_square_draw(self):
        self.m.set_square(0)
        self.m.set_square(4)
        self.m.set_square(6)
        self.m.set_square(3)
        self.m.set_square(5)
        self.m.set_square(1)
        self.m.set_square(7)
        self.m.set_square(8)
        self.m.set_square(2)
        self.assertEqual(self.m.state, model.State.DRAW, "Set square failed - invalid state")
              
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()