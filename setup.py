from setuptools import setup

setup(name='deepexplain',
      version='0.2',
      description='Perturbation and gradient-based methods for Deep Network interpretability',
      url='https://github.com/marcoancona/DeepExplain',
      author='Marco Ancona (ETH Zurich)',
      author_email='marco.ancona@inf.ethz.ch',
      license='MIT',
      packages=['deepexplain', 'deepexplain.implementation', 'deepexplain.tests'],
      install_requires=[
            'scipy',
            'matplotlib',
            'scikit-image',
            'tensorflow==1.4.0'
      ],
      zip_safe=False,
      test_suite='nose.collector',
      tests_require=['nose'],
      )
