---
title: "SLURM Array Jobs"
description: "SLURM array jobs allow you to submit and manage a collection of similar jobs using a single job submission. Each task in the array receives a unique task ID through the `SLURM_ARRAY_TASK_ID` environment variable."
tags:
  - HPC
---

# SLURM Array Jobs

SLURM array jobs allow you to submit and manage a collection of similar jobs using a single job submission. Each task in the array receives a unique task ID through the `SLURM_ARRAY_TASK_ID` environment variable.

Array jobs are especially useful when you need to run the same program many times with different:

- Input files
- Samples
- Parameters
- Simulations
- Datasets
- Experiments

Instead of submitting hundreds of individual jobs, you can submit one array job.

---

Basic Array Job:

The simplest way to create an array is with the `--array` option.

```bash
sbatch --array=1-10 my_job.sh
```

This creates 10 tasks:

```text
1
2
3
4
5
6
7
8
9
10
```

Each task has its own value of:

```bash
$SLURM_ARRAY_TASK_ID
```

Example

Create a file called `array_job.sh`:

```bash
#!/bin/bash

#SBATCH --job-name=array_example
#SBATCH --account=my_project
#SBATCH --partition=thinnode
#SBATCH --array=1-10
#SBATCH --time=00:10:00
#SBATCH --mem=1G

echo "Job ID: $SLURM_JOB_ID"
echo "Array Job ID: $SLURM_ARRAY_JOB_ID"
echo "Array Task ID: $SLURM_ARRAY_TASK_ID"

sleep 10
```

Submit it:

```bash
sbatch array_job.sh
```

SLURM will create one array containing 10 tasks.

---

## Understanding Array Job IDs

An array has a main job ID and individual task IDs.

For example:

```text
Array Job ID: 12345
Task IDs:     1-10
```

Individual tasks may be referenced as:

```text
12345_1
12345_2
12345_3
...
12345_10
```

The following variables are useful:

```bash
echo "Array Job ID: $SLURM_ARRAY_JOB_ID"
echo "Task ID: $SLURM_ARRAY_TASK_ID"
```

---

## Array Ranges

You can specify a range of task IDs.

```bash
#SBATCH --array=1-100
```

This creates 100 tasks:

```text
1, 2, 3, ..., 100
```

You can also use an array starting from zero:

```bash
#SBATCH --array=0-9
```

This creates:

```text
0, 1, 2, ..., 9
```

Starting from zero can be useful when working with programming languages such as Python, where arrays and lists commonly use zero-based indexing.

---

## Array Steps

You can specify a step size.

```bash
#SBATCH --array=1-100:10
```

This creates tasks:

```text
1
11
21
31
41
51
61
71
81
91
```

Another example:

```bash
#SBATCH --array=0-20:2
```

creates:

```text
0
2
4
6
8
10
12
14
16
18
20
```

---

## Specific Task IDs

You don't have to use a continuous range.

For example:

```bash
#SBATCH --array=1,5,10,20
```

creates four tasks:

```text
1
5
10
20
```

You can also combine ranges and individual task IDs:

```bash
#SBATCH --array=1-10,20,30-35
```

---

## Limiting Concurrent Tasks

A large array can contain hundreds or thousands of tasks.

You can limit how many tasks are allowed to run simultaneously by using `%`.

For example:

```bash
#SBATCH --array=1-100%10
```

This creates 100 tasks, but only 10 can run at the same time.

Once one task finishes, SLURM can start another task.

For Example

```text
Total tasks:       100
Maximum running:    10
```

This is useful when you want to avoid consuming too many cluster resources.

Another example:

```bash
#SBATCH --array=1-1000%50
```

creates 1000 tasks with a maximum of 50 running concurrently.

---

## Using "SLURM_ARRAY_TASK_ID"

The most important variable for array jobs is:

```bash
$SLURM_ARRAY_TASK_ID
```

It identifies the individual task.

