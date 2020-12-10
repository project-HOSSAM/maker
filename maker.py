import sys
import os

filename = sys.argv[1]
cwd = os.getcwd()
path = cwd + '/src/components/' + filename

os.mkdir(path)


with open(path + '/' + filename + '.component.jsx', 'w') as fp:
    pass

with open(path + '/' + filename + '.styles.css', 'w') as fp:
    pass
