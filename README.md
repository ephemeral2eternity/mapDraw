# mapDraw
Draw server and client geographical locations on a region/world map

## Dependencies and Prerequisites.
* Installing the SciPy Stack that includes matplotlib and numpy
```
sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose
```
* Installing GEOS following this [link](http://trac.osgeo.org/geos/wiki/BuildingOnUnixWithAutotools). Simple steps are as follows.
  * Download the GEOS source code from this [link](http://download.osgeo.org/geos/geos-3.4.2.tar.bz2)
  * Decompress the file `tar xvf geos-3.4.2.tar.bz2`
  * Configure, make and Install
  ```
  sudo ./configure
  sudo make
  sudo make install
  ```

