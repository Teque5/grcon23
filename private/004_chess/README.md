# Noir 4: Symphony of Signals (AIS Chess)

## Solution

* 199 points
* Topic: AIS / DSP / SDR / Chess
* `flag{Qc7}`

## Explanation

Investigating the symphony SigMF file, there is a baseband audio signal that says "White to move, mate in one". The metadata also indicates that white is transmitting its positions on channel A, and black is transmitting on channel B. Using gr-ais to decode the AIS signals, the messages are: 

```!AIVDM,1,1,,A,1h000DOP?w:c4mCckeJN4?wp0000,0*7A
!AIVDM,1,1,,B,10000BwP?w:bWR?cmRW>4?wp0000,0*62
!AIVDM,1,1,,B,10000DgP?w:cR8AcmRW>4?wp0000,0*64
!AIVDM,1,1,,A,1h000DgP?w:cCNkckeJN4?wp0000,0*2E
!AIVDM,1,1,,A,1h000D?P?w:b:?CcdHbN4?wp0000,0*5D
!AIVDM,1,1,,B,10000D?P?w:b:?AckeK>4?wp0000,0*7F
!AIVDM,1,1,,B,10000@gP?w:cR8AckeK>4?wp0000,0*4D
!AIVDM,1,1,,A,1h000D?P?w:bHpkcbSNN4?wp0000,0*79
!AIVDM,1,1,,A,1h000BwP?w:b:?Cc`fBN4?wp0000,0*19
!AIVDM,1,1,,B,10000D?P?w:bHpicip?>4?wp0000,0*09
!AIVDM,1,1,,B,10000DOP?w:bn;icbSO>4?wp0000,0*4C
!AIVDM,1,1,,A,1h000CgP?w:cR8Cc`fBN4?wp0000,0*66
!AIVDM,1,1,,A,1h000DOP?w:c4mCckeJN4?wp0000,0*7A
!AIVDM,1,1,,B,10000CgP?w:cCNicf=o>4?wp0000,0*70
```

These can be decoded with pyais and plotted. Then, all that's left is to solve the "Mate in 1" puzzle. 

### Getting started

* You are provided a pair of SigMF files of what you hear. 

### Dependencies

* gr-ais/another AIS receiver tool like rtl-ais
* pyais or another AIS decoder

