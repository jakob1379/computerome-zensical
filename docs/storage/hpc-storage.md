---
title: "HPC Storage"
description: "Each HPC project receives a dedicated NFS directory, which is automatically mounted on all login nodes and compute nodes."
icon: lucide/server
tags:
  - HPC
---

# HPC Storage

## HPC NFS Storage

Each HPC project receives a dedicated **NFS directory**, which is automatically mounted on all login nodes and compute nodes.
The directory path follows this format:

`/home/projects/<Project-name>`

### Permissions

- The directory uses **basic POSIX permissions** (not ACL).
- Ownership:
    - The **user owner** is by default the person who created the project in the web interface.
    - The **group owner** corresponds to the HPC project group.
- All project members have **read access** to the main project directory.

!!! note

    If you do **not** wish to remain the owner of the directory and want to delegate ownership to one of your Technical Owners, please contact us immediately after project creation.

    - Provide the username of the person you want as the new owner.
    - If you delay, replacing ownership later can take a long time depending on the number of files already stored.

### HPC Directory Structure

When a new project is created, the following subdirectories are automatically generated:

`/home/projects/<project-name>/apps`

:   For tools that you would like to install and share with your project members.
    *(See the [Tools Installation Guide](../software/hpc-software.md#hpc-custom-tool-installation))*

`/home/projects/<project-name>/data`

:   For sharing data between all project members.

`/home/projects/<project-name>/people/`

:   - Each time a new user is added to the project, a personal directory is created for them: `/home/projects/<project-name>/people/<username>`
    - This directory is intended for that specific user’s files within the project.
    - It simplifies user offboarding — you can remove their files if they leave.
    - It also allows you to monitor storage usage per user using standard Linux commands.

### HPC Backup and Restore Files

All NFS files and directories are protected by an automated **snapshot mechanism**, which allows you to restore files to previous versions. Snapshots are taken at different intervals and retained for varying durations:

| Snapshot | Retained for      | This means you always have                   |
| -------- | ----------------- | -------------------------------------------- |
| Hourly   | The past 12 hours | Hourly versions of your files (up to 12 hours back) |
| Daily    | The past 7 days   | Daily versions of your files (up to 7 days back)    |
| Weekly   | The past 4 weeks  | Weekly versions of your files (up to 4 weeks back)  |

#### How to Restore Files

1. Navigate to the directory where the file last existed:

    ```console
    $ cd /home/projects/<project-name>/<path-to-directory>
    ```

2. List the available snapshots:

    ```console
    $ ls .snapshots
    @GMT-2025.09.06-21.02.22
    @GMT-2025.09.06-22.02.22
    ...
    ```

    Each entry corresponds to the date and time the snapshot was taken.
    For example, `@GMT-2025.09.06-21.02.22` is the snapshot from 21:02 on September 6, 2025.

3. Change into the snapshot directory:

    ```console
    $ cd .snapshots/@GMT-2025.09.06-21.02.22
    ```

4. Locate the file you want to restore, then copy it back to your working directory:

    ```console
    $ cp myfile.txt /home/projects/<project-name>/<target-directory>/
    ```

### HPC Quotas

| Directory               | Quota                     | Cost                |
| ----------------------- | ------------------------- | ------------------- |
| Project directories     | **No quotas**             | **Pay-as-you-go**   |
| User home directories   | **Hard quota of 10 GB**   | **Free of charge**  |

- Please make sure you **regularly monitor your storage usage** of project directories to avoid unexpected charges on your invoices.
- Each user has a **personal home directory**. Exceeding its quota will block login until space is freed.

Please review:

- [Storage Usage Guide](../managing-projects/hpc-projects.md#hpc-usage)
- [Shared Responsibility Matrix](../getting-started/roles-and-responsibilities.md#shared-responsibility-matrix)

## HPC Scratch

Each compute node has a local **scratch directory** with a limited size of **390 GB**, located at `/scratch`.

This space is designed for **temporary files** during job execution.

- When you submit a job, the queueing system automatically creates a subdirectory for that job: `/scratch/$JOB_ID`
- You can use this directory inside your scripts for **fast I/O**, as scratch resides on local SSD disks.
- This directory is **temporary** and is automatically deleted once your job terminates.
  Do **not** use it as permanent storage.

!!! warning "Important Notes"

    - The `/scratch` directory is **shared by all users**.
    - If you place files directly under `/scratch` (outside your job subdirectory), the queueing system will **not** remove them.
    - This may create **security risks**, since other users could potentially access your files.
    - Always ensure there is **enough space** for your temporary files before running jobs.
    - If the scratch disk becomes full, your job may fail with errors such as *"Permission denied"* or *"No space left on device"*.

See also:

- [How to Run Jobs](../running-jobs/hpc-queueing-system-moab-torque.md#submit-jobs-to-hpc-cluster)

## HPC SFTP File Transfer

Computerome provides a **shared SFTP server** for all HPC users to transfer files in and out of the system.

| Setting            | Value                                                 |
| ------------------ | ----------------------------------------------------- |
| **Hostname**       | `transfer.computerome.dk`                             |
| **Port**           | `22`                                                  |
| **Authentication** | Your Computerome username, password, and 2FA token    |
| **Access**         | Available from **anywhere on the Internet**           |

### Notes

- This transfer node is **shared** between all users and is **free of charge**.
- Performance depends on the number of concurrent transfers — it may be fast or slow at times.
- Always ensure you have a **stable internet connection** when transferring large files, as interruptions may cause failures.

:lucide-monitor-play: **HPC SFTP File Transfer video guideline**

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/HPC_File_Transfer_5a85479e39.mp4" type="video/mp4"></video>

## HPC File Manager

Computerome also provides a **graphical file transfer interface** based on **Nextcloud**.
This interface allows you to:

- Transfer files via **HTTPS**.
- Browse and manage files with a graphical view.
- Share files with collaborators, even if they do **not** have a Computerome account.

### Important Notes

- Since the protocol is **HTTPS**, transferring **large files** or **too many small files** is **not recommended**.
  For such cases, please use the **SFTP service** instead.
- This interface is designed for convenience, collaboration, and occasional transfers, not for heavy data movement.
- Access is **not enabled by default**.
  Please contact us if you would like to enable this feature for your project.

:lucide-monitor-play: **HPC NextCloud FileManagement video guideline**

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Next_Cloud_File_Management_d2eff035ee.mp4" type="video/mp4"></video>
