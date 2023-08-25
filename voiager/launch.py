# System imports
import os
import sys
import gc
import pickle
import getdist
import numpy as np

# Local imports
from voiager import params
from voiager import datalib
from voiager import plotlib


if not params.runExec:
    sys.exit('Voiager has been installed successfully! Set \'runExec=True\' in \'params.py\' to run it.')


print('Loading data (angles, redshifts, catalog sizes, void properties)...')
Ngc, Nvc, Xg, Xgr, Xv, rv, tv, dv, cv, mv, vv, Cv, ev, eval, evec, mgs = datalib.loadData(params.tracerPath, params.voidPath, params.survey, params.sample, params.random, params.version, params.columnNames, params.Nmock)


print('Generating void randoms...')
Xvr, rvr = datalib.makeRandom(Xv, len(Xgr)/float(len(Xg)), params.Nside, rv)
#np.savetxt(params.outPath+'randomVoids.txt', np.vstack((Xvr.T,rvr)).T, fmt='%.6e', header='RA [rad],  DEC [rad],   Z,           R [Mpc/h]')

# Size of catalogs
Ng, Ngr, Nv, Nvr = len(Xg), len(Xgr), len(Xv), len(Xvr)

# Define redshift arrays
zv, zvr = Xv[:,2], Xvr[:,2]

# Number densities as function of redshift
zgm,  ngm  = datalib.numberDensity(Xg[:,2],  params.Nbin_nz, params.sky, params.Nmock)
zgrm, ngrm = datalib.numberDensity(Xgr[:,2], params.Nbin_nz, params.sky)
zvm,  nvm  = datalib.numberDensity(Xv[:,2],  params.Nbin_nz, params.sky, params.Nmock)
zvrm, nvrm = datalib.numberDensity(Xvr[:,2], params.Nbin_nz, params.sky)


print('Transforming coordinates...')
xg  = datalib.coordTrans(Xg,  params.Ncpu)
xgr = datalib.coordTrans(Xgr, params.Ncpu)
xv  = datalib.coordTrans(Xv,  params.Ncpu)
xvr = datalib.coordTrans(Xvr, params.Ncpu)

# Free up memory
del Xg,Xgr; gc.collect()


print('Building stacks...')
wg = wr = None # weights for galaxies and randoms (optional)

if os.path.exists(params.outPath+params.stackFile): # Load existing stacks
    print('=> Loading previous run')
    Nvi, rvi, zvi, rmi, rmi2d, xip, xipE, xi, xiE, xiC, xiCI, xi2d, xi2dC, xi2dCI  = pickle.load(open(params.outPath+params.stackFile,"rb"))
