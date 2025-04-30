
# coding: utf-8

# In[2]:


#IMPORTED DATA CELL
#Categorization: TMC - tmc data, LAB - lab data, C - compressor on, A - active system on, G - ground
plt.rcParams["font.family"] = "Times New Roman", 'Times'

LTFOFF = np.genfromtxt(r'C:\Users\JSwooty\Documents\College\Physics\Thesis\Data\LABTFOFF.txt', skip_header=7,names=True)
LPOFF = np.genfromtxt(r'C:\Users\JSwooty\Documents\College\Physics\Thesis\Data\LABPLATEOFF.txt', skip_header=7,names=True)

labfreq2, Xg, Yg, Zg, Xn, Yn, Zn, Xa, Ya, Za = zip(*LPOFF) 
xoff3, yoff3, zoff3, xon3, yon3, zon3 = zip(*LTFOFF)






# In[21]:


#Lab Data Acceleration Compressor Off Aluminum Plates

f, (ax1, ax2, ax3) = plt.subplots(3, figsize=(3.5,4.67), dpi=600, sharex=True, sharey=True)

ax1.plot(labfreq2, velroot(labfreq2, Xg, 1), c='r', label='X Ground',linewidth=.5)
ax1.plot(labfreq2, velroot(labfreq2, Xa, 1), c='b', label='X Al Plate(ON)',linewidth=.5)
ax1.plot(labfreq2, velroot(labfreq2, Xn, 1), c='c', label='X Al Plate(OFF)',linewidth=.5)
ax1.set_yscale('log')
ax1.set_xscale('log')
#ax1.set_ylabel('LogMag (m/s/rootHz)')
ax1.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax1.legend(fontsize=8,framealpha=0)
ax1.tick_params(axis='both', which='major', labelsize=8)

ax2.plot(labfreq2, velroot(labfreq2, Yg, 1), c='r', label='Y Ground',linewidth=.5)
ax2.plot(labfreq2, velroot(labfreq2, Ya, 1), c='b', label='Y Al Plate(ON)',linewidth=.5)
ax2.plot(labfreq2, velroot(labfreq2, Yn, 1), c='c', label='Y Al Plate(OFF)',linewidth=.5)
ax2.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylabel('\u221APSD(\u03BD) (m/s/\u221AHz)',fontsize=12)
ax2.legend(fontsize=8,framealpha=0)
ax2.tick_params(axis='both', which='major', labelsize=8)

ax3.plot(labfreq2, velroot(labfreq2, Zg, 1), c='r', label='Z Ground',linewidth=.5)
ax3.plot(labfreq2, velroot(labfreq2, Za, 1), c='b', label='Z Al Plate(ON)',linewidth=.5)
ax3.plot(labfreq2, velroot(labfreq2, Zn, 1), c='c', label='Z Al Plate(OFF',linewidth=.5)
ax3.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax3.set_yscale('log')
ax3.set_xscale('log')
#ax3.set_ylabel('LogMag (m/s/rootHz)')
ax3.legend(fontsize=8,framealpha=0)
ax3.tick_params(axis='both', which='major', labelsize=8)

plt.xlim([1,200])
plt.xlabel("f(Hz)", fontsize=12)

plt.rcParams["font.family"] = "Times New Roman", 'Times'
#leg = plt.legend()
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)

plt.savefig('LABPlateviboff.png',bbox_inches='tight')
plt.show()


# In[4]:


#Lab Compressor off Transfer Function

f, (ax1, ax2, ax3) = plt.subplots(3, figsize=(3.5,4.67), dpi=600, sharex=True, sharey=True)

plt.rcParams["font.family"] = "Times New Roman", 'Times'
#ax1.plot(labfreq, xoff3, c='r', label='X Al Plate (OFF)',linewidth=.5)
#ax1.plot(labfreq, xon3, c='b', label='X Al Plate (ON)',linewidth=.5)
ax1.plot(labfreq, PSDTransfer(Xg, Xn), c='r', label='X Al Plate(OFF)',linewidth=.5)
ax1.plot(labfreq, PSDTransfer(Xg, Xa), c='b', label='X Al Plate(ON)',linewidth=.5)
#ax1.set_yscale('log')
ax1.set_xscale('log')
#ax1.set_ylabel('LogMag (m/s/rootHz)',fontsize=8)
ax1.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax1.legend(fontsize=8, loc = 'lower left',framealpha=0)
ax1.tick_params(axis='both', which='major', labelsize=8)

