import os
cwp = os.getcwd()
if __name__ == '__main__':
    print cwp 
os.path.abspath('memo.txt')
os.path.exists('memo.txt')
os.path.isdir('memo.txt')
os.listdir(cwp)

def walk(dirname):
    for name in os.listdir(dirname):
        path = os.path.join(dirname, name)
        if os.path.isfile(path):
            print path
        else:
            walk(path)
