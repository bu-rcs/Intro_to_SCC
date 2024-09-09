# Troubleshooting Guide

## Check Quota in your Home Directory

Being over the quota in your home directory can cause many problems. If you get errors or problems starting your interactive apps in OnDemand or running batch jobs, check your quota:

<pre><code>
[scc1$ ~] <b>quota -s</b>
Home Directory Usage and Quota:
Name           GB    quota    limit in_doubt    grace |    files    quota    limit in_doubt    grace
ktrn      3.72791     10.0     11.0      0.0     none |  115,486  200,000  200,000        0     none
</code></pre>

If your home directory quota is exceeded 10GB, you can use the `du` command to search for the large files and folders in your home directory:

<pre><code>
[scc1$ ~] <b>cd</b>
[scc1$ ~] <b>du -h --max-depth=1</b>
</code></pre>  

If you find that your `.local` or `.conda` are large, you probably use your home directory to install Python packages. Read our [Python Documentation](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-installs/) to learn how to change the location of Python package installation.

## Check your `.bashrc` file 

Your `.bashrc` file should **NOT** contain `module load` commands or any `conda` - specific commands.
Do not run `conda init` or `conda update` commands. And if you did my mistake, remove the lines they added to your `.bashrc` file.

## `PATH` environment variable

Be careful modifying the `PATH` environment variable. 

## `sudo` usage

Only System Administrators can run `sudo` command. So do not run it (even if you find directions to do so on some webpage) - it will not work.

## Use CPU and GPU resources you request from the batch system

Do not set GPUs in your code - use the ones that are assigned to you by the system. Use `CUDA_VISIBLE_DEVICES` environment variable to see what they are.

Use `NSLOTS` environment variable in your script to set the number of parallel threads instead of letting the program use all CPU cores available on the compute node.

## Check GPU utilization and memory usage before requesting more resources

Asking for more GPUs will not necessarily make you code run faster. Make sure you optimally utilize your available GPU resources. Use `nvidia-smi` command to view GPU utilization.