#ax2.plot(labfreq, yoff3, c='r', label='Y Al Plate (OFF)',linewidth=.5)
#ax2.plot(labfreq, yon3, c='b', label='Y Al Plate (ON)',linewidth=.5)
ax2.plot(labfreq, PSDTransfer(Yg, Yn), c='r', label='Y Al Plate(OFF)',linewidth=.5)
ax2.plot(labfreq, PSDTransfer(Yg, Ya), c='b', label='Y Al Plate(ON)',linewidth=.5)
#ax2.plot(tmcfreq, velroot(tmcfreq, tmc26, 0), c='c', label='Y Payload (OFF)',linewidth=.5)
ax2.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
#ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylabel('Transfer Function (dB)',fontsize=12)
ax2.legend(fontsize=8, loc = 'lower left',framealpha=0)
ax2.tick_params(axis='both', which='major', labelsize=8)

#ax3.plot(labfreq, zoff3, c='r', label='Z Al Plate (OFF)',linewidth=.5)
#ax3.plot(labfreq, zon3, c='b', label='Z Al Plate (ON)',linewidth=.5)
ax3.plot(labfreq, PSDTransfer(Zg, Zn), c='r', label='Z Al Plate(OFF)',linewidth=.5)
ax3.plot(labfreq, PSDTransfer(Zg, Za), c='b', label='Z Al Plate(ON)',linewidth=.5)
#ax3.plot(tmcfreq, velroot(tmcfreq, tmc9, 0), c='c', label='Z Payload (OFF',linewidth=.5)
ax3.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
#ax3.set_yscale('log')
ax3.set_xscale('log')
#ax3.set_ylabel('LogMag (m/s/rootHz)', fontsize=8)
ax3.legend(fontsize=8, loc='lower left',framealpha=0)
ax3.tick_params(axis='both', which='major', labelsize=8)

#plt.ylim([-60,60])
plt.xlim([1,200])
plt.xlabel("f(Hz)", fontsize=12)
plt.rcParams["font.family"] = "Times New Roman", 'Times'
#leg = plt.legend()
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('LABtfOff.png',bbox_inches='tight')
plt.show()


# In[26]:


#Lab Data 1/3Octave Compressor Off
plt.rcParams["font.family"] = "Times New Roman", 'Times'
f, (ax1, ax2, ax3) = plt.subplots(3, figsize=(3.5,4.67), dpi=600, sharex=True, sharey=True)
ax1.scatter(octavesc,octaves(labfreq2, Xg, 1, octavesl, octavesl, octavesh), c='r', label='X Ground',linewidth=.20, s=8)
ax1.plot(octavesc,octaves(labfreq2, Xg, 1,octavesl, octavesl, octavesh), c='r', linewidth=.20)
ax1.scatter(octavesc,octaves(labfreq2, Xa, 1,octavesl, octavesl, octavesh), c='b', label='X Al Plate(ON)',linewidth=.20, s=8)
ax1.plot(octavesc,octaves(labfreq2, Xa, 1,octavesl, octavesl, octavesh), c='b', linewidth=.20)
ax1.scatter(octavesc,octaves(labfreq2, Xn, 1,octavesl, octavesl, octavesh), c='c', label='X Al Plate(OFF)',linewidth=.20, s=8)
ax1.plot(octavesc,octaves(labfreq2, Xn, 1,octavesl, octavesl, octavesh), c='c', linewidth=.20)
ax1.plot(octavesc, VCE, c='r', linewidth=.5)
ax1.plot(octavesc, VCF, c='r', linewidth=.5)
ax1.plot(octavesc, VCG, c='r', linewidth=.5)
ax1.plot(octavesc, VCH, c='r', linewidth=.5)
ax1.plot(octavesc, VCI, c='r', linewidth=.5)
ax1.plot(octavesc, VCJ, c='r', linewidth=.5)
ax1.text(1, VCE[-1], 'VCE', fontsize=6)
ax1.text(1, VCF[-1], 'VCF', fontsize=6)
ax1.text(1, VCG[-1], 'VCG', fontsize=6)
ax1.text(1, VCH[-1], 'VCH', fontsize=6)
ax1.text(1, VCI[-1], 'VCI', fontsize=6)
ax1.text(1, VCJ[-1], 'VCJ', fontsize=6)
ax1.grid(True, which="Major", ls="-", linewidth=.5)
ax1.set_yscale('log')
ax1.set_xscale('log')
ax1.legend(fontsize=8, loc = 'upper left',ncol=2, mode='expand',framealpha=0)
#ax1.set_ylabel("Log Mag (m/s rms)")
ax1.tick_params(axis='both', which='major', labelsize=8)

