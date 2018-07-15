import os


MAX_CHILDREN = [11, 5, 8, 26, 0]

class Node:
    def __init__(self, value, max_children=0):
        self.count = 0
        self.children = [None] * max_children
        self.children2 = []
        self.value = value

    def __str__(self):
        return str(self.value) + '-' + str(self.count)

    def __repr__(self):
        return self.__str__()


def find_one(node, value):
    return node.children[value]


def insert(root, params):
    node = root
    for i, p in enumerate(params):
        child = find_one(node, p)
        if child:
            child.count += 1
        else:
            child = Node(p, MAX_CHILDREN[i])
            child.count = 1
            node.children[p] = child
            node.children2.append(child)
        node = child


def find_all(node, min=None, max=None):
    if not min or min == -1:
        return node.children2

    if not max:
        max = min

    results = []
    for i in xrange(min, max + 1):
        c = node.children[i]
        if c: 
            results.append(c)

    return results


def query(root, ds, de, pid, cid, sid, rid):
    params = (pid, cid, sid, rid)
    nodes = find_all(root, ds, de)
    for p in params:
        children = []
        for node in nodes:
            children.extend(find_all(node, p))
        if not children:
            return 0
        else:
            nodes = children

    sum = 0
    for node in nodes:
        sum += node.count
    return sum


def print_node(node, is_root=True):
    if is_root:
        print 'Root', node
    print ' '.join(c.__str__() for c in node.children)

    for node in node.children:
        print_node(node, False)


def safe_get(l, idx, default=None):
    try:
        return l[idx]
    except IndexError:
        return default


def process(root, line):
    params = line.split(' ')
    op = params[0]

    # extract date
    dt = params[1].split('.')
    ds = int(dt[0])
    de = int(safe_get(dt, 1)) if len(dt) > 1 else None

    # extract product and category id
    pc = params[2].split('.')
    pid = int(pc[0])
    cid = int(safe_get(pc, 1, 0 if op == 'S' else -1))

    # extract state and region id
    sr = params[3].split('.')
    sid = int(sr[0])
    rid = int(safe_get(sr, 1, 0 if op == 'S' else -1))

    # print op, ds, de, pid, cid, sid, rid

    if op == 'S':
        insert(root, (ds, pid, cid, sid, rid))
    elif op == 'Q':
        print query(root, ds, de, pid, cid, sid, rid)


if __name__ == '__main__':
    root = Node(99, 101)
    first_line = True
    dir_path = os.path.dirname(os.path.realpath(__file__))

    lines = []
    with open(dir_path + '/sample2.in') as my_file:
        for line in my_file:
            if first_line:
                first_line = False
                continue
            # lines.append(line.strip())
            process(root, line.strip())
            
    # import time
    # now = long(time.time() * 1000)
    # for _ in xrange(0, 10000):
    #     for line in lines:
    #         process(root, line.strip())

    # print 'Took', (long(time.time() * 1000) - now)

    # print_node(root)
    print find_all(root, 1, 3)
