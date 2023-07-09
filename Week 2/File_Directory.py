import os
import shutil

a = input( 'Enter folder name: ' )

li = os.listdir(a)

for i in li:
    fileName, ext = os.path.splitext(i)

    ext = ext[1:]
<<<<<<< HEAD
    
    if ext== "":
        continue
=======
    
    
>>>>>>> b314723b9f8325eede3f443859808951c1839447
        
    if os.path.exists( a + '/' + ext ):
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
        
    else:
        os.makedirs( a + '/' + ext )
<<<<<<< HEAD
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
=======
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
>>>>>>> b314723b9f8325eede3f443859808951c1839447
