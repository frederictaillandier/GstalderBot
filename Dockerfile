FROM ubuntu:22.04

RUN apt update && apt install --no-install-recommends -y \
    python3 \
    python3-pip
RUN pip3 install \
    requests \
    dateutils

RUN useradd -ms /bin/bash gstaldergeist
USER gstaldergeist

WORKDIR /home/gstaldergeist
COPY ./srcs ./srcs
COPY ./main.py ./main.py
CMD python3 ./main.py
