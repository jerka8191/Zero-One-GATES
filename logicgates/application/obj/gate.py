from util.boolUtil import *

class Gate:
    
    def AND(self, a, b):
        return None if not booleans(a, b) else a and b
    
    def NAND(self, a, b):
        return None if not booleans(a, b) else not (a and b) 
    
    def OR(self, a, b):
        return None if not booleans(a, b) else a or b
    
    def XOR(self, a, b):
        return None if not booleans(a, b) else a is not b
    
    def NOR(self, a, b):
        return None if not booleans(a, b) else not (a or b)
    
    def XNOR(self, a, b):
        return None if not booleans(a, b) else a is b
    
    def NOT(self, a):
        return None if not boolean(a) else not a
