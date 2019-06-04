.. Perceptron documentation master file, created by
   sphinx-quickstart on Sat Feb  2 22:09:27 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Perceptron Robustness Benchmark's page!
==================================================

Perceptron is a benchmark to test safety and security properties of neural
networks for perceptual tasks.

It comes with support for many frameworks to build models including

* TensorFlow
* PyTorch
* Keras
* Cloud API
* PaddlePaddle

See currently supported evaluation metrics, models, adversarial criteria,
and verification methods in :doc:`user/summary`.

See current :doc:`user/leaderboard`.

.. raw:: html

    <style> .red {color:#aa0060; font-weight:bold; font-size:16px} </style>
    <style> .blue {color:#2D8ED3; font-weight:bold; font-size:16px} </style>
    <style> .shade {color:#0e2f44; font-weight:bold; font-size:16px} </style>

.. role:: red

.. role:: blue

.. role:: shade

Overview
========
:code:`perceptron` benchmark improves upon the existing adversarial
toolbox such as :code:`cleverhans`, :code:`foolbox`, :code:`IBM ART`,
:code:`advbox` in three important aspects:

    - Consistent API design that enables easy evaluation of models across
      different deep learning **frameworks**, computer vision **tasks**,
      and adversarial **criterions**.
    - Standardized metric design that enables DNN models' robustness to
      be compared on a large collection of **security** and :red:`safety`
      properties.
    - Gives :red:`verifiable` robustness bounds for security and safety
      properties.

Running benchmarks
==================

You can run evaluation against DNN models with chosen parameters using :code:`launcher`.
For example:

.. code-block:: bash

    python perceptron/launcher.py \
        --framework keras \
        --model resnet50 \
        --criteria misclassification\
        --metric carlini_wagner_l2 \
        --image example.png

In above command line, the user lets the framework as ``keras``, the model as ``resnet50``, 
the criterion as ``misclassification`` (i.e., we want to generate an adversary which is
similar to the original image but has different predicted label), the metric as 
``carlini_wagner_l2``, the input image as ``example.png``.  

You can try different combinations of frameworks, models, criteria, and metrics. 
To see more options using `-h` for help message.

.. code-block:: bash

    python perceptron/launcher.py -h

We also provide a coding example which serves the same purpose as above command line. Please refer
to :doc:`user/examples` for more details.

.. toctree::
   :maxdepth: 2
   :caption: User Guide

   user/examples
   user/leaderboard
   user/summary

.. toctree::
   :maxdepth: 2
   :caption: API Reference

   modules/metrics
   modules/models
   modules/adversarial
   modules/criteria
   modules/distances

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
