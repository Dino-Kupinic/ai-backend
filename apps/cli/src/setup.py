from setuptools import setup

setup(
    name='ai-backend',
    py_modules=['main'],
    install_requires=[
        'Click',
    ],
    entry_points={
        'console_scripts': [
            'main = main:cli',
        ],
    },
)
