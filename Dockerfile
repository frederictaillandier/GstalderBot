FROM ubuntu:22.04

RUN apt update && apt install --no-install-recommends -y \
    python3 \
    python3-pip
RUN pip3 install \
    requests \
    dateutils \
    openai

WORKDIR /home/gstaldergeist
COPY ./srcs ./srcs
CMD python3 ./srcs/main.py
