FROM python:3.9-bullseye

# get portaudio and ffmpeg
RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libasound-dev libsndfile1-dev -y
RUN apt-get -y update
RUN apt-get -y upgrade
RUN apt-get install -y ffmpeg

WORKDIR /code
COPY ./pyproject.toml /code/pyproject.toml
COPY ./poetry.lock /code/poetry.lock
RUN pip install --no-cache-dir --upgrade poetry
RUN pip install httpx
RUN poetry config virtualenvs.create false
RUN poetry install --no-dev --no-interaction --no-ansi
COPY main.py /code/main.py
COPY speller_agent.py /code/speller_agent.py
COPY memory_config.py /code/memory_config.py
COPY events_manager.py /code/events_manager.py
COPY config.py /code/config.py
COPY instructions.txt /code/instructions.txt
RUN mkdir -p /code/call_transcripts
RUN mkdir -p /code/db

# Copy the utils directory (and its contents) into the container
COPY ./utils /code/utils

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "3000"]