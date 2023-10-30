LightSail Deployment

AWS CLI Installation link :
https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html

LIGHTSAIL CLI Installation Link:
https://lightsail.aws.amazon.com/ls/docs/en_us/articles/amazon-lightsail-install-software

DOCKER Installation Link:
https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-18-04


Install Docker > AWS CLI > LIGHTCTL. Follow the order of installation and start the deployment

Step 1: 
Create a docker file with 5000 port exposed

Step 2:
```docker build -t flask-container .```

Step 3: 
```docker run -p 5000:5000 flask-container```
* check if the container is running or not

Step 4:
```aws lightsail create-container-service --service-name flask-service --power small --scale 1```
The output of the above command has the following
"state": "PENDING",
when the state becomes "Active" perform next step

Step 5:
```aws lightsail push-container-image --service-name flask-service --label flask-container --image flask-container```

At the ouput of this command there will the following line 
Refer to this image as ":flask-service.flask-container.X" in deployments.

in which X will be number from 1 to 10, take that number and attach it in the containers json.

Step 6:
Create a new file, containers.json. 

{
    "flask": {
        "image": ":flask-service.flask-container.X",  # replace this X from Step 5 Out
        "ports": {
            "5000": "HTTP"
        }
    }
}

Step 7:
Create a new file, public-endpoint.json. 
{
    "containerName": "flask",
    "containerPort": 5000
}

Step 8:
```aws lightsail create-container-service-deployment --service-name flask-service --containers file://containers.json --public-endpoint file://public-endpoint.json```


After some time run the following command
```aws lightsail get-container-services --service-name flask-service```

in the ouput if the state is running then the model is deployed
```"state": "RUNNING"```,

Step 9:
Cleanup
```aws lightsail delete-container-service --service-name flask-service```

Putty Installation Link
* https://www.putty.org/