---
title: "SLURM"
description: "This article explains how to use the SLURM workload manager as a cluster user."
tags:
  - HPC
---

# SLURM

## Overview

This section explains how to use the SLURM workload manager as a cluster user.

## Logging into computerome

Users access the Computerome HPC cluster through the login node:

```
hpc.computerome.dk
```
Example:

```
ssh username@hpc.computerome.dk
```

Users interact with SLURM by submitting jobs that request computing resources.

A SLURM job requests:

- CPU resources
- Memory
- Runtime
- GPU resources (if required)
- Partition
- Account (Mandatory for any job to be submitted)

---

## Basic SLURM Workflow

The typical workflow is:

```
Create job script
        |
        v
Submit job
        |
        v
Monitor job
        |
        v
Retrieve results
```

---

## Available Partitions

The cluster provides several partitions based on Node types as mentioned before in  https://computerome.dk/wiki/user-guide#node-types

| Partition | Purpose |
|---|---|
| thinnode | General CPU workloads |
| noib | CPU nodes without InfiniBand |
| fatnode | High-memory workloads |
| gpuv1 | NVIDIA V100 GPU jobs |
| gpua1 | NVIDIA A100 GPU jobs |

---

## Required Job Parameters

All jobs must specify:

```bash
#SBATCH --account=<account>
#SBATCH --job-name=<name>
#SBATCH --time=<time>
#SBATCH --ntasks=<tasks>
#SBATCH --mem=<memory>
```

Example:

```bash
#SBATCH --account=my_project
#SBATCH --job-name=test
#SBATCH --time=01:00:00
#SBATCH --ntasks=4
#SBATCH --mem=8G
```

---

## Common Commands

Check available nodes:

```bash
sinfo
```

Submit a job:

```bash
sbatch job.sh
```

View jobs:

```bash
squeue
```

Cancel a job:

```bash
scancel JOB_ID
```

View job details:

```bash
scontrol show job JOB_ID
```

---

## Storage

Temporary job storage is available through:

```
/scratch/$USER/$SLURM_JOB_ID
```

Example:

```bash
cd /scratch/$USER/$SLURM_JOB_ID
```

Scratch data is automatically removed after the job finishes.

Permanent results should be copied to:

```
$HOME
```

or project storage.
