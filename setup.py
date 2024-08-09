from setuptools import setup, find_packages

setup(
    name='mcqgenrator',  # Simple, valid package name
    version='0.1.0',     # Correct version format
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

