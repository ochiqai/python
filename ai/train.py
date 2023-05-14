import torch
from torch import nn, optim
from torchvision.models import ResNet18_Weights
from torchvision import datasets, transforms, models

import matplotlib.pyplot as plt

from ai.utils import imshow


def train():
    # Define transformations for the training data and testing data
    # transform funksiyasini qilib olayapmiz. Bu train va test uchun ishlatiladi.
    # Maqsadi: berilga rasmni standard ko'rinishga keltiradi.
    # Masalan, 1290c1300 rasmi, 224x224 ulchamga o'tkazadi.
    transform = transforms.Compose([transforms.Resize(255),
                                    transforms.CenterCrop(224),
                                    transforms.ToTensor(),
                                    transforms.Normalize([0.485, 0.456, 0.406],
                                                         [0.229, 0.224, 0.225])])

    ## data
    ## data folderi traffic_images deb ataladi: va unda good va problem folderlari bor.
    # Har bir folder nomi klass nomini bildiradi. Folderlar ichida tegishli rasmlar bo'ladi.
    # """
    # traffic_images
    # │
    # ├── good
    # │   ├── img1.jpg
    # │   ├── img2.jpg
    # │   └── ...
    # │
    # └── problem
    #     ├── img1.jpg
    #     ├── img2.jpg
    #     └── ...
    # """

    # Pass transformations in here, then run the next cell to see how the transforms look
    train_data = datasets.ImageFolder('train/', transform=transform)
    test_data = datasets.ImageFolder('test/', transform=transform)
    num_classes = len(train_data.classes)
    print('Number of classes:', num_classes)
    print('Classes:', train_data.classes)

    trainloader = torch.utils.data.DataLoader(train_data, batch_size=1, shuffle=True)
    testloader = torch.utils.data.DataLoader(test_data, batch_size=1)

    # Use a smaller pre-trained network
    model = models.resnet18(weights=ResNet18_Weights.IMAGENET1K_V1)

    # Freeze parameters so we don't backprop through them
    for param in model.parameters():
        param.requires_grad = False

    # Replace the classifier
    model.fc = nn.Sequential(nn.Linear(512, 256),
                             nn.ReLU(),
                             nn.Dropout(0.2),
                             nn.Linear(256, num_classes),
                             nn.LogSoftmax(dim=1))

    # modelni o'rgatishga yordam beradi, qayerda xato qilayotganligini ko'rsatadi.
    criterion = nn.NLLLoss()

    optimizer = optim.Adam(model.fc.parameters(), lr=0.003)

    # Move model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)

    # Train the network
    epochs = 1  # 1 ta epoch degani datani to'liq ko'rib chiqish degani
    steps = 0

    for epoch in range(epochs):
        running_loss = 0
        for inputs, labels in trainloader:
            steps += 1
            # Move input and label tensors to the default device
            inputs, labels = inputs.to(device), labels.to(device)

            optimizer.zero_grad()

            logps = model.forward(inputs)
            loss = criterion(logps, labels)
            loss.backward()
            optimizer.step()

            running_loss += loss.item()

        print(f"Epoch {epoch + 1}/{epochs}.. "
              f"Train loss: {running_loss / len(trainloader):.3f}")

    return model, testloader


def eval(model, testloader, device, vis=False):
    """
    Once you've trained your model, you can evaluate its performance on your test
    set. This function calculates the accuracy of the model on the test set by
    comparing the model's predictions to the true labels. The model.eval() call sets the model
    to evaluation mode, which is important if your model uses layers such as dropout or
    batch normalization which behave differently during training and evaluation.
    The with torch.no_grad(): block prevents PyTorch from calculating gradients during
    the testing process, which can save memory.

    Please remember to replace testloader with your actual test data loader,
    and device with the actual device you're using (CPU or CUDA).

    Example,
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    eval_model(model, testloader, device)
    """
    correct = 0
    total = 0
    model.eval()  # Set model to evaluation mode
    with torch.no_grad():
        for images, labels in testloader:
            images, labels = images.to(device), labels.to(device)

            if vis == True:
                # Assuming 'images' is your 1x3x244x244 tensor
                vis_img = imshow(images)
                plt.imshow(vis_img)
                plt.title(str(labels))
                plt.show()


            outputs = model(images)
            _, predicted = torch.max(outputs.data, 1)
            total += labels.size(0)
            correct += (predicted == labels).sum().item()
    print(f"Accuracy on test set: {100 * correct / total}%")


# train
model, testloader = train()

# eval
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
eval(model, testloader, device)