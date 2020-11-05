
FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y \
  gcc
  
RUN git clone https://github.com/2133649586/Coronavirus-Tracker

RUN conda install -c conda-forge yarn

RUN cd covid19-tracker && yarn install

RUN pip install pandas

RUN pip install bokeh

WORKDIR Coronavirus-Tracker

CMD ["bokeh", "serve", "--show", "resulting.py"]
