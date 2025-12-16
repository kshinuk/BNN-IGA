#!/bin/python3
import subprocess
import os
from datetime import datetime

seed= 42
date_time = datetime.now().strftime("%y%m%d_%H%M%S")
results_dir = f'./results/{date_time}'
os.makedirs(results_dir, exist_ok=True)
epochs = 500

#############################
model = 'resnet18_binary'

subprocess.run(f'python main_binary.py --results_dir {results_dir} --save {model} --model {model} --epochs {epochs} --seed {seed} --ao_bit 1 --w_bit 1 --adc_bit 1', shell=True)

#############################
model = 'resnet_binary'

subprocess.run(f'python main_binary.py --results_dir {results_dir} --save {model} --model {model} --epochs {epochs} --seed {seed} --ao_bit 1 --w_bit 1 --adc_bit 1', shell=True)