else:
    if not params.project2d: # LOS-projected correlations
        DDp  = datalib.getStack(xv,  xg,  rv,  zv,  Nvc, Ngc, ngm,  zgm,  wg, params.rmax, params.Nrbin, params.ell, 0, params.Nmock) # Void-Galaxy
        DRp  = datalib.getStack(xv,  xgr, rv,  zv,  Nvc, Ngc, ngrm, zgrm, wr, params.rmax, params.Nrbin, params.ell, 0, False)        # Void-RandomGalaxy
        RDp  = datalib.getStack(xvr, xg,  rvr, zvr, Nvc, Ngc, ngm,  zgm,  wg, params.rmax, params.Nrbin, params.ell, 0, False)        # RandomVoid-Galaxy
        RRp  = datalib.getStack(xvr, xgr, rvr, zvr, Nvc, Ngc, ngrm, zgrm, wr, params.rmax, params.Nrbin, params.ell, 0, False)        # RandomVoid-RandomGalaxy
    # Mulipoles of correlations
    DD   = datalib.getStack(xv,  xg,  rv,  zv,  Nvc, Ngc, ngm,  zgm,  wg, params.rmax, params.Nrbin, params.ell, 1, params.Nmock) # Void-Galaxy
    DR   = datalib.getStack(xv,  xgr, rv,  zv,  Nvc, Ngc, ngrm, zgrm, wr, params.rmax, params.Nrbin, params.ell, 1, False)        # Void-RandomGalaxy
    RD   = datalib.getStack(xvr, xg,  rvr, zvr, Nvc, Ngc, ngm,  zgm,  wg, params.rmax, params.Nrbin, params.ell, 1, False)        # RandomVoid-Galaxy
    RR   = datalib.getStack(xvr, xgr, rvr, zvr, Nvc, Ngc, ngrm, zgrm, wr, params.rmax, params.Nrbin, params.ell, 1, False)        # RandomVoid-RandomGalaxy
    # POS vs. LOS 2d correlations
    DD2d = datalib.getStack(xv,  xg,  rv,  zv,  Nvc, Ngc, ngm,  zgm,  wg, params.rmax, params.Nrbin, params.ell, 2, params.Nmock) # Void-Galaxy
    DR2d = datalib.getStack(xv,  xgr, rv,  zv,  Nvc, Ngc, ngrm, zgrm, wr, params.rmax, params.Nrbin, params.ell, 2, False)        # Void-RandomGalaxy
    RD2d = datalib.getStack(xvr, xg,  rvr, zvr, Nvc, Ngc, ngm,  zgm,  wg, params.rmax, params.Nrbin, params.ell, 2, False)        # RandomVoid-Galaxy
    RR2d = datalib.getStack(xvr, xgr, rvr, zvr, Nvc, Ngc, ngrm, zgrm, wr, params.rmax, params.Nrbin, params.ell, 2, False)        # RandomVoid-RandomGalaxy

    # Get data vectors and covariances
    if not params.project2d:
        Nvi, rvi, zvi, rmi, rmi2d, xip, xipE, xi, xiE, xiC, xiCI, xi2d, xi2dC, xi2dCI = datalib.getData(DDp, DRp, RDp, RRp, DD, DR, RD, RR, DD2d, DR2d, RD2d, RR2d, rv, rvr, zv, zvr, params.Nvbin, params.Nrbin, params.rmax, params.ell, params.symLOS, params.project2d, params.rescov)
    else:
        Nvi, rvi, zvi, rmi, rmi2d, xip, xipE, xi, xiE, xiC, xiCI, xi2d, xi2dC, xi2dCI = datalib.getData(DD, DR, RD, RR, DD, DR, RD, RR, DD2d, DR2d, RD2d, RR2d, rv, rvr, zv, zvr, params.Nvbin, params.Nrbin, params.rmax, params.ell, params.symLOS, params.project2d, params.rescov)
    # Save stacks
    pickle.dump((Nvi, rvi, zvi, rmi, rmi2d, xip, xipE, xi, xiE, xiC, xiCI, xi2d, xi2dC, xi2dCI), open(params.outPath+params.stackFile,"wb"))


# Define theory model
rs, xips, xid, xids, Xid, Xids, xit, xits, xi2dt, xi2dts = datalib.getModel(rmi, rmi2d, rvi, xip, xipE, params.Nsmooth, params.Nspline, weight=None)


print('Finding best fit...')
if params.datavec=='1d': p0, p1, chi2 = datalib.bestFit(zvi, xit, xi, xiC, xiCI)
if params.datavec=='2d': p0, p1, chi2 = datalib.bestFit(zvi, xi2dt, xi2d, xi2dC, xi2dCI)
print('=> Parameters: ',list(params.par.keys()),'\n',p1,'\n qper/qpar: \n',p1[:,1]/p1[:,2],'\n Reduced chi-square: \n',chi2)


print('MCMC sampling...')
if os.path.exists(params.outPath+params.chainFile): print('=> Continuing from previous chain')
if params.datavec=='1d': sampler = datalib.runMCMC(p1, xit, xi, xiC, xiCI, params.Nwalk, params.Nchain, params.chainFile)
if params.datavec=='2d': sampler = datalib.runMCMC(p1, xi2dt, xi2d, xi2dC, xi2dCI, params.Nwalk, params.Nchain, params.chainFile)