For example:

```bash
#!/bin/bash

#SBATCH --array=1-5

echo "Running task $SLURM_ARRAY_TASK_ID"
```

The output will be different for each task:

```text
Running task 1
Running task 2
Running task 3
Running task 4
Running task 5
```

---

## Processing Different Input Files

One of the most common uses of array jobs is processing multiple files.

Suppose you have:

```text
data/
├── sample_1.txt
├── sample_2.txt
├── sample_3.txt
├── sample_4.txt
└── sample_5.txt
```

You can use the array task ID to select the corresponding file.

```bash
#!/bin/bash

#SBATCH --job-name=process_samples
#SBATCH --account=my_project
#SBATCH --partition=thinnode
#SBATCH --array=1-5
#SBATCH --time=00:30:00
#SBATCH --mem=2G

INPUT="data/sample_${SLURM_ARRAY_TASK_ID}.txt"

echo "Processing ${INPUT}"

./my_program "${INPUT}"
```

Task 1 processes:

```text
data/sample_1.txt
```

Task 2 processes:

```text
data/sample_2.txt
```

and so on.

---

## Processing Files with Python

You can also pass the task ID to a Python program.

SLURM script

```bash
#!/bin/bash

#SBATCH --job-name=python_array
#SBATCH --account=my_project
#SBATCH --partition=thinnode
#SBATCH --array=1-10
#SBATCH --time=00:30:00
#SBATCH --mem=4G

python process.py $SLURM_ARRAY_TASK_ID
```

Python script

```python
import sys

task_id = int(sys.argv[1])

print(f"Running task {task_id}")

# Your processing code here
```

Submit the job:

```bash
sbatch python_array.sh
```

---

## Processing Multiple Samples with Python

Suppose you have:

```text
samples/
├── sample_A.txt
├── sample_B.txt
├── sample_C.txt
├── sample_D.txt
└── sample_E.txt
```

Create a Python script:

```python
import sys

samples = [
    "sample_A.txt",
    "sample_B.txt",
    "sample_C.txt",
    "sample_D.txt",
    "sample_E.txt",
]

task_id = int(sys.argv[1])

sample = samples[task_id - 1]

print(f"Processing {sample}")
```

Then submit it using:

```bash
#!/bin/bash

#SBATCH --job-name=samples
#SBATCH --array=1-5
#SBATCH --time=00:30:00
#SBATCH --mem=4G

python process.py $SLURM_ARRAY_TASK_ID
```

The tasks will process:

```text
Task 1 → sample_A.txt
Task 2 → sample_B.txt
Task 3 → sample_C.txt
Task 4 → sample_D.txt
Task 5 → sample_E.txt
```

---

## Using a Parameter File

Another useful approach is to keep parameters in a text file.

For example, `parameters.txt`:

```text
sample_A
sample_B
sample_C
sample_D
sample_E
```

You can select a line using `sed`:

```bash
PARAMETER=$(sed -n "${SLURM_ARRAY_TASK_ID}p" parameters.txt)
```

Complete example:

```bash
#!/bin/bash

#SBATCH --job-name=parameters
#SBATCH --array=1-5
#SBATCH --time=00:20:00
#SBATCH --mem=2G

PARAMETER=$(sed -n "${SLURM_ARRAY_TASK_ID}p" parameters.txt)

echo "Running with parameter: ${PARAMETER}"

./my_program "${PARAMETER}"
```

Task 1 reads:

```text
sample_A
```

Task 2 reads:

```text
sample_B
```

and so on.

---

## Using a CSV File

You can also use a CSV file to store multiple parameters.

For example:

```text
sample,temperature,iterations
A,20,100
B,25,200
C,30,300
D,35,400
```

A Python script can select the row corresponding to the task ID:

