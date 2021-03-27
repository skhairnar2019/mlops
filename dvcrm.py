import os
from glob import glob


data_dirs = ["Training_Batch_Files","Prediction_Batch_files"]

for data_dir in data_dirs:
    files = glob(data_dir + r"/*.csv")
    for filePath in files:
        # print(f"dvc add {filePath}")
        os.system(f"git rm -r --cached {filePath}")

print("\n #### all files added to dvc ####")