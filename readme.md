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
kubectl run worldcup --image rodriguezarata/worldcup:0.1 --env="champ=francia"
```

## Deploy as deployment

```bash
kubectl apply -f manifest.yaml
```

## Update env variable
You will replace the current champ value, after that, you will need to restart the pods.

```bash
kubectl edit configmaps worldcup-configmap
kubectl rollout restart deployment worldcup-deployment
```

# Undo a previous rollout

```bash
kubectl rollout undo deployment worldcup-deployment
```

## Check your logs

```bash
kubectl describe pods worldcup-deployment-85b445ccb5-8lfj9
kubectl logs deployments/worldcup-deployment -f
```

## See balancing requests to pods
You will generate a pod to connect to the service in the cluster

```bash
kubectl run -i --tty --rm debug --image=alpine --restart=Never -- sh
apk update
apk upgrade
apk add curl
watch curl 'worldcup-service.default.svc/host'
```