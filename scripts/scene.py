# Import libraries
import csv
from dataclasses import dataclass, field

import numpy as np
from scipy.io import loadmat


# Data class for a hyperspectral scene
@dataclass
class HyperspectralScene:
    name: str
    image_path: str
    gt_path: str
    labels_path: str
    palette_path: str
    image: np.ndarray = field(init=False)
    gt: np.ndarray = field(init=False)
    labels: list = field(init=False)
    palette: list = field(init=False)
    X: np.ndarray = field(init=False)
    y: np.ndarray = field(init=False)

    # Loads a hyperspectral image from a *.mat file
    def load_image(self):
        self.image = list(loadmat(file_name=self.image_path).values())[-1]
        self.X = np.reshape(a=self.image, newshape=(-1, self.image.shape[2]))

    # Loads the ground truth from a *.mat file
    def load_gt(self):
        self.gt = list(loadmat(file_name=self.gt_path).values())[-1]
        self.y = np.reshape(a=self.gt, newshape=-1)

    # Loads class labels from a *.csv file
    def load_labels(self):
        with open(self.labels_path) as file:
            self.labels = list(csv.reader(file, delimiter=','))[0]

    # Loads a custom seaborn color palette from a *.csv file
    def load_palette(self):
        with open(self.palette_path) as file:
            self.palette = list(csv.reader(file, delimiter=','))[0]

    # Initializes other class attributes
    def __post_init__(self):
        self.load_image()
        self.load_gt()
        self.load_labels()
        self.load_palette()
