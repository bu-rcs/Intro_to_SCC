# Running Notebooks on the SCC

Python Notebooks can be run interactively or can be submitted as a batch job.

## Interactive Usage

You can open a Notebook using interactive *Jupyter Notebook* App or *VSCode Server*.
See [Python Editors and IDEs](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-editing/) documentation.  
**Note:** There is a <span  style="color:red">**maximum of 5 interactive apps**</span> you can open simultaniously on the SCC.

We highly recommend to use interactive apps to develop a code using a relatively small example. For your long (production) job, submit your script as a batch job.  
**Warning:** SCC *process reaper* terminates any batch jobs if the requested GPU(s) remain idle for two hours. 


## Running notebook as a batch job
This directory contains a simple notebook and a bash script that can be used to submit this notebook as a batch job.
