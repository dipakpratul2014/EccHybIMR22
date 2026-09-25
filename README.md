# EccHybIMR22 
Eccentric Hybrid Inspiral–Merger–Ringdown model for dominant $(\ell=2,|m|=2)$ mode.

This model uses a PN model for the inspiral part and a quasicircular template for the merger-ringdown stage. It is calibrated against hybrid simulations upto mass ratio ($q$) = 10. See arxiv:id for details.

## Installation 
```
git clone https://github.com/dipakpratul2014/EccHybIMR22.git
cd EccHybIMR22
pip install .
```

## Source code
To obtain the `LALSuite` fork containing the implementation of `EccHybIMR22`, follow these steps:
```
git clone https://git.ligo.org/pratul.manna/lalsuite-EccIMR_22.git
cd lalsuite-EccIMR_22
git checkout EccIMR-dev
```

- Now `EccHybIMR22` can be called through `PyCBC` package. See [tutorial model pycbc](https://github.com/dipakpratul2014/EccIMR_22_model/blob/main/tutorial%20notebooks/tutorial_model_pycbc.ipynb).
- `EccHybIMR22` can also be used via `GWSignal`. See [tutorial model GWSignal](https://github.com/dipakpratul2014/EccIMR_22_model/blob/main/tutorial%20notebooks/tutorial_model_GWSignal.ipynb).

--------------------------------------------------------------------------------------------------------
### Required packages 
`PyCBC, LALSimulation, pyseobnr`

### Contact information
For questions, issues and suggestions, feel free to contact us at:
`mpratul@astrouw.edu.pl`
