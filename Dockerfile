FROM python:3.10-slim

WORKDIR /
COPY requirements.txt /requirements.txt
RUN pip install -r requirements.txt

# Add the model download script
COPY download_model.py /

# Download the model during build
RUN python3 /download_model.py

COPY rp_handler.py /

# Start the container
CMD ["python3", "-u", "rp_handler.py"]