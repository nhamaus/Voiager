.. _features:

Features
========

The main functionality of *Voiager* includes the following steps (external package requirements are provided as links in parentheses, all of them can be found in the file `requirements.txt <requirements.txt>`_):

- Reading of tracer and void catalogs (based on `VIDE <https://bitbucket.org/cosmicvoids/vide_public/wiki/Home/>`_)
- Generation of random catalogs (based on `healpy <https://healpy.readthedocs.io/>`_)
- Estimation of void-galaxy cross-correlation functions (based on `scipy k-d trees <https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree>`_)
- Projection and deprojection along the line of sight (based on `PyAbel <https://pyabel.readthedocs.io>`_)
- Estimation of covariances (based on jackknife resampling)
- Models and likelihood functions (based on linear theory and Gaussian statistics)
- Maximization of likelihoods (based on `scipy.optimize <https://docs.scipy.org/doc/scipy/tutorial/optimize.html>`_)
- Sampling of likelihoods (based on `emcee <https://emcee.readthedocs.io/>`_)
- Plotting of summary statistics and results (based on `matplotlib <https://matplotlib.org/>`_ and `GetDist <https://getdist.readthedocs.io/>`_)

