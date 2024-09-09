# Running a GPU job

This directory contains an example of python script with a corresponding bash script example. The python script contains a simple *pytorch* example from the [pytorch GitHub examples website](https://github.com/pytorch/examples/tree/main)

To submit a job, execute:
```
[ scc1$ gpu ] qsub gpu_job.qsub
```


**Note**: Do not change the value of `CUDA_VISIBLE_DEVICES` environment variable. It is set by the batch system when you request GPU resources.


## Checking GPU resource usage

While your job is running in the queue, you can check the GPU utilization. 
First find the name of the node where your job is running:

<pre><code>
[ scc1$gpu ] <b>qstat -u</b> username 
job-ID  prior   name       user         state submit/start at     queue                          slots ja-task-ID
-----------------------------------------------------------------------------------------------------------------
9807422 0.43438 QRLOGIN    user         r     09/08/2024 21:40:46 l40s@<b><span style="color:red">scc-506</span></b>.scc.bu.edu            1
</code></pre>

Then login to the node and run `nvidia-smi` command:

<pre><code>
[ scc1$gpu ] <b>ssh scc-506</b>
[ scc1$gpu ] <b>nvidia-smi -l</b>
</code></pre>
