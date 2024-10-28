# JARP
Discord bot

## How to run
First build the docker image from the `JARP` folder
`sudo docker build -t jarp_docker_img -f jarp_docker .`
Then run the docker image
`sudo docker run --env-file .env --hostname mycontainer --cap-add=NET_ADMIN --sysctl net.ipv6.conf.all.disable_ipv6=0 jarp_docker_img > /dev/null 2>&1 &`
