import os
import shutil
import random
from math import floor

# Paths
original_dataset = 'train'         # Folder with 7 class subfolders
target_root = 'balanced_split_data'        # New root folder to save the result
samples_per_class = 436                    # Max per class (based on smallest class)

# Split ratios
splits = ['train', 'val', 'test']
split_ratio = [0.6, 0.2, 0.2]

# Class folders
classes = os.listdir(original_dataset)
print("Found classes:", classes)

for class_name in classes:
    class_path = os.path.join(original_dataset, class_name)
    images = os.listdir(class_path)

    # Ensure enough images
    if len(images) < samples_per_class:
        print(f" Not enough images in class {class_name}. Skipping.")
        continue

    # Sample and shuffle
    sampled_images = random.sample(images, samples_per_class)
    random.shuffle(sampled_images)

    # Calculate how many to put in each split
    train_count = floor(samples_per_class * split_ratio[0])
    val_count = floor(samples_per_class * split_ratio[1])
    test_count = samples_per_class - train_count - val_count
    split_counts = [train_count, val_count, test_count]

    print(f"{class_name}: train={train_count}, val={val_count}, test={test_count}")

    start = 0
    for split, count in zip(splits, split_counts):
        split_dir = os.path.join(target_root, split, class_name)
        os.makedirs(split_dir, exist_ok=True)

        for img_name in sampled_images[start:start+count]:
            src = os.path.join(class_path, img_name)
            dst = os.path.join(split_dir, img_name)
            shutil.copyfile(src, dst)

        start += count

print(" Sampling and splitting complete.")
