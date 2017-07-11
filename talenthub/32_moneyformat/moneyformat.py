# Ju is unit for 10, 1 Ju Dlog is 10 Dlog. 
# Hu is unit for 100, 1 Hu Dlog is 100 Dlog 
# Tu is unit for 1000, 1 Tu Dlog is 1000 Dlog 
# Mu is unit for 10000, 1 Mu Dlog is 10000 Dlog 
# Pu is unit for 100000, 1 Pu Dlog is 100000 Dlog 
# Bu is unit for 10000000000, 1 Bu Dlog is 10000000000 Dlog

format = {
    'Ju': '0',
    'Hu': '00',
    'Tu': '000',
    'Mu': '0000',
    'Pu': '00000',
    'Bu': '0000000000',
    'Dlog': ''
}

def add_money_format(input):
    return ''.join([format[unit] for unit in input])

def add_string_number(s1, s2):
    l1 = len(s1)
    l2 = len(s2)
    n = max(l1, l2)
    m = min(l1, l2)
    a = list(s1) if l1 > l2 else list(s2)

    k = 0
    for i in xrange(n):
        if i < m: t = int(s1[l1-i-1]) + int(s2[l2-i-1]) + k
        else: t = int(a[n-i-1]) + k
        if t >= 10:
            k = 1
            t = t - 10
        else: k = 0
        a[n-i-1] = str(t)
        if i >= m and k == 0: break

    ret = ''.join(a)
    if k > 0: ret = str(k) + ret

    return ret

def money_format(data):
    input = data.split(' ')
    ret = '0'
    n = '1'
    units = []
    for e in input:
        if e.isdigit():
            if units:
                ret = add_string_number(ret, n + add_money_format(units))
                del units[:]
            n = e
        else:
            units.append(e)
    if units:
        ret = add_string_number(ret, n + add_money_format(units))

    ret = ret[:-2] + '.' + ret[-2:]
    if len(ret) < 4: ret = '0' + ret

    return ret


# print money_format(raw_input().rstrip())


print add_string_number('99', '99')
print add_money_format(('Ju', 'Pu', 'Dlog'))
print money_format('2 Ju Pu Dlog')
print money_format('7 Dlog 2 Hu')
print money_format('2 Ju 7 Dlog')
print money_format('2 Ju Pu Dlog')
print money_format('2 Pu 1 Mu 7 Tu 5 Hu 7 Ju 7 Dlog')

# import random
# for i in xrange(0, 100000):
#     u = 234552
#     v = 943989
#     a = random.randint(u, v)
#     b = random.randint(u, v) * 1000
#     c = a + b
#     s = add_string_number(str(a), str(b))
#     if s != str(c):
#         print a, b
#         break
#     else:
#         print 'ok', a, b






