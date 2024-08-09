from setuptools import setup, find_packages

setup(
    name='mcqgenrator@',  # Remove the '@' symbol as it’s unconventional
    version='0.1.0',
    author='aditya',
    author_email='adityajjagtap.0001@gmail.com',
    install_requires=[
        'openai',
        'langchain',
        'streamlit',
        'python-dotenv',
        'pyPDF2',
    ],
    packages=find_packages(),
)

