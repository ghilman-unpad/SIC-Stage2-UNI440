from setuptools import setup, find_packages

def read_requirements():
    with open("requirements.txt") as f:
        return [line.strip() for line in f if line and not line.startswith("#")]
    
setup(
    name="uni440-api",
    version="0.1",
    packages=["api"],
    package_dir={
        "uni440-api": "api"
    },
    requires=read_requirements(),
)
