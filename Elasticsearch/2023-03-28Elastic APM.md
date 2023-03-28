# Elastic APM

## 1. APM(Appllication Perfomance Monitoring)

- ㅊ의 성능을 모니터링을 뜻한다.
- 성능 문제를 감지하고 진단하기 위한 응답 시간, 리소스 활용도와 같은 주요 메트릭을 모니터링 하는 작업을 수행한다.

## 2. ElasticAPM

- Elastic Stack에 내장된 APM 시스템이다. 
- Software와 응용프로그램을 실시간으로 모니터링한다.
- 들어오는 요청에 대한 응답시간, DB 쿼리 시간, 캐시 호출시간 등 다양항 항목을 모니터링 할 수 있다.

## 3. Components

- ElaticAPM은 4가지 component가 있다.

![](.\image\apm1.png)

1. APM agent
   - 성능과 오류 데이터를 런타임으로 모아 APM 서버(Elatsic APM integration)로 전달한다.
2. Elatsic APM integration
   - APM agent로부터 data를 전달받은 후 검증 및 처리 후 가공하여 ES Document 형식으로 변환한다.
3. Elasticsearch
4. Kibana



## 4. 설정 및 설치

#### 1. 기본 설정

```yaml
#elasticsaerch.yml

node.name: apm_node1
network.host: 0.0.0.0
xpack.security.enrollment.enabled: true
xpack.security.enabled: true
xpack.security.authc.api_key.enabled: true
xpack.security.http.ssl:
  enabled: true
  keystore.path: certs/http.p12
xpack.security.transport.ssl:
  enabled: true
  verification_mode: certificate
  keystore.path: certs/transport.p12
  truststore.path: certs/transport.p12
cluster.initial_master_nodes: ["apm_node1"]
```

```yaml
#kibana encryption-key 발급

[an@node1 kibana]$ bin/kibana-encryption-keys generate

## Kibana Encryption Key Generation Utility

The 'generate' command guides you through the process of setting encryption keys for:

xpack.encryptedSavedObjects.encryptionKey
    Used to encrypt stored objects such as dashboards and visualizations
    https://www.elastic.co/guide/en/kibana/current/xpack-security-secure-saved-objects.html#xpack-security-secure-saved-objects

xpack.reporting.encryptionKey
    Used to encrypt saved reports
    https://www.elastic.co/guide/en/kibana/current/reporting-settings-kb.html#general-reporting-settings

xpack.security.encryptionKey
    Used to encrypt session information
    https://www.elastic.co/guide/en/kibana/current/security-settings-kb.html#security-session-and-cookie-settings


Already defined settings are ignored and can be regenerated using the --force flag.  Check the documentation links for instructions on how to rotate encryption keys.
Definitions should be set in the kibana.yml used configure Kibana.

Settings:
xpack.encryptedSavedObjects.encryptionKey: e9d06abc7408ca851b369bcf892ce15c
xpack.reporting.encryptionKey: 1989549396ea81f2df58918fd7757a94
xpack.security.encryptionKey: 4d25495afab188c82c38283f6409a8fd

#kibana.yml

server.host: 0.0.0.0
elasticsearch.hosts: ['https://192.168.52.121:9210']
elasticsearch.serviceAccountToken: AAEAAWVsYXN0aWMva2liYW5hL2Vucm9sbC1wcm9jZXNzLXRva2VuLTE2Nzk5Njg0MDc1MDA6ZjJ6eW52bnJRXzZNMW16Nm1SS0phdw
elasticsearch.ssl.certificateAuthorities: [/home/an/elk/kibana/data/ca_1679968408439.crt]
xpack.fleet.outputs: [{id: fleet-default-output, name: default, is_default: true, is_default_monitoring: true, type: elasticsearch, hosts: ['https://192.168.52.121:9210'], ca_trusted_fingerprint: 542089428a18e7ec828a82b96b45902ce8d3397d734ba6a5a4c8ac8780d413c3}]
xpack.encryptedSavedObjects.encryptionKey: e9d06abc7408ca851b369bcf892ce15c


```

#### 2. Fleet Server 설정

##### 1) add fleet server hosts

![add_fleet_host](.\image\add_fleet_host.png)

###### a. add fleet server 클릭 후, Fleet server host 이름과 사용할 url을 작성한 후 Generate Fleet Server policy 클릭

![add_fleet_host_2](.\image\add_fleet_host_2.png)

###### b. 원하는 운영체제를 선택 후 아래 설치 코드를 복사해 Fleet Server를 설치한다.

![add_fleet_host_3](.\image\add_fleet_host_3.png)

###### c. Confirm connection에 설정 완료 메시지를 확인하면 끝



##### 2) Add Fleet Server 

###### a. add fleet server를 클릭하여 fleet server를 생성

![add_fleet_server](.\image\add_fleet_server.png)

###### b. 기본값으로 설정 후 save & continue 선택 / 아래는 생성 완료된 모습

![add_fleet_server_fin](.\image\add_fleet_server_fin.png)



#### 3. APM Integraion 설정

###### a. Integrations 페이지에서 APM을 선택한다.

![integration_apm](.\image\integration_apm.png)

###### b. APM Integration을 선택 후 기본값으로 세팅하여 save & continue 선택한다.

![apm_server1](.\image\apm_server1.png)

###### c.Add Agent를 선택한다.

![apm_server2](.\image\apm_server2.png)

###### d. monitoring할 host에 agent를 설치한다.

![apm_server3](.\image\apm_server3.png)

###### error

Elastic Agent를 설치하다보면 아래와 같은 오류가 발생할 수 있다.

![apm_install_error](.\image\apm_install_error.png)

그럴땐 --insecure 옵션을 사용해서 설치하면 해결된다.

![apm_install_solution](.\image\apm_install_solution.png)

##### 4. observability > overview 선택

기본 설정이 완료된 화면이다.

![setting_fin](.\image\setting_fin.png)