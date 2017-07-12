def is_matched(expression):
    size = len(expression)
    if size % 2 != 0: 
        return False
    
    st = []    
    for i in xrange(0, size):
        c = expression[i]        
        if c == '{':
            st.append('}')
        elif c == '[':
            st.append(']'):
        elif c == '(':
            st.append(')')            
        else:
            if not st or st.pop() != c:
                return False            
            
    return len(st) == 0


def is_pair_matched(first, second):
    if first == '{' and second == '}':
        return True
    if first == '[' and second == ']':
        return True
    if first == '(' and second == ')':
        return True


def main():
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))

    # open output file
    output = []
    with open(dir_path + '/data4.out') as my_file:
        for line in my_file:
            output.append(line.strip())

    # process from input file
    first = True
    count = -1
    with open(dir_path + '/data4.in') as my_file:
        for line in my_file:
            if first:
                first = False
                continue
            line = line.strip()
            count += 1
            if not line: 
                continue            

            if is_matched(line):
                if output[count] != 'YES':
                    print 'Wrong test case', line, 'expected NO but received YES'
                    return False
                else:
                    print "YES"
            else:
                if output[count] != 'NO':
                    print 'Wrong test case', line, 'expected YES but received NO'
                    return False
                else:
                    print "NO"
    return True

if main():
    print 'All test cases correct'
