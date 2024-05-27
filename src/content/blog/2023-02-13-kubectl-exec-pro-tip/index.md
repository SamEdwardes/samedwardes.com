---
author: Sam Edwardes
date: 2023-02-13
description: I always forget how to exec into a pod in Kubernetes without knowing the pod name. This is a quick reminder for myself.
keywords: []
tags:
- kubernetes
title: kubectl exec Into a Pod Without Knowing the Pod Name
---

One common task in Kubernetes is to `exec` into a pod to run commands. The typical way to do this is as follows:

```bash
POD_NAME="test-pod-1234asdfas"
kubectl exec -it pod/$POD_NAME -- /bin/bash
```

This pattern typically works fine. However, if you are frequently creating and deleting new pods, the name will constantly change. This means you will have to retype the command with the new pod name instead of just using the up arrow to select a recent command. A more consistent way is to use the deployment name instead:

```bash
DEPLOYMENT_NAME="test-pod"
kubectl exec -it deployment/$DEPLOYMENT_NAME -- /bin/bash
```
