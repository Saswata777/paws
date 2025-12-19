FROM ubuntu:latest
LABEL authors="mitra"

ENTRYPOINT ["top", "-b"]