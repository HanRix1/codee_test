FROM python:3.12.2

RUN apt-get update -y && apt-get install -y mime-support
ENV PYTHONPATH=$PYTHONPATH:/app/src 
   
WORKDIR /app

RUN pip install pdm
COPY ./pyproject.toml ./pdm.lock ./
RUN pdm export --prod -f requirements -o requirements.txt
RUN pip install --no-cache-dir -r requirements.txt --user --no-dependencies

COPY ./src ./src
COPY alembic.ini ./
COPY main.py ./

CMD ["python", "main.py"]
