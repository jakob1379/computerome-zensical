---
title: "Cloud Software"
description: "The Environment Module system is used in both Cloud and HPC environments at Computerome to deliver preinstalled tools to our users."
icon: lucide/cloud
tags:
  - Cloud
---

# Cloud Software

## Cloud Environment Modules

The **Environment Module system** is used in both **Cloud** and **HPC** environments at Computerome to deliver preinstalled tools to our users.

If you wish to install tools that should be accessible across multiple nodes, we also recommend using Environment Modules.

!!! note

    Using Environment Modules (and the preinstalled tools) requires a solid understanding of **Linux**, **software installation**, and **environment variables**.

For general documentation on Environment Modules, see the
[Environment Modules Documentation](https://modules.readthedocs.io/en/latest/). For the
commands available on Computerome, see the [Module Environment Guide](module-environment-guide.md).

### Compatibility

- Tools installed by Computerome are compiled against the **Rocky Linux kernel**.
- In the Cloud environment, you may choose **any Linux distribution** (including Ubuntu).
    - Our preinstalled tools will **not** work on Ubuntu.
    - If you wish to use our shared repository of tools, you must use **Rocky Linux**.
    - You can still set up Environment Modules on other distributions, but you will need to configure everything from scratch.

### Requesting new software

If you need us to install a new tool (or another version of an existing tool), please send an email request to **Computerome Support** from your **registered email address in Computerome**.

Use the following template:

- **Subject line**: *Software Request, including the tool name*
- **Body**:
    - Tool name
    - Version (if applicable)
    - Homepage, please note that version locations, install guides or other sub-sections are not as relevant, since they often do not fit the Computerome environment
    - Any other relevant details

### Environment modules video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Services_tools_66e901c5cb.mp4" type="video/mp4"></video>

!!! note

    The demo is recorded on our HPC cluster, but the same principles apply to Rocky Linux in Cloud.

## Cloud Custom Tools Installation

In your **Cloud environment**, you have **root access** and can install any tools you like.
However, there are several important considerations.

### Storage considerations

- Each VM comes with **50 GB of local storage** (root partition), which is **free of charge**.
- This space is limited and not intended for large-scale tool installations or data.
- Always redirect the **data directories** of your tools to the **NFS project directory**.

!!! example "Example: Docker"

    If you install **Docker**, ensure that Docker **volumes** and **images** are stored in your NFS directory rather than on the root partition.

It is different from tool to tool how you configure data to be stored on NFS.
Please check the **official documentation** of each tool to determine how to set the correct storage path.

### Support and responsibility

- Tools you install yourself are **not supported by Computerome**.
- We can provide **consultancy hours** to assist with installation if needed.
- After installation, tools are **handed over to you** with an installation document.
- From that point onward, **you are responsible** for maintenance and troubleshooting.

### Best practices

- Whenever possible, install your tools using **Environment Modules**.
    - This ensures they are stored in your NFS directory.
    - It also makes sharing and managing tools easier.
- If Environment Modules are not suitable, you may install tools using the **standard installation process**.

### Custom tool installation video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Custom_Tool_a441c48186.mp4" type="video/mp4"></video>

!!! note

    The example is recorded on our HPC cluster, but the same process applies in Cloud environments. For detailed instructions, see the official [Environment Modules documentation](https://modules.readthedocs.io/en/latest/).
