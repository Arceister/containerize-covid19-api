# Containerized Covid19 API App

## Tech stack:
- Python as main Programming Language
- FastAPI as Web Framework
- Docker as Container

## How to run without Docker:
1) Clone this Repo.
2) Run `pip install -r requirements.txt` (Make sure you've pip installed).
3) Run `uvicorn main:app --reload`.

## How to run with Docker:
1) Clone this Repo.
2) Run `docker build -t <your desired name> .` to build the docker image.
3) Make sure the image is succesfully built. Run `docker images` and see if the image is already built.
4) After that, run `docker run -d --name container -p <your desired port>:8085 covidapi`.
5) Open your `localhost:<the port>` to see the magic!