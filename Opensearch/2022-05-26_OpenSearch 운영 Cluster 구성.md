# OpenSearch 운영 Cluster 구성

1. opensearch 설치

   ```
   wget https://artifacts.opensearch.org/releases/bundle/opensearch/1.3.2/opensearch-1.3.2-linux-x64.rpm && wget https://artifacts.opensearch.org/releases/bundle/opensearch-dashboards/1.3.2/opensearch-dashboards-1.3.2-linux-x64.rpm
   
   sudo rpm --import https://artifacts.opensearch.org/publickeys/opensearch.pgp
   
   sudo yum install opensearch-1.3.2-linux-x64.rpm && sudo yum install opensearch-dashboards-1.3.2-linux-x64.rpm
   
   sudo systemctl start opensearch.service
   sudo systemctl start opensearch-dashboards.service
   ```

   

   

2. 기본 설정으로 싱글노드 확인

## opensearch-dashboard

```bash
#기본설정에 server.host만 추가해 줬음
server.host: 0.0.0.0
opensearch.hosts: https://localhost:9200
opensearch.ssl.verificationMode: none
opensearch.username: kibanaserver
opensearch.password: kibanaserver
opensearch.requestHeadersWhitelist: [authorization, securitytenant]

opensearch_security.multitenancy.enabled: true
opensearch_security.multitenancy.tenants.preferred: [Private, Global]
opensearch_security.readonly_mode.roles: [kibana_read_only]
# Use this setting if you are running opensearch-dashboards without https
opensearch_security.cookie.secure: false

```

## Opensearch

```
#node1
cluster.name: test
node.name: os01
node.roles: [master,data]
network.host: 0.0.0.0
discovery.seed_hosts: ["https://192.168.219.170","https://192.168.219.144"]
cluster.initial_master_nodes: ["os01","os02"]
transport.port: 9300

#node2
cluster.name: test
node.name: os02
node.roles: [master,data]
network.host: 192.168.219.144
discovery.seed_hosts: ["192.168.219.170","192.168.219.144"]
cluster.initial_master_nodes: ["os01","os02"]
transport.port: 9300

```

2. 