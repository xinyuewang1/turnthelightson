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
            #print(self.lights)
        except ValueError:
            print("Fail to parse the light number.")
            
    def size(self):
        return len(self.lights)
    
    '''
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
    '''
    #numpy version
    def apply(self,cmd,x1,y1,x2,y2):
        if x2<0 or y2<0:
            pass
        elif x1>=self.size() or y1>=self.size():
            pass
        else:
            x1=max(x1,0)
            x2=min(x2,self.size()-1)
            y1=max(y1,0)
            y2=min(y2,self.size()-1)
            #area=self.lights[x1:x2+1,y1:y2+1]
        #if 0<=x1<=x2 and 0<=y1<=y2 and 0<=x2<self.size() and 0<=y2<self.size():
            #print(x1,y1,x2,y2)
            #print(area)
            if cmd == 'turn on':
                #self.lights[x][y] = True
                #self.lights[x,y] = True
                self.lights[x1:x2+1,y1:y2+1]=True
                #print(self.lights)
            elif cmd == 'turn off':
                #self.lights[x][y] = False
                #self.lights[x,y] = False
                self.lights[x1:x2+1,y1:y2+1]=False
                #print(self.lights)
            elif cmd == 'switch':
                #if self.lights[x][y] == True:
                rows1, cols1 = numpy.where(self.lights[x1:x2+1,y1:y2+1]==True)
                rows2,cols2 = numpy.where(self.lights[x1:x2+1,y1:y2+1]==False)
                self.lights[x1:x2+1,y1:y2+1][rows1,cols1]=False
                self.lights[x1:x2+1,y1:y2+1][rows2,cols2]=True
                #print(self.lights)
                #if self.lights[x,y] == True:
                    #self.lights[x][y] = False
                 #   self.lights[x,y] = False
                #else:
                    #self.lights[x][y] = True
                 #   self.lights[x,y] = True
            else:        
                #print('Wrong Command at place: ',x,' ,',y)
                pass
        #else:
         #   pass

        
            
    def count(self):
        #return sum(x.count(True) for x in self.lights)
        return sum((x==True).sum() for x in self.lights)
    
    