---
title: "Storage"
description: "In Computerome, we use NFS (Network File System) as the backbone of our shared storage infrastructure. Our storage currently has a total capacity of 50 PB."
---

# Storage

## NFS Storage in Computerome

In Computerome, we use **NFS (Network File System)** as the backbone of our shared storage infrastructure.
Our storage currently has a total capacity of **50 PB**.

## What is NFS?

NFS is a **network-based storage system**. This means that data is stored centrally and can be accessed from any node in the cluster or cloud environment, as long as the system is within the defined internal network.

For users, this means:

- Your files are always available on all compute and login nodes (HPC).
- Your files are always available on all virtual machines (Cloud).
- You do not need to copy files between nodes; NFS handles the centralized access.

## Project-Based Storage

Each project in either **Cloud** or **HPC** receives its own **isolated storage area**.

This isolation is achieved using:

1. **POSIX permissions**:
    Only project members can access the project’s directory. Unless you explicitly give others access, no one outside the project can see or edit your files.
2. **Network isolation (Cloud only)**:
    In cloud projects, there is an **extra layer of security** where projects are also isolated at the **network level**.
    This means that even if POSIX permissions were misconfigured, the data would not be exposed outside the project area.

## Quotas and Limits

- **Project Storage (HPC & Cloud):**
    There are **no hard quotas**. Usage is billed on a **pay-as-you-go model** based on your average daily usage.
- **Home Directories (HPC):**
    Each HPC user has a **personal home directory** located at:

     `/home/people/<username>`

This directory has a **hard quota of 10 GB** and is **free of charge**.
It is meant for configuration files, personal scripts, and very small data only.

!!! abstract "Key Notes"

    1. Project storage is **shared** among all members of the  project. Make sure to set file permissions appropriately to control access within the project.
    2. Large data should **always** be stored under project directories (not your home directory).
    3. Because storage is billed by usage, we recommend monitoring your project’s storage consumption regularly to avoid unexpected costs.
    4. If you need to share data with external collaborators, use our **File Manager** or **import/export features** instead of changing permissions directly on NFS directories.
