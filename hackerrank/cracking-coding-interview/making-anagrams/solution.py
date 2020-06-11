def number_needed(w1, w2):
    total = 0
    for letter in "abcdefghijklmnopqrstuvwxyz":
        total += abs(w1.count(letter) - w2.count(letter))
    return total


print(number_needed('cde', 'abc'))
