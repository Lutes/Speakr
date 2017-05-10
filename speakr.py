from pydub import AudioSegment
import nltk
import re

def makeSentence(arpabetArray):
	wordAudio = AudioSegment.from_mp3("start.mp3")
	for word in arpabetArray:
		for phone in word:
			file = phone + ".mp3"
			wordAudio = wordAudio +  AudioSegment.from_mp3(file)
		wordAudio = wordAudio +  AudioSegment.from_mp3(file)
	
	wordAudio.export("end.mp3", format="mp3")

def createArpabetArray(text):
	arpabetArray = []
	tempArray = []
	text = text.lower()
	words = text.split(" ");
	arpabet = nltk.corpus.cmudict.dict()
	for word in words:
	    try:
			aword =	arpabet[word][0]
			for phone in aword:
				out = re.sub(r'\d+', '', phone)
				tempArray.append(str(out))
			arpabetArray.append(tempArray)
			tempArray = []
	    except Exception as e:
	        print e
	return arpabetArray

makeSentence(createArpabetArray("This is"))