# Load chains
samples, logP, pMean, pStd, pErr, pLim = datalib.loadMCMC(params.chainFile,params.Nburn,params.Nthin)


# Measured and derived observables with fiducial reference values
f_b_fid = datalib.f_b_z(zvi,params.par_cosmo)
f_b_fit = np.array(pMean)[:,0]
f_b_err = np.array(pStd)[:,0]

fs8_fid = datalib.fz(zvi,params.par_cosmo)*datalib.Dz(zvi,params.par_cosmo)*params.par_cosmo['s8']
fs8_fit = f_b_fit*datalib.bz(zvi,params.par_cosmo)*datalib.Dz(zvi,params.par_cosmo)*params.par_cosmo['s8']
fs8_err = f_b_err*datalib.bz(zvi,params.par_cosmo)*datalib.Dz(zvi,params.par_cosmo)*params.par_cosmo['s8']

eps_fid = np.ones(params.Nvbin)
eps_fit = np.array(pMean)[:,1]
eps_err = np.array(pStd)[:,1]

DAH_fid = datalib.DA(zvi,params.par_cosmo)/datalib.DH(zvi,params.par_cosmo)
DAH_fit = eps_fit*DAH_fid
DAH_err = eps_err*DAH_fid

# Output strings in latex format
out_tex = []
for i in range(params.Nvbin):
    f_b_fit_str = r'$$'+'{:6.4f}\pm{:6.4f}'.format(f_b_fit[i],f_b_err[i])+'$$'
    fs8_fit_str = r'$$'+'{:6.4f}\pm{:6.4f}'.format(fs8_fit[i],fs8_err[i])+'$$'
    eps_fit_str = r'$$'+'{:6.4f}\pm{:6.4f}'.format(eps_fit[i],eps_err[i])+'$$'
    DAH_fit_str = r'$$'+'{:6.4f}\pm{:6.4f}'.format(DAH_fit[i],DAH_err[i])+'$$'
    out_tex.append(f_b_fit_str+' & '+fs8_fit_str+' & '+eps_fit_str+' & '+DAH_fit_str)

# Gather different measurements (only for illustration)
tags = ['VGCF']
fs8f, fs8e, DAHf, DAHe = [],[],[],[]

fs8f.append(fs8_fit)
fs8e.append(fs8_err)
DAHf.append(DAH_fit)
DAHe.append(DAH_err)



print('Constraining cosmology...')
if os.path.exists(params.outPath+params.cosmoFile): print('=> Continuing from previous cosmology chain')
sampler_cosmo = datalib.runMCMC_cosmo(zvi, DAH_fit, DAH_err, params.Nwalk, params.Nchain, params.cosmoFile, params.cosmology)

# Load cosmology chains:
samples_cosmo, logP_cosmo, pBest_cosmo, pMean_cosmo, pStd_cosmo, pErr_cosmo, pLim_cosmo = datalib.loadMCMC_cosmo(params.cosmoFile, params.cosmology, params.Nburn, params.Nthin, blind=params.blind)

cosmo = []
cosmo.append(samples_cosmo)