```python
import csv
import sys

task_id = int(sys.argv[1])

with open("parameters.csv") as f:
    rows = list(csv.DictReader(f))

row = rows[task_id - 1]

sample = row["sample"]
temperature = row["temperature"]
iterations = row["iterations"]

print(f"Sample: {sample}")
print(f"Temperature: {temperature}")
print(f"Iterations: {iterations}")
```

Submit it with:

```bash
#!/bin/bash

#SBATCH --job-name=csv_array
#SBATCH --account=my_project
#SBATCH --partition=thinnode
#SBATCH --array=1-4
#SBATCH --time=01:00:00
#SBATCH --mem=2G

python process.py $SLURM_ARRAY_TASK_ID
```

---

## Array Output Files

Array jobs can produce separate output files for each task.

SLURM provides two useful filename substitutions:

```text
%A = Array job ID
%a = Array task ID
```

For example:

```bash
#SBATCH --output=logs/job_%A_%a.out
#SBATCH --error=logs/job_%A_%a.err
```

For an array job with ID `12345`, the output could look like:

```text
logs/job_12345_1.out
logs/job_12345_2.out
logs/job_12345_3.out
```

and error files:

```text
logs/job_12345_1.err
logs/job_12345_2.err
logs/job_12345_3.err
```

This makes it easy to identify which task produced a particular output.

---

## Complete Output Example

A complete script might look like this:

```bash
#!/bin/bash

#SBATCH --job-name=process_samples
#SBATCH --array=1-20%5
#SBATCH --time=01:00:00
#SBATCH --mem=4G
#SBATCH --cpus-per-task=2
#SBATCH --output=logs/%A_%a.out
#SBATCH --error=logs/%A_%a.err

INPUT="data/sample_${SLURM_ARRAY_TASK_ID}.txt"
OUTPUT="results/sample_${SLURM_ARRAY_TASK_ID}.out"

echo "=============================="
echo "Array Job ID: ${SLURM_ARRAY_JOB_ID}"
echo "Job ID:       ${SLURM_JOB_ID}"
echo "Task ID:      ${SLURM_ARRAY_TASK_ID}"
echo "Input:        ${INPUT}"
echo "Output:       ${OUTPUT}"
echo "=============================="

./my_program "${INPUT}" > "${OUTPUT}"
```

This example:

- Creates 20 tasks.
- Allows a maximum of 5 tasks to run simultaneously.
- Allocates 2 CPUs per task.
- Allocates 4 GB of memory per task.
- Gives each task its own output file.
- Uses the task ID to select the input file.

Submit it with:

```bash
sbatch array_job.sh
```

---

## Monitoring Array Jobs

Use `squeue` to monitor jobs:

```bash
squeue
```

You can also specify a job ID:

```bash
squeue -j 12345
```

For more detailed information:

```bash
squeue -j 12345 -o "%.18i %.9P %.20j %.8u %.2t %.10M %.6D %R"
```

You can also filter by your username:

```bash
squeue -u $USER
```

---

Checking Completed Array Jobs:

Use `sacct` to inspect completed jobs:

```bash
sacct -j 12345
```

For more detailed information:

```bash
sacct -j 12345 --format=JobID,JobName,State,Elapsed,MaxRSS,ExitCode
```

You may see output similar to:

```text
JobID       JobName      State      Elapsed    MaxRSS    ExitCode
------------ ------------ ---------- ---------- --------- --------
12345        process      COMPLETED  00:12:31
12345_1      process      COMPLETED  00:12:20  3500K     0:0
12345_2      process      COMPLETED  00:11:45  4200K     0:0
12345_3      process      FAILED     00:02:10  3900K     1:0
```

An exit code of:

```text
0:0
```

normally indicates successful completion.

---

Cancelling an Entire Array:

To cancel the entire array:

```bash
scancel 12345
```

Replace `12345` with the array job ID.

---

Cancelling One Array Task:

You can cancel an individual task:

```bash
scancel 12345_5
```

This cancels task 5 while leaving the other tasks running.

For example:

