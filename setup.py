from setuptools import setup

setup(name='fets',
      version='0.0.1',
      packages=['fets',
                'fets.models',
                'fets.models.pytorch',
                'fets.models.pytorch.pt_3dresunet',
                'fets.models.pytorch.brainmage',
                'fets.models.pytorch.deepscan', 
                'fets.models.pytorch.nnunet',
                'fets.data',
                'fets.data.pytorch'],
      install_requires=['protobuf', 'grpcio', 'tqdm', 'coloredlogs', 'nibabel', 'scikit-learn', 'nnUNet==1.7.1', 'batchgenerators==0.23', 'opencv-python', 'MedPy==0.4.0']
)
