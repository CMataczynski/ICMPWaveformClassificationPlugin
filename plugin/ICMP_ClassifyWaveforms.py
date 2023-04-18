import sys
import os
import inspect
from pathlib import Path

library_path = "C:\\Users\\Public\\Documents\\ICM+\\Plugins64\\Python\\pulse_detection"
if library_path not in sys.path:
    sys.path.append(str(library_path))

import numpy as np
import torch
from classifier_pipeline import ProcessingPipeline

class ClassifyWaveforms:
    # DO NOT MODIFY this method
    # It will provide backward compatibility wth the older ICM+--Python interface.
    def set_parameter(self, param_name, param_value):
        setattr(self, param_name, param_value)

    # You can append your own code to the constructor, if needed.
    # You should not set here values of parameters declared in your XML
    # configuration file because ICM+ will do it for you.
    # You will have to add your own code, only if you need to initialise some
    # extra data structures which were not declared in the XML config file.
    def __init__(self):
        self.processing_pipeline = ProcessingPipeline(memorize_last_segment=False)
        self.variables = []
        self.sampling_freq = None
        # print("gpu available")
        # print(torch.cuda.is_available())

    # You can append your own code to the destructor but most likely you will not need it
    def __del__(self):
        pass

    # 'calculate' is the main work-horse function.
    # It is called with a data buffer (one or more) of size corresponding to the Calculation Window
    # It must return one floating-point number
    # It take the following parameters:
    # sig1 - input variable/signal 1
    # ts_time - part of the data time stamp - number of milliseconds since midnight
    # ts_date - Part of the data time stamp - One plus number of days since 1/1/0001
    # Use the class member self.sampling_freq to calculate the time vector
    # Note: the class member 'self.variables' includes indices of the used variables
    #       These can be used to check if the function has already been called with identical parameters
    #       in order to avoid unnecessery re-calculations
    def calculate(self, sig1, ts_time, ts_date):
        # my_own_code_here
        sig1= np.array(sig1)
        sig1 = sig1[(~np.isnan(sig1))]
        if len(sig1) > 1:
            return np.nan
        
        ts_time_seconds = ts_time * 1e-3
        time_step = 1 / self.sampling_freq
        time_vector = ts_time_seconds + time_step * np.arange(len(sig1))
        

        classes, _ = self.processing_pipeline.process_signal(sig1, time_vector)
        classes = np.argmax(classes, axis=1)
        uniq, cnt = np.unique(classes, return_counts=True)

        cnt = cnt[uniq != 4]
        uniq = uniq[uniq != 4]
        cnt = cnt / cnt.sum()
        
        psi = 0
        for cls, cnt in zip(uniq, cnt):
            psi += (cls+1) * cnt
        

        return psi