```text
12345_1  RUNNING
12345_2  RUNNING
12345_3  RUNNING
12345_4  RUNNING
12345_5  CANCELLED
12345_6  PENDING
```

---

Re-running a Failed Task:

If one task fails, you can submit that task again.

For example:

```bash
sbatch --array=5 array_job.sh
```

This submits only task 5.

You can also submit several specific tasks:

```bash
sbatch --array=3,5,8 array_job.sh
```

---

## Array Jobs with Different Resources

All tasks in a normal array use the same resource request.

For example:

```bash
#SBATCH --array=1-20
#SBATCH --cpus-per-task=4
#SBATCH --mem=8G
```

Each task requests:

```text
4 CPUs
8 GB memory
```

If different tasks require substantially different resources, it may be better to use separate jobs or job arrays designed around similar resource requirements.

---

## Array Jobs with GPUs

Array jobs can also be used for GPU workloads.

For example:

```bash
#!/bin/bash

#SBATCH --job-name=gpu_array
#SBATCH --account=my_project
#SBATCH --partition=gpuv1
#SBATCH --array=1-10
#SBATCH --gres=gpu:1
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00

echo "Running GPU task ${SLURM_ARRAY_TASK_ID}"

python train.py ${SLURM_ARRAY_TASK_ID}
```

This creates 10 GPU tasks.

If you want to limit concurrent GPU usage:

```bash
#SBATCH --array=1-10%2
```

Only two tasks will run at the same time.

---

## Array Jobs with Environment Variables

Environment variables can be passed into an array job.

For example:

```bash
export DATASET=my_dataset

sbatch --array=1-10 array_job.sh
```

The script can access:

```bash
echo "Dataset: $DATASET"
echo "Task: $SLURM_ARRAY_TASK_ID"
```

This allows the same array script to be reused with different datasets.

---

## Using a Bash Array

Bash arrays can also be combined with SLURM arrays.

For example:

```bash
#!/bin/bash

#SBATCH --array=1-4

FILES=(
    "sample_A.txt"
    "sample_B.txt"
    "sample_C.txt"
    "sample_D.txt"
)

INDEX=$((SLURM_ARRAY_TASK_ID - 1))

INPUT=${FILES[$INDEX]}

echo "Processing ${INPUT}"
```

The task ID is converted from SLURM's numbering to Bash's zero-based indexing.

---

## Common Mistake: Incorrect Array Index

Suppose you have:

```bash
FILES=(
    "sample_A.txt"
    "sample_B.txt"
    "sample_C.txt"
)
```

Bash indexes this array as:

```text
0 → sample_A.txt
1 → sample_B.txt
2 → sample_C.txt
```

But your SLURM array may be:

```bash
#SBATCH --array=1-3
```

Therefore, you need:

```bash
INDEX=$((SLURM_ARRAY_TASK_ID - 1))
```

Then:

```bash
INPUT=${FILES[$INDEX]}
```

Without subtracting one, task 1 would select the second file instead of the first.

---

## Complete Practical Example

Suppose you have 100 samples:

```text
data/
├── sample_001.txt
├── sample_002.txt
├── sample_003.txt
...
└── sample_100.txt
```

Create `process_samples.sh`:

```bash
#!/bin/bash

#SBATCH --job-name=samples
#SBATCH --array=1-100%10
#SBATCH --time=00:30:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=4G
#SBATCH --output=logs/%A_%a.out
#SBATCH --error=logs/%A_%a.err

INPUT=$(printf "data/sample_%03d.txt" "$SLURM_ARRAY_TASK_ID")
OUTPUT=$(printf "results/sample_%03d.out" "$SLURM_ARRAY_TASK_ID")

echo "Processing ${INPUT}"

mkdir -p results

./my_program "${INPUT}" > "${OUTPUT}"

echo "Finished ${INPUT}"
```

Create the directories:

```bash
mkdir -p logs results
```

Submit:

```bash
sbatch process_samples.sh
```

