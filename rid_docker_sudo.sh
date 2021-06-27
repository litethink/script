sudo groupadd docker
sudo gpasswd -a ${USER} docker
newgrp docker #pkill X
sudo chmod a+rw /var/run/docker.sock
