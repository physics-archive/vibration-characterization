
# coding: utf-8

# In[ ]:


#FUNCTIONS CELL
#http://prosig.com/wp-content/uploads/pdf/blogArticles/OmegaArithmetic.pdf reference for conversions
#Octave Calculation init
import math as m
#bandwidth: width of each frequency band
#acceleration to velocity: v = a/(2pif)

#####PSD unit conversion calculations#####

def normalize(vibs):            #this function is just to take the square root of the PSD spectra, which starts in
    v = []                      #units of V^2/Hz
    for i in range(len(vibs)):
        v.append(m.sqrt(vibs[i])) 
    return(v) ##returns units, from raw data, of g/rootHz

def normalizetmc(vibs, freq):   #this function is effectively converting the units of the data aqcuired using the 
    v = []                      #DataPhysics and SignalCalc software, as the output is in units of g. We then divide 
    for i in range(len(vibs)):  #by the square root of the bandwidth to get units of g/rootHz
        v.append(vibs[i]/(m.sqrt((freq[5]-freq[4])*2)))
    return v

def velroot(freq, data, option):    #0 for TMC data, 1 for rms(?), any for other data(in PSD units V^2/Hz)
    gr = 9.81                       #defining 'g' for ease
    if option == 0:                 #payload data is in units of g, so need to divide by bandwidth to get back to roothz
        bw = freq[5] - freq[4]      
        tmc = []
        for i in range(len(freq)):
            tmc.append((gr*data[i])/(m.sqrt(bw)*2**(3/2)*m.pi*freq[i]))  #to convert from a to v, we need to 
        return(tmc)                                                      #multiply by 9.81 (in 1 g, there are 9.81ms^-2)
    elif option == 1:                           #and divide by omega, or 2 pi f in our case, and root2 as an rms factor
        v = normalize(data)                         
        w = []
        for i in range(len(data)):                       #For our data, we do almost the same thing but don't divide 
            w.append((v[i]*gr)/(2*m.pi*freq[i]))         #by bandwidth since already in roothz units.
        return(w) #returns units, from normalized data, of m/s/roothz
    
#####Octave Calculations#####

octavesc = []
octavesh = []
octavesl = []

def octavecenter(n, i):                      #defining the center frequency of my 1/3 octave bands based on a reference
    return(1000/((2**(1/3))**(n - i)))       #frequency of 1000 Hz

num = 30
for i in range(0,(num + 1)):                 #this calls each center octave frequency and creates the bandwidth for 
    octavesc.append(octavecenter(num, i))    #each.
    octavesh.append(octavesc[i]*(2**(1/6)))
    octavesl.append(octavesc[i]/(2**(1/6)))

#function to filter our data into the 1/3 octave bands
def octaves(x, y, option, ran1, octlow, octhigh):
    tot = []
    num = 0
    cnt = 0
    j = 0
    i = 0
    bw = x[5] - x[4]                         #bw is the bandwidth, just picked two random frequency points in the 
    vel = velroot(x,y,option)                #data as the bandwidth is constant
    for j in range(len(ran1)):
        for i in range(len(x)):
            if x[i] > octlow[j] and x[i] <= octhigh[j]: #this function calls our velocity function velroot, so we are  
                cnt = cnt + (vel[i]**2)*bw              #squaring our PSD units and multiplying by the bandwidth to 
                num = num + 1                           #remove the Hz factor.
        #if num == 0:
         #   num += 1
        tot.append(m.sqrt(cnt))    
        cnt = 0
        num = 0
        
    return(tot)

#####Transfer Function calculation#####

def PSDTransfer(PSDG, PSDL):          #Because output units are the same, we can use the raw PSD output numbers without
    v = []                            #converting to any other units
    for i in range(len(PSDG)):
        v.append(20*m.log10(m.sqrt(PSDL[i]/PSDG[i])))   #We are converting power to decibels here
    return v

