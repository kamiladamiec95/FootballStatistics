# # pobranie obrazu Pythona z DockerHub
# FROM python:latest
# # wyznaczenie working directory w kontenerze
# RUN apt-get update \
#     && apt-get install -y unixodbc unixodbc-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app
# # skopiowanie zawartości pliku requirements.txt do working directory
# COPY ./requirements.txt .
# # instalacja dependencji
# RUN pip install -r requirements.txt
# # skopiowanie zawartości katalogu src/ do working directory
# COPY ./src/ /app
# # komendy do uruchomienia aplikacji
# CMD ["python", "./main.py"]


# FROM python:latest

# RUN apt-get update \
#     && apt-get install -y unixodbc unixodbc-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# WORKDIR /app

# COPY ./requirements.txt .

# RUN pip install -r requirements.txt

# COPY ./src/ /app

# CMD ["python", "./main.py"]

# pobranie obrazu Pythona z DockerHub
FROM python:latest

# ??????
RUN apt-get update \
    && apt-get install -y unixodbc unixodbc-dev \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# wyznaczenie working directory w kontenerze
WORKDIR /app
# skopiowanie zawartości pliku requirements.txt do working directory
COPY ./requirements.txt .
# instalacja dependencji
RUN pip install -r requirements.txt
# skopiowanie zawartości katalogu src/ do working directory
COPY ./src/ /app
# komendy do uruchomienia aplikacji
CMD ["python", "./main.py"]

#docker run -ti test123