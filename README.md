# Usage
```
git clone https://github.com/supplepentan/penta-robustvideomatting
cd penta-robustvideomatting
pyenv local 3.8.6
python -m venv venv
venv/scripts/activate
python -m pip install -r requirements.txt
python -m pip install torch==1.10.1+cu113 torchvision==0.11.2+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html
python setup.py
python run.py
```

# Original
 [Robust High-Resolution Video Matting with Temporal Guidance](https://peterl1n.github.io/RobustVideoMatting/)