# Cluster-level shard allocation settings

## cluster.routing.allocation.enable

1. all - (default) 모든 종류의 shard 재배치를 허용한다.
2. primaries - primary shard의 재배치만 허용한다.
3. 새로운 index의 기본 shard에 대해서만 재배치를 허용한다.
4. 어떠한 shard의 재배치도 허용하지 않는다.