# # # pobranie obrazu Pythona z DockerHub
# # FROM python:latest
# # # wyznaczenie working directory w kontenerze
# # RUN apt-get update \
# #     && apt-get install -y unixodbc unixodbc-dev \
# #     && apt-get clean \
# #     && rm -rf /var/lib/apt/lists/*

# # WORKDIR /app
# # # skopiowanie zawartości pliku requirements.txt do working directory
# # COPY ./requirements.txt .
# # # instalacja dependencji
# # RUN pip install -r requirements.txt
# # # skopiowanie zawartości katalogu src/ do working directory
# # COPY ./src/ /app
# # # komendy do uruchomienia aplikacji
# # CMD ["python", "./main.py"]


# # FROM python:latest

# # RUN apt-get update \
# #     && apt-get install -y unixodbc unixodbc-dev \
# #     && apt-get clean \
# #     && rm -rf /var/lib/apt/lists/*

# # WORKDIR /app

# # COPY ./requirements.txt .

# # RUN pip install -r requirements.txt

# # COPY ./src/ /app

# # CMD ["python", "./main.py"]

# # pobranie obrazu Pythona z DockerHub
# FROM python:latest

# # ??????
# RUN apt-get update \
#     && apt-get install -y unixodbc unixodbc-dev \
#     && apt-get clean \
#     && rm -rf /var/lib/apt/lists/*

# # wyznaczenie working directory w kontenerze
# WORKDIR /app
# # skopiowanie zawartości pliku requirements.txt do working directory
# COPY ./requirements.txt .
# # instalacja dependencji
# RUN pip install -r requirements.txt
# # skopiowanie zawartości katalogu src/ do working directory
# COPY ./src/ /app
# # komendy do uruchomienia aplikacji
# CMD ["python", "./main.py"]

# #docker run -ti test123

# #docker run -v "$(pwd)/data:/app/data" test123
#docker exec -it 4dfd051ec013 /bin/bash

# ///////////////////////////////////////////////////////

# FROM apache/airflow:2.9.0-python3.8
# ENV PIP_USER=false
# #python venv setup
# RUN python3 -m venv /opt/airflow/venv1
# COPY requirements.txt /requirements.txt
# RUN pip install --upgrade pip
# RUN pip install --no-cache-dir -r /requirements.txt


# RUN pip install --user --upgrade pip
# RUN pip install --no-cache-dir --user -r /requirements.txt



FROM apache/airflow:2.9.0
COPY requirements.txt .
RUN pip install setuptools wheel
# RUN pip install manager
RUN pip install --upgrade setuptools
RUN python -m pip install pandas
RUN pip install -r requirements.txt