def is_balanced(s):
    stack = []
    br_dict = {
        '[': ']',
        '{': '}',
        '(': ')'
    }
    for i in s:
        if i in br_dict.keys():
            stack.append(i)
        else:
            if len(stack) == 0 or br_dict[stack.pop()] != i:
                return 'NO'
    return 'YES' if len(stack) == 0 else 'NO'


def main():
    s = '([{}}{}{}])'
    print s
    print '{}'.format(is_balanced(s))


if __name__ == '__main__':
    main()
