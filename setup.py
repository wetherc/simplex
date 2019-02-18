from setuptools import setup, find_packages

setup(
    name='simplex',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    description='Visual ML model debugger',
    author='Christopher Wetherill',
    author_email='simplex@tbmh.org',
    license='MIT',
    install_requires=[
        'flask',
        'pandas',
        'numpy'],
    test_suite='nose.collector',
    tests_require=['nose'],
    zip_safe=False)
