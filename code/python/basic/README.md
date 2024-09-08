# Submit a Basic Batch Job

This directory contains 3 scripts:

`hello_world.py` - a Python script that prints a *Hello, World!* message, current python version and a list of the locally installed packages;<br>
`python_job.qsub` - a bash script to submit the above *hello_world.py* script using a regular *python3* module;<br>
`conda_job.qsub` - a bash script to submit the above *hello_world.py* script using a *miniconda* module.<br>

To submit a job, execute:

<pre><code>
[scc1$ ~] <b>qsub python_job.qsub</b>
</code></pre>
or 
<pre><code>
[scc1$ ~] <b>qsub conda_job.qsub</b>
</code></pre>
