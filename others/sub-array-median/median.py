import math

def count_median(arr, i, j, n, orders):
    size = j + 1 - i
    med_pos = math.ceil(size/2)
    is_odd = size % 2 != 0
    # print(med_pos)
    for k in range(0, n):
        if orders[k] == med_pos:
            break
    if is_odd:
        return k
    else:
        k2 = k
        while k2 < n:
            k2 += 1
            if orders[k2] != orders[k]:
                break
        return (k+k2)/2


def sub_array_median(arr, n):
    for i in range(0, len(arr)):
        orders = [0] * n
        sub_arr = []
        for j in range(i, len(arr)):
            sub_arr.append(arr[j])
            for k in range(arr[j], n):
                orders[k] += 1
            # print('orders', orders)
            med = count_median(arr, i, j, n, orders)
            print(sub_arr, med)


def main():
    sub_array_median([1, 4, 1, 2, 7, 5, 2], 10)
    # arr = [1, 4, 1, 2, 7, 5, 2]
    # orders = [0, 2, 4, 4, 5, 6, 6, 7, 7, 7]
    # count_median(arr, 0, 7, 10, orders)


if __name__ == '__main__':
    main()
