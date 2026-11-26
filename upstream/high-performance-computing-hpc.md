---
title: "High-Performance Computing (HPC)"
description: "The High-Performance Computing (HPC) solution offers access to a secure and powerful storage and compute cluster where data can be analysed and stored.The standard HPC solution is a compute-resource-as-a-service, allowing users to request remote access to dynamic and scalable storage and compute resources as a pay-as-you-go service."
tags:
  - HPC
  - High Performance Computing
---

# High-Performance Computing (HPC)

![HPC_01.png](assets/uploads/HPC_01_ced6648d0f.png)

## Introduction
The High-Performance Computing (HPC) solution offers access to a secure and powerful storage and compute cluster where data can be analysed and stored.The standard HPC solution is a compute-resource-as-a-service, allowing users to request remote access to dynamic and scalable storage and compute resources as a pay-as-you-go service.

Users can submit jobs to the cluster’s work queue, and Computerome’s workload and resource management system will ensure that all users share the cluster’s resources evenly and fairly. Users can also reserve resources for a short or longer period in case they need to ensure the resources are available in a specific period and not shared with other users.

To access the HPC solution you need to request an account for you and your users. Once you receive your HPC login you can access the HPC environment and start your research project.

## How To
- [Setup two factor authentication (2FA)](two-factor-authentication-2fa.md)
- [Login in for the first time ](high-performance-computing-hpc.md#login)
- [Run jobs](running-jobs/index.md#running-jobs)
- [Transfer data ](high-performance-computing-hpc.md#file-transfer)
- [Administer my project](high-performance-computing-hpc.md#project-administration)

## More Information
- [High-Performance Computing (HPC) Solution](https://computerome.dk/hpc-servers)
- [Linux Guides ](high-performance-computing-hpc.md)
- [Computerome Terms of Use](https://computerome.dk/terms-of-use)
- [Computerome Security Overview](https://computerome.dk/security)
- [Server Status and Maintenance](https://computerome.dk/server-status)

## Getting Started
This guide will help you start working your research project in [Computerome's High-Performance Computing (HPC)](https://computerome.dk/hpc-servers) environment. Before you can start you will need your login details and to [setup two factor authentication (2FA)](two-factor-authentication-2fa.md). You will receive your login details in a welcome mail once your account is created.

!!! tip "First Time Login"

    To login for the first time you will need:

    1. A Computerome user name
    2. A temporary password
    3. An Entrust Identity (2FA) soft token

!!! info "Two Factor Authentication (2FA)"

    Computerome uses Entrust Identity for two factor authentication (2FA). Please download the Entrust Identity app before you login to Computerome. For help, see our [Two Factor Authentication (2FA) guide](two-factor-authentication-2fa.md).

!!! info "Alternative to Two Factor Authentication (2FA)"

    Computerome also provides an SMS passcode service for users who do not wish to use Entrust Identity for two factor authentication. If you have not setup Entrust Identity, you will recieve a one time passcode (OTP) via SMS

!!! info "Password Security"

    Please change your password the first time you login to the HPC environment. To change your password use the `passwd` command. Remember to keep your user name and password private. For more information, see our [Terms of Use](https://computerome.dk/terms-of-use).

## Login
There are 3 ways to login to Computerome's HPC environment: SSH via terminal, SSH via client, and virtual desktop. If need to work with graphical applications we recommend using an SSH client or virtual desktop, which can display graphical applications. We recommend you download the latest versions of [PuTTY SSH client](https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html) or [MobaXterm SSH client](https://mobaxterm.mobatek.net/download.html).  To use the virtual desktop service please download and install the latest version of the
[Cendio ThinLinc Virtual Desktop SSH application](https://www.cendio.com/thinlinc/download).

| Login Service | Operating System | Graphical Applications | Documentation |
| --- | --- | --- |  --- |
| SSH via Terminal | Linux, Mac  | :fontawesome-solid-circle-check: | [SSH](https://www.openssh.com/manual.html) |
| SSH via Client | Linux, Windows | :fontawesome-solid-circle-check:| [PuTTY](https://www.chiark.greenend.org.uk/~sgtatham/putty/docs.html)/[MobaXterm](https://mobaxterm.mobatek.net/documentation.html)|
| Virtual Desktop | Linux, Mac, Windows| :fontawesome-solid-circle-check: | [Cendio ThinLinc](https://www.cendio.com/thinlinc/docs/install)|

<div id="name-of-hashtag"
## SSH via Terminal

</div>
---

On a Mac or Linux machine open a new Terminal and enter `ssh user_name@ssh.computerome.dk`. Remember to replace `user_name` with your Computerome user name. Next enter the temporary password you received via SMS. Now you will receive an Entrust Identity mobile notification to confirm. After you have confirmed the notification you will be logged into the HPC environment.

``` bash
$ ssh user_name@ssh.computerome.dk

#############################################################
#                                                           #
#                 Welcome to  Computerome                   #
#                                                           #
#                         NOTICE !!!                        #
#        This system requires 2-factor authentication       #
#                                                           #
#       To login, type your password and press Enter.       #
#     This sends either an SMS passcode to your mobile      #
#    or a push-notification to Entrust IdentityGuard app.   #
#   If the push-notification times out, a new prompt line   #
#    asks for the 8 digit security code shown in the app.   #
#                                                           #
#           BY LOGGING INTO THIS SYSTEM YOU ACCEPT          #
#         COMPUTEROME'S TERMS AND CONDITIONS OF USE.        #
#                                                           #
#############################################################

Password:
```

## SSH via Client
!!! tip "PuTTY Users"

    PuTTY users need to install an X11 server on their computer before they can work with graphical applications. For help installing an X11 server, see for instance [Xming X Server documentation.](http://www.straightrunning.com/XmingNotes/)

!!! tip "MobaXterm Users"

    Older versions of MobaXterm do not work with 2FA. If you are using an older version of MobaXterm, make the following changes to solve the problem:

    Under Settings => Configuration => SSH

    SFTP Settings

    [ ] Enable graphical SSH-browser - must be unchecked

    [ ] Automatically switch to SSH-browser tab after login - must be
    unchecked

    [X] Use 2-factor authentication for SSH gateways - must be checked

## Virtual Desktop
After downloading and installing the Cendio ThinLinc application, open the application and enter `desktop.computerome.dk` into the Server field. Enter your user name and password and then click "Connect". Remember to replace `user_name` with your Computerome user name.

![cendio_thin_linc_virtual_desktop](assets/uploads/cendio_thin_linc_virtual_desktop_01_0413771604.png)

The popup window below will then appear, press "Continue". Now you will receive an Entrust Identity mobile notification to confirm. Once you have confirmed the notification you will be logged into the HPC environment.

![cendio_thin_linc_virtual_desktop](assets/uploads/cendio_thin_linc_virtual_desktop_02_be5e61ebb5.png)

!!! tip "VNC Auth Error Message"

    If you get the message "no password configured for VNC Auth", select the following in the ThinLinc Client startup options:

    [X] End existing session  -  must be checked

## Tips and Tricks
!!! tip "SSH Version 2"

    Authorised users are able login to the HPC environment with SSH Version 2 to the interactive front end node `ssh.computerome.dk`. For security reasons, access is only possible from known internet domains of authorised users

!!! tip "Broken Pipe Error Message"

    If you are connecting to Computerome though a slightly unstable connection (Internet/WAN/similar), you may experience the "packet_write_wait: ... broken pipe error". You can troubleshoot this by adding `ServerAliveInterval 60`  to your `~/.ssh/config`  file.

    For PuTTY users

    Under PuTTY Configuration => Connection =>

    Set seconds between keepalives to 60

!!! tip "Gnome GUI on ThinLinc"

    Users may experience that the Gnome GUI runs very slow in ThinLinc. We recommend using other alternatives, such as Mate.

!!! tip "Anaconda Conflict on ThinLinc"

    You cannot loading the anaconda module in your login environment if you are connecting using ThinLinc. This is because anaconda will conflict with ThinLinc, resulting in error messages such as "Could not acquire name on the session bus".

## User Workshops
Computerome provides workshops and training sessions for all our users. Please [contact us](https://computerome.dk/contact-us) if you would like to arrange a workshop or training session for your research group. Computerome customises workshops and training to meet the specific needs of your research group. Below you can find slides from previous workshop and training sessions:

 :fontawesome-solid-file-pdf: [Computerome New User Workshop 2022](https://delphiapp.computerome.dk/strapi/uploads/Computerome_New_User_Workshop_03032022_e5e9c38a9e.pdf)

 :fontawesome-solid-file-pdf: [General Computerome Workshop 2021](https://delphiapp.computerome.dk/strapi/uploads/Computerome_General_User_Workshop_10032021_35c8c7a8a1.pdf)

 :fontawesome-solid-file-pdf: [Computerome Hackinar 2016](assets/uploads/Hackinars_in_Computerome_07032016_5d1217dd06.pdf)

## Useful Guides
Below are a list of useful guides for first time Linux users. If you have suggestions other guides and learning resources, please [contact us](https://computerome.dk/contact-us) and they will be added to this section. We update this section regularly so Computerome's user community can benefit from new learning resources.

:fontawesome-solid-file-pdf: [The Linux Command Line by William Shotts](https://altushost-swe.dl.sourceforge.net/project/linuxcommand/TLCL/19.01/TLCL-19.01.pdf)

:fontawesome-solid-file-pdf: [Introduction to Linux by Machtelt Garrels](https://tldp.org/LDP/intro-linux/intro-linux.pdf)

## CentOS Cheatsheet
!!! info "Manual Pages for Commands"

    Use `man <command>`  to learn more about how to use a specific command

| Bash Variable Commands | Description |
| ------  | ------      |
| `env` | List current enviro­nment variables |
| `export $NAME` | Output value of $NAME variable|
| `export NAME=­value` | Set $NAME to value in environment|
| `set` | Change value of shell attributes and positional parameters or display list of shell variables and functions|
| `$PATH` | Executable search path|
| `$HOME` | Home directory|
| `$SHELL` | Current shell|

| Partition and Disk Management Commands | Description |
| ------  | ------      |
| `df` | Clears your screen |
| `mount` | Show what is mounted or mount a file system |
| `unmo­unt` | Unmount a file system|
| `fuser` | Identifies processes using files or sockets|
| `isof` | List open files on the system |

| Directory Operation Commands | Description |
| ------  | ------      |
| `clear` | Report file system disk space usage |
| `pwd` | Show current directory |
| `cd` | Change directory|
| `ls` | List directory contents|
| `mkdir` | Create new directory |
| `rmdir` | Delete an empty directory |

| File Operation Commands | Description |
| ------  | ------      |
| `grep` | Search text files for lines containing a matching pattern |
| `locate` | Find files by matching the whole path name |
| `find` | Search for files in a directory hierarchy |
| `cat` | Print a file on the screen, concat­enate files |
| `touch` | Create an empty file, change file timestamps |
| `cp` | Copy direct­ories or files |
| `mv` | Moves direct­ories or files|
| `rm` | Removes direct­ories or files (This is how you remove recurs­ively) |
| `ln` | Creates a symbolic or hard link for a file |
| `less` | View a file on page at a time, allows for going backwards |
| `head` | Print the first 10 lines of a file |
| `tail` | Print the last 10 lines of a file |
| `wc` | Count the number of words or characters in a file |
| `stat` | Display file of file system status |
| `cut` | Remove sections from lines of input |
| `paste` | Merge line of files |

| ls Options | Description |
| ------  | ------      |
| `-a` | Show all (including hidden) |
| `-R` | Recursive list |
| `-r` | Reverse order |
| `-t` | Sort by last modified |
| `-S` | Sort by file size |
| `-l` | Long listing format |
| `-1` | One file per line|
| `-m` | Comma sep­arated output |
| `-Q` | Quoted output|

| grep Options | Description |
| ------  | ------      |
| `-i` | Case insens­itive search |
| `-r` | Recursive search |
| `-v` | Inverted search |
| `-o` | Show matched part of file only |

## Directory Structure
!!! tip "Best Practices"

    - Project owners are responsible for maintaining their project directory
    - Project owners should inform Computerome when their project is ended
    - Old data should be removed from the project directory once the project is closed
    - When data is no longer in use it should be removed from the `/scratch` directory
    - All project related data should be stored in the project directory

| HPC Project Directory Structure | Recommended Use |
| --- | --- |
| `/home/projects/<project>` | The project home directory which contains... |
| `"..."/apps/modulefiles` | For project specific modulefiles, typically modulefiles for software installed and maintained by the project itself  |
| `"..."/archive` | For archived project data |
| `"..."/data` | For project generated data  |
| `"..."/people/<user>` | For a project user's private, project related files (e.g data, scripts etc.) |
| `"..."/scratch` | For temporary data  |

!!! info "Note"

    `You should go directly to /home/projects/<project> (ex. '$ cd /home/projects/<project>) to access it.`

    `Often, it will not be visible if you just list (ex. '$ ls /home/projects' or '$ ls /home/projects/<project>/data')`

## User Home Directory
All HPC users have a home directory `/home/people/<user>` which contains their environment setup and other user specific information. The `/home/people/<user>` directory is limited to 10GB and free of charge. For security reasons, only you can access your own home directory. Because users often switch projects, graduate, or change employment, project related data (e.g results, project modulefiles) should never be stored in the `/home/people/<user>` directory. All project related data must be stored in your HPC project directory.

## File Transfer
To securely and safely transfer data to Computerome, we recommend using the following file transfer services: scp, rsync, SFTP commands or SFTP clients like Filezilla or Cyberduck. However, in order to use these, you need to connect to **transfer.computerome.dk**.

!!! info "Note"

    You cannot login via ssh to transfer.computerome.dk, it **only** supports file transfer protocols, ex. sftp, rsync.

Any rsync and SFTP transfers running on the login node (ssh.computerome.dk), will be terminated at the discretion of the system administrators, in order to avoid server overload.

| File Transfer Service | Operating System | 2FA | Documentation |
| --- | --- | --- |  --- |
| [File Manager](https://files.computerome.dk/index.php/login) | Linux, Mac, Windows  | Google Authenticator | [File Manager Documentation](high-performance-computing-hpc.md#file-transfer) |
| [FileZilla](https://filezilla-project.org/) | Linux, Mac, Windows | Entrust Identity| [FileZilla Wiki](https://wiki.filezilla-project.org/Main_Page)|
| [Cyberduck](https://cyberduck.io/) | Mac, Windows| Entrust Identity| [Cyberduck Wiki](https://docs.cyberduck.io/) |
| [WinSCP](https://winscp.net/eng/index.php) | Windows | Entrust Identity| [WinSCP Documentation](https://winscp.net/eng/docs/start) |

!!! info "Note"

    `You should configure your file transfer service to go directly to
    /home/projects/<project>`

## File Manager
!!! info "Request Access to File Manager"

    To use [File Manager](https://files.computerome.dk/index.php/login) please contact the Computerome support team to request access. Either use the [Contact us ](https://computerome.dk/contact-us)form or write to computerome@dtu.dk.

Before you can use [File Manager](https://files.computerome.dk/index.php/login) you need to download the Google Authenticator app for either [iOS](https://apps.apple.com/us/app/google-authenticator/id388497605?platform=iphone) or [Android](https://play.google.com/store/apps/details?id=com.google.android.apps.authenticator2&hl=da&gl=US). We recommend using the [Mozilla Firefox](https://www.mozilla.org/en-US/firefox/new/) browser with [File Manager](https://files.computerome.dk/index.php/login) for the best experience.

:fontawesome-solid-video:
[How to login](https://delphiapp.computerome.dk/strapi/uploads/data_and_storage_file_manager_loggingin_979795cb1e.mp4)

:fontawesome-solid-video: [How to add directories](https://delphiapp.computerome.dk/strapi/uploads/data_and_storage_file_manager_adding_directories_7451c75cc0.mp4)

:fontawesome-solid-video:
[How to share files](https://delphiapp.computerome.dk/strapi/uploads/data_and_storage_file_manager_sharing_files_abf74ace8e.mp4)

:fontawesome-solid-video:
[How to upload files](https://delphiapp.computerome.dk/strapi/uploads/data_and_storage_file_manager_uploading_files_b2e2dfd3e7.mp4)

:fontawesome-solid-video:
[How to search files](https://delphiapp.computerome.dk/strapi/uploads/data_and_storage_file_manager_searching_files_b6182ba6ce.mp4)

 ## FileZilla
---

In order to use [FileZilla](https://filezilla-project.org/)  it needs to be configured to work with Computerome's two factor authentication (2FA) service, Entrust Identity.

!!! tip "FileZilla Configuration"

    Global

    - Go to Edit->Settings->Transfers
    - Change Maximum simultaneous transfers to 1

    Site Profile/Bookmark

    - Go to File->Site Manager->(your profile)->Transfer Settings
    - Check Limit number of simultaneous connections
    - Change Maximum number of connections to 1
    - Change Login type to Interactive

!!! info "Quickconnect"

    Please be aware that Quickconnect no longer works with 2FA in recent versions of [FileZilla.](https://filezilla-project.org/)

## Cyberduck
In order to use [Cyberduck](https://cyberduck.io/) it needs to be configured to work with Computerome's two factor authentication (2FA) service, Entrust Identity.

!!! tip "Cyberduck Configuration"

    Global

    - Go to Edit->Preferences->Transfers
    - Change Transfer Files to Use Browser Connection

    Site Profile/Bookmark

    - Right click your Profile and select Edit Bookmark
    - Change Transfer Files to Use browser connection

## Data Backup and Storage
!!! info "Data Backup and Storage"

    Computerome does not offer a long-term archive solution or cold storage services for project data. We are working on providing a data archiving solution in the future.

## Snapshot Recovery
The snapshot recovery feature allows users to recover individual files or whole directory structures which were deleted up to 4 weeks ago.

To use the self-service snapshot recovery option, go to the directory, (e.g `example_oops_I_deleted_something`) that used to contain the files you want recover. Then use the `cd` command to go to the hidden `.snapshots` directory which will contain a number of timestamped subdirectories. Now go to the subdirectory that contained the files or directories you wish to recover, before the time of deletion. The deleted files or directories can then be recovered using the `cp` command.

``` bash
$ cd example_oops_I_deleted_something
$ cd .snapshots
$ ls -l
...
drwx------ 38 <myaccount> <mygroup> 1490 Sep 23 14:32
drwx------ 38 <myaccount> <mygroup> 1490 Sep 24 13:04
...
drwx------ 38 <myaccount> <mygroup> 1490 Sep 24 13:04
drwx------ 38 <myaccount> <mygroup> 1490 Sep 24 13:04
...
drwx------ 36 <myaccount> <mygroup> 1471 Sep 10 07:32
drwx------ 37 <myaccount> <mygroup> 1464 Sep 17 08:42
```

## Running Jobs
To run jobs in the HPC environment you first have to submit jobs to a queueing system. The HPC environment queueing system shares compute resources fairly and efficiently among users and schedules when jobs should run. The queueing system is based on [TORQUE](https://support.adaptivecomputing.com/wp-content/uploads/2021/02/torque/torque.htm#topics/torque/0-intro/torquewelcome.htm) (`q` type commands) and [Moab](https://docs.adaptivecomputing.com/8-1-2/enterprise/MAM/help.htm) (`m` type commands). In addition, we provide Perl wrapper scripts which can build job submission scripts for you.

Jobs are submitted to the queueing system from the cluster's login nodes. In HPC the login nodes are `g-12-l0001`, `g-12-l0002`, and `g-12-l0003`. The login nodes act as a platform for users to submit jobs to the rest of the cluster. Please never run jobs on login nodes, as it will affect the performance and stability of the cluster for all users. In addition to login nodes, there are 3 other node types: fat, thin, and GPU.

| Node Type | CPUs | Memory |
| --- | --- | --- |
| Thin Node | 40 cores | 192 GB |
| Fat Node | 40 cores | 1.5 TB |
| GPU Node Type 1 | 40 cores | 192 GB |
| GPU Node Type 2 | 20 cores | 400 GB |

!!! tip "Memory Allocation"

    Please note that the node OS uses a small portion of memory. Therefore, the maximum memory that can be allocated to a job for **thin nodes and GPU nodes type 1 is 188 GB**, **for GPU nodes type 2 is 394 GB** and for **fat nodes it is 1511 GB**.

## Best Practices
Please follow the queueing system best practices to ensure all users can benefit from a stable and well-functioning system.

!!! tip "Queueing System Best Practices"

    - Never run jobs or scripts on the login nodes
    - Use the `qsub` command to submit batch jobs
    - Add a delay between jobs when submitting multiple jobs
    - Use job arrays for submitting multiple identical jobs
    - Use `iqsub` for testing and interactive jobs
    - Use software modules in your pipelines for better environment control
    - Always included your "group_name" when submitting jobs
    - 64 KB is the maximum size limit for scripts submitted to the queueing system
    - Scripts submitted to the queuing system should mainly consist of queueing system parameters and job executions
    - Always specify which type of node you require in order to avoid unwanted costs, if you do not request a specific node type, your job may be submitted to a GPU node

!!! tip "Login Node"

    Do not run anything compute related on Computerome HPC login nodes (through ssh.computerome.dk or Thinlinc).

    These nodes are only provided for access to Computerome, and should not be used as a personal workstation or for any sort of general work, including data management.

    In principle, the only things you should have there are:

    - Your login session
    - [OPTIONAL] A terminal multiplexer (TMUX, SCREEN, or similar)
    - Queueing system job submission(s), either regular or interactive job(s)

    Any compute activities, running on the login nodes, will be terminated at the discretion of the system administrators, in order to avoid server overload.

## Job Submission
Use the command `qsub` and/or `msub` to submit jobs. For documentation on `qsub` and `msub`, see [here](https://support.adaptivecomputing.com/wp-content/uploads/2021/02/torque/torque.htm#topics/torque/commands/qsub.htm) and [here](https://docs.adaptivecomputing.com/8-1-2/enterprise/MAM/help.htm). Please note that the flags for `qsub` and `msub` are the same. In order to submit a job using `qsub` or `msub` you have to specify the options below:

| Option | Description | Parameter(s)|
| --- | --- | --- |
| `-W` | Your project "group_name" |  `-W group_list=<group_name>` |
| `-A` | Your project "group_name" |  `-A <group_name>` |
| `-l` | Required resources (nodes, node type, CPUs/GPUs, memory, walltime) |  `-l nodes=1:<node_type>:ppn=<number_of_CPUs>:gpus=<number_of_GPUs>,mem=<xxxGB>,walltime=<time_in_seconds>` |

!!! tip "-l option"

    Please note that the `-l` option will contain less or more parameters depending on the resources your job requires.

## Job Submission Examples
Below are some examples of job submission commands using the `qsub` and `msub` commands

!!! tip "Example 1"

    The following `qsub` command will run a job with *20 CPUs*, *100 GB* of memory, for *one hour*, on a single *thin node*

``` bash
$ qsub -W group_list=<group_name> -A <group_name> -l nodes=1:thinnode:ppn=20,mem=100gb,walltime=3600 <job_script>

```

!!! tip "Example 2"

    The following `qsub` command will run a job with *40 CPUs*, *150 GB* of memory, for *two hours* on a single *GPU node*

``` bash
$ qsub -W group_list=<group_name> -A <group_name> -l nodes=1:gpus=1:ppn=40,mem=150gb,walltime=7200 <job_script>

```

!!! tip "Example 3"

    The following `msub` command will run a job with *40 CPUs*, *150 GB* of memory, for *two hours* on a single *GPU node*

``` bash
$ msub -W group_list=<group_name> -A <group_name> -l nodes=1:gpus=1:ppn=40,mem=150gb,walltime=7200 <job_script>

```

!!! tip "Example 4"

    The following `qsub` command will run a job with *80 CPUs*, *150 GB* of memory, for *two hours* on two *thin nodes*

``` bash
$ qsub -W group_list=<group_name> -A <group_name> -l nodes=2:ppn=40:thinnode,mem=10gb,walltime=7200 <your script>
```

!!! tip "Example 5"

    The following `qsub` command will run a job with *40 CPUs*, *50 GB* of memory, for *two hours* on the *g-01-c0052* node

``` bash
$ qsub -W group_list=<group_name> -A <group_name> -l nodes=g-01-c0052:ppn=40,mem=50gb, walltime=7200 <your script>
```

## Job Submission and Project Membership
In order to give a user access to data generated in a project, jobs must be submitted with parameters `-W group_list=<group_name>` and `-A <group_name>`. Users who are members of `<group_name>` will then be able to access the generated data in the project's directory. `-A` supplies account information for use in the Moab Accounting Manager.

To check your group membership use the `id` command. In most cases, `group_name` and `project_name` will be the same and follow the format `xx_12345`.

``` bash
$ id

uid=00001(user) gid=00001(user)
groups=00001(user),2345(xx_12345),4321(xx_54321)
```

Look for the group(s) that do not match the user uid/gid. Then locate those groups in the `/home/project/` directories:

``` bash
$ ls -l /home/project | grep -e xx_12345 -e xx_54321

drwxr-x--- 8 user xx_12345 147 Jan 19 12:45 xx_12345
drwxr-x--- 4 user xx_54321 48 Sep 26 12:27 xx_54321
```

## Script File Example
The `$PBS...` variables are set by TORQUE. If you already have loaded some modules in your login environment , you do not need to specify them in the jobscript. However, we recommend that you do it since it improves the portability of the jobscript and acts as a reminder of the requirements.

We also strongly advise against the use of the `-V` option, as it makes it hard to debug possible errors during runtime. The complete list of variables str documented in exported batch environment variables. Further examples of TORQUE job submission is documented here. See below for an example script for a file to be submitted with `qsub`:

``` bash
#!/bin/sh
### Note: No commands may be executed until after the #PBS lines
### Account information
#PBS -W group_list=pr_12345 -A pr_12345
### Job name (comment out the next line to get the name of the script used as the job name)
#PBS -N test
### Output files (comment out the next 2 lines to get the job name used instead)
#PBS -e test.err
#PBS -o test.log
### Only send mail when job is aborted or terminates abnormally
#PBS -m n
### Number of nodes
#PBS -l nodes=1:ppn=8
### Memory
#PBS -l mem=120gb
### Requesting time - format is <days>:<hours>:<minutes>:<seconds> (here, 12 hours)
#PBS -l walltime=12:00:00

# Go to the directory from where the job was submitted (initial directory is $HOME)
echo Working directory is $PBS_O_WORKDIR
cd $PBS_O_WORKDIR

### Here follows the user commands:
# Define number of processors
NPROCS=`wc -l < $PBS_NODEFILE`
echo This job has allocated $NPROCS nodes

# Load all required modules for the job
module load tools
module load perl/5.20.2
module load <other stuff>

# This is where the work is done
# Make sure that this script is not bigger than 64kb ~ 150 lines,
otherwise put in separate script and execute from here
<your script>
```

## Job Arrays
To submit multiple jobs which are identical you can use job arrays. Job arrays are created using the `-t`option in your qsub submission script. The `-t` option allows many copies of the same script to be submitted at once. Additional information about `-t`option can be found in the `qsub` command [reference](https://support.adaptivecomputing.com/wp-content/uploads/2021/02/torque/torque.htm#topics/torque/commands/qsub.htm). Moreover, the PBS_ARRAYID environmental variable allows you to differentiate between the different jobs in the array. The amount of resources required in the qsub submission script is the amount of resources that each job will get. Please note that jobs in jobs array will run independently and not in any specific order.

``` bash
  #PBS -t 0-20%5
```

For example, adding the above line in the qsub script will result in running the job 15 times with no more than 5 actives jobs at any given time. Remember to use the `%#` option for limiting the number of active jobs. `PBS_ARRAYID` values will run from 0 to 20, as shown below:

``` bash
 ( perl process.pl dataset${PBS_ARRAYID} )

  perl process.pl dataset0
  perl process.pl dataset1
  perl process.pl dataset2
  …
  perl process.pl dataset20
```

## Interactive Jobs
It is strongly recommended to work interactively when you want to test submission scripts. To start an interactive session use the `iqsub` command. After you have answered the questions below you will be redirected to your own private node which you will be able to use for testing without affecting other users.

``` bash
$ iqsub

[ Interactive job ]

  => [ Select group ]

    => [ Select time needed (non extendable) ]

      => [ Enter number of Processors needed (1-40) ]

         => [ Enter number of GPUs needed (0-1) ]

            => [ Enter amount of memory needed ]

```

## Tips and Tricks
!!! tip "Running jobs under different projects"

    Tips and tricks

If you need to run jobs under different projects, for instance *pr_12345* and *pr_54321*, you must make sure that each project gets accounted for separately in the system's accounting statistics. You need specify the relevant project account (for example, *pr_54321*) for each individual job by using these flags to the `qsub` command:

`qsub -W group_list=pr_54321 -A pr_54321 ...`

Or in the job script file, add line like this near the top:
`#PBS -W group_list=pr_54321 -A pr_5432`

!!! tip "Estimating job resource requirements"

    Tips and tricks

The first time you run your script, you may not have a clear picture of what kind of resource requirements it has. To get a rough estimate, you could submit a job to a full node, with a large walltime.

Thin node:

`qsub -W group_list=<group_NAME> -A <group_NAME> -l nodes=1:ppn=40:thinnode,walltime=99:00:00,mem=180gb -m n <script>`

Fat node:

`qsub -W group_list=<group_NAME> -A <group_NAME> -l nodes=1:ppn=40:fatnode,walltime=99:00:00,mem=1200gb -m n <script>`

To see the actual resource usage, see the output from the `qstat` command. Add `qstat -f -1 $PBS_JOBID` to the bottom of your script, which will generate something like the following:

``` bash
Job Id: <jobid>
    Job_Name = <job_NAME>
    Job_Owner = <user>
    resources_used.cput = 323:00:30
    resources_used.energy_used = 0
    resources_used.mem = 1129928kb
    resources_used.vmem = 3082824kb
    resources_used.walltime = 12:00:35
...
    Resource_List.nodes = 1:ppn=28
    Resource_List.mem = 120gb
    Resource_List.walltime = 12:00:00
    Resource_List.nodect = 1
    Resource_List.neednodes = 1:ppn=28
...
```

!!! tip "Requesting minimum memory size"

    Tips and tricks

!!! info "Maximum physical amount of RAM"

    Do not request the maximum physical amount of RAM, since the RAM memory available to users is slightly less than the physical RAM memory.

A number of node features can be requested. For example, you may require a minimum physical memory size by requesting:

`qsub -W group_list=<group_NAME> -A <group_NAME> -l nodes=2:ppn=16,mem=120gb <your script>`

i.e.: 2 entire nodes, 16 CPU cores on each, the total memory of all
nodes \>= 120 GB RAM.

!!! tip "Waiting for specific jobs"

    Tips and tricks

It is possible to specify that a job should only run after another job has completed successfully, please see the `-W` flags in the `qsub` [documentation](https://support.adaptivecomputing.com/wp-content/uploads/2021/02/torque/torque.htm#topics/torque/commands/qsub.htm).

`qsub -W depend=afterok:12345 <your script>`

Be sure that the exit status of job 12345 is meaningful: if it exits
with status 0, you second job will run. If it exits with any other
status, you second job will be cancelled. It is also possible to run a
job if another job fails `afternotok\` or after another job
completes, regardless of status `afterany\`. Be aware that the
keyword `after\` (as in `-W depend=after:12345\` means run
after job 12345 has started.

!!! tip "Running parallel jobs using MPI"

    Tips and tricks

In order to optimise performance, the queuing system is configured to place jobs on nodes connected to the same InfiniBand switch (30 nodes per switch) if possible. To get nodes close to each other, use `procs=<number_of_procs>` and leave out `node=` and `ppn=`. To avoid interference with other jobs, `procs=` should be a multiple of cores per node (ie. 40 for mpinode). See the example script below:

``` bash
#!/bin/sh
### Note: No commands may be executed until after the #PBS lines
### Account information
#PBS -W group_list=pr_12345 -A pr_12345
### Job name (comment out the next line to get the name of the script used as the job name)
#PBS -N test
### Output files (comment out the next 2 lines to get the job name used instead)
#PBS -e test.err
#PBS -o test.log
### Only send mail when job is aborted or terminates abnormally
#PBS -m n
### Number of nodes, request 240 cores from 6 nodes
#PBS -l nodes=6:ppn=40
### Requesting time - 720 hours
#PBS -l walltime=720:00:00

### Here follows the user commands:
# Go to the directory from where the job was submitted (initial directory is $HOME)
echo Working directory is $PBS_O_WORKDIR
cd $PBS_O_WORKDIR
# NPROCS will be set to 240, not sure if it used here for anything.
NPROCS=`wc -l < $PBS_NODEFILE`
echo This job has allocated $NPROCS nodes

module load tools openmpi/gcc/64/1.10.2 gromacs/5.1.2-plumed

export OMP_NUM_THREADS=1
# Using 236 cores for MPI threads leaving 4 cores for overhead, '--mca btl_tcp_if_include ib0' forces InfiniBand interconnect for improved latency
mpirun -np 236 $mdrun -s gmx5_double.tpr -plumed plumed2_path_re.dat -deffnm md-DTU -dlb yes -cpi md-DTU -append --mca btl_tcp_if_include ib0
```

!!! tip "Searching for free resources"

    Tips and tricks

To show what resources are available use the `showbf` command:

`showbf -f <fatnode/thinnode/gpus`

`pestat` can also be used to check what resources are free

``` bash
$ pestat | grep free
  risoe-r01-f006  free    29* 1034109  32 1046397  13226  1/1    1    100074 user 1
  risoe-r01-f010  free   2.4* 1034109  32 1046397  79972  2/1    1*   20078 user 2
  risoe-r01-f013  free  0.84  1034109  32 1046397   8395  0/0    1    102268 user 3
  risoe-r02-f015  free  0.81  1034109  32 1046397   8212  0/0    1    102268 user 4
  risoe-r02-f017  free  0.15* 1034109  32 1046397   8489  0/0    1    102268 user 5
  risoe-r02-f023  free  0.56  1034109  32 1046397   8313  0/0    1    102268 user 5
  risoe-r02-f024  free  0.08* 1034109  32 1046397   8101  0/0    1    102268 user 5
  risoe-r02-f025  free  0.02* 1034109  32 1046397   7984  0/0    1    102268 user 5
  risoe-r08-cn289  free   1.4  128946  28 133042   3117  1/1    1    102536 user 5
  risoe-r08-cn300  free   1.5  128943  56 133039   6995  3/2    1*   102406 user 6
  risoe-r12-cn527  free   1.3  128946  28 133042   2741  1/1    1    10047 user 7
  risoe-r02-f018  free    29* 1034110  64 1046398  15376  1/1    1    99432 user 7
```

The node risoe-r01-f010 is occupied by 1 job (9th column) and two users
(8th column) each requesting 1 core. The node risoe-r02-f024 is totally
free.

!!! tip "Resource usage"

    Tips and tricks

To inquire about your usage of Computerome, you can run the `usage` command, available through the usage_script module. `usage u` will provide information for yourself. `usage -a <account>` will provide information for any account you are member of.

``` bash
$ module load tools usage_script/2.0
$ usage -u

Usage report for <user>
From 2016-01-04 to 2016-05-30
Account          CPU Hours       Jobs
-------------------------------------
pr_12345:         14832.89         13
pr_23451:         13018.72       2347
pr_34512:         26585.01        729
pr_45123:        264068.02       3248
-------------------------------------
Total:           318504.64       6337
```

!!! info "Investigating badly behaving jobs"

    Tips and tricks

`pestat`has not been maintained since 2018 and is unsupported. As a result, it may not be up to date with current Moab and TORQUE versions, and you should only use the results as a quideline and pointer to further investigation using standard queueing system tools, such as checkjob, showq and qstat. `pestat` shows status of badly behaving jobs, with bad fields marked by star *

``` bash
$ module load tools pestat
$ pestat -f

Listing only nodes that are flagged by *e
  node state  load    pmem ncpu   mem   resi usrs tasks  jobids/users
  risoe-r01-f002  free     2* 1034109  32 1046397   8017  1/1    1    103125 s147214
  risoe-r01-f010  free  0.53* 1034109  32 1046397   8451  0/0    0
  risoe-r01-f012  free  0.55* 1034109  32 1046397   8019  0/0    0
  risoe-r02-f019  offl* 0.27  1034107  64 1046395   6590  0/0    0
  risoe-r02-f024  free     1* 1034109  32 1046397   8730  0/0    0
  risoe-r03-cn001  excl    29* 128946  28 133042   8266  1/1    1    100096 qyli
```

One of the most common bad behaviors of batch jobs is exhausting of
available RAM memory. An example of usage of pestat:

``` bash
$ pestat | grep -e node -e 263945
  node state  load    pmem ncpu   mem   resi usrs tasks  jobids/users
  q008  excl  4.08    7974   4  18628   1275  1/1    4    263945 user
  q037  excl  4.02    7974   4  18628   1285  1/1    4    263945 user
```

The example job above is behaving correctly. Please consult the script located at `which pestat` for the description of the fields. The most important fields are: state = Torque state (second column) node can be free (not all the cores used), excl (all cores used) or download = CPU load average (third column)pmem = Physical memory (fourth column) amount of physical RAM installed in the node ncpu = total number of CPU cores (fifth column)resi = Resident (used) memory (seventh column)total memory in use on the given node (the one reported under RES by the "top" command). If used memory exceeds physical RAM on the node, or CPU load is significantly lower than number of CPU cores, the job becomes a candidate to be killed. An example of a job exceeding physical memory:

``` bash
$ pestat -f | grep 128081

m016  busy* 4.00    7990   4  23992   9937* 1/1    4    128081 user
m018  excl  4.00    7990   4  23992   9755* 1/1    4    128081 user
```

An example of a job with incorrect CPU load:

``` bash
$ pestat -f| grep 129284

a014  excl  7.00*  24098   8  72097   2530  1/1    8    129284 user
```

## Job Control
!!! info "Privileged Job Control Commands"

    Please note some commands will only work for privileged accounts. Please contact computerome@dtu.dk if you need to run these.

!!! tip "Checking job status"

    Non-privileged command

`checkjob -v <jobid>`

!!! tip "Monitoring batch jobs"

    Non-privileged command

The TORQUE command `qstat` is used to inquire about the status of one or more jobs:

``` bash
$ qstat -f <jobid>     (Inquire about a particular jobid)
$ qstat -r             (List all running jobs)
$ qstat -a             (List all jobs)
```

In addition, the Moab scheduler can be inquired using the `showq` command

``` bash
$ showq -r             (List all running jobs)
$ showq -i             (List all idle jobs. Idle jobs are ordered from highest priority to lowest priority)
$ showq                (List all jobs)
```

If you want to check the status of a particular jobid use `checkjob` command:

``` bash
$ checkjob <jobid>
```

!!! tip "Check when job will run"

    Non-privileged command

`showstart <jobid>`

Adding `-v` flag(s) to this command will increase the verbosity

!!! tip "Get status of fair-share"

    Non-privileged command

`diagnose -f`

!!! tip "Canceling a given job"

    Privileged command

`mjobctl -c <jobid>` or `canceljob <jobid>`

Force cancel job, try this if regular cancel fails

`mjobctl -F <jobid>`

!!! tip "Canceling jobs of a given user"

    Privileged command

`mjobctl -c -w user=<user_name>`

!!! tip "Requeue a job"

    Privileged command

`mjobctl -R <jobex>`

!!! tip "Change walltime"

    Privileged command

Changing the wallclock limit of a job by 10 hours 11 minutes and 12 seconds (request Computerome Support in good time to extend walltime for a running job). `<jobex\>` is a regex(7) regular expression preceeded by `x:` e.g.`x:abc12\[0-9\]`

` mjobctl -m wclimit+=10:11:12 <jobex>`

!!! tip "Check resource usage of a completed job"

    Privileged command

`tracejob -v <jobid>`

## Project Administration
!!! info "Project Administration"

    Request access and administer your project in Computerome's HPC environment using the following forms. Please download and fill in the relevant form and send it to computerome@dtu.dk. For more information, see our [Terms of Use](https://computerome.dk/terms-of-use).

:fontawesome-solid-file-pdf:  [Create a new HPC project](assets/uploads/request_to_create_a_new_HPC_project_updated_3d3575b094.pdf)

:fontawesome-solid-file-pdf:  [Create a new HPC project (DTU)](assets/uploads/request_to_create_a_new_HPC_project_at_dtu_updated_880f7b8d9a.pdf)

:fontawesome-solid-file-pdf:  [Modify user information](assets/uploads/request_to_modify_a_users_information_updated_37fcae683d.pdf)

:fontawesome-solid-file-pdf:  [Add new users to an existing HPC project](assets/uploads/request_to_add_new_users_to_an_existing_HPC_project_updated_826e19ef39.pdf)

:fontawesome-solid-file-pdf:  [Add existing users to an existing HPC project](assets/uploads/request_to_add_existing_users_to_an_existing_HPC_project_updated_6c1fc4ff27.pdf)

:fontawesome-solid-file-pdf:  [Remove user in an HPC project](assets/uploads/request_to_remove_a_user_from_an_HPC_project_updated_8c7a5d3590.pdf)

:fontawesome-solid-file-pdf:  [Inactivate user in an HPC project](assets/uploads/request_to_inactivate_a_user_of_an_HPC_project_updated_9854bbef3e.pdf)

:fontawesome-solid-file-pdf:  [Reactivate user in an HPC project](assets/uploads/request_to_reactivate_a_user_of_an_HPC_project_updated_4871addf0e.pdf)

:fontawesome-solid-file-pdf:  [Request to change legal project owner of an existing HPC project](assets/uploads/Request_to_change_legal_project_owner_of_an_existing_HPC_project_b51ef7cccc.pdf)

:fontawesome-solid-file-pdf: [Request to change technical project owner of an existing HPC project](assets/uploads/Request_to_change_technical_project_owner_of_an_existing_HPC_project_51143240a2.pdf)

:fontawesome-solid-file-pdf:  [Remove legal project owner and add new legal project owner](assets/uploads/request_to_change_legal_project_owner_of_an_existing_HPC_project_updated_6268c2dcc4.pdf)
