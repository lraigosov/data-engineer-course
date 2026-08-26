FROM python:3.11-slim

WORKDIR /workspace

ARG PIP_TRUSTED_HOST=""

RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    git \
    && rm -rf /var/lib/apt/lists/*

COPY requirements requirements
COPY locks/docker-py3.11.txt locks/docker-py3.11.txt
RUN trusted_hosts="$(printf '%s' "$PIP_TRUSTED_HOST" | tr ',' ' ')" \
    && PIP_TRUSTED_HOST="$trusted_hosts" pip install --no-cache-dir --upgrade pip \
    && PIP_TRUSTED_HOST="$trusted_hosts" pip install --no-cache-dir -r locks/docker-py3.11.txt

COPY . .

EXPOSE 8888

CMD ["jupyter", "lab", "--ip=0.0.0.0", "--port=8888", "--no-browser", "--allow-root"]
