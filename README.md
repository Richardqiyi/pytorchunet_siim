# pytorchunet_siim
unet for SIIM dataset
#### Docker
```
docker pull stevezeyuzhang/colab:2.0
```
#### Installation
```
pip install -r requirements.txt
```
#### Training
```
nohup python train.py -b 8 -e 20 -l 1e-4 -c 2 > train.log 2>&1 &
```
