FROM python:3.9-slim


WORKDIR /app
ENV DEFAULT_PORT=8000



COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy local code to the container image.
COPY . ./


CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT:-$DEFAULT_PORT}"] 