ax2.scatter(octavesc,octaves(labfreq2, Yg, 1, octavesl, octavesl, octavesh), c='r', label='Y Ground',linewidth=.20, s=8)
ax2.plot(octavesc,octaves(labfreq2, Yg, 1,octavesl, octavesl, octavesh), c='r', linewidth=.20)
ax2.scatter(octavesc,octaves(labfreq2, Ya, 1,octavesl, octavesl, octavesh), c='b', label='Y Al Plate(ON)',linewidth=.20, s=8)
ax2.plot(octavesc,octaves(labfreq2, Ya, 1,octavesl, octavesl, octavesh), c='b', linewidth=.20)
ax2.scatter(octavesc,octaves(labfreq2, Yn, 1,octavesl, octavesl, octavesh), c='c', label='Y Al Plate(OFF)',linewidth=.20, s=8)
ax2.plot(octavesc,octaves(labfreq2, Yn, 1,octavesl, octavesl, octavesh), c='c', linewidth=.20)
ax2.plot(octavesc, VCE, c='r', linewidth=.5)
ax2.plot(octavesc, VCF, c='r', linewidth=.5)
ax2.plot(octavesc, VCG, c='r', linewidth=.5)
ax2.plot(octavesc, VCH, c='r', linewidth=.5)
ax2.plot(octavesc, VCI, c='r', linewidth=.5)
ax2.plot(octavesc, VCJ, c='r', linewidth=.5)
ax2.text(1, VCE[-1], 'VCE', fontsize=6)
ax2.text(1, VCF[-1], 'VCF', fontsize=6)
ax2.text(1, VCG[-1], 'VCG', fontsize=6)
ax2.text(1, VCH[-1], 'VCH', fontsize=6)
ax2.text(1, VCI[-1], 'VCI', fontsize=6)
ax2.text(1, VCJ[-1], 'VCJ', fontsize=6)
ax2.grid(True, which="Major", ls="-", linewidth=.5)
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.legend(fontsize=8,loc='upper left',ncol=2, mode='expand',framealpha=0)
ax2.set_ylabel("\u221APSD(\u03BD) (m/s rms)", fontsize=12)
ax2.tick_params(axis='both', which='major', labelsize=8)


ax3.scatter(octavesc,octaves(labfreq2, Zg, 1, octavesl, octavesl, octavesh), c='r', label='Z Ground',linewidth=.20, s=8)
ax3.plot(octavesc,octaves(labfreq2, Zg, 1,octavesl, octavesl, octavesh), c='r', linewidth=.20)
ax3.scatter(octavesc,octaves(labfreq2, Za, 1,octavesl, octavesl, octavesh), c='b', label='Z Al Plate(ON)',linewidth=.20, s=8)
ax3.plot(octavesc,octaves(labfreq2, Za, 1,octavesl, octavesl, octavesh), c='b', linewidth=.20)
ax3.scatter(octavesc,octaves(labfreq2, Zn, 1,octavesl, octavesl, octavesh), c='c', label='Z Al Plate(OFF)',linewidth=.20, s=8)
ax3.plot(octavesc,octaves(labfreq2, Zn, 1,octavesl, octavesl, octavesh), c='c', linewidth=.20)
ax3.grid(True, which="Major", ls="-", linewidth=.5)
ax3.set_yscale('log')
ax3.set_xscale('log')
ax3.legend(fontsize=8, loc='upper left',ncol=2, mode='expand',framealpha=0)
ax3.plot(octavesc, VCE, c='r', linewidth=.5)
ax3.plot(octavesc, VCF, c='r', linewidth=.5)
ax3.plot(octavesc, VCG, c='r', linewidth=.5)
ax3.plot(octavesc, VCH, c='r', linewidth=.5)
ax3.plot(octavesc, VCI, c='r', linewidth=.5)
ax3.plot(octavesc, VCJ, c='r', linewidth=.5)
ax3.text(1, VCE[-1], 'VCE', fontsize=6)
ax3.text(1, VCF[-1], 'VCF',fontsize=6)
ax3.text(1, VCG[-1], 'VCG',fontsize=6)
ax3.text(1, VCH[-1], 'VCH',fontsize=6)
ax3.text(1, VCI[-1], 'VCI',fontsize=6)
ax3.text(1, VCJ[-1], 'VCJ',fontsize=6)
#ax3.set_ylabel("Log Mag (m/s rms)")
ax3.tick_params(axis='both', which='major', labelsize=8)

