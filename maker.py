import sys
import os

filename = sys.argv[1]
try:
    cssFormat = sys.argv[2]
except:
    cssFormat = 'css'

cwd = os.getcwd()
path = cwd + '/src/components/' + filename

os.mkdir(path)


with open(path + '/' + filename + '.component.jsx', 'w') as fp:
    pass

with open(path + '/' + filename + '.styles.' + cssFormat, 'w') as fp:
    pass

