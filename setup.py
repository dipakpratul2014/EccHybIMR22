from setuptools import setup, find_packages

setup(
    name="EcchybIMR_22",
    version="1.0.0",
    description="Plugin providing eccentric IMR 22 waveform model",
    author="P. Manna, T. Roychowdhury, C.K. Mishra",
    author_email="mpratul@astrouw.edu.pl",
    license="GPL-3.0",

    py_modules=[
        "EccIMR_22_Model",   # original model file
        "eccentric_wrapper_ecctd",    # PyCBC-facing wrapper
    ],

    python_requires=">=3.8",

    install_requires=[
        "pycbc",
        "numpy",
        "scipy",
        "lalsuite",          # provides MSUN_SI, PC_SI, MTSUN_SI, etc.
        "pyseobnr",
    ],

    entry_points={
        "pycbc.waveform.td": [
            "EcchybIMR_22=eccentric_wrapper_ecctd:eccmodel_wrapper",
        ],
    },

    classifiers=[
        "Programming Language :: Python :: 3",
        "Topic :: Scientific/Engineering :: Physics",
        "Intended Audience :: Science/Research",
    ],
)
