"""Solution script to 004_chess."""

import pyais
import matplotlib.pyplot as plt
import matplotlib.cm as cm

# messages output from gnuradio solution.grc flowgraph
messages = """!AIVDM,1,1,,A,1h000DOP?w:c4mCckeJN4?wp0000,0*7A
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
!AIVDM,1,1,,B,10000CgP?w:cCNicf=o>4?wp0000,0*70"""

# read through coordinates
pieces = []
for m in messages.split("\n"):
    channel = "white" if m.split(",")[4] == "A" else "black"
    d = pyais.decode(m)
    piece = {"channel": channel, 
            "piece": chr(d.mmsi), # mmsi is the ASCII code of the piece, e.g., 80->"P" (pawn)
            "lat": d.lat, 
            "lon": d.lon}
    pieces.append(piece)

lats = [p["lat"] for p in pieces]
lons = [p["lon"] for p in pieces]
colors = [p["channel"] for p in pieces]

diff = 0.05 #this is the size of each square of the chessboard, can be deduced by piece spacing
lat_lims = [min(lats)-diff/2,max(lats)+diff/2]
lon_lims = [min(lons)-diff/2,max(lons)+diff/2]

#plotting
fig, ax = plt.subplots()
chessboard = [[10,0]*4, [0,10]*4]*4 #chessboard pattern

ax.set_ylim(lat_lims)
ax.set_xlim(lon_lims)
ax.imshow(chessboard, cmap=cm.jet, extent=lon_lims+lat_lims)

for p in pieces:
    ax.scatter(p["lon"], p["lat"], marker=f"${p['piece']}$", color=p["channel"], s=200)


plt.savefig("chessboard_result.png")
plt.show()