# The demo of NEMO output

The nemo output is implemented using python with [SQLObject](http://sqlobject.org/) with sqlite.
This is also an especially small demo, with the dimensions reduced to 1/512 of the proposed original.

###### Requirement
```python
python 3.5 or higher
SQLObject
numpy
tqdm
scipy
```

### THE SQLITE VERSION

###### How to run
Simply run ```python sqltest.py``` to generate a sqlite database at the same folder named ```reduced.db```.

In order to change the size/estimation, change the settings inside the ```sqltest.py``` file.


###### Time and space constraint

It takes 3 hours using the default settings. Using the default settings it should not take more than a few mb.
For even larger settings, without any connections the database itself is only 2mb in size.
However, processing time is a big problem, and it is hard to do any concurrency using sqlite in general. 
With 62500 streamlines, it takes ~ 1hr to generate all streamlines. It also takes much more time to add voxels to streamline using a larger settings.

###### TODO
Find some method to mass generating relations between Voxels and Streamlines.

Write code for detecting disconnection.


### THE SCIPY SPARSE MATRIX VERSION
###### How to run
Simply run ```python sparsetest.py``` to generate two sparse matrices at the same folder named ```WM_ST.npz and ST_GM.npz```.

In order to change the size/estimation, change the settings inside the ```sparsetest.py``` file.

###### Time and space constraint
The bigger matrix takes 63mB in a downscaled version. It might takes up to 190Gb in the full version.
It takes 105 hours to generate the full version. The small version takes less than 10 minutes.