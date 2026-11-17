---
title: "Roles & responsibilities"
description: "Computerome operates under a shared responsibility model. Read this article to understand the roles and responsibilities in your projects at Computerome."
icon: lucide/users
---

# Shared Responsibility Matrix

Computerome operates under a **shared responsibility model**.

- You, as a user, have certain responsibilities.
- We, as Computerome, provide and maintain the infrastructure.

The sections below explain this for **HPC users** and **Cloud users**.

## HPC Users

When you join Computerome HPC (regardless of your user type), you receive:

1. A **personal account** to log in to HPC services.
2. A **home directory** at `/home/people/<username>`
    - Free of charge.
    - Hard limit: **10 GB**.
3. One or more **project directories**, depending on your project memberships:
    - `/home/project/<project_name>`
4. One or more **groups** for access control (linked to your project memberships).
5. A **personal directory inside each project**:
    - `/home/project/<project_name>/people/<username>`

!!! note "Project name vs. group name"

    Project names and group names are identical but serve different purposes:

    - **Project name** → used for accounting.
    - **Group name** → used for permissions and service authorization.

### Your Responsibilities as a Normal HPC User

As a normal HPC user, you must:

1. Use a **strong and safe password**.
2. Set up your **two-factor authentication (2FA)**.
3. **Log in at least once every 6 months** to keep your account active.
4. Keep your **account information** (full name, phone number, email) up to date.
5. Monitor your **home directory usage** and stay below **8–10 GB**. Exceeding this may prevent login.
6. Monitor your **storage usage** in your project directories.
7. Keep your files and directories **organized and with correct permissions**.
8. Track your **CPU/GPU usage** via the web interface. Report unusual activity to your group’s Legal/Technical Owner or to Computerome.
9. Monitor your **running jobs**. Stop failed jobs that keep running to avoid unnecessary costs (this can happen in a queueing system).
10. Ensure that the **tools we provide** work with your pipelines.
    - A tool is considered _working_ if it installs correctly and its basic commands run.
    - It is your responsibility to test whether the tool works as expected for your workflow.
    - If you confirm there is an **installation issue**, report it to us so we can fix it.

### Your Responsibilities as a Technical Owner (HPC Groups)

As a **Technical Owner**, you have additional responsibilities on top of being a normal user:

1. You also carry all the responsibilities of a **Normal User**.
2. **Monitor group memberships** and keep them updated according to your project’s needs.
3. **Track resource usage** of the users in your groups.
    - Report abnormal usage directly to the user or to Computerome immediately.
    - **Important**: Computerome will not take any action regarding usage after the invoice has been issued.
4. **Monitor group storage usage** and ensure it stays within the project’s limits.

### Your Responsibilities as a Legal Owner (HPC Groups)

As a **Legal Owner**, you carry the responsibilities of both a Normal User and a Technical Owner, plus:

1. **Maintain accurate billing information** for your projects.
2. **Ensure timely payment** of invoices.

### Computerome Responsibilities (HPC)

Computerome is responsible for providing and maintaining the infrastructure. This includes:

1. Keeping core services such as the **queueing system** and **storage** available and operational.
2. Investigating **reported failed jobs** to determine whether the cause is an infrastructure issue or a user error.
3. Installing **requested tools** and fixing **installation errors**.
4. Resolving **day-to-day issues** reported by users in a timely manner during business hours on working days.

## Cloud Users

### Your Responsibilities as a Normal Cloud User

1. Use a **strong and safe password**.
2. Set up your **two-factor authentication (2FA)**.
3. **Log in at least once every 6 months** to keep your account active.
4. Keep your **account information** (full name, phone number, email) up to date.
5. Monitor your **storage usage** within the projects you are a member of.
6. Keep your files and directories **organized and with correct permissions**.
7. Ensure that the **tools we provide** work with your pipelines.
    - A tool is considered _working_ if it installs correctly and its basic commands run.
    - It is your responsibility to test whether the tool works as expected for your workflow.
    - If you confirm there is an **installation issue**, report it to us so we can fix it.

### Your Responsibilities as a Technical Owner (Cloud Projects)

As a **Technical Owner**, you are responsible for managing your cloud projects:

1. You also carry all the responsibilities of a **Normal User**.
2. Monitor and maintain **project memberships**.
3. Ensure your **cloud services** are up and running.
4. Maintain and verify **internet access** settings for your cloud.
5. Monitor your **cloud nodes** as well as CPU, GPU, and storage usage.
6. **Scale resources** up or down when needed.
7. Handle **assignments and workflows**, such as:
    - Adding or removing compute resources.
    - Processing import/export requests.
8. Manage **permissions on shared directories** for your users.
9. Ensure that the **operating systems** on your cloud nodes are functioning correctly.
10. Ensure your users have the **necessary access** to their environments.
11. Keep **backups of your configurations**.

### Your Responsibilities as a Legal Owner (Cloud Projects)

As a **Legal Owner**, you have the combined responsibilities of a Normal User and a Technical Owner, plus:

1. Maintain **up-to-date billing information**.
2. Ensure **timely payment** of invoices.

### Computerome’s Responsibilities (Cloud)

Computerome ensures the availability and operation of the infrastructure. Specifically, we are responsible for:

1. Keeping **self-service workflows** operational.
2. Ensuring that **running nodes** remain available.
3. Installing tools in the **shared repository**.
4. Assisting customers with **customizations**.
5. Enabling or disabling **internet access** upon request.
6. Assigning **public IPs** upon request.
7. Adjusting **firewall settings** upon request.
8. Ensuring the **storage system** is up and running.
