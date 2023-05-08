FROM python:3.11.3-alpine3.17

# Upgrade pip
RUN pip install --upgrade pip

# Get curl for health checks
RUN apk update && apk upgrade && apk add --no-cache curl

# Permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /home/app/ && chown -R nonroot:nonroot /home/app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /home/app
USER nonroot

# Copy all the files to the container
COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/home/app/venv

# Python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py
RUN pip install Flask
RUN pip install gunicorn

# Define the port number the container should expose
EXPOSE 5000

CMD ["python", "app.py"]