FROM ubuntu:20.04

RUN apt-get -y update && \
    apt-get -y install wget

# INSTALL MINICONDA -------------------------------
ARG CONDA_DIR=/home/coder/local/bin/conda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh
RUN bash Miniconda3-latest-Linux-x86_64.sh -b -p $CONDA_DIR
RUN rm -f Miniconda3-latest-Linux-x86_64.sh

# Install mamba (speed up packages install with conda)
# Must be in base conda env
ENV PATH="/home/coder/local/bin/conda/bin:${PATH}"
RUN conda install mamba -n base -c conda-forge

# Install env requirements
COPY environment.yml .
RUN conda create -n monenv python=3.10
RUN mamba env update -n monenv -f environment.yml

# Make monenv env activated by default in shells
ENV PATH="$CONDA_DIR/envs/monenv/bin:${PATH}"
RUN echo "export PATH=$PATH" >> /home/coder/.bashrc  # Temporary fix while PATH gets overwritten by code-server

ADD main.py /
ADD config.yaml /
COPY src src/

EXPOSE 5000
CMD [ "python", "main.py"]