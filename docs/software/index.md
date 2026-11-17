---
title: "Software"
description: "We generally use Environment Modules in both our Cloud and HPC environments to deliver preinstalled tools to our users. While we take care of the installation and availability of these tools, it is the user’s responsibility to have a working understanding of the tools they use."
icon: lucide/package
---

# Software

In the following section, you will see the different solutions for having your tools available in Computerome.

<div class="grid cards" markdown>

-   :lucide-cloud:{ .lg .middle } **Cloud Software**

    ---

    Environment Modules on Rocky Linux VMs, requesting new software, and
    installing your own tools with root access.

    [:octicons-arrow-right-24: Cloud software](cloud-software.md)

-   :lucide-server:{ .lg .middle } **HPC Software**

    ---

    Environment Modules, RStudio Server, Jupyter Notebook and VS Code Server on
    the HPC cluster, and custom tool installation.

    [:octicons-arrow-right-24: HPC software](hpc-software.md)

-   :lucide-terminal:{ .lg .middle } **Module Environment Guide**

    ---

    Find, load and manage preinstalled tools with the `module` command.

    [:octicons-arrow-right-24: Module guide](module-environment-guide.md)

</div>

We generally use **Environment Modules** in both our **Cloud** and **HPC** environments to deliver preinstalled tools to our users.
While we take care of the **installation and availability** of these tools, it is the user’s responsibility to have a **working understanding of the tools they use**.

## Important considerations

Every tool comes with its own **configuration requirements**.
Simply loading a module does not complete the job for you. You need to understand:

- What the tool does.
- How it behaves in a **Linux environment**.
- What default configurations may affect your work.

## Example: R

When you use **R**, it automatically creates hidden directories and files under your **home directory** (`/home/people/<username>`), such as:

| Path | Contents |
| --- | --- |
| `~/.R/` | Runtime options |
| `~/.Rhistory` | Command history |
| `~/.RData` | Saved workspace (if enabled) |
| `~/.cache/R/` or `~/.local/share/R/` | Caches for certain packages |
| `~/R/` | Default location for user-installed R packages |

!!! warning "Home directory quota"

    Because your home directory has a **hard quota of 10 GB**, these files can quickly fill it up.
    If the quota is exceeded, jobs may fail with errors like `cannot write to directory` or `no space left on device`.

### Recommended solution

To avoid filling up your home directory:

1. **Redirect R default directories to your project directory** (which has no hard quota).
2. **Clean or disable unnecessary files** like `.RData` and `.Rhistory`.

You can configure this permanently by adding the following line to your `~/.Renviron` file:

```bash title="~/.Renviron"
R_LIBS_USER="/home/projects/<project-name>/apps/Rlibs"
```

## Key takeaway

You must always be **on top of the tools you are using**:

- Learn how they behave in the Linux environment.
- Adjust their configurations to fit Computerome’s limitations (e.g., home quota, project storage, job scheduling).
- This will help you avoid **failures** and **unwanted costs**.
