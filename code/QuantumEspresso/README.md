# Quantum Espresso Example


## Run Interactively

To run this example interactively, open a Desktop Interactive Session (in SCC OnDemand) and select appropriate number of CPU cores.
Run the following command in the terminal window:

```
module load openmpi/4.1.5_gnu-12.2.0
module load quantumespresso/7.2

export PSEUDO_DIR=$ESPRESSO_PSEUDO
export BIN_DIR=$SCC_QUANTUMESPRESSO_BIN

./run_example
```

## Batch Job

To run this example within a batch job:

```
qsub job.qsub
```

To run the above job on  several nodes (using MPI), instead of `-pe omp 4` flag in the job.qsub file, add `-pe mpi_tasks_28 56` flag, where 56 is the total number of CPU cores you need. This number should be a multiple of 28 (the number of CPU tasks in the flag). 

