# Docker error

```
#elasticsearch vm.max_map_count 부족 오류 발생시
wsl -d docker-desktop
sysctl -w vm.max_map_count=262144

#VMMem이 자원을 너무 많이 먹을 때 
1. wsl --shutdown

2. C:\Users\your-username\.wslconfig파일 생성한 후

3. 내용 추가
[wsl2]
guiApplications=false  #cpu

memory=6GB #memory
swap=0

4. Restart-Service LxssManager
```

