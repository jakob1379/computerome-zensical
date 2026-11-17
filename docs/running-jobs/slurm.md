---
title: "SLURM"
description: "This article explains how to use the SLURM workload manager as a cluster user."
icon: lucide/terminal
tags:
  - HPC
---

# SLURM

## Overview

This section explains how to use the SLURM workload manager as a cluster user.

## Logging into Computerome

Users access the Computerome HPC cluster through the login node `hpc.computerome.dk`.

```console
$ ssh <username>@hpc.computerome.dk
```

Users interact with SLURM by submitting jobs that request computing resources.

A SLURM job requests:

- CPU resources
- Memory
- Runtime
- GPU resources (if required)
- Partition
- Account (mandatory for any job to be submitted)

## Basic SLURM workflow

The typical workflow is:

```mermaid
flowchart LR
    A[Create job script] --> B[Submit job]
    B --> C[Monitor job]
    C --> D[Retrieve results]
```

## Available partitions

The cluster provides several partitions based on the [node types](../compute/hpc-compute.md#node-types).

| Partition | Purpose |
| --- | --- |
| `thinnode` | General CPU workloads |
| `noib` | CPU nodes without InfiniBand |
| `fatnode` | High-memory workloads |
| `gpuv1` | NVIDIA V100 GPU jobs |
| `gpua1` | NVIDIA A100 GPU jobs |

## Required job parameters

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

!!! warning

    The account is mandatory: no job can be submitted without `--account`.

## Common commands

| Task | Command |
| --- | --- |
| Check available nodes | `sinfo` |
| Submit a job | `sbatch job.sh` |
| View jobs | `squeue` |
| Cancel a job | `scancel JOB_ID` |
| View job details | `scontrol show job JOB_ID` |

For submitting many similar jobs at once, see [SLURM Array Jobs](slurm-array-jobs.md).

## Storage

Temporary job storage is available through `/scratch/$USER/$SLURM_JOB_ID`:

```bash
cd /scratch/$USER/$SLURM_JOB_ID
```

!!! warning

    Scratch data is automatically removed after the job finishes.
    Permanent results should be copied to `$HOME` or [project storage](../storage/hpc-storage.md).
