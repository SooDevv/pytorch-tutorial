from datetime import datetime
from setuptools import setup, find_packages

setup(
    name='pytorch-tutorial',
    packages=find_packages(),
    version=f'{datetime.now():%Y%m%d}',
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'python-snappy==0.6.0',
        'pyarrow==4.0.1',
        'fastparquet==0.5.0',
        'pandas==1.1.5',
        'transformers==4.30.0',
        'albumentations',
        'faiss',
        'sklearn',
        'opencv-python',
    ],
)
