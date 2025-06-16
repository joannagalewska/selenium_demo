FROM python:3.11-slim

WORKDIR /app

# Copy everything
COPY . /app

# Install dependencies
RUN pip install -r requirements.txt

# run pytest
CMD ["pytest"]
