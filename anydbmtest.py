import anydbm
db = anydbm.open('captions.db','c')
db['cleese.png'] = 'Photo of John Cleese.'
print db['cleese.png']
for key in db:
    print key
db.close()
