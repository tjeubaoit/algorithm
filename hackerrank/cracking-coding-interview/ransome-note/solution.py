def ransom_note(magazine, ransom):
    m = dict()
    r = dict()
    for word in magazine:
        m[word] = m[word] + 1 if m.get(word) else 1
    for word in ransom:
        r[word] = r[word] + 1 if r.get(word) else 1
    for word in r:
        expected = r[word]
        if not m.get(word) or m[word] < expected:
            return False
    return True

m, n = map(int, raw_input().strip().split(' '))
magazine = raw_input().strip().split(' ')
ransom = raw_input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print "Yes"
else:
    print "No"