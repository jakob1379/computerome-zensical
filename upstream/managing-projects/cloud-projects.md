---
title: "Cloud Projects"
description: "Learn how to manage your cloud project in Computerome"
tags:
  - Cloud
---

# Cloud Projects

## Cloud Project Creation

**Creating a New Project (Legal Owner)**
If you request a new project, you will automatically become its **Legal Owner**.

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > Cloud > Applications**
3. Complete the application steps.
4. After submission, our Administration team will:
    - Review your application.
    - Contact you to arrange contracts and paperwork.
    - Approve the project, after which it will be created.

**Create Cloud Project video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Create_Cloud_Project_ef9d085df3.mp4" type="video/mp4"></video>

---

## Invite new users (Cloud)

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > Cloud > Projects**
3. Click on the **Project Name** you want to manage.
4. Go to the **Users tab**.
5. Invite new users by providing their:
    - **Full name**
    - **Email address**
    - **Phone number**
6. You may also assign one of the invited users as a **Technical Owner**.

**Cloud Invite User video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Cloud_Invite_User_be03cf9d25.mp4" type="video/mp4"></video>

!!! note

    When you send invitations, there are two possible scenarios:

    1. If the invited user already has one or more Computerome accounts, they will receive one email. They can click the link, log in with the account of their choice, and accept the invitation.
    2. If the invited user does not yet have a Computerome account, they will receive two emails:
        2.1 An email with instructions to create and activate their account.
        2.2 A second email with the project invitation link, which they can use after account creation to log in and accept the invitation.

!!! note "Please inform your users about this process in advance."

---

## User-Group Management

As the Legal or Technical Owner of a Cloud project, you must ensure that only the correct users are members of your project.

**Managing Users**

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > Cloud > [Project Name] > Users tab**
3. From here, you can view the list of current users and remove members if needed.

**Managing User Groups**

In addition to individual user management, Cloud projects also support **internal groups**:

1. Go to the **User Groups tab** in your Cloud project.
2. From here, you can:
    - Create groups
    - Delete groups
    - Edit group memberships

!!! note "Purpose of internal groups"

    1. Separate users within your project.
    2. Assign different permissions on your **shared directory** (`/dp<your_project_name>`) available on your VMs.

**Cloud Group Management video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Cloud_Group_Management_2e3074bb3a.mp4" type="video/mp4"></video>

---

## Cloud Usage

As the **Legal Owner** or **Technical Owner** of a project, you are responsible for monitoring your project’s compute and storage usage on a regular basis.

- Any **abnormal activity** must be reported to Computerome **immediately**.
- Please note: **Computerome does not take any action after the invoice has been issued**.

To monitor compute and storage usage for your Cloud project:

1. Log in to the **Computerome Web Interface**.
2. Navigate to:
    **My Solutions > Cloud > Projects > Your Project**
3. Review the usage overview for the selected project.

!!! warning "Important Note for Cloud Projects"

    1. Each VM includes **50 GB of local storage** free of charge.
    2. This local storage is **per VM** and is not counted in the project overview.
    3. The usage shown in the overview reflects your **shared directory**:
        `/dp<project_name>` (accessible on your VMs).

---

**Cloud Cost Calculation**

!!! info "Note on Billing Hours"

For all CPU/GPU/storage usage, Computerome uses a standardized month length of 730.5 hours (the yearly average), rather than the actual number of hours in each month. This ensures consistent billing across months with different lengths (28, 30, or 31 days). As a result, there may be a small difference between detailed day-by-day calculations and the official billing.

In our cloud environment, costs are calculated based on **average reservation** of the following resources:

- **CPU core hours**
- **GPU memory (per GB per hour)**
- **Storage (per GB per day)**

**Example Scenario**

Consider a month with **30 days**:

**Storage**

- First 5 days: **1 TB (1000 GB)**
- Next 15 days: **500 GB**
- Last 10 days: **700 GB**

Calculation:

(5 days × 1000 GB) + (15 days × 500 GB) + (10 days × 700 GB)
= 5000 + 7500 + 7000 = 19,500 GB
Average per day = 19,500 ÷ 30 = 650 GB/day

**Total cost for storage = 650 GB × unit price**

**CPU**

- First 20 days: **2 cores (VM1) + 4 cores (VM2) = 6 cores**
- Last 10 days: **2 cores (VM1 only)**

Calculation:
(20 days × 6 cores) + (10 days × 2 cores) = 120 + 20 = 140 core-days
Average per day = 140 ÷ 30 = 4.6 cores/day

Convert to hours:

4.6 cores × 30 days × 24 hours = 3,312 CPU core hours

**Total cost for CPU = 3,312 × CPU unit price**

**GPU**

- First 20 days: **20 GB GPU memory (VM2)**
- Last 10 days: **0 GB**

Calculation:
(20 days × 20 GB) + (10 days × 0 GB) = 400 GB-days
Average per day = 400 ÷ 30 = 13.3 GB/day

Convert to hours:

13.3 GB × 30 days × 24 hours = 9,576 GPU GB-hours

**Total cost for GPU = 9,576 × GPU unit price**

!!! abstract "Key Notes"

    1. Billing is based on **average usage over the entire month**.
    2. CPU, GPU, and storage are billed **separately**.
    3. Local VM storage (50 GB) is free of charge.

**Cloud Usage video guideline**

<video controls preload="none" width="100%"><source src="https://delphiapp.computerome.dk/strapi/uploads/Cloud_Usage_688dc59ca9.mp4" type="video/mp4"></video>
