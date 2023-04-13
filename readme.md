# Kubernetes demo
---
## Worldcup

Worldcup is an application to be tested in Kubernetes environment.
The champion is set in `champ` environment variable.

## Build

You should build and deploy it into your own registry.

```bash
docker build . -t rodriguezarata/worldcup:0.1
docker push rodriguezarata/worldcup:0.1
```

## Deploy in docker

```bash
docker run -d --env champ=francia --name worldcup -p 80:80 rodriguezarata/worldcup:0.1
```

## Deploy pod in Kubernetes

```bash
k run worldcup --image rodriguezarata/worldcup:0.1 --env="champ=francia" 
```

## Deploy as deployment

## Update env variable

