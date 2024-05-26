---
author: Sam Edwardes
date: 2023-04-15
description: I always forget these commands... so here is my list of helpful commands to get information about your server.
keywords:
- Linux server info
- How to get external ip address
- How to get linux server info
tags:
- linux
title: How to Get Basic Info About Your Linux Server
---

I always forget these commands... so here is my list of helpful commands to get information about your server.

- Get your external IP address.

```bash
curl ifconfig.io
```

- Get your internal IP address. For example, this can be helpful if you are working with several EC2 instances that need to communicate with each other. You can use this instead of the external IP address for node to node communication. This has the benefit of being static even if you stop and start your EC2 instance.

```bash
hostname -i
```

- Get information about your operating system.

```bash
lsb_release -a
```

- Get information about your current operating system when in a Docker image.

```bash
cat  /etc/os-release
```