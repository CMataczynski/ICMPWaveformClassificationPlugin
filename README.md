# ICMPWaveformClassificationPlugin
ICP Pulse Waveform Classification Plugin (from [End-to-End Automatic Morphological Classification of Intracranial Pressure Pulse Waveforms Using Deep Learning](https://ieeexplore.ieee.org/document/9453152)) for ICM+.

# Expected performance

The plugin's speed was tested on different length of files. The testing platform was equipped with Nvidia 3070Ti GPU, Ryzen 5600x CPU, 16 Gb of RAM and tested under ICM+ version 9.1. All of the results are of only PSI computation with 300 second window and 10 second stride.
| File length | ICP sampling frequency | Processing time |
| ----------- | ---------------------- | --------------- |
| 34 min | 240 Hz | 31s |
| 1hr 35min | 240 Hz | 2min 13s |
| 7hr 16min | 200 Hz | 5m 37s |
| 1hr 42min | 30 Hz | 1m 17s |


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
We recommend setting the calculations to 300 second window with 60 second stride (or 10 seconds for improved resolution. This however will result in slower computation speed).

# Cite this work
```
@article{kazimierska2023relationship,
  title={Relationship between the shape of intracranial pressure pulse waveform and computed tomography characteristics in patients after traumatic brain injury},
  author={Kazimierska, Agnieszka and Uryga, Agnieszka and Mataczy{\'n}ski, Cyprian and Czosnyka, Marek and Lang, Erhard W and Kasprowicz, Magdalena},
  journal={Critical Care},
  volume={27},
  number={1},
  pages={447},
  year={2023},
  publisher={Springer}
}

@article{mataczynski2021end,
  title={End-to-end automatic morphological classification of intracranial pressure pulse waveforms using deep learning},
  author={Mataczy{\'n}ski, Cyprian and Kazimierska, Agnieszka and Uryga, Agnieszka and Burzy{\'n}ska, Ma{\l}gorzata and Rusiecki, Andrzej and Kasprowicz, Magdalena},
  journal={IEEE Journal of Biomedical and Health Informatics},
  volume={26},
  number={2},
  pages={494--504},
  year={2021},
  publisher={IEEE}
}
```
