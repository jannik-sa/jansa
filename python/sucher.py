'''search all ids from opt-text-APS1.txt'''
import sys
import re



def grep_ids(filename):
    '''make the ids in a list'''
    result1 = set()
    result2 = set()
    
    for line in open(filename,"r"):
        id = parse_line2(line) 
        if id:
            try:
                num = int(id)
                result1.add(num)
            except:
                result2.add(id)

    return result1, result2
    
def parse_line2(line):
    '''search ids'''
    hit = re.search(r"gen des Teils\s+(\S+)", line)
    if hit:
        return hit.group(1)
    return None


def printi()
    '''print ids'''
    filename = sys.argv[1]
    print('filename=', filename)

    ids, ids2 = grep_ids(filename)

    print()
    print("Ids aus Zahlen:")
    print()

    for id in sorted(ids):
        print(id)
    print()
    print("Ids nicht nur mit Zahlen:")
    print()
    for id in sorted(ids2):
        print(id)

printi()