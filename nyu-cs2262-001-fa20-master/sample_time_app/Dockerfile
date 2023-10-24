FROM python:3.5

RUN apt-get update \
  && apt-get clean \
  && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*



# Set up a working folder and install the pre-reqs
WORKDIR /app

RUN pip install Flask


COPY --chown=nyu:nyu . .

CMD [ "python", "./run.py" ]
