from setuptools import setup, find_packages

setup(name='ozon_sdk_python',
      version='0.0.1',
      description='Ozon API to pydantic class',
      long_description='Ozon API to pydantic class',
      classifiers=[
          'Programming Language :: Python :: 3.10',
      ],
      url='https://gitlab.com/ajvarnabiullin/ozon-sdk-python',
      author='Aivar Nabiullin',
      author_email='ajvarnabiullin0@gmail.com',
      packages=find_packages(),
      # include_package_data=False,
      zip_safe=False)