# Save chains as text file:
Nsig = 1 # Number of sigmas for confidence intervals
Ndig = 4 # Number of significant digits in headline results for MEAN and MAP (best fit)
header = 'Posterior for Beyond-2pt challenge with void-galaxy cross-correlation analysis of the wCDM light-cone \n\n'
for i,chain in enumerate(cosmo):
    if params.cosmology=='LCDM':
        results  = getdist.MCSamples(samples=chain,names=['Om']).getInlineLatex('Om',limit=Nsig,err_sig_figs=Ndig)+' (MEAN), '+str(np.round(pBest_cosmo[0],Ndig))+' (MAP) \n'
    if params.cosmology=='wCDM':
        results  = getdist.MCSamples(samples=chain,names=['Om','w0']).getInlineLatex('Om',limit=Nsig,err_sig_figs=Ndig)+' (MEAN), '+str(np.round(pBest_cosmo[0],Ndig))+' (MAP) \n'
        results += getdist.MCSamples(samples=chain,names=['Om','w0']).getInlineLatex('w0',limit=Nsig,err_sig_figs=Ndig)+' (MEAN), '+str(np.round(pBest_cosmo[1],Ndig))+' (MAP) \n'
    if params.cosmology=='w0waCDM':
        results  = getdist.MCSamples(samples=chain,names=['Om','w0','wa']).getInlineLatex('Om',limit=Nsig,err_sig_figs=Ndig)+' (MEAN), '+str(np.round(pBest_cosmo[0],Ndig))+' (MAP) \n'
        results += getdist.MCSamples(samples=chain,names=['Om','w0','wa']).getInlineLatex('w0',limit=Nsig,err_sig_figs=Ndig)+' (MEAN), '+str(np.round(pBest_cosmo[1],Ndig))+' (MAP) \n'
        results += getdist.MCSamples(samples=chain,names=['Om','w0','wa']).getInlineLatex('wa',limit=Nsig,err_sig_figs=Ndig)+' (MEAN), '+str(np.round(pBest_cosmo[2],Ndig))+' (MAP) \n'
    np.savetxt(params.outPath+'chains_'+params.cosmology+'_'+str(i+1)+'.txt', chain, fmt='%12.8f', header=header+results)



print('Plotting...')
# Void sample properties
plotlib.voidSky(Xv, Xvr)
plotlib.voidBox(xv, zv)
plotlib.voidRedshift(rv, zv, rvr, zvr)
plotlib.voidAbundance(cv, params.Nbin_nv, r'c_\mathrm{v}', '', 'density-contrast')
plotlib.voidAbundance(dv, params.Nbin_nv, r'n_\mathrm{c}', r'[\bar{n}]', 'core-density')
plotlib.voidAbundance(ev, params.Nbin_nv, r'e_\mathrm{v}', '', 'ellipticity')
plotlib.voidAbundance(mv, params.Nbin_nv, r'm_\mathrm{v}', '', 'richness')
plotlib.voidAbundance(Cv, params.Nbin_nv, r'\Delta_\mathrm{v}', r'[\bar{n}]', 'compensation')
plotlib.voidAbundance(rv, params.Nbin_nv, r'R', r'[h^{-1}\mathrm{Mpc}]', 'effective-radius', yvr=rvr)
plotlib.redshiftDistribution(zgm, zvm, ngm, nvm, zv, zgrm, zvrm, ngrm, nvrm)
plotlib.tracerBias(zgm, datalib.bz(zgm,params.par_cosmo))

# Data vectors and covariances
plotlib.xi_p_test(rs, rmi, rvi, xid)
plotlib.xi_p(xip, xipE, xips, xid, xipE, xids, xi, xiE, xits, rmi, rs, rvi, zvi, p1)
plotlib.xi(xi, xiE, xits, rmi, rs, rvi, zvi, p1, chi2)
plotlib.xi_ell(xi, xiE, xits, rmi, rs, rvi, zvi, p1)
plotlib.xi_2d(xi2d, xi2dts, rmi2d, rvi, zvi, p1, chi2)
plotlib.xi_cov(xiC, dim=1)
plotlib.xi_cov(xi2dC, dim=2)

# Cosmological constraints
plotlib.fs8_DAH(zvi, fs8f, fs8e, DAHf, DAHe, tags)
plotlib.triangle([samples], p0, np.vstack((p1[:,0],p1[:,1]/p1[:,2],p1[:,2:].T)).T, rvi, zvi, pLim, ['qpar'])
plotlib.triangle_cosmo(cosmo, logP_cosmo, pLim_cosmo, params.cosmology, tags)


print('Done.')

#####################
###### THE END ######
#####################
