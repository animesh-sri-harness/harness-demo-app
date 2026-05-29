from setuptools import setup, find_packages

setup(
    name="harness-demo-app",
    version="1.0.0",
    description="Sample Flask app for Harness CI/CD/STO hands-on exercise",
    packages=find_packages(),
    install_requires=["Flask==3.0.0"],
    python_requires=">=3.11",
)
