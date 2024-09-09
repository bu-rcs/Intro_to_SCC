# Submit a Basic Batch Job

This directory contains 3 scripts:

`hello_world.py` - a Python script that prints a *Hello, World!* message, current python version and a list of the locally installed packages;<br>
`python_job.qsub` - a bash script to submit the above *hello_world.py* script using a regular *python3* module;<br>
`conda_job.qsub` - a bash script to submit the above *hello_world.py* script using a *miniconda* module.<br>

To submit a job, execute:

<pre><code>
[scc1$ ~] <b>qsub python_job.qsub</b>
Your job 9800289 ("test_py_hello") has been submitted
</code></pre>
or 
<pre><code>
[scc1$ ~] <b>qsub conda_job.qsub</b>
Your job 9800290 ("test_conda_hello") has been submitted
</code></pre>

When a batch job completes, it generates an output file that has a name of the job and extension as a `*.o<JOB_ID>`.
This file will contain the messages that usually go to the console output together with warning and error messages (if any).
