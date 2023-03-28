# docker

```bash
docker run -i -t ubuntu:14.04

- 우분투 컨테이너 실행

docker pull centos:7

- image download

docker create -i -t --name mycentos centos:7

- create container 
- --name option gives name to container
```

```bash
docker start mycentos
- start the docker container
docker attach mycentos
- enter the docker container
```

```bash
difference bertweeb run and create

run 
pull > create > start > attach

create
pull > create
```

```bash
docker ps
- check docker container list
```

# docker run option

```bash
-i -t > attach 가능한 상태로 설정
-d > detached 모드로 컨테이너 실행, 컨테이너를 백그라운드에서 동작하는 애플리케이션으로써 실행하도록 설정
-e > container 내부의 환경변수 설정
```



# delete docker container

```bash
docker stop mycentos

docker rm mycentos

-force remove
docker rm -f mycentos

-delete all container
docker container prune

docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q
```

# network

```bash
docker run -i -t --name mywebserver -p 80:80 ubuntu:14.04

docker run -i -t --name mywebserver -p 80:80 -p 192.168.52.121:7777:80 ubuntu:14.04

-p : 컨테이너의 포트를 호스트의 포트와 바인딩
```

# attach container

```bash
docker exec -i -t container_name /bin/bash
```



# volume

## share host volume

```bash
docker run -d \
--name wordpressdb_hostvolume \
-e MYSQL_ROOT_PASSWORD=123456 \
-e MYSQL_DATABASE=wordpress \
-v /home/wordpress_db:/var/lib/mysql \
mysql:5.7

docker run -d \
-e WORDPRESS_DB_PASSWORD=123456 \
--name wordpress_hostvolume \
--link wordpressdb_hostvolume:mysql \
-p 80 \
wordpress

-v 옵션을 통해 볼륨을 공유할 수 있다. [호스트 공유 디렉터리]:[컨테이너 공유 디렉터리] 형식을 사용한다
```

## volume container



## docker volume

```bash
#volume create
docker volume create myvolume

#
docker run -i -t \
--name myvolume \
-v myvolume:/root/ \
ubuntu:14.04

#-v 사용하면 volume create 없어도 자동으로 생성된다
docker run -i -t \
--name volume_auto \
-v /root \
ubuntu:14.04
```

## volume command

```bash
#volume 확인
docker container inspect volume_auto
=> volume_auto는 container명임

#volume 삭제
docker volume prune
```

# network

## docker network 기능

```bash
#network connect/disconnect
docker network connect [driver_name] [container_name]
docker network disconnect [driver_name] [container_name]
```

### bridge

- 172.17.0.x IP 대역을 컨테이너에 순차적으로 할당한다.

```bash
#bridge driver 생성
docker network create --driver bridge mybridge

#생성한 dirver 사용하여 container 생성
docker run -i -t --name mynetwork_container \
--net mybridge \
ubuntu:14.04

ifconfig로 확인해보면 172.18.0.2 가 할당되어있다.
```

### host

- host 네트워크 환경을 그대로 쓸 수 있다.

```bash
#host는 따로 driver를 생성할 필요가 없다
docker run -i -t \
--name network_host \
--net host \
ubuntu:14.04

#내부로 진입해서 ifconfig 를 날려보면 host와 동일하게 나온다.
#그리고 host이름도 16진수가 아닌 host의 hostname과 동일하게 나온다.
```

# logging

### json-file 로그 사용하기

```
#로그 출력
docker logs CONTAINER_NAME

#로그 마지막 출력
docker logs --tail 2 CONTAINER_NAME

#실시간으로 로그 출력
docker logs -f -t CONTAINER_NAME

#로그파일 확인
cat /var/lib/containers/CONTAINER_ID/CONTAINER_ID-json.log

#로그 파일 크기 지정
docker run -it \
--log-opt max-size=10k --log-opt max-file=3\
--name log-test ubuntu:14.04
```

### syslog 로그



# resource 할당 제한

## memory 할당 제한

```dockerfile
docker run -d \
--memory="1g" \
--name memory_1g \
nginx

#메모리 확인
docker inspect memory_1g | grep \"Memory\" 

#Swap 메모리
docker run -it --name swap_500m \
--memory=200m \
--memory-swap=500m \
ubuntu:14.04
```

## container CUP 제한

### --cpu-shares

- 컨테이너에 가중치를 설정해 해당 컨테이너가 CUP를 상대적으로 얼마나 사용할 수 있는지를 나타낸다.
- CPU를 한개씩 할당하는 방식이 아닌, 시스템에 존재하는 CPU를 어느 비중만큼 나눠 쓸 것인지 명시하는 옵션이다. 

```dockerfile
docker run -d name cpu_512 \
--cpu-shares 512
```

### --cpuset-cpu

- 호스트에 CPU가 여러개 있을 때 컨터이너가 특정 CPU만 사용하도록 설정할 수 있다.

```
docker run -d --name cpuset_2 \
--cpuset-cpus=2 
```

# image

## image 생성

### docker commit

```dockerfile
docker commit \
-a "작성자명" -m "커밋메시지" \
commit_test2 \ => 생성할 이미지 명
commit_test:second  => 생성할 이미지명:태그명
```

## image 추출

### docker save

```
#저장
docker save -o ubintu_14_04.tar ubuntu:14.04

#로드
docker load -i ubuntu_14_04.tar
```

```dockerfile
docker export -o rootFS.tar mycontainer => mycontainer 를 rootFS.tar로 저장
docker import rootFS.tar myimage:0.0 => rootFS.tar을 image로 저장		
```

## image 배포

## image 빌드

- 기본 이미지에 원하는 작업(apt-get update 등) 을 한 상태로 이미지를 생성할 수 있다.

1. Dockerfile 생성

```dockerfile
#Dockerfile

#기본 이미지
FROM ubuntu:14.04
#작성자
MAINTAINER alicek106
#이미지 라벨
LABEL "purpose"="practice"
#수행할 작업
RUN apt-get update
RUN apt-get install apache2 -y
#복사할 파일
ADD test.html /var/www/html
#Run 실행할 장소로 이동
WORKDIR /var/www/html
#열어둘 port
EXPOSE 80
#CMD 명령어
CMD apachectl -DFOREGROUND
```

2. image build

```shell
docker build -t mybuild:0.0 /path/to/dockerfile
```

3. run

```shell
docker run -d -P --name myserver mybuild:0.0
```

