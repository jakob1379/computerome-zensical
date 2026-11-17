---
title: "HPC Software"
description: "The Environment Module system is used in both Cloud and HPC environments at Computerome to deliver preinstalled tools to our users."
icon: lucide/server
tags:
  - HPC
---

# HPC Software

## HPC Environment Modules

The **Environment Module system** is used in both **Cloud** and **HPC** environments at Computerome to deliver preinstalled tools to our users.

If you would like to install tools that need to be accessible across multiple nodes, we recommend using **Environment Modules**.

!!! note

    Using Environment Modules and preinstalled tools requires a solid understanding of **Linux**, **software installation**, and **environment variables**.

For general documentation on Environment Modules, see the
[Environment Modules Documentation](https://modules.readthedocs.io/en/latest/). For the
commands available on Computerome, see the [Module Environment Guide](module-environment-guide.md).

### Compatibility

- Tools installed by Computerome are compiled against the **Rocky Linux kernel**.
- In rare cases, if a tool is incompatible with a standard Red Hat–based kernel, it cannot be installed on our HPC environment.

### Requesting new software

To request installation of new software (or another version of an existing tool), please send an email to **Computerome Support** from your **registered email address in Computerome**.

Use the following template:

- **Subject line**: *Software Request, including the tool name*
- **Body**:
    - Tool name
    - Version (if applicable)
    - Homepage, please note that version locations, install guides or other sub-sections are not as relevant, since they often do not fit the Computerome environment
    - Any additional relevant details

### Environment modules video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Custom_Tool_a441c48186.mp4" type="video/mp4"></video>

!!! note

    This video demonstrates the basic commands and is intended to familiarize you with the system.

## HPC RStudio Server

You can request your own **dedicated RStudio Server** in the HPC cluster.
Because RStudio is not designed to be delivered as an Environment Module or to run easily within a queueing system, we have created custom integrations to make it available to you.

!!! info "Important notes"

    1. Always use the **latest version** available.
    2. Be aware that **RStudio** (desktop IDE) is different from **RStudio Server**. This guideline covers **RStudio Server** only.
    3. Pay close attention to the **R version** used by your RStudio Server.
        - When requesting installation of new R libraries, always specify the **R version**, not the RStudio Server version.

### RStudio Server on HPC video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Rstudio_server_on_HPC_ee82946564.mp4" type="video/mp4"></video>

## HPC Jupyter Notebook Server

You can request your own **dedicated Jupyter Notebook server** in the HPC cluster.
Similar to RStudio, Jupyter is not designed to run natively as an Environment Module or within a queueing system, so we have implemented custom integrations to make it available to you.

!!! info "Important notes"

    1. Always use the **latest version** available.
    2. Be aware that this guideline is about **Jupyter Notebook servers**, not local desktop installations.

### Jupyter Notebook on HPC video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Jupyter_Notebook_on_HPC_5acb825199.mp4" type="video/mp4"></video>

## HPC VS Code Server

You can request your own **dedicated VS Code Server** in the HPC cluster.
Like RStudio and Jupyter, VS Code web server is not designed to run directly as an Environment Module or within a queueing system, so we have implemented custom integrations to make it available for remote use.

!!! info "Important notes"

    1. Always use the **latest version** available.
    2. This guideline refers specifically to the **VS Code Server** (web-based/remote version), not the desktop VS Code client.
    3. Be mindful of the **extensions and plugins** you enable in VS Code Server, as some may consume significant resources.
    4. For heavy computations, always submit jobs through the **queueing system**, not directly within VS Code Server.

### Visual Studio Code on HPC video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/vs_Code_on_HPC_83e3857e55.mp4" type="video/mp4"></video>

## HPC Custom Tool Installation

If you decide not to use the **preinstalled tools repository**, you can install your own tools under your **project directory**.
Your project directory is accessible on all compute nodes, making it a suitable place for custom installations.

!!! warning "Important notes"

    - **Support**:
        - Computerome does **not** provide support for custom tool installation.
        - Installation, configuration, and ongoing maintenance are entirely your responsibility.
    - **Complexity**:
        - The example video below demonstrates installation of a **very simple tool**.
        - More advanced software often requires a **deep understanding** of:
            - Linux system administration
            - Tool installation in Linux
            - Compilers and libraries
            - Environment Modules
    - Make sure you have sufficient experience before attempting complex tool installations.

### Custom tool installation video guideline

<video controls preload="metadata" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Custom_Tool_a441c48186.mp4" type="video/mp4"></video>
