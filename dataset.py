from torch.utils.data import Dataset
import medmnist
from medmnist import INFO
import textwrap
import torchvision.transforms as transforms
import torch
from PIL import Image
import numpy as np

class GetMedMNIST(Dataset):
    def __init__(self, name='BloodMNIST', split='train', transform=transforms.ToTensor(),
                 download=True, size=224, hf=True):
        """
        PathMNIST, ChestMNIST, DermaMNIST, OCTMNIST, PneumoniaMNIST, RetinaMNIST,
        BreastMNIST, BloodMNIST, TissueMNIST, OrganAMNIST, OrganCMNIST, OrganSMNIST,
        OrganMNIST3D, NoduleMNIST3D, AdrenalMNIST3D, FractureMNIST3D, VesselMNIST3D, SynapseMNIST3D
        """
        assert size in [28, 64, 128, 224], 'size should be: 28 | 64 | 128 | 224'
        assert split in ['train', 'val','test'], 'split should be: train | val | test'

        self.name = name
        self.split = split
        self.transform = transform
        self.size = size
        self.info = INFO[name.lower()]
        self.label_str = self.info['label']
        self.n_classes = len(self.label_str)
        self.hf = hf
        
        self.dataset = getattr(medmnist, self.name)\
            (split=self.split, transform=self.transform, download=download, size=self.size)
        
    def __len__(self):
            return len(self.dataset)
    
    def __getitem__(self, index):
            img = self.dataset.imgs[index]
            img = Image.fromarray(img, mode='RGB')
            img = self.transform(img)
            label = torch.tensor(self.dataset.labels[index], dtype=torch.int64, device=img.device)
            if self.hf:
                return {"pixel_values": img, "labels": label}
            return img, label