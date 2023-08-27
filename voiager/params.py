# Survey information
survey = 'Beyond2pt' # Name of survey
sample = 'C_mock_lightcone' # Name of tracer sample
random = 'C_mock_lightcone_R10' # Name of random sample
version = '_0240' # Version (suffix) of void catalog
zmin,zmax = 0.8,1.3 # Redshift range
sky = 3759.6159 # Sky area in square degrees (full sky ~ 41253)
cosmology = "wCDM" # Cosmological model to constrain (current options: "LCDM", "wCDM", "w0waCDM")


# Input / output
import os
runExec = True # If True, run executable when called
basePath = os.getcwd() # Location of the top level code directory
tracerPath = basePath+'/catalogs/tracers/' # Location of tracer catalogs
voidPath = basePath+'/catalogs/voids/' # Location of void catalogs
outPath = basePath+'/results/'+survey+'/'+sample+version+'/' # Location to store output files
plotPath = outPath+'/plots/' # Location to store plots
columnNames = ['RA','DEC','Z_red'] # Tracer and random catalog column headers for right ascension, declination, redshift
stackFile = "stacks.dat" # Filename for data of stacks
chainFile = "chains.dat" # Filename for data of chains
cosmoFile = "chains_"+cosmology+".dat" # Filename for data of cosmology chains
figFormat = "pdf" # Format to save figures (e.g., pdf, png, jpg)


# Void selection
zvmin,zvmax = 0.8,1.3 # Void redshift range
rvmin,rvmax = 35.,1e9 # Void radius range
mvmin,mvmax = 0.0,1e9 # Void mass range (number of tracers per void)
dvmin,dvmax = 0.0,1e9 # Void core (minimum) density range
Cvmin,Cvmax = 0.0,1e9 # Void compensation range
evmin,evmax = 0.0,1.0 # Void ellipticity range
mgsmin,mgsmax = 2.0,1e9 # Void radius range in units of mean galaxy separation (mgs)


# Binning parameters
vbin = 'zv' # 'zv': void-redshift bins, 'rv': void-radius bins
binning = 'lin' # 'eqn': equal void-number bins, 'lin': linearly spaced bins, 'log': logarithmicly spaced bins
Nvbin = 2 # Number of void bins
Nrbin = 20 # Number of radial bins in correlation function
Nrskip = 1 # Number of radial bins to skip in fit (starting from the first bin)
rmax = 3. # Maximum radial distance in units of void radius
ell = (0,2,4) # Multipole orders to consider
Nside = 128 # Mask resolution for generating random voids
symLOS = True # If True, assume void-centric symmetry along LOS (no odd multipoles).
project2d = True # If True, the projected correlation function is calculated from the POS vs. LOS 2d correlation function
rescov = False # If True, calculate covariance matrix for residuals between data and model (experimental!)
datavec = '2d' # Define data vector, '1d': multipoles, '2d': POS vs. LOS 2d correlation function


# Computing parameters
Ncpu = 16 # Number of CPUs to use
Nmock = 1 # Number of mock realizations (for observation = 1)
Nbin_nz = 20 # Number of bins for redshift distributions
Nbin_nv = 8 # Number of bins for void abundance function
Nspline = 200 # Number of nodes for splines (only for visualization in plots, does not affect fit)
Nsmooth = 0.5 # Smoothing factor for splines (for no smoothing = 0)
Nwalk = 16 # Number of MCMC walkers (ideally equal to Ncpu)
Nchain = 1000 # Length of each MCMC chain
Nburn = 3.0 # Initial burn-in steps of chain to discard, in units of auto-correlation time
Nthin = 0.5 # Thinning factor of chain, in units of auto-correlation time


# Model parameters with fiducial values, priors, and labels
from collections import OrderedDict
par = OrderedDict()
par['f/b']   =  0.5
par['qper']  =  1.0
par['qpar']  =  1.0
par['M']     =  1.0
par['Q']     =  1.0

prior = OrderedDict()
prior['f/b']  = (-10.,10.)
prior['qper'] = (-10.,10.)
prior['qpar'] = (-10.,10.)
prior['M']    = (-10.,10.)
prior['Q']    = (-10.,10.)

label = OrderedDict()
label['f/b']  = r'f/b'
label['qper'] = r'q_\perp/q_\parallel' # r'\varepsilon'
label['qpar'] = r'q_\parallel'
label['M']    = r'\mathcal{M}'
label['Q']    = r'\mathcal{Q}'


# Cosmological parameters with fiducial values and priors
par_cosmo = {
    'Om': 0.24,  # Omega_matter
    'Ok': 0.00,  # Curvature
    'w0': -1.0,  # DE eq. of state (constant)
    'wa': 0.00,  # DE eq. of state (slope)
    's8': 0.80,  # RMS of density fluctuations of scale 8 Mpc/h
    'h' : 0.70,  # Reduced Hubble constant
    'b0': 1.40}  # Linear tracer bias at z=0

prior_cosmo = {
    'Om': (0.0,1.0),
    'w0': (-2,-1/3),
    'wa': (-10,10)}

blind = True # If True, subtract mean of cosmology posterior


# Physical constants
G = 6.67385e-11 # Newton's constant in m^3/kg/s^2
c = 299792.458 # Speed of light in km/s
KmMpc = 3.24078e-20 # km in Mpc
KgMsol = 5.02740e-31 # kg in solar masses
DegRad = 3.14159/180. # degrees in radians
