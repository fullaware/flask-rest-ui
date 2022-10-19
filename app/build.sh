pack build fullaware/flask-app:1.0.0 --buildpack paketo-buildpacks/python   --builder paketobuildpacks/builder:base
docker run -d -ePORT=8080 -p8080:8080 --name flask-app fullaware/flask-app:1.0.0
