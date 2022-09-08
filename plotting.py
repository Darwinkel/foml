#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Plotting utilities.
"""

__author__ = "Johannes Bjerva, and Malvina Nissim (modified by Mike Zhang)"
__credits__ = ["Johannes Bjerva", "Malvina Nissim"]
__license__ = "GPL v3"
__version__ = "0.2"
__maintainer__ = "Mike Zhang"
__email__ = "mikz@itu.dk"
__status__ = "early alpha"

from datetime import datetime
from typing import List

import numpy as np

import matplotlib.pyplot as plt


def plot_confusion_matrix(
    cm: np.ndarray, test_y: List[str], title="Confusion matrix", cmap=plt.cm.Blues
):
    plt.figure()
    plt.imshow(
        np.vstack((cm, np.zeros(cm.shape[0]))), interpolation="nearest", cmap=cmap
    )
    plt.title(title)
    plt.colorbar()
    tick_marks = np.arange(cm.shape[0])
    plt.xticks(tick_marks, sorted(list(set(test_y))), rotation=45)
    plt.yticks(tick_marks, sorted(list(set(test_y))))
    plt.tight_layout()
    plt.ylabel("True label")
    plt.xlabel("Predicted label")
    plt.savefig("plot_images/" + datetime.now().isoformat() + "-" + title + "-plot.png")