This creates 100 tasks but runs at most 10 simultaneously.

---

## Useful SLURM Array Variables

The following variables are particularly useful:

| Variable | Description |
|---|---|
| `SLURM_ARRAY_JOB_ID` | Main job ID of the array |
| `SLURM_ARRAY_TASK_ID` | ID of the current array task |
| `SLURM_ARRAY_TASK_COUNT` | Total number of tasks |
| `SLURM_ARRAY_TASK_MIN` | Lowest task ID |
| `SLURM_ARRAY_TASK_MAX` | Highest task ID |
| `SLURM_JOB_ID` | ID of the current job/task |

Example:

```bash
echo "Array job:   ${SLURM_ARRAY_JOB_ID}"
echo "Job ID:      ${SLURM_JOB_ID}"
echo "Task ID:     ${SLURM_ARRAY_TASK_ID}"
echo "Task count:  ${SLURM_ARRAY_TASK_COUNT}"
echo "Minimum ID:  ${SLURM_ARRAY_TASK_MIN}"
echo "Maximum ID:  ${SLURM_ARRAY_TASK_MAX}"
```

---

## Quick Reference

Submit an array:

```bash
sbatch --array=1-10 job.sh
```

Submit an array with a concurrency limit:

```bash
sbatch --array=1-100%10 job.sh
```

Submit specific tasks:

```bash
sbatch --array=1,5,10 job.sh
```

Check jobs:

```bash
squeue -u $USER
```

Check completed jobs:

```bash
sacct -j JOB_ID
```

Cancel the complete array:

```bash
scancel JOB_ID
```

Cancel one task:

```bash
scancel JOB_ID_TASK_ID
```

Get the current task ID:

```bash
echo $SLURM_ARRAY_TASK_ID
```

Get the array job ID:

```bash
echo $SLURM_ARRAY_JOB_ID
```

Create separate output files:

```bash
#SBATCH --output=logs/%A_%a.out
```

Create separate error files:

```bash
#SBATCH --error=logs/%A_%a.err
```

---

## Best Practices

When using SLURM array jobs:

1. **Use `%` to limit concurrency** when submitting large arrays.

    ```bash
    #SBATCH --array=1-1000%20
    ```

2. **Use `$SLURM_ARRAY_TASK_ID`** to select input files or parameters.

3. **Use separate output files** for each task.

    ```bash
    #SBATCH --output=logs/%A_%a.out
    ```

4. **Create output and log directories before running the job.**

    ```bash
    mkdir -p logs results
    ```

5. **Check completed tasks with `sacct`.**

    ```bash
    sacct -j JOB_ID
    ```

6. **Retry only failed tasks** rather than resubmitting the entire array.

    ```bash
    sbatch --array=5 array_job.sh
    ```

7. **Avoid unnecessarily large resource requests.** Resource requests apply to each task, so requesting 16 CPUs for a 100-task array can represent a very large resource demand.

---

### Summary

SLURM array jobs provide an efficient way to run many similar jobs with a single submission.

A basic array looks like:

```bash
#SBATCH --array=1-10
```

A concurrency-limited array looks like:

```bash
#SBATCH --array=1-100%10
```

The task ID is available through:

```bash
$SLURM_ARRAY_TASK_ID
```

and can be used to select different inputs:

```bash
INPUT="data/sample_${SLURM_ARRAY_TASK_ID}.txt"
```

Separate output files can be created with:

```bash
#SBATCH --output=logs/%A_%a.out
#SBATCH --error=logs/%A_%a.err
```

For monitoring:

```bash
squeue -u $USER
```

For completed jobs:

```bash
sacct -j JOB_ID
```

And to cancel an individual task:

```bash
scancel JOB_ID_TASK_ID
```

Array jobs are therefore well suited for large collections of independent or similarly structured computations, while allowing SLURM to manage scheduling, resource allocation, monitoring, and task execution.
