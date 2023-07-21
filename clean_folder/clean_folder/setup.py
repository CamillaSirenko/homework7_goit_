from setuptools import setup, find_namespace_packages

setup(name='clean_folder_sov',
      version='1.0',
      description='Clean Folder',
      author='Olga Sirenko',
      author_email='olga19022020@gmail.com',
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:run_clean']}
)