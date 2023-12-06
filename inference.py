import os
import subprocess

input_folder = '/code/SIIM-ACR-Pneumothorax-Seg-XR/imagesTs'
output_folder = '/code/Pytorch-UNet/UNet_infer_new'

for filename in os.listdir(input_folder):
    file_path = os.path.join(input_folder, filename)
    
    if os.path.isfile(file_path):
        command = f"python predict.py -i {file_path} -o {os.path.join(output_folder, filename)}"
        
        subprocess.run(command, shell=True)
