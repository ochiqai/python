import os
import shutil
import numpy as np
import cv2
import matplotlib.pyplot as plt

def imshow(tensor):
    # Remove the batch dimension
    img = tensor.squeeze(0) # 1x3x244x244 -> 3x244x244

    # Convert to numpy array and transpose dimensions to (H, W, C)
    img = img.cpu().numpy().transpose((1, 2, 0)) # 3x244x244 -> 244x244x3

    # Unnormalize the image
    img = img * np.array([0.229, 0.224, 0.225]) + np.array([0.485, 0.456, 0.406])
    img = img.clip(0, 1)

    return img

    # Convert the image from RGB to BGR
    # img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    #
    # # Display the image
    # cv2.imshow('image', img)
    # cv2.waitKey(0)  # waits until a key is pressed
    # cv2.destroyAllWindows()  # destroys the window showing image




def train_test_split(source_directory, training_directory, testing_directory, split_size):
    """
    Assuming your source directory is 'my_images', and you want to split 80% for training and 20% for testing
    traffic_images
    │
    ├── good
    │   ├── img1.jpg
    │   ├── img2.jpg
    │   └── ...
    │
    └── problem
        ├── img1.jpg
        ├── img2.jpg
        └── ...
    Misol,
    source_directory = './traffic_images/'
    training_directory = './train/'
    testing_directory = './test/'
    train_test_split(source_directory, training_directory, testing_directory, split_size=0.8)
    """
    classes = ['good', 'problem']

    for cls in classes:
        os.makedirs(training_directory + cls, exist_ok=True)
        os.makedirs(testing_directory + cls, exist_ok=True)

        src_dir = os.path.join(source_directory, cls)
        files = os.listdir(src_dir)

        # randomize the files
        np.random.shuffle(files)

        # calculate the split index
        split_index = int(len(files) * split_size)

        # split the files
        train_files = files[:split_index]
        test_files = files[split_index:]

        # copy the split files into their respective directories
        for file in train_files:
            shutil.copy(os.path.join(src_dir, file), os.path.join(training_directory, cls, file))

        for file in test_files:
            shutil.copy(os.path.join(src_dir, file), os.path.join(testing_directory, cls, file))


