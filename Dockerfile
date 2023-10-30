# Set base image (host OS)
FROM python:3.7


# By default, listen on port 5000
EXPOSE 5000/tcp

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY requirements.txt .

# Move the files from your host machine to docker image 
ADD ./MLPipeline ./MLPipeline
ADD ./Input ./Input
ADD ./Output ./Output

# Install any dependencies
RUN /usr/local/bin/python -m pip install --upgrade pip
RUN pip install -r /app/requirements.txt


# Copy the content of the local src directory to the working directory
COPY app.py .

# Specify the command to run on container start
CMD [ "python", "./app.py" ]