FROM ubuntu:20.04

RUN apt-get -y update && \
    apt-get -y install wget

# Install Miniconda
RUN wget https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh && \
    bash Miniconda3-latest-Linux-x86_64.sh && \
    rm -f Miniconda3-latest-Linux-x86_64.sh

# Define working directory in the Docker image
WORKDIR /app

# Copy project files in the Docker image
COPY . /app

# Create conda env
RUN conda create -f environment.yml

# Make Python interpreter from the conda env available
ENV PATH="~/miniconda/envs/monenv/bin:${PATH}"

# Make container listen on port 5000
EXPOSE 5000

CMD [ "python", "main.py"]
