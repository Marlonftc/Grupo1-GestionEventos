FROM python:3.13.1-slim
WORKDIR /usr/src/app
RUN apt-get update && apt-get install -y curl
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .  
CMD ["flask","--debug", "run", "--host=0.0.0.0"]

