# BNN-IGA
BNN-IGA is an Effective DNN training algorithm for ADC-Less In-Memory Computing Hardware, developed by [HPIC Design Lab.](https://hpic-lab.github.io/) at Hanyang University, South Korea.

## Quick Start
You can train/inference ResNet-18 and ResNet-20 with cmd belo.
### -train
```bash
python auto_train_cifar10.py
```

or

```bash
./auto_train_cifar10.py
```
### -inference
```bash
python auto_test_cifar10.py
```

or

```bash
./auto_test_cifar10.py
```
More args are defined at main_binary.py
For example, train/inference code with 1-bit actiavtion out, 1-bit weight, and 1-bit partial sum cmd can be defined as:
This code only supports quantization up to 4 bits, and if the bit is set to 5 or higher, it operates in full precision. Additionally, if the bit is set to 1.5, it operates in ternary mode
