import os
import setuptools


long_description = '''
[**BigDL**](https://github.com/intel-analytics/BigDL/)
makes it easy for data scientists and data engineers to build end-to-end, 
distributed AI applications.

For more information, you may [read the docs](https://bigdl.readthedocs.io/).
'''

bigdl_home = os.path.abspath(__file__ + "/../../")

exclude_patterns = ["*__pycache__*", "*ipynb_checkpoints*"]

VERSION = open(os.path.join(bigdl_home, 'python/version.txt'), 'r').read().strip()

def setup_package():
    metadata = dict(
        name='bigdl'
    )

    setuptools.setup(**metadata)

if __name__ == '__main__':
    setup_package()