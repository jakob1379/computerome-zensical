---
title: "HPC Projects"
description: "Learn how to manage your HPC projects at Computerome."
tags:
  - HPC
---

# HPC Projects

## HPC Project Creation

### Creating a New Project (Legal Owner)

If you request a new project, you will automatically become its **Legal Owner**.

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > HPC > Applications**
3. Complete the application steps.
4. After submission, our Administration team will:
    - Review your application.
    - Contact you to arrange contracts and paperwork.
    - Approve the project, after which it will be created.

**Create HPC project video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Creat_HPC_project_668b504814.mp4" type="video/mp4"></video>

---

### Invite new users

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > HPC > [Project Name] > Members tab**
3. From here, you can:
    - Add a **Technical Owner**
    - Add a **Security Contact**
    - Add a **Normal Member**

!!! note

    You will need each user’s **username**.

    - If they don’t have an account yet, ask them to create one first (see the [Account Creation Guide](../getting-started/first-time-login.md#first-time-login)) and send you their username.

**HPC user invite video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/HPC_user_invite_57526bbf88.mp4" type="video/mp4"></video>

---

## Group Management

As a **Legal Owner** or **Technical Owner**, you are responsible for managing memberships in your HPC groups for keeping the membership of your HPC groups up to date.

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > HPC > [Group Name] > Members tab**
3. Here you can view, add, or remove members of your group.

**HPC Group Modification video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/HPC_Group_Modification_e137cdfacb.mp4" type="video/mp4"></video>

---

## HPC Usage

As the **Legal Owner** or **Technical Owner** of a project, you are responsible for monitoring your project’s compute and storage usage on a regular basis.

Note: You are only billed for the duration but not the walltime specified.

- Any **abnormal activity** must be reported to Computerome **immediately**.
- Please note: **Computerome does not take any action after the invoice has been issued**.

To monitor compute and storage usage for your HPC group:

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > HPC > View detailed usage**

---

### HPC Cost Calculation

!!! info "Note on Billing Hours"

For all CPU/GPU/storage usage, Computerome uses a standardized month length of **730.5 hours** (the yearly average), rather than the actual number of hours in each month.
This ensures consistent billing across months with different lengths (28, 30, or 31 days).
As a result, there may be a small difference between detailed day-by-day calculations and the official billing.

### Cost Components

In our HPC environment, costs are calculated based on:

- **CPU core hours** (from standard CPU nodes)
- **GPU core hours** (from GPU nodes – Type 1 and Type 2)
- **Average storage usage (per GB per day)**

### Exclusivity Policy

When you run jobs on a node, the **entire node is reserved for your user** during the time your jobs run on it — even if your jobs use fewer CPU cores than the node provides.
You can run multiple jobs on the same node (as long as the requested resources fit), but you are billed for the **full node capacity** that is reserved.

- Standard CPU node → **40 cores per node**
- GPU Type 1 node → **40 CPU cores** (+ 1 V100 GPU, 16 GB)
- GPU Type 2 node → **20 CPU cores** (+ 1 A100 slice, 20 GB)

Billing reflects the **reserved cores** across the nodes you occupy, not just the per-job core requests.

**Example Scenario 200 jobs in total in a 30‑day month**

**Standard CPU Jobs**

- **150 jobs**, each using **1 CPU core** for **1 hour**.
- With exclusivity, these can be packed onto nodes as follows:
    - 40 cores on node 1, 40 on node 2, 40 on node 3, **30 on node 4** (10 cores unused).
- **Billed cores**: `ceil(150 / 40) = 4 nodes` → `4 × 40 = 160 cores` for **1 hour**.

**Total cost for CPU jobs = 160 core‑hours × CPU core‑hour unit price**

**GPU Type 1 Jobs**

- **50 jobs** (assume 1 hour).
- GPU Type 1 node has **40 CPU cores**.
- Packing with exclusivity: `ceil(50 / 40) = 2 nodes` → **80 reserved CPU cores** for **1 hour**.

**Total cost for GPU Type 1 jobs = 80 GPU core‑hours × GPU core‑hour unit price**

**GPU Type 2 Jobs**

- **30 jobs** (assume 1 hour).
- GPU Type 2 node has **20 CPU cores**.
- Packing with exclusivity: `ceil(30 / 20) = 2 nodes` → **40 reserved CPU cores** for **1 hour**.

**Total cost for GPU Type 2 jobs = 40 GPU core‑hours × GPU core‑hour unit price**

!!! note

    The examples above assume the jobs overlap within the same hour so they occupy the shown number of nodes concurrently. In practice, billing is based on the *actual reservation timeline* — i.e., how jobs were placed and overlapped on nodes over time.

**Storage**

- First 5 days: **1000 GB (1 TB)**
- Next 15 days: **500 GB**
- Last 10 days: **700 GB**

**Calculation:**

(5 × 1000) + (15 × 500) + (10 × 700)
= 5000 + 7500 + 7000
= 19,500 GB total
Average per day = 19,500 ÷ 30 = 650 GB/day

**Total cost for storage = 650 GB × storage unit price**

!!! abstract "Key Notes"

    1. Due to **exclusivity**, billing uses the number of **full nodes reserved** (converted to core‑hours), not just per‑job core requests.
    2. GPU nodes are charged by **GPU core‑hours** which is the same on both GPU types.
    3. Billing is based on **resource reservations over time** (placement and overlap), not OS‑level utilization.
    4. Storage is billed by **average daily usage** over the month.

**HPC Usage video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/HPC_Usage_a7e90113b0.mp4" type="video/mp4"></video>
