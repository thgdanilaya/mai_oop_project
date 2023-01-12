FROM continuumio/miniconda3


# Create the environment:

SHELL ["/bin/bash", "--login", "-c"]
COPY ./environment.yml /environment.yml
RUN conda env create -f environment.yml
RUN conda init bash

RUN apt update && \
    apt install --no-install-recommends -y build-essential gcc && \
    apt clean && rm -rf /var/lib/apt/lists/*

RUN conda activate musika
RUN conda install -c conda-forge cudatoolkit=11.2 cudnn=8.1.0




FROM python:3.9
COPY ./requirements.txt ./requirements.txt
COPY . /src/
RUN pip install -r ./requirements.txt

RUN apt-get update && apt-get install -y libsndfile1-dev

ENTRYPOINT ["python", "./src/musika_generate.py","--num_samples", "1", "--seconds", "120","--save_path", "./src/generations"]