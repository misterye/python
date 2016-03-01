import os
cmd = 'ls -l'
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print stat

filename = 'book.tex'
cmd = 'md5sum ' + filename
fp = os.popen(cmd)
res = fp.read()
stat = fp.close()
print res
print stat
