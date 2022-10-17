FROM python:3.10

# Create a working directory, here we will deploy store application
WORKDIR /code

# Copy the requirments to working directory
COPY ./requirements.txt /code/requirements.txt

# Install packages
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copy application code to working directory
COPY ./app /code/app

# Start application
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
