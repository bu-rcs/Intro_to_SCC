# Introduction to the Shared Computing Cluster for Academic Classes
*Research Computing Services*


## Introduction
The Boston University Shared Computing Cluster (SCC) is a heterogeneous Linux cluster composed of both Shared and Buy-in components. The system currently includes over 28,000 CPU cores, 400 GPUs, and nearly 14 petabytes of storage for research data.

The SCC is suitable for high-performance computing in a wide range of disciplines, from the physical sciences, engineering, biostatistics, public and global health, bioinformatics, genomics, neuroscience, and geographic information systems (GIS), to emerging computational communities such as machine learning, economics, finance, the social sciences, microbiology, and infectious diseases.

## Connecting to the SCC

### Using SCC-OnDemand:

SCC OnDemand is the recommended way to access the BU Shared Computing Cluster (SCC) over the web using a graphical, menu-based environment that doesn’t require using an SSH client. It is particularly well suited to applications like MATLAB, RStudio, and Jupyter Notebook which have a graphical component. Additionally, OnDemand allows you to upload and download files, launch applications, view disk quotas and do many other things on the SCC.

To launch OnDemand, go to: [scc-ondemand.bu.edu](https://scc-ondemand.bu.edu/)

### Using `ssh`

To connect to the SCC, use either `scc1` or `scc2` login node:

```
ssh username@scc1.bu.edu
```

## SCC Navigation & Storage Quotas

Each SCC user has a small (10GB) private home directory. It is commonly used to store personal files. The space in home directory **cannot** be increased. To monitor your *Home Directory* space usage, execute:
<pre><code>
[scc1$ ~] <b>quota -s</b>
Home Directory Usage and Quota:
Name           GB    quota    limit in_doubt    grace |    files    quota    limit in_doubt    grace
ktrn      3.72791     10.0     11.0      0.0     none |  115,486  200,000  200,000        0     none
</code></pre>

In addition to home directory, SCC users have a project space. To see the list of projects to which you belong to, execute:
<pre><code>
[scc1$ ~] <b>groups</b>
cs101
</code></pre>

To see the path to the project space and the project space quota, execute:
<pre><code>
[scc1$ ~] <b>pquota</b>
                                      quota     quota       usage     usage
project space                          (GB)    (files)       (GB)   (files)
-----------------------------------  ------  ---------  ---------  --------
/projectnb/cs101                       1000   32768000     187.08     47984
</code></pre>

For many academic projects, the project space has the following structure:
<pre><code>
# Set current directory to the project directory  
[scc1$ ~] <b>cd /projectnb/cs101</b>

# List files and directories  
[scc1$ ~]<b> ls -l</b>
drwxrws---  2 root cs101ta 4096 Sep  7  2024 admin
drwxr-s--- 18 root cs101ta 4096 Sep  7  2024 archive
drwxrwsr-x  5 root cs101ta 4096 Sep  7  2024 materials
drwxrwsr-t  7 root cs101   4096 Sep  7  2024 projects
drwxr-sr-x 21 root cs101ta 4096 Sep  7  2024 students
</code></pre>

`admin` -  can be accessed and edited by the course instructors only<br>
`archive` -  archive directory, can only be accessed by the course instructors<br> 
`materials` - a directory with course materials prepared by the instructors<br>
`projects` - a directory that can be used by students to work on group projects<br>
`students` - a directory for the student individual assignments. Student folders in this directory can only be accessed by the student and instructors. Students do not have permissions to view each others folders.




