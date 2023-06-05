![GEE_ML](./Images/GEE_ML_Hydrological_Cycle.jpg)

# Getting Started: Virtual Environment
It is a best practice to create a virtual environment when starting a new project, as a virtual environment essentially creates an isolated working copy of Python for a particular project. 
I.e., each environment can have its own dependencies or even its own Python versions.
Creating a Python virtual environment is useful if you need different versions of Python or packages for different projects.
Lastly, a virtual environment keeps things tidy, makes sure your main Python installation stays healthy, and supports reproducible and open science.

## Creating your Python-GEE Virtual Environment
Since we will be using Jupyter Notebooks for this exercise, we will use the Anaconda command prompt to create our vitual environment. 
In the command line type: 
![GEE_venv](./Images/condaEnv.JPG)

For this example, we will be using Python version 3.9.12, specify this version when setting up your new virtual environment.
After Anaconda finished setting up your GEE_env, activate it using the activate function.
![GEE_activate](./Images/condaActivate.JPG)

You should now be working in your new GEE_env within the command prompt. 
However, we will want to work in this environment within our Jupyter Notebook and need to create a kernel to connect them.
We begin by installing the **ipykernel** python package:
![GEE_ipykernel](./Images/GEE_ipkernel.JPG)

With the package installed, we can connect the GEE_env to our Python Notebook
![GEE_ipykernel_install](./Images/GEE_ipkernel_install.JPG)

Open up the [GEE_Workshop_CH1.ipynb](./GEE_Workshop_CH1.ipynb) file, click the kernal tab on the top toolbar, and select the GEE_env. 
The GEE_env should show up on the top right of the Jupyter Notebook.
![GEE_Notebook_GEE_env](./Images/GEE_Jupyter_Kernel2.JPG)