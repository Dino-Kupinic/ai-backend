from setuptools import setup, find_packages

setup(
    name="ai-backend",
    version="0.1.0",
    author="Dino Kupinic",
    py_modules=["main"],
    packages=find_packages(),
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "aibackend=main:cli",
        ],
    },
)
