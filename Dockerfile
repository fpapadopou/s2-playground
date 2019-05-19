FROM python:3.7

# Update & install deps
RUN apt-get update && apt-get install -y \
    libgflags-dev libgoogle-glog-dev libgtest-dev libssl-dev \
    swig cmake

# Clone official s2geometry
RUN mkdir -p /opt/s2geometry
WORKDIR /opt/s2geometry
RUN git clone https://github.com/google/s2geometry.git .

# Build Python s2geometry port
RUN mkdir build && \
    cd build && \
    cmake -DCMAKE_INSTALL_PREFIX:PATH=/usr  .. && \
    make && \
    make install

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

# Install the app
COPY . .
RUN pip install -r requirements.txt

# Make s2geometry Python port path accessible
ENV PYTHONPATH=$PYTHONPATH:/usr/lib/python3.7/site-packages

ENTRYPOINT ["./entrypoint.sh"]