FROM python:3.10-slim as base
# NOTE: When using COPY, the build context is the root directory.
FROM base as builder
RUN mkdir /install
WORKDIR /install
COPY requirements.txt .
RUN apt update && apt-get install --yes --no-install-recommends \
    gcc g++ libffi-dev \
    && pip install --upgrade pip && pip install --prefix="/install" -r requirements.txt \
    && apt-get autoremove --yes gcc g++ libffi-dev \
    && rm -rf /var/lib/apt/lists/* 
FROM base
COPY --from=builder /install /usr/local
COPY . /app
WORKDIR /app
ENTRYPOINT [ "sh", "entrypoint.sh" ]