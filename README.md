# s2-playground
Convert polygons to S2 cells &amp; vice versa.

## Running the app locally

First off, install requirements:

`pip install -r requirements.txt`

The `Flask` application can be started with

`FLASK_APP=service.py flask run`

This will just run the development server.

Another option is to use `uWSGI`'s HTTP server mode. A sample command
has been added to `entrypoint.sh` bash script. 

Running `./entrypoint.sh dev` will run the uWSGI HTTP server with hot-reload 
option enabled, so all changes applied to the codebase will trigger a server restart.

## Running containerized app

`docker build -t s2playground .`

`docker run --rm -p 8080:80 s2playground`

Head over to `127.0.0.1:8080` and enjoy.

## Installing Python port of S2Geometry

The following commands will work on Mac OS  Mojave 10.14 with PyCharm IDE & its Python 3.7 `venv`.

Install deps

`brew install swig gflags glog openssl`

Clone repo in venv directory

`cd venv && git clone git@github.com:google/s2geometry.git && cd s2geometry`


Download & unzip googletest suite

`wget https://github.com/google/googletest/archive/release-1.8.0.zip && unzip release-1.8.0.zip`

Create `build` directory

`mkdir build && cd build`

Configure cmake

`cmake -DCMAKE_INSTALL_PREFIX:PATH=/path/to/pycharm/venv -DOPENSSL_ROOT_DIR=/usr/local/Cellar/openssl/1.0.2q -DOPENSSL_LIBRARIES=/usr/local/Cellar/openssl/1.0.2q/lib -DGTEST_ROOT=./googletest-release-1.8.0/googletest  ..`

Build & install the S2 Python library (available as pywraps2)

`make && make install`