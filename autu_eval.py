#!/bin/python3
import subprocess

seed= 42
date_time = 'pretrained'
results_dir = f'./results/{date_time}'

#############################
model = 'resnet18_binary'
model_path = f'{results_dir}/{model}/model_best.pth.tar'

subprocess.run(f'python main_binary.py --evaluate {model_path} --results_dir {results_dir} --save {model} --model {model} --seed {seed} --ao_bit 1 --w_bit 1 --adc_bit 1', shell=True)

#############################
model = 'resnet_binary'
model_path = f'{results_dir}/{model}/model_best.pth.tar'

subprocess.run(f'python main_binary.py --evaluate {model_path} --results_dir {results_dir} --save {model} --model {model} --seed {seed} --ao_bit 1 --w_bit 1 --adc_bit 1', shell=True)


