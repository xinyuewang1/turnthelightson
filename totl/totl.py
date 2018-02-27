# -*- coding: utf-8 -*-

"""Main module."""
import re

# light class
class lightTester:
    lights = None
    
    # n is the first number from input file
    def __init__(self,n):
        
        # Error handling, check input type
        #if type(n) is int: 
        # Initial state of all the lights are off
        try:
            n=int(n)
            self.lights = [[False]*n for _ in range(n)]
        except ValueError:
            print("Fail to parse the light number.")
    
    def apply(self,cmd,x,y):
        # Three recognizable cmd and error handling
        if cmd == 'turn on':
            self.lights[x][y] = True
        elif cmd == 'turn off':
            self.lights[x][y] = False
        elif cmd == 'switch':
            if self.lights[x][y] == True:
                self.lights[x][y] = False
            else:
                self.lights[x][y] = True
        else:        
            print('Wrong Command at place: ',x,' ,',y)
            
    def count(self):
        return sum(x.count(True) for x in self.lights)
    
# Main function
def main (filename):
    with open(filename) as file:
        instructions = file.readlines()
        instructions = [x.strip() for x in instructions]
        #return instructions[0]
        #print(instructions)
        lights = lightTester(instructions[0])
        
        for cmd in instructions[1:]:
            #print(cmd)
            pat = re.compile(r".*(turn on|turn off|switch)\s*([+-]?\d+) \
\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
            
            
            
            
        
        
        
        