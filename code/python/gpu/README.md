# Running a GPU job

This directory contains an example of python script with a corresponding bash script example. The python script contains a simple *pytorch* example from the [pytorch GitHub examples website](https://github.com/pytorch/examples/tree/main)

To submit a job, execute:
```
[ scc1$ gpu ] qsub gpu_job.qsub
```


**Note**: Do not change the values of `CUDA_VISIBLE_DEVICES` environment variables. They are set by the batch system when you request GPU resources.
