# Migration From Es TO Os

## 7.10 버전 이하

| Elasticsearch version | Rolling upgrade path                                         | Cluster restart upgrade path                                 |
| :-------------------- | :----------------------------------------------------------- | :----------------------------------------------------------- |
| 5.x                   | 5.6 버전으로 업그레이드 하고, 6.8 버전으로 업그레이드 한 후, 모든 5.x버전의 index를 reindex 하고 7.10.2로 업그레이드 하고 Opensearch로 업그레이드 해라 | Upgrade to 6.8, reindex all 5.x indices, and upgrade to OpenSearch. |
| 6.x                   | 6.8 버전으로 업그레이드 하고, 7.10.2 버전으로 업그레이드 하고 OpsenSearch로 업그레이드 해라. | Upgrade to OpenSearch.                                       |
| 7.x                   | OpenSearch로 업그레이드 해라                                 | Upgrade to OpenSearch.                                       |



## 7.11 버전 이상

rolling upgrade를 사용하지 않는다. 





## Migration methods

총 4가지의 방법이 존재한다.

1. Rolling upgrades
2. Snapshots
3. Reindex API
4. OpenSearch upgrade tool



### 1. Rolling Upgrades

롤링 업그레이드는 공식적인 업그레이드 방법이다. migrate 할 때 서비스의 방해 없이 처리가 가능하다. 

롤링 업그레이드는 다음의 버전에 지원된다.

- Between minor versions
- [From 5.6 to 6.8](https://www.elastic.co/guide/en/elastic-stack/6.8/upgrading-elastic-stack.html)
- From 6.8 to 7.14.1
- From any version since 7.14.0 to 7.14.1

6.7 버전 혹은 더 아래 버전에서 7.14.1 버전으로 바로 업그레이드 하려면 전체 클러스터를 재시작 해야한다. 

es 버전이 6.8 ~ 7.10.2 사이인 경우 OpenSearch로 직접 업그레이드가 가능하다. 그렇지 않으면 먼저 Es를 6.8로 업그레이드 해야한다. 

#### Upgrade Elasticsearch

1. shards 할당을 disable한다.

   ```json
   PUT _cluster/settings
   {
    "persistent": {
      "cluster.routing.allocation.enable": "primaries"
    }
   }
   #cluster가 재시작 됐을 떄 shards의 임의적인 재배치를 막기 위한 설정
   ```

   

2. ES의 노드를 정지한다.

   ```bash
   sudo systemctl stop elasticsearch.service
   ```

3. 노드를 upgrade 한다.

   ```bash
   sudo yum install elasticsearch-oss-7.10.2 --enablerepo=elasticsearch
   ```

   ​	*command는 사용하는 시스템에 따라 변경될 수 있지만, 일반적으로는 다음과 같이 사용한다.*

4. ES를 재시작하고 node가 rejoin 될 때 까지 기다린다.

   ```bash
   sudo systemctl start elasticsearch.service
   ```

5. 모든 노드가 동일한 버전을 사용할 때 까지 2~4 번 내용을 반복한다.

6. 1번에서 disable 했던 설정을 enable 한다

   ```json
   PUT _cluster/settings
   {
    "persistent": {
      "cluster.routing.allocation.enable": "all"
    }
   }
   ```

   

### 2. Snapshot

es에서 sanpshot을 사용하여 os로 data를 restore 할 수 있다.

1. elastisearch.yml 파일에 다음 라인을 추가해 준다.

   ```bash
   path.repo: ["sanpshot 저장 경로"]
   ```

2. dev tools에서 다음의 query를 입력하여 snapshot 경로를 설정해준다.

   ```json
   PUT _snapshot/backups
   {
       "type" : "fs",
       "settings" : {
         "location" : "sanpshot 저장 경로"
     }
   }
   ```

3. es의 snapshot을 생성한다

   ```json
   PUT _snapshot/backups/snapshot_index명
   {
     "indices": "저장할 index명"
   }
   #모든 index를 저장하고 싶다면 indices에 *을 사용할 수 있다.
   ```

4. 앞서 생성한 snapshot을 확인한다.

   ```bash
   GET _snapshot/backups/snapshot_index명
   ```

5. os도 es와 동일한 설정을 yml에 추가해준다.

   ```
   path.repo: ["sanpshot 저장 경로"]
   #os에 설정 시 snapshot 폴더에 접근이 안돼서 실행이 안되는 경우가 있다.
   #그럴때는 /etc/opensearch 폴더에 넣어두고 하면 된다.
   ```

6. os도 마찬가지로 query를 통해 sanpshot 경로를 설정해준다.

   ```json
   PUT _snapshot/backups
   {
       "type" : "fs",
       "settings" : {
         "location" : "sanpshot 저장 경로"
     }
   }
   ```

   1. 여기서 오류가 발생한다.

      ```json
      {
        "error" : {
          "root_cause" : [
            {
              "type" : "repository_verification_exception",
              "reason" : "[backups] [[UHfTijNLQhGKjLaK9EN76g, 'RemoteTransportException[[os02][192.168.219.144:9300][internal:admin/repository/verify]]; nested: RepositoryMissingException[[backups] missing];']]"
            }
          ],
          "type" : "repository_verification_exception",
          "reason" : "[backups] [[UHfTijNLQhGKjLaK9EN76g, 'RemoteTransportException[[os02][192.168.219.144:9300][internal:admin/repository/verify]]; nested: RepositoryMissingException[[backups] missing];']]"
        },
        "status" : 500
          
      #검색해보니 os의 모든 node가 같은 repo를 바라보지 않고 있어서 그런 것 같다.\
      ```

   2. 야매로 진행하려고 node2를 종료하고 restore 해본 결과 어떠한 shard에도 할당되지 않는다. 

7. 저장된 snapshot으로 restore해준다

   ```bash
   POST _snapshot/backups/es_bk/_restore
   ```

   

