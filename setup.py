import codecs
import re
import os
from setuptools import setup


def find_version(*file_paths):
    with codecs.open(
        os.path.join(os.path.abspath(os.path.dirname(__file__)), *file_paths), "r"
    ) as fp:
        version_file = fp.read()
    m = re.search(r"^__version__ = \((\d+), ?(\d+), ?(\d+)\)", version_file, re.M)
    if m:
        return "{}.{}.{}".format(*m.groups())
    raise RuntimeError("Unable to find a valid version")


VERSION = find_version("deepmoji", "__init__.py")


setup(
    name="deepmoji",
    version=VERSION,
    packages=["deepmoji"],
    description="DeepMoji library",
    long_description=open("README.md", encoding="UTF-8").read(),
    long_description_content_type="text/markdown",
    license="MIT",
    include_package_data=True,
    install_requires=[
        "emoji>=0.4.5,<1.0.0",
        "h5py>=2.7.0,<3.0.0",
        "Keras>=2.3.1,<3.0.0",
        "numpy>=1.18.1,<2.0.0",
        "scikit-learn>=0.19.0,<1.0.0",
        "text-unidecode>=1.0,<2.0",
    ],
    tests_require=["nose>=1.3.7,<2.0.0",],
    extras_require={
        "tensorflow_backend": [
            "tensorflow>=2.0.0,!=2.1.0,<3.0.0",  # tensorflow==2.1.0 has import issues on windows
        ],
    },
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
)
