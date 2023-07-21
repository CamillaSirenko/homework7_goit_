from setuptools import setup, find_namespace_packages

setup (name='clean_folder_sov_hm07',
      version='1.0',
      description='Clean Folder',
      author='Olga Sirenko',
      author_email='olga19022020@gmail.com',
      license="MIT"
      classifiers = [
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"],
      packages=find_namespace_packages(),
      entry_points={'console_scripts': ['clean_folder=clean_folder.clean:run_clean']} 
)