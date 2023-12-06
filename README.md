# pytorchunet_siim
unet for SIIM dataset
#### Docker
```
docker pull stevezeyuzhang/colab:2.0
```
#### Environment
Python 3.9.13 cuda=11.7 pytorch=2.0.0 
```
conda create -n myenv python=3.9.13

conda activate myenv

conda install pytorch=2.0.0 cudatoolkit=11.7 -c pytorch
```

#### Dataset
```
|-- pytorchunet_siim
    |-- data
        |-- imgs
            |-- <your image>
        |-- masks
            |-- <your label>
```
#### Installation
```
pip install -r requirements.txt
```
#### Training
```
nohup python train.py -b 8 -e 20 -l 1e-4 -c 2 > train.log 2>&1 &
```
