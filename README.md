<center>
<img src="docs/voiager.png" alt="Voiager" width="200"/>
</center>

# *Voiager*

**Voi**d dyn**a**mics and **g**eometry **e**xplore**r** (*Voiager*, or short [*V'Ger*](https://intl.startrek.com/database_article/vger)) provides a framework to perform cosmological analyses using voids identified in large-scale structure survey data. The code measures dynamic and geometric shape distortions in void stacks and propagates them to constraints on cosmological parameters using Bayesian inference. More detailed information on this method can be found in the publications listed below. The documentation of the code can be found on [Read*the*Docs](https://docs.readthedocs.io).

*Voiager* is an homage to [NASA's](https://voyager.jpl.nasa.gov/) [Voyager program](https://en.wikipedia.org/wiki/Voyager_program). The twin Voyager 1 and 2 spacecrafts are exploring where nothing from Earth has flown before. Continuing on their nearly 50-year journey since their 1977 launches, they each are much farther away from Earth and the sun than Pluto.

> *"Voyager did things no one predicted, found scenes no one expected, and promises to outlive its inventors. Like a great painting or an abiding institution, it has acquired an existence of its own, a destiny beyond the grasp of its handlers."* 
— Stephen J. Pyne


## Features

The main functionality of *Voiager* includes the following steps:

- Reading of tracer and void catalogs (based on [VIDE](https://bitbucket.org/cosmicvoids/vide_public/wiki/Home/))
- Generation of random catalogs (based on [healpy](https://healpy.readthedocs.io/))
- Estimation of void-galaxy cross-correlation functions (based on [scipy k-d trees](https://docs.scipy.org/doc/scipy/reference/generated/scipy.spatial.KDTree.html#scipy.spatial.KDTree))
- Projection and deprojection along the line of sight (based on [PyAbel](https://pyabel.readthedocs.io))
- Estimation of covariances (based on jackknife resampling)
- Models and likelihood functions (based on linear theory and Gaussian statistics)
- Maximization of likelihoods (based on [scipy.optimize](https://docs.scipy.org/doc/scipy/tutorial/optimize.html))
- Sampling of likelihoods (based on [emcee](https://emcee.readthedocs.io/))
- Plotting of summary statistics and results (based on [matplotlib](https://matplotlib.org/) and [GetDist](https://getdist.readthedocs.io/))


## Installation
The latest stable version on https://pypi.org is obtained via:
```sh
pip install Voiager
```
You may want to append the `--user` flag, or use a virtual environment, in case you are working on a machine without admin rights. The latest development version on github is obtained via:
```sh
git clone https://github.com/nhamaus/Voiager.git
cd Voiager
pip install .
```
External package requirements are provided in the file [requirements.txt](requirements.txt). Follow the instructions provided on the [VIDE wiki](https://bitbucket.org/cosmicvoids/vide_public/wiki/Home/) to install VIDE. For correctly rendering the plots you additionally need [LaTeX](https://texblog.org/installing-latex/).

## Usage

The simplest way to get started is to execute the script [launch.py](voiager/launch.py) from within the [Voiager/](./) package directory with python (version 3) in interactive mode:
```sh
python -i voiager/launch.py
```
It is set up to perform an example run from the [Beyond-2pt](https://github.com/ANSalcedo/Beyond2ptMock) blind data challenge, based on a simulated light-cone in a *w*CDM cosmology ([C_mock_lightcone.h5](https://github.com/ANSalcedo/Beyond2ptMock/blob/main/C_mock_lightcone.h5)). The input data is retrieved from the [catalogs/](catalogs/) folder including void catalogs produced with [VIDE](https://bitbucket.org/cosmicvoids/vide_public/wiki/Home/), while the output of the code is stored in the [results/](results/) directory.


*Note*: The example data in [catalogs/](catalogs/) and the example results in [results/](results/) are not automatically downloaded upon installation, but they can be accessed via the repository. The [catalogs/](catalogs/) folder can be downloaded as a compressed archive [catalogs.tar.gz](https://github.com/nhamaus/Voiager/releases/download/v0.1.0/catalogs.tar.gz) and unpacked via
```sh
tar -xvzf catalogs.tar.gz
```

You can also execute the code via the installed package from the [Voiager/](./) directory, either via
```sh
python -m voiager
```
or by calling the executable `voiager` from the terminal.

*Note*: All the parameters of *Voiager* are configured in the file [params.yaml](voiager/params.yaml), which is used as default configuration. You can also point to your customized parameter file in [yaml](https://pyyaml.org/) format like this:
```sh
voiager 'path/to/parameter_file.yaml'
```
Previously calculated data vectors are saved in the file [stacks.dat](/results/Beyond2pt/C_mock_lightcone_0240/stacks.dat), this step in the pipeline will be skipped in case the file already exists (i.e., it needs to be removed to start a new calculation). Similarly, the files named [chains.dat](/results/Beyond2pt/C_mock_lightcone_0240/chains.dat) contain previously run MCMCs, which the code will continue sampling when found. Human readable ASCII versions of the chains are also produced.

The file [params.yaml](voiager/params.yaml) contains the main adjustable parameters of the code, each of which appears with a brief comment about its meaning.


## Publications
The development of *Voiager* is based on a consecutive series of papers: [Hamaus et al. 2015](https://arxiv.org/abs/1507.04363), [2016](https://arxiv.org/abs/1602.01784), [2017](https://arxiv.org/abs/1705.05328), [2020](https://arxiv.org/abs/2007.07895), [2022](https://arxiv.org/abs/2108.10347). Please consider citing those that are relevant for your particular application of *Voiager*. Citation records can be retrieved via the [NASA ADS](https://ui.adsabs.harvard.edu/) server:

- *Probing cosmology and gravity with redshift-space distortions around voids*\
([Hamaus, Sutter, Lavaux, Wandelt, JCAP 2015](https://ui.adsabs.harvard.edu/abs/2015JCAP...11..036H/exportcitation))
- *Constraints on Cosmology and Gravity from the Dynamics of Voids*\
([Hamaus, Pisani, Sutter, Lavaux, Escoffier, Wandelt, Weller, PRL 2016](https://ui.adsabs.harvard.edu/abs/2016PhRvL.117i1302H/exportcitation))
- *Multipole analysis of redshift-space distortions around cosmic voids*\
([Hamaus, Cousinou, Pisani, Aubert, Escoffier, Weller, JCAP 2017](https://ui.adsabs.harvard.edu/abs/2017JCAP...07..014H/exportcitation))
- *Precision cosmology with voids in the final BOSS data*\
([Hamaus, Pisani, Choi, Lavaux, Wandelt, Weller, JCAP 2020](https://ui.adsabs.harvard.edu/abs/2020JCAP...12..023H/exportcitation))
- *Euclid: Forecasts from redshift-space distortions and the Alcock-Paczynski test with cosmic voids*\
([Hamaus, Aubert, Pisani, Contarini, Verza, et al., A&A 2022](https://ui.adsabs.harvard.edu/abs/2022A%26A...658A..20H/exportcitation))


## License
This code is copyrighted under the MIT licence, see [LICENSE](LICENSE).

## Contact
You can reach me via the information provided on my personal [homepage](https://www.usm.uni-muenchen.de/people/hamaus/).