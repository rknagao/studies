print('Example 1: name and main')
print('executing main.py')

if __name__ == '__main__':
    print('I am main.')

from not_main import not_main
not_main()

print('ending main.py')