from pydub import AudioSegment
from pydub.playback import play

# Initial media AudioSegments
bass = AudioSegment.from_wav("../media/djembe/D2_O.wav")
tone = AudioSegment.from_wav("../media/djembe/D2_U.wav")
slap = AudioSegment.from_wav("../media/djembe/D2_V.wav")

d_mute = AudioSegment.from_wav("../media/dundun/D_M.wav")
d_open = AudioSegment.from_wav("../media/dundun/D_O.wav")
d_bell = AudioSegment.from_wav("../media/dundun/G_D_O.wav")

s_mute = AudioSegment.from_wav("../media/dundun/S_M.wav")
s_open = AudioSegment.from_wav("../media/dundun/S_O.wav")
s_bell = AudioSegment.from_wav("../media/dundun/G_S_O.wav")

k_mute = AudioSegment.from_wav("../media/dundun/K_M.wav")
k_open = AudioSegment.from_wav("../media/dundun/K_O.wav")
k_bell = AudioSegment.from_wav("../media/dundun/G_K_O.wav")


duration = 150


b_score = "11011010"
t_score = "00110000"
s_score = "00011010"

b_score = list(b_score)
t_score = list(t_score)
s_score = list(s_score)

mix = []

for i in range(len(b_score)):

    seg = AudioSegment.silent(duration)

    if b_score[i] == "1":
        print("bass")
        seg = seg.overlay(bass)
    if t_score[i] == "1":
        print("tone")
        seg = seg.overlay(tone)
    if s_score[i] == "1":
        print("slap")
        seg = seg.overlay(slap)

    mix.append(seg)

sentence = AudioSegment.empty()
for seg in mix:
    sentence += seg

print(len(sentence))
sentence = sentence * 10
play(sentence)
