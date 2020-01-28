
import sys
import re

def grep_ids(filename):
    result = {}
    for line in open(filename,"r"):
        id = parse_line(line) 
        if id:
            result.setdefault(id, 0)
            result[id] += 1
            # result[id] = result[id] + 1
            """
            
            if id in result:
                result[ide] += 1
            else:   
                result[ide] = 1
            """
    return result

def parse_line2(line):
    hit = re.search(r"gen des Teils\s+(\S+)", line)
    if hit:
        return hit.group(1)
    return None

def parse_line(line):
    
    result = None
    if line.find("des Teils ") != -1:
        y=line
        x = line.find("des Teils ")
        result = (y[x+10:line.find(" kann kein")])
    return result
   
                  
filename = sys.argv[1]
print('filename=', filename)

ids = grep_ids(filename)


#for i in range(len(ids)):

 #   print(ids(i))
  #  i += 1


for id in sorted(ids):
    if ids[id]>1:
        print(ids[id],"",id )
    else:
        print("  ",id)
