FROM python:3.9.15-slim
ENV PYTHONUNBUFFERED True

WORKDIR /app
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
VOLUME /app

COPY . .
RUN apt-get update && apt-get install zip unzip libxtst6 libxt6 default-jre wget curl make git -y
RUN curl -sSL https://install.python-poetry.org | python3 -
ENV PATH="${PATH}:/root/.local/share/pypoetry/venv/bin"
RUN wget -O /tmp/libOPERA2.9_Py.tar.gz https://github.com/NIEHS/OPERA/releases/download/v2.9.1/libOPERA2.9_Py.tar.gz
RUN ls

# RUN chmod 777 libOPERA2.9_Py.tar.gz
RUN tar -xvf /tmp/libOPERA2.9_Py.tar.gz
RUN /tmp/libOPERA2_Py/OPERA2.9_Py_mcr.install -agreeToLicense yes -mode silent

WORKDIR /usr/local/bin/OPERA/application
RUN python setup.py install
RUN mv libOPERA_Py /app/libOPERA_Py
ENV XAPPLRESDIR /usr/local/MATLAB/MATLAB_Runtime/v912/X11/app-defaults
ENV LD_LIBRARY_PATH /usr/local/MATLAB/MATLAB_Runtime/v912/runtime/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v912/bin/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v912/sys/os/glnxa64:/usr/local/MATLAB/MATLAB_Runtime/v912/sys/opengl/lib/glnxa64
WORKDIR /app
