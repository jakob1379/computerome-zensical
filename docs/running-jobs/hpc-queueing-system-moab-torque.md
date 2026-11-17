---
title: "HPC Queueing System (Moab/Torque)"
description: "In the HPC environment, Computerome uses the Moab/Torque queueing system. The queueing system is responsible for managing the cluster resources (compute nodes) and ensuring that users receive the resources they request."
icon: lucide/list-ordered
tags:
  - HPC
---

# HPC Queueing System (Moab/Torque)

In the HPC environment, Computerome uses the **Moab/Torque queueing system**.
The queueing system is responsible for managing the cluster resources (compute nodes) and ensuring that users receive the resources they request.

To interact with the queueing system, you must use a specific **command syntax**.
Your job submissions tell the queueing system:

- What resources you need (CPU, memory, nodes, walltime, etc.)
- What scripts or programs to run
- Where to store output and error logs

## Purpose of These Guidelines

In the following sections, we will cover:

- The different scenarios in which you may submit jobs
- How to request and use resources effectively
- How to monitor and troubleshoot your jobs
- Best practices for running jobs in the cluster

These guidelines are designed to help you **find your way in the queueing system** and make efficient use of the available resources.

## Submit Jobs to HPC Cluster

Jobs on Computerome are submitted to the **Moab/Torque queueing system** using the `qsub` command.
When submitting a job, you need to specify:

- The **resources** your job requires (e.g., CPUs, memory, walltime, node types).
- The **account/group** your job should run under.
- The **script or command** you want to execute.

### Ways to Submit Jobs

1. **One-line command**

    You can submit a quick job directly from the command line:

    ```bash
    qsub -W group_list=<group> -A <account> -l nodes=1:ppn=40,mem=120g,walltime=01:00:00 job.sh
    ```

2. **PBS script (recommended)**

    A PBS script allows you to clearly separate resource requests from job logic, making your workflows easier to manage and reproduce.
    Example:

    ```bash title="PBS script"
    #!/bin/bash
    #PBS -W group_list=<group>
    #PBS -A <account>
    #PBS -l nodes=1:ppn=40,mem=120g,walltime=01:00:00
    #PBS -o job.out
    #PBS -e job.err

    cd $PBS_O_WORKDIR
    ./my_program input_file > result.txt
    ```

3. **Job arrays**

    If you need to run the same job multiple times with small variations (e.g., processing 100 input files), you can use a job array.
    This allows you to submit and manage many related jobs more efficiently.
    Example:

    ```bash
    #PBS -t 1-100
    ./my_program input_${PBS_ARRAYID}.txt > result_${PBS_ARRAYID}.txt
    ```

4. **Specifying GPU types in your job**

    We have A100 and V100 GPUs. To specify the GPU type, use the parameter `gpua1` for A100 or `gpuv1` for V100.
    Example:

    ```bash
    #!/bin/bash
    #PBS -N gpu_check
    #PBS -l nodes=1:ppn=20:gpuv1:gpu=1 # (1)!
    #PBS -l walltime=00:01:00
    #PBS -j oe
    #PBS -W group_list=<usergroup> -A <usergroup>
    ```

    1. `gpuv1` requests a V100 GPU. Use `gpua1` instead to request an A100 GPU.

### Video Tutorial

Watch the full video guide where we demonstrate:

- Submitting a one-line job with `qsub`
- Using PBS scripts

Submitting jobs to HPC:

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Submitting_jobs_to_HPC_704ea11d9c.mp4" type="video/mp4"></video>

## Job Policies and Limits on HPC cluster

The Computerome HPC cluster uses the **Moab/Torque queueing system** to manage resources.
To ensure fair usage and reliable operation, the following policies apply:

### Job Submission

- You **must specify** both a **group list** and an **account** when submitting jobs.
- You can only run jobs under **groups you are a member of**.

### Node Access

- Nodes are **not shared between users**.
    - Only one user’s jobs can run on a node at a time.
    - A user may run multiple jobs on the same node if resources allow.
- Even if you request **fewer CPU cores** than the node provides, the **entire node is reserved for you**.
    - No other user will be scheduled on that node.
    - You will be charged for a **full node**, regardless of how many cores you use.
    - Best practice: make full use of the node by running a single large job or multiple smaller jobs in parallel.

### Storage Awareness

- The queueing system is **not aware of storage or permissions**.
    - If your job writes to a directory you don’t have permission for, the job will not fail automatically.
    - Jobs may continue running without producing results.
- Always check your directory permissions and available space before submitting jobs.

### Resource Limits

