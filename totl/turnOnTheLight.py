# -*- coding: utf-8 -*-

"""Main module."""
import re
from totl.lightTester import LightTester  
 
# Main function
def main (filename):
    with open(filename) as file:
        instructions = file.readlines()
        instructions = [x.strip() for x in instructions]
        #return instructions[0]
        #print(instructions)
        lights = LightTester(instructions[0])
        
        pat = re.compile(r".*(turn on|turn off|switch)\s*([+-]?\d+)\s*,\s*([+-]?\d+)\s*through\s*([+-]?\d+)\s*,\s*([+-]?\d+).*")
        for instruction in instructions[1:]:
            #print(cmd)
            ins = pat.match(instruction)
            #lights.apply(pat.group, x, y)
            #print(ins)
            # Start to work on 'through'
            x1 = int(ins.group(2))
            y1 = int(ins.group(3))
            x2 = int(ins.group(4))
            y2 = int(ins.group(5))
            for x in range(x1,x2+1):
                for y in range(y1,y2+1):
                    lights.apply(ins.group(1),x,y)
    print(lights.count())
    return lights.count()
            
            
            
        
        
        
        