---
author: Sam Edwardes
date: 2024-07-14
description: How to use nushell with kubectl
keywords:
- kubernetes
tags:
- kubernetes
title: Using nushell with kubectl
---

I recently discovered [nushell](https://www.nushell.sh/). It is similar to shells like bash and zsh, but every command works on structure data. Here are some examles of how you can use with `kubectl` to explore your kubernetes cluster more ergonomically.

## kubectl get pods

Normal kubectl pods looks like this.

```bash
kubectl get pods

NAME                                 READY   STATUS              RESTARTS      AGE
grafana-alloy-tqb7l                  2/2     Running             0             2d14h
grafana-alloy-tlwm9                  2/2     Running             0             2d14h
prometheus-server-659b75c446-nzxbp   0/2     ContainerCreating   0             10h
grafana-79c45cd5f9-jpr6k             0/1     Init:0/1            0             10h
grafana-alloy-tlrvl                  2/2     Running             6 (68m ago)   2d14h
kube-state-metrics-6965d77b4-jzvlb   1/1     Running             3 (68m ago)   2d14h
grafana-alloy-97c8n                  2/2     Running             6 (68m ago)   2d14h
```

You can parse this information with nushell like this.

```bash
kubectl get pods -o json | from json | get items | flatten | select apiVersion kind name namespace creationTimestamp

╭───┬────────────┬──────┬────────────────────────────────────┬────────────┬──────────────────────╮
│ # │ apiVersion │ kind │                name                │ namespace  │  creationTimestamp   │
├───┼────────────┼──────┼────────────────────────────────────┼────────────┼──────────────────────┤
│ 0 │ v1         │ Pod  │ grafana-alloy-tqb7l                │ monitoring │ 2024-07-12T01:49:46Z │
│ 1 │ v1         │ Pod  │ grafana-alloy-tlwm9                │ monitoring │ 2024-07-12T01:49:46Z │
│ 2 │ v1         │ Pod  │ prometheus-server-659b75c446-nzxbp │ monitoring │ 2024-07-14T06:24:25Z │
│ 3 │ v1         │ Pod  │ grafana-79c45cd5f9-jpr6k           │ monitoring │ 2024-07-14T06:24:25Z │
│ 4 │ v1         │ Pod  │ grafana-alloy-tlrvl                │ monitoring │ 2024-07-12T01:49:46Z │
│ 5 │ v1         │ Pod  │ kube-state-metrics-6965d77b4-jzvlb │ monitoring │ 2024-07-12T01:46:58Z │
│ 6 │ v1         │ Pod  │ grafana-alloy-97c8n                │ monitoring │ 2024-07-12T01:49:46Z │
╰───┴────────────┴──────┴────────────────────────────────────┴────────────┴──────────────────────╯
```

There are many other fields in metadata that we can capture as well.

```bash
kubectl get pods -o json | from json | get items | flatten | columns

╭────┬───────────────────────────────╮
│  0 │ apiVersion                    │
│  1 │ kind                          │
│  2 │ annotations                   │
│  3 │ creationTimestamp             │
│  4 │ generateName                  │
│  5 │ labels                        │
│  6 │ name                          │
│  7 │ namespace                     │
│  8 │ ownerReferences               │
│  9 │ resourceVersion               │
│ 10 │ uid                           │
│ 11 │ affinity                      │
│ 12 │ containers                    │
│ 13 │ dnsPolicy                     │
│ 14 │ enableServiceLinks            │
│ 15 │ nodeName                      │
│ 16 │ preemptionPolicy              │
│ 17 │ priority                      │
│ 18 │ restartPolicy                 │
│ 19 │ schedulerName                 │
│ 20 │ securityContext               │
│ 21 │ serviceAccount                │
│ 22 │ serviceAccountName            │
│ 23 │ terminationGracePeriodSeconds │
│ 24 │ tolerations                   │
│ 25 │ volumes                       │
│ 26 │ conditions                    │
│ 27 │ containerStatuses             │
│ 28 │ hostIP                        │
│ 29 │ hostIPs                       │
│ 30 │ phase                         │
│ 31 │ podIP                         │
│ 32 │ podIPs                        │
│ 33 │ qosClass                      │
│ 34 │ startTime                     │
│ 35 │ automountServiceAccountToken  │
│ 36 │ initContainers                │
│ 37 │ initContainerStatuses         │
╰────┴───────────────────────────────╯
```

Now that we have access to this metadata, we can do all sorts of interesting queries on our data.

## Sorting

Sort by the created date.

```bash
# Get the oldest pods
kubectl get pods -Ao json | from json | get items | flatten | sort-by creationTimestamp | select kind name namespace creationTimestamp | first 5

╭───┬──────┬──────────────────────────────────────┬──────────────────────┬──────────────────────╮
│ # │ kind │                 name                 │      namespace       │  creationTimestamp   │
├───┼──────┼──────────────────────────────────────┼──────────────────────┼──────────────────────┤
│ 0 │ Pod  │ coredns-59b4f5bbd5-nswpf             │ kube-system          │ 2023-06-19T23:00:16Z │
│ 1 │ Pod  │ debug-7b578644b5-mkv6d               │ default              │ 2023-06-22T21:53:34Z │
│ 2 │ Pod  │ api-6bfbf64b59-gqf4w                 │ default              │ 2024-01-19T02:54:50Z │
│ 3 │ Pod  │ homer-d58596598-8jkfn                │ default              │ 2024-05-15T13:35:12Z │
│ 4 │ Pod  │ kubernetes-dashboard-64d75468c-pzcsx │ kubernetes-dashboard │ 2024-05-15T13:35:12Z │
╰───┴──────┴──────────────────────────────────────┴──────────────────────┴──────────────────────╯

# Get the newest pods
kubectl get pods -Ao json | from json | get items | flatten | sort-by creationTimestamp --reverse | select kind name namespace creationTimestamp | first 5

╭───┬──────┬─────────────────────────────────────────────────────┬─────────────────┬──────────────────────╮
│ # │ kind │                        name                         │    namespace    │  creationTimestamp   │
├───┼──────┼─────────────────────────────────────────────────────┼─────────────────┼──────────────────────┤
│ 0 │ Pod  │ instance-manager-e-0ca1593f370359a01871d9fdfe0dae2f │ longhorn-system │ 2024-07-14T15:33:19Z │
│ 1 │ Pod  │ instance-manager-r-0ca1593f370359a01871d9fdfe0dae2f │ longhorn-system │ 2024-07-14T15:33:19Z │
│ 2 │ Pod  │ instance-manager-e-2624c5ccb0ea251f9017c48e42e2996b │ longhorn-system │ 2024-07-14T15:33:16Z │
│ 3 │ Pod  │ instance-manager-r-2624c5ccb0ea251f9017c48e42e2996b │ longhorn-system │ 2024-07-14T15:33:16Z │
│ 4 │ Pod  │ longhorn-driver-deployer-9d85f7675-q45zx            │ longhorn-system │ 2024-07-14T06:29:08Z │
╰───┴──────┴─────────────────────────────────────────────────────┴─────────────────┴──────────────────────╯
```

Yes, it is true that you could do all of this with kubectl, but I can never remember the correct way to use jsonpath and/or jq. I find the nushell syntax a lot easier to work with.

## Filtering

Get all of the pods created in June.

```bash
kubectl get pods -Ao json | from json | get items | flatten | select kind name namespace creationTimestamp | into datetime creationTimestamp | insert month { $in.creationTimestamp | date to-record | get month } | where month == 6 | first 5

╭───┬──────┬──────────────────────────────────┬─────────────────┬───────────────────┬───────╮
│ # │ kind │               name               │    namespace    │ creationTimestamp │ month │
├───┼──────┼──────────────────────────────────┼─────────────────┼───────────────────┼───────┤
│ 0 │ Pod  │ longhorn-csi-plugin-jmtdf        │ longhorn-system │ a month ago       │     6 │
│ 1 │ Pod  │ longhorn-csi-plugin-nl8ls        │ longhorn-system │ a month ago       │     6 │
│ 2 │ Pod  │ csi-resizer-6ddc566bd6-lvzjk     │ longhorn-system │ a month ago       │     6 │
│ 3 │ Pod  │ csi-attacher-6fd696d46d-88qc5    │ longhorn-system │ a month ago       │     6 │
│ 4 │ Pod  │ csi-provisioner-7797d44fd9-5hwft │ longhorn-system │ a month ago       │     6 │
╰───┴──────┴──────────────────────────────────┴─────────────────┴───────────────────┴───────╯
```

This is pretty verbose. But, I like that I can read the command and pretty easily parse out what is happening. I am also very new to nushell, so there is probably a more effecient way to do this.












