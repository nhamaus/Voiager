.. _checks:

Checks
======

*Voiager* should not be used as a black box! Consistency checks are essential in order to gain confidence in the stability of your results. Below is a non-exhaustive list of possible tests to identify systematic effects. The variables in `params.py <https://github.com/nhamaus/Voiager/blob/main/voiager/params.py>`_ can be used to explore those.

- Variation of void selection cuts, especially minimum size, maximum ellipticity and core density
- Variation of binning schemes in redshift or scale (number of bins, min and max range, etc.)
- Consistency between different data vectors (multipoles vs. 2D correlation via variable ``datavec``)
- Variation of prior ranges for model parameters
- Variation of fiducial parameter values