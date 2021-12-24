import subprocess

subprocess.run(["python", "-m", "pip", "install", "-U", "pip", "setuptools"])
subprocess.run(["python", "-m", "pip", "install", "-r", "requirements.txt"])
subprocess.run(["python", "-m", "pip", "install", "torch==1.10.1+cu113", "torchvision==0.11.2+cu113", "-f", "https://download.pytorch.org/whl/cu113/torch_stable.html"])


import torch
model = torch.hub.load("PeterL1n/RobustVideoMatting",
                       "mobilenetv3").cuda()  # or "resnet50"
convert_video = torch.hub.load("PeterL1n/RobustVideoMatting", "converter")