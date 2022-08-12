# read images from directory and split them into train/test/val folders

import os
import numpy as np
from tqdm import tqdm
from shutil import copyfile
from imutils.paths import list_images
from sklearn.model_selection import train_test_split

# set seed
np.random.seed(42)

db_dir = "/home/choppy/TOC/datasets/openeds"

# make subdirectories for train/test/val
os.makedirs(os.path.join(db_dir, "ttv", "train/images"), exist_ok=True)
os.makedirs(os.path.join(db_dir, "ttv", "train/labels"), exist_ok=True)

os.makedirs(os.path.join(db_dir, "ttv", "test/images"), exist_ok=True)
os.makedirs(os.path.join(db_dir, "ttv", "test/labels"), exist_ok=True)

os.makedirs(os.path.join(db_dir, "ttv", "val/images"), exist_ok=True)
os.makedirs(os.path.join(db_dir, "ttv", "val/labels"), exist_ok=True)

images = sorted([*list_images(os.path.join(db_dir, "images"))])
labels = sorted([*list_images(os.path.join(db_dir, "labels"))])

idx_list = np.arange(len(images))
# randomize index list
np.random.shuffle(idx_list)

X_train_idx, X_test_idx, _, _ = train_test_split(idx_list, idx_list, test_size=0.2)

X_train_idx, X_val_idx, _, _ = train_test_split(
    X_train_idx, X_train_idx, test_size=0.25
)  # 0.25 x 0.8 = 0.2

# train
for idx in tqdm(X_train_idx, desc="train"):
    img_path = images[idx]
    label_path = labels[idx]
    copyfile(
        img_path,
        os.path.join(db_dir, "ttv", "train/images", os.path.basename(img_path)),
    )
    copyfile(
        label_path,
        os.path.join(db_dir, "ttv", "train/labels", os.path.basename(label_path)),
    )

# test
for idx in tqdm(X_test_idx, desc="test"):
    img_path = images[idx]
    label_path = labels[idx]
    copyfile(
        img_path, os.path.join(db_dir, "ttv", "test/images", os.path.basename(img_path))
    )
    copyfile(
        label_path,
        os.path.join(db_dir, "ttv", "test/labels", os.path.basename(label_path)),
    )

# val
for idx in tqdm(X_val_idx, desc="val"):
    img_path = images[idx]
    label_path = labels[idx]
    copyfile(
        img_path, os.path.join(db_dir, "ttv", "val/images", os.path.basename(img_path))
    )
    copyfile(
        label_path,
        os.path.join(db_dir, "ttv", "val/labels", os.path.basename(label_path)),
    )

# copy csv file into ttv folder
copyfile(
    os.path.join(db_dir, "class_dict.csv"),
    os.path.join(db_dir, "ttv", "class_dict.csv"),
)
