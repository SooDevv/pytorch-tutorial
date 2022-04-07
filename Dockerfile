FROM pytorch/torchserve:latest-gpu

RUN python --version
RUN pip --version

USER root

RUN apt-get update 
RUN pip install --upgrade pip


RUN pip install --no-cache-dir transformers
RUN pip install --no-cache-dir seqeval
RUN pip install --no-cache-dir seaborn
