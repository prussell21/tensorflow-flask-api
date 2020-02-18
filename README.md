## Deploy TensorFlow Models with Flask API & Docker Containers

Data Science Multi Docker Container Workflow:

  1: Tensorflow Notebook - https://hub.docker.com/r/jupyter/tensorflow-notebook
  
  2: Flask API container - DockerFile
  
Quickly build and test new ML models within the TensorFlow Notebook container, then save .h5 models locally to deploy with a Flask API container.


### Setup

Install Docker: https://docs.docker.com/install/

Utilize Jupyter's Docker images to quickly spin up powerful TensorFlow dev environments

```
#pull image from dockerhub
$ docker pull jupyter/tensorflow-notebook

#set "PWD" to current working directory for volume mounting
$ docker run --rm -p 8888:8888 -e JUPYTER_ENABLE_LAB=yes -v "PWD":/home/jovyan/work jupyter/tensorflow-notebook
```
You can mount any local directory by replacing "PWD". This allows your container files to persist.


### In the Jupyter Notebook - Build, train and save TensorFlow models

```python
#Save model locally to be used in Flask container
model.save('mnist_model.h5')
```

### Build Flask API container with Dockerfile

```
#Build image from Dockerfile in current directory
$ docker build ml_app .

$ docker run -p 5000:5000 ml_app
```

### Test the API

If testing the API within the TensorFlow Notebook container you'll need to find the flask app ip address

```
$ docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <docker container name or id>
```


```python
url = 'http://'+flask_app_ip+':5000/api/'

params = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8'}
img = img_to_predict # img = array.shape(784,1)
data = {'params': params, 'arr': img.tolist()}

response = requests.post(url, json=data)

response.text
```

### All in all
Spin up powerful tensorflow environments, and quickly develop tf models and deploy them to a Flask API container :)
