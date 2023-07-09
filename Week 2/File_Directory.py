import os
import shutil

a = input( 'Enter folder name: ' )

li = os.listdir(a)

for i in li:
    fileName, ext = os.path.splitext(i)

    ext = ext[1:]
    
    if ext == "":
        continue
        
    if os.path.exists( a + '/' + ext ):
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
        
    else:
        os.makedirs( a + '/' + ext )
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )