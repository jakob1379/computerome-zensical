---
title: "Cloud Storage"
description: "Each Cloud project is provisioned with a dedicated NFS directory that is automatically mounted (via NFSv4) when a VM is created. All VMs inside your Cloud have this directory mounted by default."
icon: lucide/cloud
tags:
  - Cloud
---

# Cloud Storage

## Cloud NFS storage

Each Cloud project is provisioned with a dedicated **NFS directory** that is automatically mounted (via NFSv4) when a VM is created. All VMs inside your Cloud have this directory mounted by default.

Access management is handled via standard **POSIX Linux permissions**.

- As a **Technical or Legal Owner**, you can request the ability to override file ownership (root-level access to all data).

!!! warning "Root-level access"

    This feature is disabled by default. If enabled, **any root user on any VM in your Cloud will have full access to all files and directories** under the NFS directory. Please contact us if you wish to enable this option.

### Cloud Directory Structure

The NFS directory is created with the following default structure and permissions.

While you may delete or modify these directories, be aware that the **Import/Export feature relies on this default structure**.
Read more about Import/Export procedures here: *[Secure Import and Export](#cloud-secure-import-and-export)*

`/dp<project-shortname>/data`

:   - Intended for the Technical/Legal Owner.
    - Owners can place data here.
    - All other users have **read-only access** (so they can copy files to their own directories).

`/dp<project-shortname>/home`

:   - Each time a new user is invited to the Cloud, their **home directory** is created here.

`/dp<project-shortname>/people`

:   - Contains system-created directories for each user.
    - Used by the **Import/Export procedures**.

`/dp<project-shortname>/shared`

:   - For sharing files among project members.
    - Each user has their own subdirectory here.
    - Includes a `group/` subdirectory where **all project members can share files at group level**.

!!! abstract "Summary"

    - **Default structure** is strongly recommended if you plan to use Import/Export.
    - Owners may restructure directories, but changes affect usability and security.
    - Permissions and access can be adjusted by the Technical/Legal Owner, with optional root-level access available upon request.

### Cloud Backup and Restore Files

All NFS files and directories are protected by an automated **snapshot mechanism**, which allows you to restore files to previous versions. Snapshots are taken at different intervals and retained for varying durations:

| Snapshot | Retained for      | This means you always have                   |
| -------- | ----------------- | -------------------------------------------- |
| Hourly   | The past 12 hours | Hourly versions of your files (up to 12 hours back) |
| Daily    | The past 7 days   | Daily versions of your files (up to 7 days back)    |
| Weekly   | The past 4 weeks  | Weekly versions of your files (up to 4 weeks back)  |

#### How to Restore Files

1. Navigate to the directory where the file last existed:

    ```console
    $ cd /dp<project-shortname>/<path-to-directory>
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
    $ cp myfile.txt /dp<project-shortname>/<target-directory>/
    ```

## Cloud Local Storage

Each VM that you deploy in your Cloud project comes with a default **50 GB of local storage** for the root (`/`) partition. This storage is **free of charge** but limited in size.

### Important Notes

- **Responsibility**:
  You are responsible for monitoring and maintaining free space on your VM.

    - Use `df -h` to check usage.
    - Ensure that installed tools and applications store **all data on your NFS directory** (`/dp<project-shortname>`), not on the local root disk.

- **No Backups**:
  Local storage is **not included in backups or snapshots**.

    - If a VM is deleted, rebuilt, or corrupted, all data stored locally will be lost.
    - Always store data on the NFS directory for persistence and recovery.

- **Docker Usage**:
  If you plan to use Docker inside your VM, you need to downgrade the NFS mount to **NFSv3**.

    - This can be done by editing your `/etc/fstab` file and remounting the directory.

- **Expanding Local Storage**:
  By default, the root partition is 50 GB. If you require more space or additional local volumes, please contact support. Be aware that **extra volumes are also not backed up** by default.

!!! tip "Best Practice"

    - Keep the root partition for the **operating system and minimal application installs only**.
    - Store **all user data, project files, and outputs on the NFS directory**.
    - Treat local storage as **temporary scratch space**, not as a long-term data store.

## Cloud Secure Import and Export

Data movement into and out of Cloud projects is managed through a secure approval-based workflow. This ensures that all transfers are tracked, auditable, and approved by project owners before completion.

=== ":lucide-download: Import Procedure"

    1. Log in to [https://computerome.dk](https://computerome.dk).
    2. Open the **My Solutions > Data Import/Export/Transfer** menu.
    3. Click on the **Import** tile.
    4. Click **Create New Import**.
    5. Select the project where you want to import data.
    6. Write a description for the request (e.g., what files you are importing).
    7. Click **Create** to submit the request.

    Approval process:

    - The **Legal Owner** or **Technical Owner(s)** of the project will log in and open **My Solutions > Assignments**.
    - The approver opens the request.
    - If the request is **approved**, the data is imported. If it is **rejected**, the transfer is cancelled.

    Imported files are automatically moved to:

    `/dp<project-shortname>/people/<username>/import/<random-generated-request-id>/`

=== ":lucide-upload: Export Procedure"

    1. Copy or move the files you want to export into `/dp<project-shortname>/people/<username>/export/`.
    2. Log in to [https://computerome.dk](https://computerome.dk).
    3. Open the **My Solutions > Data Import/Export/Transfer** menu.
    4. Click on the **Export** tile.
    5. Click **Create New Export**.
    6. Select the project you want to export data from.
    7. Write a description for the request (e.g., what files you are exporting).
    8. Click **Create** to submit the request.

    Approval process:

    - The **Legal Owner** or **Technical Owner(s)** of the project will log in and open **My Solutions > Assignments**.
    - The approver opens the request.
    - If the request is **approved**, the files are staged and made available for download as a **single ZIP file**. If it is **rejected**, the transfer is cancelled.

    !!! note

        When an export request is created, files under
        `/dp<project-shortname>/people/<username>/export/`
        are automatically moved to a **staging area** that the user cannot access. This ensures no additional files are added to the request while it is awaiting approval.

:lucide-monitor-play: **Cloud Import Export video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Cloud_Import_Export_7bde903d1e.mp4" type="video/mp4"></video>

## Cloud File Manager

The **Cloud File Manager** is available under
**My Solutions > Data Import/Export/Transfer**.

This graphical interface allows you to:

- Browse your files and folders under the NFS directory.
- Move files around (if your project is not restricted).
- Directly upload and download files (if your project is not restricted).
- Share files with collaborators — even if they do **not** have a Computerome account (if your project is not restricted).

If your Cloud project is **restricted** (as configured by the Legal/Technical Owner), the File Manager only allows navigation and viewing. Upload/download functionality will be disabled.

!!! note

    The File Manager respects **POSIX permissions**.
    If you do not have access to a file under the NFS directory, you will not be able to see or access it in the File Manager.

:lucide-monitor-play: **Cloud File Manager video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Cloud_File_Manager_5c73bd563e.mp4" type="video/mp4"></video>
