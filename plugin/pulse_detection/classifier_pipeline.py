import numpy as np
import yaml
from pathlib import Path
import os

from pulse_detector import Segmenter
from pulse_classifier import Classifier

class ProcessingPipeline:
    def __init__(self, estimate_fs=True, memorize_last_segment=True) -> None:
        self._load_parameters()
        self.segmenter = Segmenter()
        self.classifier = Classifier(self.params)
        self.estimate_fs = estimate_fs
        self.memory = None
        self.memorize_last_segment = memorize_last_segment

    def _load_parameters(self) -> None:
        params_path = Path(os.path.dirname(__file__)) / 'params.yaml'
        with open(params_path, 'r') as stream:
            try:
                self.params = yaml.safe_load(stream)
            except yaml.YAMLError as exc:
                print(exc)

    def flush_memory(self):
        self.memory = None

    def process_signal(self, signal: np.ndarray, time: np.ndarray):
        signal = np.concatenate((self.memory[0], signal)) if self.memory is not None else signal
        time = np.concatenate((self.memory[1], time)) if self.memory is not None else time

        if self.estimate_fs:
            fs = 1/(time[1] - time[0])
        else:
            fs = np.mean(np.diff(time))

        segments, times, _ = self.segmenter.split_pulses(signal, time, fs, mean_time=True)
        
        classes = self.classifier.classify_batch(segments)
        
        if self.memorize_last_segment:
            self.memory = (segments[-1], times[-1])
            classes = classes[:-1]
            times = times[:-1]
        
        return classes, times
