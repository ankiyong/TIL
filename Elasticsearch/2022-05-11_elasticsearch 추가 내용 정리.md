# elasticsearch 추가 내용 정리

## node

node는 elasticsearch의 cluster를 구성하는 하나의 instance다. cluster를 구성하는 node의 이름은 중복돼선 안된다.

### master node 

##### *index의 설정, 매핑 정보, 물리적 위치 등 cluster의 모든 상태 정보를 관리한다.*

cluster는 반드시 하나의 master node를 가져야 한다. master node는 cluster 내 master 후보 노드들에 의해 투표로 선출된다. 이 때 과반 이상의 득표 node가 정해져야 하기 때문에 node는 언제나 홀수를 유지해야 한다. 또한 장애 발생으로 cluster가 분리되는 split brain이 발생했을 때 새로운 master node를 선출해야 하기 때문에 최소 3개 이상의 master 후보 node를 둬야 한다. 

## shard

##### *데이터를 저장할 때 나누어진 하나의 조각에 대한 단위를 뜻한다.*

##### primary shard

elasticsearch는 데이터를 shard에 나누어 저장하게 되고, index 생성시 지정이 가능하며 기본값은 5개다. 아래의 그림처럼 5개의 shard에 data를 분산 저장하게 되고, node가 추가되면 기존 5개 shard는 2개의 node에 균일하게 분산된다. 이렇게 가장 먼저 1 copy씩 존재하는 data shard를 primary shard라고 한다. 

###### primary shard가 많으면 색인 성능이 좋아진다.

![Figure 2. Shard relocating](http://i0.wp.com/guruble.com/wp-content/uploads/2014/02/shards_and_replicas-002.png?resize=500%2C357)

##### replica shard

replica shard는 primarty shard를 제외한 복제본의 개수를 뜻한다. 기본값은 1이며, 이는 primary shard와 동일한 복제본이 1개 존재한다는 것을 뜻한다.

###### replica shard가 필요한 이유는 검색성능과 장애복구다.

![Figure 3. Primary shards & replica shards](http://i1.wp.com/guruble.com/wp-content/uploads/2014/02/shards_and_replicas-003.png?resize=593%2C292)

## cluster health 

| status | explain                                                      |
| ------ | ------------------------------------------------------------ |
| green  | primary shards와 replica shards 모두 정상 작동하고 있을 때   |
| yellow | primary shards 또는 replica shards 둘 중 하나만 작동하고 있을 때 |
| red    | primary shards와 replica shards 모두 정상 작동하지 않을 때   |



## path

elasticsearch.yml 파일 내에서 색인된 data와 실행 log를 저장하는 경로를 지정할 수 있다. 

##### 이 때 되도록이면 타 disk에 저장할 수 있도록 한다. 

