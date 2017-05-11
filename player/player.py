from pydub import AudioSegment
from pydub.playback import play
import scorer

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



# Initial djembe score
score = scorer.get_scores("../scores/moribayassa.sc")

duration = 170
volume_dj1 = 0
volume_dj2 = 0
volume_sangban = 0
volume_kenkeni = 0
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
