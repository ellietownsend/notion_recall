import AVFoundation
import Cocoa

# Create the speech utterance string
utterance = AVFoundation.AVSpeechUtterance.speechUtteranceWithString_(
    "Hello from Python using Apple speech synthesis."
)



# Configure optional speech parameters
utterance.setRate_(0.5)
utterance.setPitchMultiplier_(1.0)
utterance.setVolume_(0.8)

# Select a voice (e.g., British English)
voice = AVFoundation.AVSpeechSynthesisVoice.voiceWithLanguage_("en-GB")
utterance.setVoice_(voice)

# Initialize the synthesizer and speak
synth = AVFoundation.AVSpeechSynthesizer.alloc().init()
synth.speakUtterance_(utterance)

# Keep the run loop alive long enough to finish speaking
Cocoa.NSRunLoop.currentRunLoop().runUntilDate_(
    Cocos.NSDate.dateWithTimeIntervalSinceNow_(5)
)
