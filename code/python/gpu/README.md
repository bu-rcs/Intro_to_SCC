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


## Enabling GPU usage in Pytroch

Use the command `torch.cuda.is_available()` to see if a GPU is available:

```
import torch
# Set the device name to cuda when GPU is available, cpu otherwise
if torch.cuda.is_available():
    device = torch.device("cuda")
else:
    device = torch.device("cpu")
print("Code is running on :", "CPU" if device.type=="cpu" else "GPU")
```

## Enabling GPU usage in Tensorflow

If a TensorFlow operation has both `CPU` and `GPU` implementations, by default, the `GPU` device is prioritized when the operation is assigned. For example, `tf.matmul` has both `CPU` and `GPU` kernels and on a system with devices `CPU:0` and `GPU:0`, the `GPU:0` device is selected to run tf.matmul unless you explicitly request to run it on another device.

```
import tensorflow as tf

# Check if GPUs are available to you:
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))

# Enable debug print statements to view if GPUs are used
tf.debugging.set_log_device_placement(True)
```
Do not set visible devices `tf.config.set_visible_devices ` manually. GPUs are assigned to your job by the scheduler



