from os import path
from setuptools import setup,find_packages

exec(compile(open('s3n2bin/s3n2bin_version.py').read(),
             's3n2bin/s3n2bin_version.py', 'exec'))

try:
    long_description = open('README.md', encoding='utf-8').read()
except:
    long_description = open('README.md').read()


setup(name='semi_metabin',
      version=__version__,
      description='Metagenomic binning with semi-supervised siamese neural network',
      long_description = long_description,
      long_description_content_type = 'text/markdown',
      classifiers=[
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
      ],
      url='https://github.com/psj1997/Semi-supervised-siamese-neural-network-for-metagenomic-binning',
      author='Shaojun Pan',
      author_email='shaojun1997777@gmail.com',
      license='MIT',
      packages = ['s3n2bin'],
      install_requires=[
          'numpy',
          'Biopython',
          'tqdm',
          'pyyaml',
          'atomicwrites',
          'torch'
      ],
      package_data={
          's3n2bin': ['*.hmm','*.pl']},
      zip_safe=False,
      entry_points={
            'console_scripts': ['S3N2Bin=s3n2bin.main:main'],
      }
)