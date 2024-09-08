# Introduction to the Shared Computing Cluster
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
