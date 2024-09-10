FROM python:slim

RUN pip install uv

WORKDIR /code
COPY requirements.lock /code/.
RUN uv pip install --no-cache --system -r requirements.lock

COPY app /code/app
CMD ["fastapi", "run", "--port", "80"]
