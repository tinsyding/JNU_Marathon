from setuptools import setup, find_packages

setup(
    name='JNU_Marathon',
    version='0.1.0',
    author='tinsyding',
    author_email='tinsyding@gmail.com',
    packages=find_packages(),
    description='A web scraper for Jiangnan University 2023 Marathon event',
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        'selenium',
        'requests'
    ],
    python_requires='>=3.6',
    include_package_data=True,
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Natural Language :: Chinese (Simplified)',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12'
    ],
    keywords='web scraping selenium marathon jiangnan-university',  
)
