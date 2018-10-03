def push(x):
    mas.append(x)
    if len(arr) ==0 or arr[-1] <x:
        arr.append(x)
    else:
        arr.append(arr[-1])
    print('Added successfully.', mas)

def pop():
    if len(arr) == 0:
        print('Nothing to remove')
    else:
        arr.pop()
        mas.pop()
        print('Removed successfully.', mas)
    
def get_max():
    if len(arr) == 0:
        print('Stack is empty')
    else:
        print('Maximum:', arr[-1])
    
if __name__ == '__main__':
    mas = []
    arr = []
    cmd = input()
    while cmd != 'exit':
        if cmd == 'push':
            x = int(input())
            push(x)
        elif cmd == 'pop':
            pop()
        elif cmd == 'get_max':
            get_max()
        else:
            print('Command not found')
        cmd = input()
    print('Goodbye')
