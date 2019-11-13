from setuptools import setup, find_packages
from os import path
from io import open

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()


setup(
    name='mc-sim-fin',
    version='0.1.1b3',
    description='montecarlo simulations/analysis library for finance',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/gaugau3000/montecarlo_simulation_finance',
    author='Gautier Pialat',
    author_email='g.pialat@gmail.com',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Financial and Insurance Industry',
        'Topic :: Office/Business :: Financial',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],
    keywords='finance montecarlo simulations backtest risk management',
    packages=find_packages(),
    python_requires='>=3.7, <4',
    install_requires=['numpy', 'pandas'],
)
