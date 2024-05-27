---
title: How to Set Linux User Passwords Without Interaction
authors: sedwardes
tags: [linux, bash]
---

I often want to create new users in Linux for testing. Creating new users without interaction can be challenging to automate because the `passwd` command provides no way for you to pass in a plain text password. It will prompt you for a password which is OK for interactive sessions but not suitable for automation (e.g. creating new users in Pulumi).

```bash
NEW_USER_NAME=sam
useradd --create-home --home-dir /home/$NEW_USER_NAME -s /bin/bash $NEW_USER_NAME
passwd $NEW_USER_NAME
# New password: 
# Retype new password: 
# passwd: password updated successfully
```

The solution I have found is to pipe the password into the `passwd` command like this:

```bash
NEW_USER_NAME=sam
NEW_USER_PASSWORD=password
useradd --create-home --home-dir /home/$NEW_USER_NAME -s /bin/bash $NEW_USER_NAME
echo -e "${NEW_USER_PASSWORD}\n${NEW_USER_PASSWORD}" | passwd $NEW_USER_NAME
```

This trick allows you to create new users and set their passwords without interaction!