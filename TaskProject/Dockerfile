
# Define the base image
FROM python:3.10-bullseye

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory within the container
WORKDIR /code

# Copy your project code into the container
COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . .

#EXPOSE 8000

#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]