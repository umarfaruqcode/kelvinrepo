import wave, array, math, time, argparse, sys
import numpy, pywt
from scipy import signal
import pdb
import matplotlib.pyplot as plt
import pyaudio
import bpm_detector

SAMPLE_RATE = 48000
RECORD_DURATION = 10 # Seconds
CHUNKSIZE = 1000
NCHANNELS = 1
SAMPLES_PER_SECOND = SAMPLE_RATE/CHUNKSIZE
SAMPLE_DURATION = 5


# Setup stuff
p = pyaudio.PyAudio()
inStream = p.open(format=pyaudio.paInt16, channels=NCHANNELS, rate=SAMPLE_RATE, input=True, frames_per_buffer=CHUNKSIZE)



data = []
correl=[]
bpm = 0
#nsamps = len(samps)
window_samps = int(SAMPLE_DURATION*SAMPLE_RATE)
samps_ndx = 0; #first sample in window_ndx 
#max_window_ndx = nsamps / window_samps;
#bpms = numpy.zeros(max_window_ndx)



frames = [] # A python-list of chunks(numpy.ndarray)
print "Recording "#, RECORD_DURATION, "seconds of audio"
frame = None



# Start recording
i = 0
n = 20
while True and n > 0:
 if i % (SAMPLES_PER_SECOND) == 0: print i / (SAMPLES_PER_SECOND),

 data = inStream.read(CHUNKSIZE)

 frame = numpy.fromstring(data, dtype=numpy.int16)
 frames.append(frame)
 #print frame

 if i % (SAMPLES_PER_SECOND * SAMPLE_DURATION) == 0 and i > 0:
 print
 numpydata = numpy.hstack(frames)

 samps,fs = bpm_detector.read_wav(numpydata)
 #data = samps[0:window_samps]
 bpm, correl_temp = bpm_detector.bpm_detector(samps,fs)

 # Reset stuff
 frames = []
 n -= 1

 i += 1

#numpydata = numpy.hstack(frames)


print "Recording finished, analysing"






'''
#iterate through all windows
for window_ndx in xrange(1,max_window_ndx):
 #get a new set of samples
 data = samps[samps_ndx:samps_ndx+window_samps]
 if not ((len(data) % window_samps) == 0):
 raise AssertionError( str(len(data) ) ) 
 
 bpm, correl_temp = bpm_detector.bpm_detector(data,fs)
 #print bpm
 #assert False
 if bpm == []:
 continue
 bpms[window_ndx] = bpm
 correl = correl_temp
 
 #iterate at the end of the loop
 samps_ndx = samps_ndx+window_samps;
bpm = numpy.median(bpms)
print 'Completed. Estimated Beats Per Minute:', bpm
n = range(0,len(correl))
plt.plot(n,correl); 
plt.show(True); #plot non-blocking
time.sleep(10);
plt.close();
'''