# Troubleshooting Guide

## Check Quota in your Home Directory

Being over the quota in your home directory can cause many problems. If you get errors or problems starting your interactive apps in OnDemand or running batch jobs, check your quota:

<pre><code>
[scc1$ ~] <b>quota -s</b>
Home Directory Usage and Quota:
Name           GB    quota    limit in_doubt    grace |    files    quota    limit in_doubt    grace
ktrn      3.72791     10.0     11.0      0.0     none |  115,486  200,000  200,000        0     none
</code></pre>

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


