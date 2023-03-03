# ICMPWaveformClassificationPlugin
ICP Pulse Waveform Classification Plugin for ICM+.
# Installation
1. Install ICM+ Version that supports Python scripting.
2. Install [Anaconda](https://www.anaconda.com/) 
3. Clone or Download this repository
4. Copy the files contained in the ```plugin``` directory to ICM+ Plugin directory. It's usually located at:
```
C:\Users\Public\Documents\ICM+\Plugins64\Python
```
5. Create new anaconda environment using Anaconda Prompt and commands
```
cd <path to main directory of the repository>
conda env create -f environment.yml
```
After creating the environment, activate it using
```
conda activate ICMPlugin
```
And install one of the recommended requirement packages:
 - If you have [CUDA 11.7 capable GPU](https://docs.nvidia.com/deploy/cuda-compatibility/index.html) on your machine use:
 ```
 pip install -r requirements-gpu.txt
 ```
 Otherwise use
 ```
 pip install -r requirements-cpu.txt
 ```

 Once it's installed the Anaconda Prompt window can be closed

6. Launch ICM+ and in the Settings provide the path to your Anaconda environment. Usually located at:
```
C:\Users\<user>\anaconda3\envs\ICMPlugin\
```
7. You can use the Plugin for calculations within the ICM+.
It provides a function called PyClassifyWaveforms that takes ICP signal as an argument.
We recommend setting the calculations to 300 second window with 60 second stride.