plt.rcParams["font.family"] = "Times New Roman", 'Times'
plt.xlim([1,100])
plt.ylim([1e-9, 9.9e-5])
plt.xlabel("f(Hz)", fontsize=12)
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('LABPlateoctoff.png',bbox_inches='tight')
plt.show()


# In[25]:


#Lab acceleration Compressor off
plt.rcParams['mathtext.fontset'] = 'custom'
plt.rcParams['mathtext.it'] = 'Times New Roman:italic'

f, (ax1, ax2, ax3) = plt.subplots(3, figsize=(3.5,4.67), dpi=600, sharex=True, sharey=True)

ax1.plot(labfreq, normalize(Xg), c='r', label='X Ground',linewidth=.5)
ax1.plot(labfreq, normalize(Xa), c='b', label='X Al Plate(ON)',linewidth=.5)
ax1.plot(labfreq, normalize(Xn), c='c', label='X Al Plate(OFF)',linewidth=.5)
ax1.set_yscale('log')
ax1.set_xscale('log')
#ax1.set_ylabel('LogMag (m/s/rootHz)')
ax1.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax1.legend(fontsize=8, loc='upper left',framealpha=0)
ax1.tick_params(axis='both', which='major', labelsize=8)

ax2.plot(labfreq, normalize(Yg), c='r', label='Y Ground',linewidth=.5)
ax2.plot(labfreq, normalize(Ya), c='b', label='Y Al Plate(ON)',linewidth=.5)
ax2.plot(labfreq, normalize(Yn), c='c', label='Y Al Plate(OFF)',linewidth=.5)
ax2.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax2.set_yscale('log')
ax2.set_xscale('log')
ax2.set_ylabel('\u221APSD($\mathit{a}$) (g/\u221AHz)', fontsize=12)
ax2.legend(fontsize=8, loc='upper left',framealpha=0)
ax2.tick_params(axis='both', which='major', labelsize=8)

ax3.plot(labfreq, normalize(Zg), c='r', label='Z Ground',linewidth=.5)
ax3.plot(labfreq, normalize(Za), c='b', label='Z Al Plate(ON)',linewidth=.5)
ax3.plot(labfreq, normalize(Zn), c='c', label='Z Al Plate(OFF)',linewidth=.5)
ax3.grid(True, which="Major", axis="both", ls="-", linewidth='.5')
ax3.set_yscale('log')
ax3.set_xscale('log')
#ax3.set_ylabel('LogMag (g/rootHz)')
ax3.legend(fontsize=8, loc='upper left',framealpha=0)
ax3.tick_params(axis='both', which='major', labelsize=8)

plt.xlim([1,200])
plt.xlabel("f(Hz)", fontsize=12)
plt.ylim([1.001e-8,9.9e-4])
plt.rcParams["font.family"] = "Times New Roman", 'Times'
#leg = plt.legend()
f.subplots_adjust(hspace=0)
plt.setp([a.get_xticklabels() for a in f.axes[:-1]], visible=False)
plt.savefig('LABPlatevibaoff.png',bbox_inches='tight')
plt.show()

