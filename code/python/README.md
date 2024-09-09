# Using Python on the Shared Computing Cluster

View full Python on the SCC documentation on [our website](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/).

There are 3 Python environments available on the SCC:  
- python
- conda
- pre-defined ML coda environment

## Python
This environmen is most suitable for the code developers who use standard Python packages and do not require ML/DL Python packages such as *Tensorflow* or *Pytorch*. It also comes with Jupyter Notebook and Spyder code development environments.
We have several python versions installed. Use `module avail` command to query available python versions:

<pre><code>
[scc1$ ~] <b>module avail python</b>
--------------------------------------- /share/module.8/programming ----------------------------------
   python3/3.6.9     python3/3.7.5     python3/3.8.3           python3/3.8.16    python3/3.10.12 (L,D)
   python3/3.6.10    python3/3.7.7     python3/3.8.6           python3/3.9.4     python3/3.12.4
   python3/3.6.12    python3/3.7.9     python3/3.8.10.clean    python3/3.9.9
   python3/3.7.3     python3/3.7.10    python3/3.8.10          python3/3.10.5
</code></pre>

The above python installations include many popular packages such as *numpy*, *pandas*, *matplotlib*, etc.

We recommend you use [Python virtual environments](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-installs/virtualenv/#venv) if you need to install additional Python packages. 

## Conda
This environment is suitable for the code developers who are planning to install various Python packages and set up their own environments.
By default it does not contain any packages. Follow the steps below to get started. 
### 1. Load miniconda module
There are a few versions of miniconda. We recommend you use the latest version:
<pre><code>
[scc1$ ~] <b>module avail miniconda</b>
--------------------------------------- /share/module.8/programming ----------------------------------
miniconda/23.1.0    miniconda/23.5.2    miniconda/23.11.0 (L)    miniconda/24.5.0 (D)
</code></pre>

### 2. Configure ( one time only )
By default, conda packages are installed into user's home directory. To avoid exceeding home directory quota, configure the location for environments and packages in your project space:

<pre><code>
[scc1$ ~] <b>module load miniconda</b>
[scc1$ ~] <b>setup_scc_condarc.sh</b>
</code></pre>
The above script will generate a `.condarc` file in your home directory which you can later adjust if needed:

```
[scc1$ ~] cat ~/.condarc
envs_dirs:
    - /projectnb/your_project/your_loginname/.conda/envs
    - ~/.conda/envs
pkgs_dirs:
    - /projectnb/your_project/your_loginname/.conda/pkgs
    - ~/.conda/pkgs
env_prompt: ({name})
```

**Note**: Do not run `conda init` or `conda update` commands on the SCC. They will cause unexpected behavior of various applications on the SCC.


### 3. Set up your environment and install packages

Use `mamba create` command to install the desired Python version and packages. You can also use `conda create` command, but it will run significantly slower. In the example below, we install Python version 3.10, Jupyter Notebook, Jupyter Lab and Spyder. You can adjust this command to add or remove other packages.
<pre><code>
[scc1 ~] <b>module load miniconda</b>
[scc1 ~] <b>mamba create</b> -y -n my_conda_env python=3.10 notebook jupyterlab spyder
</code></pre>   


### 4. Activate your environment

If you run your code in a terminal or submit your script as a batch job, you need to activate your environment once you load miniconda module
<pre><code>
[scc1 ~] <b>module load miniconda</b>
[scc1 ~] <b>mamba activate </b> my_conda_env
</code></pre>  

when you no longer need this environment, you can deactivate it:
<pre><code>
[scc1 ~] <b>conda deactivate </b>
</code></pre>

If you run your code in on of the SCC OnDemand Interactive app (like Jupyter Lab, Spyder or VSCode), make sure you add `conda activate` command in the *Pre-Launch command* field in the Apps Initialization form (see our [Python Editors and IDEs Documentation](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-editing/) for more information)

## Academic Machine Learning Environment

The module academic-ml provides a set of conda environments with several different machine learning (ML) libraries installed, in addition to a large amount of useful Python software. 

First, follow the first two steps outlined in the previous session to set up your `.condarc` file.

Academic ML module comes with 3 environments:
**fall-2024-pyt**  – PyTorch 2.4.0<br>
**fall-2024-tf**  – Tensorflow 2.17.0<br>
**fall-2024-jax**  – Jax 0.43.0<br>

To use this environment to run a pytorch script for example, execute:
<pre><code>
[scc1 ~] <b>module load miniconda</b>
[scc1 ~] <b>module load academic-ml/fall-2024</b>
[scc1 ~] <b>conda activate fall-2024-pyt</b>
</code></pre>  

For more information or to learn how to customize your ML environment see our [Academic Machine Learning Environment Documentation](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/python-ml/academic-machine-learning-environment/)
