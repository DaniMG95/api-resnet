# API Resnet
This Api is in charge of the classification of images using a predictive model Resnet.
is the deployment of an API that is responsible for collecting the image to be classified and call this predictive model to return the class it belongs to.
to return the class it belongs to.

The request and response is a JSON object. The composition of this object depends on the request type or verb. See the API specific sections below for details.

In case of error, all APIs will return a JSON object in the response body with error as key and the error message as the value:

```
{
  "msg": <error message string>
}
```

##Instructions
To deploy this API in docker it is necessary to have docker and docker-compose installed, to install it follow these steps.
 - [docker](https://docs.docker.com/get-docker/)
 - [docker-compose](https://docs.docker.com/compose/install/)

After installation it is only necessary to go to the path where we have the cloned repository and execute the following commands
```
curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz | tar --strip-components=2 -C /tmp/resnet -xvz
docker-compose up -d
```

And this will generate the respective dockers for the Resnet model and the API.

In case you don't want to deploy with docker-compose, you would need to have Python installed and install the packages 
packages from the requirements.txt.  
But it is necessary to have docker for the deployment of the model, these would be the commands to deploy the application without
docker-compose

```
curl -s https://storage.googleapis.com/download.tensorflow.org/models/official/20181001_resnet/savedmodels/resnet_v2_fp32_savedmodel_NHWC_jpg.tar.gz | tar --strip-components=2 -C /tmp/resnet -xvz
docker run --rm -d -p port:8501 -v "/tmp/resnet:/models/resnet" -e MODEL_NAME=resnet tensorflow/serving
Export server=localhost:port
python3 server.py
```



##EndPoints

These are the endpoints that are available in the API 

###POST /api/image/
This endpoint is passed in the body an image in base64 format and will give an output with the class it belongs to and the average time it has taken to classify it. 
average time it has taken to classify it.

####Input
```
{
    "img":"base64_img"
}
```

####Output
```
{
    "class": {
        "class Prediction": X,
        "avg latency": Y
    }
}
```


###POST /api/url/

This endpoint is passed a url of an image in the body and will give an output with the class that belongs to an image. 
average time it has taken to classify it 10 times.

```
{
    "img":"url_img"
}
```

####Output
```
{
    "class": {
        "class Prediction": X,
        "avg latency": Y
    }
}
```


##Example

I will now show an example of the call to the /api/url/ endpoint.

```
curl -i -X POST -H "Content-Type: application/json" -d "{""url"":""https://st.depositphotos.com/1020341/4233/i/600/depositphotos_42333899-stock-photo-portrait-of-huge-beautiful-male.jpg""}" http://localhost:5000/api/url/
```

Output:
```
{"class": {"class Prediction": 292, "avg latency": 62.315599999999996}}
```