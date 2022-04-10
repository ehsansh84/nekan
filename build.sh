#git pull
docker rmi nekan 
docker build -t nekan .
docker stop nekan
docker rm nekan
docker run --name nekan -p 8100:8282 -d --restart always --network cluster-manager_default -e MONGO=mongodb  nekan

