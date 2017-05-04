from pydub import AudioSegment
from pydub.playback import play

# Initial media AudioSegments
bass = AudioSegment.from_wav("../media/djembe/D2_O.wav")
tone = AudioSegment.from_wav("../media/djembe/D2_U.wav")
slap = AudioSegment.from_wav("../media/djembe/D2_V.wav")

s_bell = AudioSegment.from_wav("../media/dundun/G_S_O.wav")
s_open = AudioSegment.from_wav("../media/dundun/S_O.wav")
s_mute = AudioSegment.from_wav("../media/dundun/S_M.wav")

k_bell = AudioSegment.from_wav("../media/dundun/G_K_O.wav")
k_open = AudioSegment.from_wav("../media/dundun/K_O.wav")
k_mute = AudioSegment.from_wav("../media/dundun/K_M.wav")

d_bell = AudioSegment.from_wav("../media/dundun/G_D_O.wav")
d_open = AudioSegment.from_wav("../media/dundun/D_O.wav")
d_mute = AudioSegment.from_wav("../media/dundun/D_M.wav")

slap = slap - 3

s_bell = s_bell -10
s_open = s_open +5
s_mute = s_mute +5

d_bell = d_bell -10
d_open = d_open +5
d_mute = d_mute +5

k_bell = k_bell -13
k_open = k_open +5
k_mute = k_mute +5

# Load scores
dj1_bass_score = "1000100010001000"
dj1_tone_score = "0011000000110000"
dj1_slap_score = "0000001000000010"

dj2_bass_score = "0000000000000000"
dj2_tone_score = "0000001100000011"
dj2_slap_score = "1001100010011000"

s_bell_score = "1010101010101010"
s_open_score = "1000000000101010"
s_mute_score = "0000100010000000"

k_bell_score = "1010101010101010"
k_open_score = "1000100010001000"
k_mute_score = "0000000000000000"

d_bell_score = "1011011010110110"
d_open_score = "1000001010000010"
d_mute_score = "0000000000000000"

# Initial djembe score
score = {}
score["dj1_bass_score"] = list(dj1_bass_score)
score["dj1_tone_score"] = list(dj1_tone_score)
score["dj1_slap_score"] = list(dj1_slap_score)
score["dj2_bass_score"] = list(dj2_bass_score)
score["dj2_tone_score"] = list(dj2_tone_score)
score["dj2_slap_score"] = list(dj2_slap_score)

score["s_bell_score"] = list(s_bell_score)
score["s_open_score"] = list(s_open_score)
score["s_mute_score"] = list(s_mute_score)

score["k_bell_score"] = list(k_bell_score)
score["k_open_score"] = list(k_open_score)
score["k_mute_score"] = list(k_mute_score)

score["d_bell_score"] = list(d_bell_score)
score["d_open_score"] = list(d_open_score)
score["d_mute_score"] = list(d_mute_score)



duration = 170
volume_dj1 = 1
volume_dj2 = 0
volume_sangban = 1
volume_kenkeni = 1
volume_dundunba = 1

segments = []  # The list each element is overlaid segment

for i in range(len(score["dj1_bass_score"])):

    seg = AudioSegment.silent(duration)

    if volume_dj1 != 0:
        if score["dj1_bass_score"][i] == "1":
            seg = seg.overlay(bass)
        if score["dj1_tone_score"][i] == "1":
            seg = seg.overlay(tone)
        if score["dj1_slap_score"][i] == "1":
            seg = seg.overlay(slap)

    if volume_dj2 != 0:
        if score["dj2_bass_score"][i] == "1":
            seg = seg.overlay(bass)
        if score["dj2_tone_score"][i] == "1":
            seg = seg.overlay(tone)
        if score["dj2_slap_score"][i] == "1":
            seg = seg.overlay(slap)

    if volume_sangban != 0:
        if score["s_bell_score"][i] == "1":
            seg = seg.overlay(s_bell)
        if score["s_open_score"][i] == "1":
            seg = seg.overlay(s_open)
        if score["s_mute_score"][i] == "1":
            seg = seg.overlay(s_mute)

    if volume_kenkeni != 0:
        if score["k_bell_score"][i] == "1":
            seg = seg.overlay(k_bell)
        if score["k_open_score"][i] == "1":
            seg = seg.overlay(k_open)
        if score["k_mute_score"][i] == "1":
            seg = seg.overlay(k_mute)

    if volume_dundunba != 0:
        if score["d_bell_score"][i] == "1":
            seg = seg.overlay(d_bell)
        if score["d_open_score"][i] == "1":
            seg = seg.overlay(d_open)
        if score["d_mute_score"][i] == "1":
            seg = seg.overlay(d_mute)

    segments.append(seg)

# From a list of segments to a single sentence
sentence = AudioSegment.empty()
for seg in segments:
    sentence += seg

sentence = sentence * 8
play(sentence)
