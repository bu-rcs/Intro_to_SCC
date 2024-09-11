# Submit a Basic Batch Job

This directory contains 2 scripts:

`hello.R` - an R script that prints a *Hello, World!* message, current R version and create a basic histogram plot<br>
`rjob.qsub` - a bash script to submit the above *hello.R* script using an *R* module;<br>

To submit a job, execute:

<pre><code>
[scc1$ ~] <b>qsub rjob.qsub</b>
Your job 9800289 ("r_test") has been submitted
</code></pre>

When a batch job completes, it generates an output file that has a name of the job and extension as a `r_test.o<JOB_ID>`.
This file will contain the messages that usually go to the console output together with warning and error messages (if any).

