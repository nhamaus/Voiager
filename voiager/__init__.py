"""
VOId dynAmics and Geometry ExploreR provides a framework to perform cosmological analyses using voids identified in large-scale structure survey data. The code measures dynamic and geometric shape distortions in void stacks and propagates those to constraints on cosmological parameters using Bayesian inference.
"""
__version__ = "0.2.0"
__author__ = 'Nico Hamaus'


import os
import argparse
import yaml
from collections import OrderedDict


# Find and read parameter file from default or specified location
defaultFile = os.getcwd()+'/voiager/params.yaml'

def parseParamsFile():
    parser = argparse.ArgumentParser(prog='voiager', description='VOId dynAmics and Geometry ExploreR provides a framework to perform cosmological analyses using voids identified in large-scale structure survey data.')
    parser.add_argument('parameters',
                    nargs='?',
                    type=argparse.FileType('r'),
                    default=defaultFile,
                    help='Path to location of parameter yaml file')
    parser.add_argument('--version', action='version', version=__version__)
    return parser

#file = open(defaultFile, 'r')
#if __name__ == '__main__':
#    parser = parseParamsFile()
#    args = parser.parse_args()
#    file = args.parameters

parser = parseParamsFile()
args = parser.parse_args()
file = args.parameters

#global params
params = yaml.safe_load(file)


# Survey information
survey = params['Info']['survey'] # Name of survey
sample = params['Info']['sample'] # Name of tracer sample
random = params['Info']['random'] # Name of random sample
version = params['Info']['version'] # Version (suffix) of void catalog
zmin,zmax = params['Info']['redshift'] # Redshift range
sky = params['Info']['sky'] # Sky area in square degrees (full sky ~ 41253)
cosmology = params['Info']['cosmology'] # Cosmological model to constrain (current options: "LCDM", "wCDM", "w0waCDM")


# Input / output
runExec = params['IO']['runExec'] # If True, run executable when called
basePath = os.getcwd()+params['IO']['basePath'] # Location of the top level code directory
tracerPath = basePath+params['IO']['tracerPath'] # Location of tracer catalogs
voidPath = basePath+params['IO']['voidPath'] # Location of void catalogs
outPath = basePath+params['IO']['outPath']+survey+'/'+sample+version+'/' # Location to store output files
plotPath = outPath+params['IO']['plotPath'] # Location to store plots
inputFormat = params['IO']['inputFormat'] # Filetype for input tracer and random catalogs (supported types: https://docs.astropy.org/en/stable/io/unified.html)
inputExtension = params['IO']['inputExtension'] # Filename extension for input tracer and random catalogs
figFormat = params['IO']['figFormat'] # Format to save figures (e.g., pdf, png, jpg)
columnNames = params['IO']['columnNames'] # Tracer and random catalog column headers for right ascension, declination, redshift (angles in degrees)
stackFile = params['IO']['stackFile']+'.dat' # Filename for data of stacks
chainFile = params['IO']['chainFile']+'.dat' # Filename for data of chains
cosmoFile = params['IO']['chainFile']+'_'+cosmology+'.dat' # Filename for data of cosmology chains
continueChain = params['IO']['continueChain'] # If True, continue sampling of previous chains. If False, delete old chains.


# Void selection
zvmin,zvmax = params['Selection']['zv'] # Void redshift range
rvmin,rvmax = params['Selection']['rv'] # Void radius range
mvmin,mvmax = params['Selection']['mv'] # Void mass range (number of tracers per void)
dvmin,dvmax = params['Selection']['dv'] # Void core (minimum) density range
Cvmin,Cvmax = params['Selection']['Cv'] # Void compensation range
evmin,evmax = params['Selection']['ev'] # Void ellipticity range
mgsmin,mgsmax = params['Selection']['mgs'] # Void radius range in units of mean galaxy separation (mgs)


# Binning parameters
vbin = params['Bins']['vbin'] # 'zv': void-redshift bins, 'rv': void-radius bins
binning = params['Bins']['binning'] # 'eqn': equal number of voids, 'lin': linearly spaced, 'log': logarithmicly spaced. Alternatively, provide a list for custom bin edges
Nvbin = params['Bins']['Nvbin'] # Number of void bins
Nrbin = params['Bins']['Nrbin'] # Number of radial bins in correlation function
Nrskip = params['Bins']['Nrskip'] # Number of radial bins to skip in fit (starting from the first bin)
rmax = params['Bins']['rmax'] # Maximum radial distance in units of void radius
ell = params['Bins']['ell'] # Multipole orders to consider
Nside = params['Bins']['Nside'] # Mask resolution for generating random voids
symLOS = params['Bins']['symLOS'] # If True, assume void-centric symmetry along LOS (no odd multipoles).
project2d = params['Bins']['project2d'] # If True, the projected correlation function is calculated from the POS vs. LOS 2d correlation function
rescov = params['Bins']['rescov'] # If True, calculate covariance matrix for residuals between data and model (experimental!)
datavec = params['Bins']['datavec'] # Define data vector, '1d': multipoles, '2d': POS vs. LOS 2d correlation function


# Computing parameters
Ncpu = params['Computing']['Ncpu'] # Number of CPUs to use
Nmock = params['Computing']['Nmock'] # Number of mock realizations (for observation = 1)
Nbin_nz = params['Computing']['Nbin_nz'] # Number of bins for redshift distributions
Nbin_nv = params['Computing']['Nbin_nv'] # Number of bins for void abundance function
Nspline = params['Computing']['Nspline'] # Number of nodes for splines (only for visualization in plots, does not affect fit)
Nsmooth = params['Computing']['Nsmooth'] # Smoothing factor for splines (for no smoothing = 0)
Nwalk = params['Computing']['Nwalk'] # Number of MCMC walkers (ideally equal to Ncpu)
Nchain = params['Computing']['Nchain'] # Length of each MCMC chain
Nburn = params['Computing']['Nburn'] # Initial burn-in steps of chain to discard, in units of auto-correlation time
Nthin = params['Computing']['Nthin'] # Thinning factor of chain, in units of auto-correlation time


# Model parameters with fiducial values and priors
par = OrderedDict(params['Model']['par'])
prior = OrderedDict(params['Model']['prior'])


# Cosmological parameters with fiducial values and priors
par_cosmo = params['Cosmo']['par_cosmo']
prior_cosmo = params['Cosmo']['prior_cosmo']
blind = params['Cosmo']['blind'] # If True, subtract mean of cosmology posterior


# Physical constants
G = 6.67385e-11 # Newton's constant in m^3/kg/s^2
c = 299792.458 # Speed of light in km/s
KmMpc = 3.24078e-20 # km in Mpc
KgMsol = 5.02740e-31 # kg in solar masses
DegRad = 0.01745329252 # degrees in radians (pi/180)

