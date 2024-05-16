FROM ubuntu:latest

RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev \
    python3-venv

COPY . .

RUN python3 -m venv venv
ENV PATH="/venv/bin:$PATH"

RUN . venv/bin/activate && pip install -r requirements.txt

CMD ["python3", "bot.py"]
