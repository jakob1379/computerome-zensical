---
title: "HPC Compute"
description: "Learn how to access your HPC Compute resources. What are node types and how are the node policies at Computerome"
tags:
  - HPC
---

# HPC Compute

## Login to HPC

Assuming you already have:

- An active account
- Access to an HPC project (see earlier sections)

You can now log in to the HPC environment and run jobs.

The HPC cluster runs on a **traditional queueing system** (currently **Moab/Torque**). You will need basic knowledge of **Linux** and **queueing systems** to use it effectively.

!!! warning "Important Note on Login Nodes"

    1. The login nodes are **shared resources**.
    2. You **cannot run heavy CPU or memory jobs** on login nodes.
    3. These restrictions keep the login environment stable for all users.
    4. If you want to test your scripts or code:
    - Request an **interactive node** (reserved for you for a set time).You can See the **[Interactive Node Guide](../running-jobs/hpc-queueing-system-moab-torque.md#interactive-jobs-on-hpc-cluster)**.

Once you are ready:

- Submit your jobs from the login node.
- Submitting a job means sending your script to the queueing system, which schedules it on the requested number of cores/memory.
- Results will be placed in your specified output directory.
- See the **[Job Submission Guide](../running-jobs/hpc-queueing-system-moab-torque.md#submit-jobs-to-hpc-cluster)**.

---

**Login Methods**

You can access the cluster in two ways:

1. **SSH Login**
    - Connect to: `ssh.computerome.dk`
    - Use your **username, password, and 2FA token**.

**SSH to HPC video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/SSH_to_HPC_ce7f0a9893.mp4" type="video/mp4"></video>

---

2. **ThinLinc (Graphical Login)**
    - Connect to: `desktop.computerome.dk` using the **ThinLinc client**.
    - Provides a full graphical desktop environment.

Please download and install Thinlinc from their official website:

[Download Thinlinc](https://www.cendio.com/thinlinc/docs/install)

**HPC Thinlinc Login video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/HPC_Thinlinc_Login_b009b0d557.mp4" type="video/mp4"></video>

---

## Node Types

There are four different node types available for submitting jobs to the HPC queueing system:

- **Thin Node**
    - 40 CPU cores
    - 192 GB memory
    - Currently

- **Fat Node**
    - 40 CPU cores
    - 1.5 TB memory

- **GPU Node Type 1**
    - 40 CPU cores
    - 192 GB memory
    - 1 × NVIDIA V100 GPU (16 GB memory)

- **GPU Node Type 2**
    - 20 CPU cores
    - 400 GB memory
    - 1 × virtualized slice of NVIDIA A100 GPU (20 GB memory)

!!! note "Memory Allocation Notes"

> Please note that a small portion of each node’s memory is reserved for the operating system. Therefore, the **maximum allocatable memory** for jobs is:
> - Thin Node: **188 GB**
> - Fat Node: **1511 GB**
> - GPU Node Type 1: **188 GB**
> - GPU Node Type 2: **394 GB**

---

## Login Nodes Policies

The **login nodes** on Computerome are shared among all users and are intended only for:

- Logging in
- Navigating the file system
- Preparing and submitting jobs to the queueing system
- Lightweight file editing (e.g., `nano`, `vim`, `vi`)

**Why restrictions exist**
To ensure fair usage and stability, processes that consume excessive CPU or memory on the login nodes are **automatically monitored and killed**. This protects all users and keeps the login environment responsive.

**Policies in effect**

- **CPU and memory limits**:
    - Processes using more than ~90% CPU or >9 GB memory will be terminated.
- **Editors**:
    - Text editors (e.g., `nano`, `vim`, `vi`, `code`) are allowed but must stay within reasonable limits:
        - ≤ 25% CPU
        - ≤ 512 MB memory
    - Editors exceeding these thresholds will be terminated.
- **General compute tools**:
    - Programs like `python`, `R`, `java`, `samtools`, `conda`, `mamba`, `rsync`, `wget`, `curl`, and many others are **not allowed on login nodes**.
    - If started on the login node, they will be killed automatically.
- **Other processes**:
    - Certain heavy or long-running commands (e.g., `jupyter-notebook`, `snakemake`, `bowtie2`, `cellranger`, `busco`, `blast`, etc.) are explicitly blocked.

**What happens if you exceed limits**

- Your process will be **terminated automatically**.
- You will receive a notification message explaining that your process exceeded resource thresholds or was not allowed on login nodes.

**Correct way to work**

- Use the login node **only** for lightweight operations.
- For testing or interactive work, request an **interactive node**:
    - [Interactive Node Guide](../running-jobs/hpc-queueing-system-moab-torque.md#interactive-jobs-on-hpc-cluster)
