import numpy as np
from scipy.io import wavfile

tone_map = {
    '1' : (697, 1209),
    '2' : (697, 1336),
    '3' : (697, 1477),
    'A' : (697, 1633),
    '4' : (770, 1209),
    '5' : (770, 1336),
    '6' : (770, 1477),
    'B' : (770, 1633),
    '7' : (852, 1209),
    '8' : (852, 1336),
    '9' : (852, 1477),
    'C' : (852, 1633),
    '*' : (941, 1209),
    '0' : (941, 1336),
    '#' : (941, 1477),
    'D' : (941, 1633),
    'DIAL' : (350, 440),
    'RING' : (440, 480),
    'BUSY' : (480, 620),
    'HIGH' : (480, 0)
}

text_map = {
    'a' : '2',
    'b' : '22',
    'c' : '222',
    'd' : '3',
    'e' : '33',
    'f' : '333',
    'g' : '4',
    'h' : '44',
    'i' : '444',
    'j' : '5',
    'k' : '55',
    'l' : '555',
    'm' : '6',
    'n' : '66',
    'o' : '666',
    'p' : '7',
    'q' : '77',
    'r' : '777',
    's' : '7777',
    't' : '8',
    'u' : '88',
    'v' : '888',
    'w' : '9',
    'x' : '99',
    'y' : '999',
    'z' : '9999',
    ' ' : '0'
}

def generate_dual_tone(fs, f1, f2, duration):
    """
    fs: sample rate, samples/sec
    f1: first frequency hz
    f2: second frequency hz
    duration: duration in seconds
    ---------------------
    returns: sample array
    """
    t = np.linspace(0,duration,int(duration*fs))
    dual_tone = np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)
    return dual_tone

def generate_message_wav(message, filename='output.wav', dial_tone_duration=3):
    tone_arr = []
    fs = 44100
    tap_dur = 0.1 # duration of tap tone
    tap_gap = 0.1 # time gap s between taps
    char_gap = 0.3 # additional time gap s between chars sharing same num
    n_prev = None
    
    f1,f2 = tone_map['DIAL']
    tone_arr.append(generate_dual_tone(fs,f1,f2,dial_tone_duration))
     
    for char in message:
        mt_code = text_map[char]
        n = mt_code[0]
        if n == n_prev:
            tone_arr.append(np.zeros(int(fs*char_gap)))
        for num in mt_code:
            f1,f2 = tone_map[num]
            tone_arr.append(generate_dual_tone(fs,f1,f2,tap_dur))
            tone_arr.append(np.zeros(int(fs*tap_gap)))
        n_prev = num
        
        
    # write out wav to file
    wavfile.write(filename, fs, np.concatenate(tone_arr))

if __name__ == "__main__":
    generate_message_wav("the flag is babushka")