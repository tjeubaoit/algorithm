class File:
 
    def __init__(self, name, parent=None, length=0):
        self.name = name
        self.length = length
        self.parent = parent
        self.childs = []

    def __repr__(self):
        return self.name
 
 
def find_longest_file(s):
    begin = 0
    index = 0
    current_dir = None
 
    max_len = 0
    max_path_file = None
 
    while index != -1:
        index = s.find('/', begin)
        name = s[begin:index] if index != -1 else s[begin:]
        begin = index + 1
 
        if name == '.':
            if not current_dir.childs: current_dir = current_dir.parent
            continue
        elif name == '..':
            tmp = current_dir
            current_dir = current_dir.parent
            if not tmp.childs: current_dir = current_dir.parent
            continue
 
        length = (current_dir.length if current_dir else 0) + len(name)
        file = File(name, parent=current_dir, length=length)

        if current_dir:
            current_dir.childs.append(file)
 
        if '.' not in name: # if is folder                  
            current_dir = file
            # print current_dir
        else:
            if max_len <= length:
                max_len = length
                max_path_file = file
 
    return max_path_file
 

def find_longest_path(file):
    if not file: return 0

    path = ''
    while file is not None:
        path = file.name + '/' + path
        file = file.parent
 
    return path[:-1]
 
 
# file = find_longest_file('root/subdir1/file1.ext/./subsubdir1/../subdir2/subsubdir2/file2.ext/./file3.txt')
# print find_longest_path(file)
 
print find_longest_path(find_longest_file(raw_input()))