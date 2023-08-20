---
title: How to Create a K8s Ingress for an External Service
authors: sedwardes
tags: [linux, r, python, kubernetes, web, infrastructure, data science, outdoors, command line]
keywords:
    - keyword 1
    - keyword 2
draft: true
---

This will show in preview.

<!--truncate-->

Not in preview.

```yaml
# https://stackoverflow.com/questions/57764237/kubernetes-ingress-to-external-service
apiVersion: v1
kind: Service
metadata:
  name: plex
spec:
  ports:
  - name: plex
    port: 32400
    protocol: TCP
    targetPort: 32400
  clusterIP: None
  type: ClusterIP
---
apiVersion: v1
kind: Endpoints
metadata:
  name: plex
subsets:
- addresses:
  - ip: 100.118.49.101 # Tailscale IP address for homelab-utils server.
  ports:
  - name: plex
    port: 32400
    protocol: TCP
---
apiVersion: networking.k8s.io/v1
kind: Ingress
metadata:
  name: plex
  labels:
    name: plex
spec:
  rules:
  - host: plex.homelab.me
    http:
      paths:
      - pathType: Prefix
        path: "/"
        backend:
          service:
            name: plex
            port: 
              number: 32400
---