- Jobs continue running as long as they stay within the requested **CPU, memory, and walltime**.
- If your job exceeds these limits, it will be terminated.

### Job Completion

- The queueing system may report a job as **successfully completed** even if the operating system encountered an error.
- It is your responsibility to:
    - Check your job’s **output (`.out`) and error (`.err`) files**.
    - Verify that results are correct and complete.

### Job Arrays

- If you need to run many similar jobs, use **job arrays** instead of submitting hundreds of individual jobs.
- Job arrays are more efficient and reduce scheduling overhead.

## Interactive Jobs on HPC cluster

An **interactive job** gives you temporary exclusive access to a compute node through the queueing system.
Instead of submitting a script and waiting for results, you are placed directly into a shell session on a reserved node.

### Why Use Interactive Jobs?

- **Testing and debugging**
    - Interactive jobs are ideal for trying out commands, testing scripts, or debugging workflows before running them at scale.
- **Avoiding login node restrictions**
    - Login nodes are shared by all users and have strict policies that prevent running intensive tasks.
    - By using an interactive job, you avoid overloading the login nodes.
- **Exclusive resources**
    - The node you reserve is dedicated to you for the duration of your job.
    - You can experiment freely without affecting other users.

### Interactive Job Video Guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Interactive_Job_a2d99f0822.mp4" type="video/mp4"></video>

## Reservation on HPC cluster

In the HPC cluster, you can request a **reservation**.
A reservation means that one or more compute nodes are set aside **exclusively for your group** for a specified amount of time.

### Why Use Reservations?

- Reservations allow you to **skip the queue** and guarantee immediate access to the nodes you need.
- However, be aware that when you reserve nodes, you are **charged for the entire reservation period**, even if the nodes are idle or underused.

### How to Request a Reservation

1. Send a request to Computerome Support.
    - Include the **group name** the reservation is for.
    - Specify the **duration** of the reservation.
2. Once the reservation is created, you will be informed of the reserved node(s).

### Using a Reserved Node

After a node is reserved for your group, you can access it in the following ways:

=== ":lucide-terminal: Interactive session"

    ```bash
    qsub -I -W group_list=demo -A demo -l nodes=g-01-c0004
    ```

=== ":lucide-file-code: Batch job"

    ```bash
    qsub -W group_list=demo -A demo -l nodes=g-01-c0004:ppn=40,mem=180gb,walltime=7200 job.sh
    ```

## Job Monitoring on HPC cluster

Monitoring your jobs is critical to ensure they run correctly and to avoid wasted compute time and unexpected charges.
The queueing system only monitors **resource usage** (CPU, memory, walltime).
It does **not** check whether your code is producing the expected results or if storage/permission errors occur.

This means you are responsible for verifying that your jobs complete successfully.

### Queueing System Monitoring (Torque/Moab)

Use the following commands to check the status of your jobs:

| Command | Purpose |
| --- | --- |
| `qstat -u <username>` | List your jobs |
| `checkjob <jobid>` | Detailed job info |
| `showq` | View queue status |

### Best Practices in Job Scripts

To avoid silent failures (e.g., permission denied, missing files, storage full), we strongly recommend adding checks in your job scripts:

- **Enable error handling** at the top of your script:

    ```bash
    set -euo pipefail
    ```

    This ensures the script stops immediately if a command fails.

- **Check input files** before running:

    ```bash
    if [ ! -f "input.txt" ]; then
        echo "ERROR: Input file not found!"
        exit 1
    fi
    ```

- **Check write permissions** before writing:

    ```bash
    touch /home/projects/<project>/testfile || {
        echo "ERROR: Cannot write to project directory!"
        exit 1
    }
    rm /home/projects/<project>/testfile
    ```

- **Log job details** for debugging:

    ```bash
    echo "Running on host: $HOSTNAME"
    echo "Job ID: $PBS_JOBID"
    echo "Date: $(date)"
    ```

These checks help catch OS-level and storage-level errors **while the job is running**, instead of discovering failures only at the end.

### Usage Monitoring

Computerome provides **daily usage reports**, updated nightly.

- You can check your compute and storage usage under **My Solutions > HPC**.
- Please review your usage regularly.
- If you notice abnormalities (e.g., a job consuming resources but failing to produce results), report it **immediately**.

!!! warning

    Once an invoice has been sent, we cannot exclude jobs from billing — it is your responsibility to monitor and report problems in time.

!!! abstract "Summary"

    - Use `qstat`, `checkjob`, and `showq` to monitor job state.
    - Add error handling and checks inside your scripts to detect OS/storage issues.
    - Review daily usage reports and report anomalies quickly.
