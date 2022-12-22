docker build -t finitive-socket-server:latest .
docker run --rm -it --name=finitive-notif -d --net=host finitive-socket-server:latest
start chrome ./index.html