FROM python:3.11.3

# Get curl for health checks
RUN apk update && apk upgrade && apk add --no-cache curl
# RUN apk add make automake gcc g++ subversion python3-dev

# Permissions and nonroot user for tightened security
RUN adduser -D nonroot
RUN mkdir /app/ && chown -R nonroot:nonroot /app
RUN mkdir -p /var/log/flask-app && touch /var/log/flask-app/flask-app.err.log && touch /var/log/flask-app/flask-app.out.log
RUN chown -R nonroot:nonroot /var/log/flask-app
WORKDIR /app
USER nonroot

# Copy all the files to the container
COPY --chown=nonroot:nonroot . .

# venv
ENV VIRTUAL_ENV=/app/venv

# Python setup
RUN python -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN export FLASK_APP=app.py

# Update pip
RUN pip install --upgrade pip

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

# Define the port number the container should expose
EXPOSE 5000

CMD ["python", "app.py"]