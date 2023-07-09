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

    
    if ext== "":
        continue

>>>>>>> 5d6e0dc9d421244f71ad192ddf0a397f0dfd9753
        
    if os.path.exists( a + '/' + ext ):
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
        
    else:
        os.makedirs( a + '/' + ext )
<<<<<<< HEAD
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )
=======

        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )

        shutil.move( a + '/' + i, a + '/' + ext + '/' + i )

>>>>>>> 5d6e0dc9d421244f71ad192ddf0a397f0dfd9753
