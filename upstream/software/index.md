---
title: "Software"
description: "We generally use Environment Modules in both our Cloud and HPC environments to deliver preinstalled tools to our users. While we take care of the installation and availability of these tools, it is the user\u2019s responsibility to have a working understanding of the tools they use."
---

# Software

In the following section, you will see the different solutions for having your tools available in Computerome.

We generally use [**Environment Modules**](module-environment-guide.md) in both our [**Cloud**](cloud-software.md) and [**HPC**](hpc-software.md) environments to deliver preinstalled tools to our users.
While we take care of the **installation and availability** of these tools, it is the user’s responsibility to have a **working understanding of the tools they use**.

**Important Considerations**

Every tool comes with its own **configuration requirements**.
Simply loading a module does not complete the job for you. You need to understand:

- What the tool does.
- How it behaves in a **Linux environment**.
- What default configurations may affect your work.

**Example: R**

When you use **R**, it automatically creates hidden directories and files under your **home directory** (`/home/people/<username>`), such as:

- `~/.R/` → runtime options
- `~/.Rhistory` → command history
- `~/.RData` → saved workspace (if enabled)
- `~/.cache/R/` or `~/.local/share/R/` → caches for certain packages
- `~/R/` → default location for user-installed R packages

Because your home directory has a **hard quota of 10 GB**, these files can quickly fill it up.
If the quota is exceeded:

- Jobs may fail with errors like *“cannot write to directory”* or *“no space left on device.”*

**Recommended Solution**

To avoid filling up your home directory:

1. **Redirect R default directories to your project directory** (which has no hard quota).
2. **Clean or disable unnecessary files** like `.RData` and `.Rhistory`.

You can configure this permanently by adding the following line to your `~/.Renviron` file:

`R_LIBS_USER="/home/projects/<project-name>/apps/Rlibs"`

**Key Takeaway**

You must always be **on top of the tools you are using**:

- Learn how they behave in the Linux environment.
- Adjust their configurations to fit Computerome’s limitations (e.g., home quota, project storage, job scheduling).
- This will help you avoid **failures** and **unwanted costs**.
