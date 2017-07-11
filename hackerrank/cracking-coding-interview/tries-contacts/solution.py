
class Node:
    def __init__(self, value=None):
        self.count = 0
        self.children = []
        self.value = value

def add(contact):
    node = root    
    for c in contact:       
        child = find_node(node.children, c)
        if child:
            child.count += 1
        else:
            child = Node(c)
            child.count = 1
            node.children.append(child)            
        node = child

def find(contact):
    node = root
    for c in contact:
        child = find_node(node.children, c)
        if not child: 
            return 0        
        node = child
    return node.count

def find_node(nodes, value):    
    for node in nodes:
        if node.value == value:
            return node    

def do_operation(op, contact):
    if op == 'add':
        print 'add', contact
        add(contact)
    elif op == 'find':
        print 'find', contact, find(contact)


root = Node()
first_line = True
import os 
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + '/data12.in') as my_file:
    for line in my_file:
        if first_line:
            first_line = False
            continue
        line = line.strip()
        if line:
            op, contact = line.split(' ')
            do_operation(op, contact)