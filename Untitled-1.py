def verbing(s):
    if len(s) >= 3:
        if s.endswith('ing'):
            return s + 'ly'
        else:
            return s + 'ing'
    return s
def not_bad(s):
    not_index = s.find('not')
    bad_index = s.find('bad')
    
    if not_index != -1 and bad_index != -1 and bad_index > not_index:
        return s[:not_index] + 'good' + s[bad_index + 3:]
    return s
def front_back(a, b):
    def split_string(s):
        mid = (len(s) + 1) // 2  # This ensures the front half gets the extra character if the length is odd
        return s[:mid], s[mid:]

    a_front, a_back = split_string(a)
    b_front, b_back = split_string(b)
    
    return a_front + b_front + a_back + b_back
def main():
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')
    
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This dinner is not so bad!'), 'This dinner is not so bad!')
    test(not_bad('This is bad but not terrible.'), 'This is bad but not terrible.')
    
    test(front_back('abcd', 'xy'), 'abcyxd')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('kitten', 'donut'), 'kitdontenut')

def test(output, expected):
    if output == expected:
        print('OK')
    else:
        print(f'X: got {output}, expected {expected}')

if __name__ == '__main__':
    main()
git add string2.py
git commit -m "Completed the string2.py exercises"
git push origin main
