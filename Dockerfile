# Select the base image
FROM python:3.11

# # Update the packages and install the necessary dependencies
# RUN apt-get update && \
#     apt-get install -y git build-essential autoconf automake libtool pkg-config libpng-dev libjpeg-dev libtiff-dev zlib1g-dev libleptonica-dev libicu-dev libcairo-dev libpango1.0-dev libjpeg62-turbo-dev libtiff5-dev libicu-dev libcairo2-dev libpango-1.0-0 libicu-dev
#
# # Clone the Tesseract OCR repository
# RUN git clone https://github.com/tesseract-ocr/tesseract.git && \
#     cd tesseract && \
#     ./autogen.sh && \
#     ./configure && \
#     make && \
#     make install && \
#     ldconfig && \
#     make training && \
#     make training-install

# Set the working directory
WORKDIR /app

# Copy the application files into the container
COPY . .

# Update pip
RUN pip install --upgrade pip

# Install any necessary dependencies
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000