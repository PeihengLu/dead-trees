"""
Set up the dead-tree package and install the necessary dependencies.
"""

from setuptools import setup

setup(
    name='dead-tree',
    version='0.1.0',
    packages=['dead-tree'],
    install_requires=[
        'numpy',
        'matplotlib',
        'scipy',
        'pandas',
        'seaborn',
        'scikit-learn',
        'joblib',
        'xgboost',
        'catboost',
        'statsmodels',
        'tqdm',
        'torch',
        'torchvision',
        'pandas-profiling',
        'missingno',
        'category_encoders',
        'imbalanced-learn',
        'shap',
        'eli5',
        'pdpbox',
        'pydot',
        'graphviz',
        'dtreeviz',
        'jupyter',
        # transformers
        'transformers',
    ],
)

