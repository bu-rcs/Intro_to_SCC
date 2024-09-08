# Python Examples

View full Python on the SCC documentation on [our website](https://www.bu.edu/tech/support/research/software-and-programming/common-languages/python/).

There are 3 Python environments available on the SCC:  
- python
- conda
- pre-defined ML coda environment

## Python
This environmen is most suitable for the code developers who use standard Python packages and do not require ML/DL Python packages such as *Tensorflow* or *Pytorch*.
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
