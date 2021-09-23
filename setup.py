# Copyright (c) 2020, NVIDIA CORPORATION. All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions
# are met:
#  * Redistributions of source code must retain the above copyright
#    notice, this list of conditions and the following disclaimer.
#  * Redistributions in binary form must reproduce the above copyright
#    notice, this list of conditions and the following disclaimer in the
#    documentation and/or other materials provided with the distribution.
#  * Neither the name of NVIDIA CORPORATION nor the names of its
#    contributors may be used to endorse or promote products derived
#    from this software without specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS ``AS IS'' AND ANY
# EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED.  IN NO EVENT SHALL THE COPYRIGHT OWNER OR
# CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
# EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO,
# PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR
# PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY
# OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
# (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import os
from setuptools import find_packages
from setuptools import setup


def req_file(filename):
    with open(filename) as f:
        content = f.readlines()
    return [x.strip() for x in content if not x.startswith("#")]


install_requires = req_file("requirements.txt")

data_files = [
    ("", ["LICENSE.txt"]),
]

setup(
    name="pyotritonclient",
    version="0.1.0rc4",
    author="Wei OUYANG",
    author_email="oeway007@gmail.com",
    description="A Pyodide python http client library and utilities for communicating with Triton Inference Server (based on tritonclient from NVIDIA)",
    long_description="""This is a simplified implemetation of the triton client from NVIDIA, it is mainly made for running in the web browser with pyodide."""
    """It only implement the http client, and most of the API remains the same but changed into async."""
    """For example, instead of doing `client.infer(...)`, you need to do `await client.infer(...)`."""
    """See [download-using-python-package-installer-pip](https://github.com/triton-inference-server/client/tree/main#download-using-python-package-installer-pip) """
    """for package details.\n\nThe [client examples](https://github.com/triton-inference-server/client/tree/main/src/python/examples) demonstrate how to use the """
    """package to issue request to [triton inference server](https://github.com/triton-inference-server/server).""",
    long_description_content_type="text/markdown",
    license="BSD",
    url="https://developer.nvidia.com/nvidia-triton-inference-server",
    keywords=[
        "http",
        "triton",
        "tensorrt",
        "inference",
        "server",
        "service",
        "client",
        "nvidia",
    ],
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Information Technology",
        "Topic :: Scientific/Engineering",
        "Topic :: Scientific/Engineering :: Image Recognition",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries",
        "Topic :: Utilities",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Environment :: Console",
        "Natural Language :: English",
        "Operating System :: OS Independent",
    ],
    install_requires=install_requires,
    packages=find_packages(),
    zip_safe=False,
    data_files=data_files,
)
