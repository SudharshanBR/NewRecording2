"""
Name : runMe.py
Purpose : Note Recognition.
Song of the day : Day One - Hans Zimmer
You might be wondering multiple things, here are a few explanations. Relax, this is pretty simple.

W1. How to use this file?
1. Select an audio file (.wav || .m4a).
2. In the "Terminal" - travel to the directory which has me.
3. Paste the audio file in the directory.
4. Run the following command - python runMe.py <fileName>


"""

## List of all imports.
# from pydub import AudioSegment
import numpy as np
import sys
import librosa
from matplotlib import pyplot as plt

#Class definition
class RecognizeNotes:

    # Main method
    def main(self):

        if not sys.warnoptions:
            import warnings
            warnings.simplefilter("ignore")

        theAudioFile = 'allNotesSlow.m4a'
        if len(sys.argv) > 1:
            theAudioFile = sys.argv[1]
        theAudio, samplingRate = librosa.load(theAudioFile)
        valuesOfSpectrogram = plt.specgram(theAudio,NFFT=1000,Fs=samplingRate,noverlap=100)
        spectrogramNP = valuesOfSpectrogram[0]
        sumOfSpectrogram = np.sum(spectrogramNP,axis=0)
        sumOfSpectrogram = np.expand_dims(sumOfSpectrogram,axis=0)
        specNP = np.transpose(spectrogramNP, (1, 0))
        threshold = 7e-5
        beta = 0.1
        outputName = []
        frequency = []
        resultList = []
        musicalNotes = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        noteFrequencies = np.array(list(range(len(musicalNotes)))) + 11

        for eachItem in sumOfSpectrogram[0]:
            if eachItem > threshold:
                outputName.append(1)
            else:
                outputName.append(0)

        for index,value in enumerate(specNP):
            for eachVariable in range(len(value)):
                if (value[eachVariable] - max(value) * beta) > 0:
                    frequency.append(eachVariable)
                    break


        for index1,value in enumerate(outputName):
            if value == 1:
                intermediateList = noteFrequencies - frequency[index1]
                for index2, eachItem in enumerate(intermediateList):
                    if eachItem == 0:
                        if musicalNotes[index2] not in resultList:
                            resultList.append(musicalNotes[index2])


        print(resultList)



recognizeMe = RecognizeNotes()
recognizeMe.main()





