---
title: Home
description: User documentation for Computerome HPC and Cloud. Accounts, 2FA, projects, compute, storage, software and running jobs.
hide:
  - navigation
  - toc
---

# Computerome Wiki

Computerome is the Danish national supercomputer for life sciences. This wiki
covers everything you need to work on the platform, whether you are a
**Cloud user**, an **HPC user**, or both.

!!! question "Not sure which kind of user you are?"

    Sign in at [computerome.dk](https://computerome.dk) and open
    **My Solutions**. The **Cloud** and **HPC** menus list the projects you are
    a member of. You may have a separate username for each.
    [Read more](getting-started/index.md).

## Start here

<div class="grid cards" markdown>

-   :lucide-rocket:{ .lg .middle } **Getting Started**

    ---

    Create your account, log in for the first time and learn who is
    responsible for what.

    [:octicons-arrow-right-24: First-time login](getting-started/first-time-login.md)

-   :lucide-shield-check:{ .lg .middle } **Two Factor Authentication**

    ---

    2FA is mandatory for every HPC and Cloud login. Set up the privacyIDEA app
    and enroll your tokens.

    [:octicons-arrow-right-24: Set up 2FA](two-factor-authentication-2fa.md)

-   :lucide-folder-kanban:{ .lg .middle } **Managing Projects**

    ---

    Invite users, manage groups and understand how Cloud and HPC projects are
    billed.

    [:octicons-arrow-right-24: Projects](managing-projects/index.md)

-   :lucide-cpu:{ .lg .middle } **Compute**

    ---

    Log in to the HPC cluster or your Cloud VMs, and pick the right node type
    for your work.

    [:octicons-arrow-right-24: Compute](compute/index.md)

-   :lucide-hard-drive:{ .lg .middle } **Storage**

    ---

    Project directories on 50 PB of NFS storage, snapshots, and secure
    import/export.

    [:octicons-arrow-right-24: Storage](storage/index.md)

-   :lucide-package:{ .lg .middle } **Software**

    ---

    Find and load preinstalled tools with Environment Modules, or install your
    own.

    [:octicons-arrow-right-24: Software](software/index.md)

-   :lucide-list-checks:{ .lg .middle } **Running Jobs**

    ---

    Submit batch, array and interactive jobs with SLURM or Moab/Torque, or use
    Open OnDemand in the browser.

    [:octicons-arrow-right-24: Running jobs](running-jobs/index.md)

-   :lucide-tags:{ .lg .middle } **Browse by tag**

    ---

    Every page is tagged by platform (Cloud, HPC) and topic.

    [:octicons-arrow-right-24: Tags](tags.md)

</div>

## Quick reference

=== "HPC"

    | What | Where |
    | --- | --- |
    | SSH login (Moab/Torque) | `ssh <username>@ssh.computerome.dk`, see [HPC compute](compute/hpc-compute.md) |
    | SSH login (SLURM) | `ssh <username>@hpc.computerome.dk`, see [SLURM](running-jobs/slurm.md) |
    | Graphical desktop | `desktop.computerome.dk` with the [ThinLinc client](https://www.cendio.com/thinlinc/docs/install) |
    | Web portal | [Open OnDemand](running-jobs/open-on-demand.md) |
    | Job scheduler | [Moab/Torque](running-jobs/hpc-queueing-system-moab-torque.md), [SLURM](running-jobs/slurm.md) |
    | Storage | [HPC storage](storage/hpc-storage.md) |

=== "Cloud"

    | What | Where |
    | --- | --- |
    | Desktop login | Omnissa Horizon Client from [vdi.computerome.dk](https://vdi.computerome.dk) |
    | Your VMs | SSH from the Horizon desktop, see [Cloud compute](compute/cloud-compute.md) |
    | Storage | [Cloud storage](storage/cloud-storage.md) |
    | Software | [Cloud software](software/cloud-software.md) |

!!! tip "Need help?"

    Check the [server status](https://computerome.dk/server-status) for
    maintenance windows, or [contact Computerome support](https://computerome.dk/contact-us).
