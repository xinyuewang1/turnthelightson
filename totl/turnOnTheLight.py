# -*- coding: utf-8 -*-

"""Main module."""
import re
from totl.lightTester import LightTester  
 
# Main function
def main (filename):
    #check if file exist.
    try:
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
                # take care of match nothing, aka wrong command.
                if ins != None:
                    x1 = min(int(ins.group(2)),int(ins.group(4)))
                    y1 = min(int(ins.group(3)),int(ins.group(5)))
                    x2 = max(int(ins.group(4)),int(ins.group(2)))
                    y2 = max(int(ins.group(3)),int(ins.group(5)))
                    #for x in range(x1,x2+1):
                     #   for y in range(y1,y2+1):
                      #      lights.apply(ins.group(1),x,y)
                    lights.apply(ins.group(1),x1,y1,x2,y2)
        print("#occupied: ",lights.count())
        return lights.count()
    except OSError:
        print('No such file or directory: ',filename)
        return None
    