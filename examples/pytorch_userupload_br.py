""" Test case for Torch """

from __future__ import absolute_import

import torch
import torchvision.models as models
import numpy as np
from perceptron.models.classification.pytorch import PyTorchModel
from perceptron.utils.image import imagenet_example
from perceptron.benchmarks.brightness import BrightnessMetric
from perceptron.utils.criteria.classification import Misclassification
from perceptron.utils.tools import plot_image
from perceptron.utils.tools import bcolors
from perceptron.models.classification.pytorchmodelupload import PyModelUpload


# initialize the PyTorchModel
mean = np.array([0.485, 0.456, 0.406]).reshape((3, 1, 1))
std = np.array([0.229, 0.224, 0.225]).reshape((3, 1, 1))
fmodel = PyModelUpload(
     bounds=(0, 1), num_classes=1000, preprocessing=(mean, std))

# get source image and print the predicted label
image, _ = imagenet_example(data_format='channels_first')
image = image / 255.  # because our model expects values in [0, 1]

# set the type of noise which will used to generate the adversarial examples
metric = BrightnessMetric(fmodel, criterion=Misclassification())

# set the label as the predicted one
label = np.argmax(fmodel.predictions(image))

print(bcolors.BOLD + 'Process start' + bcolors.ENDC)
adversary = metric(image, label, verify=True, unpack=False)  # set 'unpack' as false so we can access the detailed info of adversary
print(bcolors.BOLD + 'Process finished' + bcolors.ENDC)

if adversary.image is None:
    print(bcolors.WARNING + 'Warning: Cannot find an adversary!' + bcolors.ENDC)
    exit(-1)

###################  print summary info  #####################################

keywords = ['PyTorch', 'UserUploadModel', 'Misclassification', 'Brightness']

true_label = np.argmax(fmodel.predictions(image))
fake_label = np.argmax(fmodel.predictions(adversary.image))

# interpret the label as human language
with open('perceptron/utils/labels.txt') as info:
    imagenet_dict = eval(info.read())

print(bcolors.HEADER + bcolors.UNDERLINE + 'Summary:' + bcolors.ENDC)
print('Configuration:'  + bcolors.CYAN + ' --framework %s '
                                         '--model %s --criterion %s '
                                         '--metric %s' % tuple(keywords) + bcolors.ENDC)
print('The predicted label of original image is '
      + bcolors.GREEN + imagenet_dict[true_label] + bcolors.ENDC)
print('The predicted label of adversary image is '
      + bcolors.RED + imagenet_dict[fake_label] + bcolors.ENDC)
print('Minimum perturbation required: %s' % bcolors.BLUE
      + str(adversary.distance) + bcolors.ENDC)
print('Verifiable bound: %s' % bcolors.BLUE
      + str(adversary.verifiable_bounds) + bcolors.ENDC)
print('\n')

plot_image(adversary,
           title=', '.join(keywords),
           figname='examples/images/%s.png' % '_'.join(keywords))

