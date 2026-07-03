# Sonification Specification v0.1

The Observatory sonifies HTE mappings as an audible interface. The generated audio is a rendering of the mapping, not a claim that a material literally sounds like the output.

## Core mapping

```text
pitch_class = atomic_number mod 12
pitch_class -> note class
octave_band -> register
stoichiometric count -> amplitude / duration weighting
overlay state -> timbre and envelope
uncertainty -> optional detune / noise layer
```

## Default note table

```text
0  C
1  C#
2  D
3  Eb
4  E
5  F
6  F#
7  G
8  Ab
9  A
10 Bb
11 B
```

## v0.1 audio behavior

- Browser-native Web Audio API.
- Equal temperament by default.
- Base frequency: A4 = 440 Hz.
- Weighted chord is played as a short arpeggio and then as a combined tone cluster.
- Counts increase duration and gain, with conservative caps to avoid harsh output.

## Future controls

- Base frequency selector.
- Temperament selector.
- Greek modal field selector.
- Timbre profile selector.
- Calibration confidence filter.
- Export audio clip.

## Claim boundary

Sound is an exploratory interface for pattern recognition. It can reveal clusters, tension, repetition, and comparative structure, but it does not by itself validate physical material behavior.
