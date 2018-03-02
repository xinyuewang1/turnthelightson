'''
Created on 27 Feb 2018

@author: naomiwang
'''
import numpy

# light class
class LightTester:
    lights = None
    
    # n is the first number from input file
    def __init__(self,n):
        # Error handling, check input type
        #if type(n) is int: 
        # Initial state of all the lights are off
        try:
            n=int(n)
            #self.lights = [[False]*n for _ in range(n)]
            self.lights = numpy.array([[False]*n for _ in range(n)])
        except ValueError:
            print("Fail to parse the light number.")
            
    def size(self):
        return len(self.lights)
    
    def apply(self,cmd,x,y):
        # Three recognizable cmd and error handling
        #take care of out of range
        if 0<=x<self.size() and 0<=y<self.size():
            if cmd == 'turn on':
                #self.lights[x][y] = True
                self.lights[x,y] = True
            elif cmd == 'turn off':
                #self.lights[x][y] = False
                self.lights[x,y] = False
            elif cmd == 'switch':
                #if self.lights[x][y] == True:
                if self.lights[x,y] == True:
                    #self.lights[x][y] = False
                    self.lights[x,y] = False
                else:
                    #self.lights[x][y] = True
                    self.lights[x,y] = True
            else:        
                print('Wrong Command at place: ',x,' ,',y)
                pass
        else:
            pass
            
    def count(self):
        #return sum(x.count(True) for x in self.lights)
        return sum((x==True).sum() for x in self.lights)
    
    