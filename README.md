# BNN-IGA
ADC-Less Binarized Neural Networks with Impulse Gaussian Approximation.
This neural network algorithm is developed by [HPIC Design Lab](https://hpic-lab.github.io/) at Hanyang University, South Korea.

## Quick Start
You can train/inference Res20 with cmd below.\
### -train
```bash
python main_binary.py --results_dir ./results/resnet20 --save test_model --model resnet_binary
```
### -inference
```bash
python main_binary.py --evaluate ./results/resnet20/test_model/model_best.pth.tar --model resnet_binary
```

More args are defined at main_binary.py\
![image](https://github.com/hpic-lab/BNN_IGA/assets/174296776/45e9c7af-6987-469d-8d12-4d3d9ccae864)\
As you can see above code, actiavtion out, weight, and partial sum quantization bits can be set with arg.
For example, train/inference code with 1-bit actiavtion out, 1-bit weight, and 1-bit partial sum cmd can be defined as:
### -train
```bash
python main_binary.py --results_dir ./results/resnet20 --save test_model --model resnet_binary --ao_bit 1 --w_bit 1 --adc_bit 1
```
### -inference
```bash
python main_binary.py --evaluate ./results/resnet20/test_model/model_best.pth.tar --model resnet_binary  --ao_bit 1 --w_bit 1 --adc_bit 1
