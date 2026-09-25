"""
eccentric_wrapper.py
--------------------
PyCBC plugin wrapper for the eccentric IMR waveform model `eccmodel`.

This wrapper translates PyCBC's standard keyword arguments into the
parameter names expected by `eccmodel` in eccentric_waveform.py.

Entry point registered in setup.py:
    pycbc.waveform.plugin =
        eccmodel = eccentric_wrapper:eccmodel_wrapper

Usage via PyCBC:
    from pycbc.waveform import get_td_waveform
    hp, hc = get_td_waveform(
        approximant = "eccmodel",
        mass1       = 30.0,       # solar masses (larger body)
        mass2       = 20.0,       # solar masses (smaller body)
        eccentricity= 0.1,        # initial eccentricity e0
        mean_anomaly= 0.0,        # initial mean anomaly l0 (radians), optional
        distance    = 100.0,      # luminosity distance in Mpc
        inclination = 0.0,        # inclination angle in radians
        delta_t     = 1.0/4096,   # time step in seconds
        f_lower     = 20.0,       # starting frequency in Hz
        mode_array  = [[2, 2]],   # list of (l,m) modes, optional
    )
"""

from EccIMR_22_Model import eccmodel   # your original model file


def eccmodel_wrapper(**kwargs):
    """
    Wrapper called by PyCBC's get_td_waveform() dispatcher.

    PyCBC keyword          ->   eccmodel parameter
    ---------------------------------------------
    mass1, mass2           ->   Mass  (total, solar masses)
                                q0    (mass ratio mass1/mass2, >= 1)
    eccentricity           ->   e0
    mean_anomaly           ->   l0    (optional, default 0.0)
    f_lower                ->   fmin
    inclination            ->   inclination
    distance               ->   d     (Mpc)
    delta_t                ->   delta_t
    mode_array             ->   modes (optional, default [[2,2]])

    Returns
    -------
    hp : pycbc.types.TimeSeries
    hc : pycbc.types.TimeSeries
    """

    # ------------------------------------------------------------------ #
    #  Required parameters — crash loudly if any are missing
    # ------------------------------------------------------------------ #
    required = ["mass1", "mass2", "eccentricity", "f_lower", "delta_t",
                "inclination", "distance"]
    for param in required:
        if param not in kwargs:
            raise ValueError(
                f"eccmodel_wrapper: required parameter '{param}' not provided."
            )

    mass1       = float(kwargs["mass1"])
    mass2       = float(kwargs["mass2"])
    e0          = float(kwargs["eccentricity"])
    fmin        = float(kwargs["f_lower"])
    delta_t     = float(kwargs["delta_t"])
    inclination = float(kwargs["inclination"])
    d           = float(kwargs["distance"])

    # ------------------------------------------------------------------ #
    #  Optional parameters — defaults are physically meaningful
    # ------------------------------------------------------------------ #
    l0    = float(kwargs.get("mean_anomaly", 0.0))  # 0.0 is standard assumption
    modes = kwargs.get("mode_array", None) or [[2, 2]]

    # ------------------------------------------------------------------ #
    #  Derived parameters
    # ------------------------------------------------------------------ #
    # Total mass in solar masses
    Mass = mass1 + mass2

    # Mass ratio q >= 1 (swap if needed so larger mass is in numerator)
    if mass1 >= mass2:
        q0 = mass1 / mass2
    else:
        q0 = mass2 / mass1

    # ------------------------------------------------------------------ #
    #  Sanity checks
    # ------------------------------------------------------------------ #
    if mass1 <= 0 or mass2 <= 0:
        raise ValueError("eccmodel_wrapper: mass1 and mass2 must be positive.")
    if not (0.0 <= e0 < 1.0):
        raise ValueError(
            f"eccmodel_wrapper: eccentricity e0={e0} must be in [0, 1)."
        )
    if fmin <= 0:
        raise ValueError(f"eccmodel_wrapper: f_lower={fmin} must be positive.")
    if delta_t <= 0:
        raise ValueError(f"eccmodel_wrapper: delta_t={delta_t} must be positive.")
    if d <= 0:
        raise ValueError(f"eccmodel_wrapper: distance={d} must be positive.")

    # ------------------------------------------------------------------ #
    #  Call your model
    # ------------------------------------------------------------------ #
    hp, hc = eccmodel(
        Mass        = Mass,
        q0          = q0,
        e0          = e0,
        l0          = l0,
        fmin        = fmin,
        inclination = inclination,
        d           = d,
        delta_t     = delta_t,
        modes       = modes,
    )

    return hp, hc
