#build docker image
docker build --no-cache -t api-marvel:latest .

#execute new image on local
docker run -it -p 5000:80 api-marvel:latest