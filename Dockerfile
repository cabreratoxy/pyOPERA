FROM python:3.9.15-slim
ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . .
RUN tar -xvf libOPERA2.9_Py.tar.gz
RUN apt-get update && apt-get install zip unzip libxtst6 libxt6 default-jre -y
RUN libOPERA2_Py/OPERA2.9_Py_mcr.install -agreeToLicense yes -mode silent

WORKDIR /usr/local/bin/OPERA/application
RUN python setup.py install
ENV XAPPLRESDIR /usr/local/MATLAB/MATLAB_Runtime/v912/X11/app-defaults
ENV LD_LIBRARY_PATH /usr/local/MATLAB/MATLAB_Runtime/v912/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v912/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v912/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v912/sys/opengl/lib/glnxa64
