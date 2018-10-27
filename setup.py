__author__ = 'Alex Rogozhnikov'

from setuptools import setup

setup(
    name="einops",
    version='0.1.0',
    description="A new flavour of deep learning operations",
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/arogozhnikov/einops',
    author='Alex Rogozhnikov',

    packages=['einops', 'einops.layers'],

    classifiers=[
        'Intended Audience :: Science/Research',
        'Programming Language :: Python :: 3 ',
    ],
    keywords='deep learning, neural networks, tensor manipulation, scientific computations',

    install_requires=[
        # no run-time or installation-time dependencies
    ],
    tests_require=[
        'nose',
        'numpy',
        'mxnet',
        'torch',
        'tensorflow',
        'cupy',  # may fail, requires cuda
        'chainer',
        'keras',
    ],
    test_suite='nose.collector',
)