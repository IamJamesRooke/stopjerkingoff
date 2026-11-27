# Draws the illustrations in images/illustrations/ as SVG. Usage: python3 tools/draw_illustrations.py images/illustrations/
# PNGs are rendered from the SVGs at 2x (a headless browser screenshot of the <svg> element).
import sys
OUT=sys.argv[1]
INK="#141414"; LIME="#9BD13A"; STINK="#C7F05A"; SHIRT="#2F6BFF"; RED="#FF3B30"; YEL="#FFD23F"; GLOW="#BFE3FF"
SW=5
def head(w,h,bg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
<defs><filter id="r" x="-3%" y="-3%" width="106%" height="106%"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="2"/></filter></defs>
<rect width="{w}" height="{h}" rx="28" fill="{bg}"/>
<g filter="url(#r)" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round" fill="none">
'''
TAIL="</g></svg>\n"
def dot(x,y,r=3.6): return f'<circle cx="{x}" cy="{y}" r="{r}" fill="{INK}" stroke="none"/>'
def seg(x,y,s,ch):
    a=(x,y,x+s,y); b=(x+s,y,x+s,y+s); c=(x+s,y+s,x+s,y+2*s); d=(x,y+2*s,x+s,y+2*s); e=(x,y+s,x,y+2*s); f=(x,y,x,y+s); g=(x,y+s,x+s,y+s)
    m={'2':[a,b,g,e,d],'0':[a,b,c,d,e,f]}
    return "".join(f'<line x1="{p[0]}" y1="{p[1]}" x2="{p[2]}" y2="{p[3]}" stroke="{RED}" stroke-width="3.4"/>' for p in m[ch])
def clock(x,y):
    s=9; o=f'<rect x="{x}" y="{y}" width="80" height="40" rx="7" fill="{INK}"/>'
    o+=seg(x+11,y+10,s,'2')+dot(x+30,y+15,2).replace(INK,RED)+dot(x+30,y+25,2).replace(INK,RED)+seg(x+38,y+10,s,'0')+seg(x+56,y+10,s,'0')
    return o
def stars(pts): return "".join(f'<circle cx="{x}" cy="{y}" r="2.6" fill="#fff" stroke="none"/>' for x,y in pts)
def moon(x,y,r=20): return f'<path d="M{x},{y-r} a{r},{r} 0 1,0 {r*0.9},{r*1.5} a{r*0.75},{r*0.75} 0 1,1 {-r*0.9},{-r*1.5} Z" fill="{YEL}" stroke="none"/>'
def monster(tx,ty,pose,sc=1.0,stink=True):
    o=f'<g transform="translate({tx},{ty}) scale({sc})">'
    if stink:
        for dx in (-20,0,20):
            o+=f'<path d="M{dx},-66 c-7,-9 7,-15 0,-24 c-7,-9 7,-15 0,-24" stroke="{STINK}" stroke-width="4"/>'
    if pose=="bang":
        o+=f'<path d="M-24,-26 Q-42,-20 -44,-8"/><path d="M24,-26 Q42,-20 44,-8"/>'
        o+=f'<circle cx="-44" cy="-6" r="7" fill="{LIME}"/><circle cx="44" cy="-6" r="7" fill="{LIME}"/>'
    o+=f'<path d="M-30,-8 C-34,-38 -19,-56 0,-56 C19,-56 34,-38 30,-8 C27,2 -27,2 -30,-8 Z" fill="{LIME}"/>'
    o+='<path d="M-4,-55 q1,-12 6,-3 q3,-11 7,1" stroke-width="4"/>'
    if pose=='dangle':
        o+='<circle cx="-10" cy="-35" r="9" fill="#fff"/><circle cx="10" cy="-35" r="9" fill="#fff"/>'
    if pose=="dangle":
        o+=dot(-8,-33)+dot(12,-33)
        o+='<path d="M-19,-46 L-4,-41"/><path d="M19,-46 L4,-41"/><path d="M-7,-18 q7,-8 14,0" stroke-width="4"/><path d="M-4,-17 q4,4 8,0" fill="#FF8FA3" stroke-width="2.5"/>'
        o+='<path d="M-16,-27 q-3,6 0,9 q3,-3 0,-9 Z" fill="#4FB3FF" stroke-width="2"/>'
        o+='<path d="M-22,-12 Q0,-2 16,-9"/><path d="M22,-12 Q0,-2 -16,-9"/>'
        o+=f'<ellipse cx="-11" cy="6" rx="6" ry="8" fill="{LIME}"/><ellipse cx="11" cy="6" rx="6" ry="8" fill="{LIME}"/>'
    else:
        # tantrum: eyes screwed shut, mouth wide open, tears flying
        o+='<path d="M-17,-40 l8,4 l-8,4" stroke-width="3.5"/><path d="M17,-40 l-8,4 l8,4" stroke-width="3.5"/>'
        o+='<ellipse cx="0" cy="-17" rx="10" ry="8" fill="#5a1414"/><path d="M-5,-12 q5,-4 10,0" stroke="#FF8FA3" stroke-width="3"/>'
        o+='<path d="M-20,-34 q-12,4 -18,16" stroke="#4FB3FF" stroke-width="3.5"/><path d="M20,-34 q12,4 18,16" stroke="#4FB3FF" stroke-width="3.5"/>'
        o+='<circle cx="-40" cy="-14" r="3" fill="#4FB3FF" stroke="none"/><circle cx="40" cy="-14" r="3" fill="#4FB3FF" stroke="none"/>'
        o+=f'<ellipse cx="-13" cy="0" rx="9" ry="5" fill="{LIME}"/><ellipse cx="13" cy="0" rx="9" ry="5" fill="{LIME}"/>'
    return o+'</g>'

# A. The back room (Intro)
s=head(800,560,"#2B3A8F")
s+=moon(690,70)+stars([(90,60),(150,120),(600,50),(740,140),(60,180)])
s+='<line x1="40" y1="520" x2="760" y2="520"/>'
s+='<path d="M140,210 L400,70 L660,210 Z" fill="#FF5A5F"/>'
s+='<rect x="160" y="210" width="480" height="310" fill="#FFF6E5"/>'
s+='<line x1="160" y1="365" x2="640" y2="365" stroke-width="7"/><line x1="440" y1="210" x2="440" y2="365"/>'
s+='<path d="M200,520 L200,500 L230,500 L230,480 L260,480 L260,460 L290,460 L290,440 L320,440 L320,420 L350,420 L350,400 L380,400 L380,385 L410,385 L410,365"/>'
s+=f'<rect x="240" y="250" width="100" height="75" fill="{YEL}"/><line x1="290" y1="250" x2="290" y2="325"/>'
s+=monster(545,362,"bang",0.85)
for (x,y,dx,dy) in [(492,352,-14,-8),(494,364,-16,4),(598,352,14,-8),(596,364,16,4)]:
    s+=f'<line x1="{x}" y1="{y}" x2="{x+dx}" y2="{y+dy}" stroke="{RED}" stroke-width="5"/>'
s+='<path d="M480,378 q10,8 20,0 q10,-8 20,0" stroke-width="3.5"/><path d="M575,378 q10,8 20,0 q10,-8 20,0" stroke-width="3.5"/>'
# couch + man
s+=f'<rect x="465" y="460" width="160" height="42" rx="10" fill="{RED}"/><rect x="460" y="430" width="26" height="72" rx="10" fill="{RED}"/><rect x="604" y="430" width="26" height="72" rx="10" fill="{RED}"/>'
s+='<line x1="478" y1="502" x2="478" y2="518"/><line x1="612" y1="502" x2="612" y2="518"/>'
s+=f'<path d="M520,432 C510,445 512,470 522,478 L556,478 C562,468 562,445 552,432 Z" fill="{SHIRT}"/>'
s+='<circle cx="536" cy="408" r="24" fill="#fff"/>'+dot(530,400)+dot(545,399)
s+='<line x1="531" y1="417" x2="543" y2="417" stroke-width="3.5"/>'
s+='<path d="M540,478 L580,478 L583,516"/><path d="M548,446 L566,456 L578,446"/>'
s+=f'<rect x="572" y="432" width="14" height="24" rx="3" fill="{INK}" transform="rotate(15 579 444)"/>'
s+=TAIL; open(OUT+"intro-back-room.svg","w").write(s)

# B. Carry him out (Intro)
s=head(680,480,"#33C3D6")
s+='<line x1="30" y1="430" x2="650" y2="430"/>'
s+=f'<rect x="520" y="170" width="110" height="260" fill="{YEL}"/><rect x="520" y="170" width="110" height="260"/>'
s+='<path d="M520,170 L478,192 L478,420 L520,430 Z" fill="#FFF6E5"/>'+dot(491,305,4)
s+='<circle cx="238" cy="166" r="34" fill="#fff"/>'
s+='<path d="M240,158 l10,4 l-10,4" stroke-width="3.5"/><path d="M270,158 l-9,4 l9,4" stroke-width="3.5"/>'
s+='<path d="M246,184 q5,-5 10,0 q5,5 10,0" stroke-width="3.5"/>'
s+=f'<path d="M222,204 C206,230 206,290 220,318 L258,318 C268,290 266,230 252,204 Z" fill="{SHIRT}"/>'
s+='<path d="M230,318 L208,426"/><path d="M248,318 L282,426"/>'
s+='<path d="M222,228 L204,272 L196,306"/>'
s+='<path d="M252,228 L320,236 L376,226"/>'
s+='<path d="M372,220 q9,-5 13,4 q-4,9 -13,4" fill="#fff" stroke-width="4"/>'
s+=monster(384,298,"dangle",1.05,stink=False)
for dx in (420,438):
    s+=f'<path d="M{dx},270 c7,-9 -7,-15 0,-24 c7,-9 -7,-15 0,-24" stroke="#4E7A12" stroke-width="4"/>'
s+=TAIL; open(OUT+"intro-carry-him-out.svg","w").write(s)

# C. The button
s=head(680,440,"#1B2459")
s+=moon(590,70,18)+stars([(80,60),(160,110),(470,50),(640,150),(300,40)])
s+='<line x1="30" y1="400" x2="650" y2="400" stroke="#fff"/>'
s+='<rect x="170" y="240" width="250" height="160" fill="#FFF6E5"/><line x1="170" y1="312" x2="420" y2="312"/>'+dot(295,276,5)
s+=clock(186,200)
for (x1,y1,x2,y2) in [(345,170,345,148),(300,186,286,172),(390,186,404,172),(286,220,266,220),(404,220,424,220)]:
    s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="6"/>'
s+='<rect x="305" y="222" width="80" height="18" fill="#D9D9D9"/><ellipse cx="345" cy="222" rx="40" ry="9" fill="#D9D9D9"/>'
s+=f'<path d="M315,222 C315,188 375,188 375,222 Z" fill="{RED}"/><path d="M328,206 q7,-8 16,-8" stroke="#fff" stroke-width="4"/>'
s+=f'<ellipse cx="490" cy="262" rx="46" ry="20" fill="{GLOW}" stroke="none"/>'
s+='<rect x="445" y="272" width="210" height="62" rx="10" fill="#FFF6E5"/><line x1="462" y1="334" x2="462" y2="398" stroke="#fff"/><line x1="638" y1="334" x2="638" y2="398" stroke="#fff"/>'
s+=f'<rect x="472" y="252" width="36" height="20" rx="4" fill="{INK}" transform="rotate(-8 490 262)"/>'
s+=TAIL; open(OUT+"button-on-the-nightstand.svg","w").write(s)

# D. Shoes two sizes too small (The Easy Method)
s=head(680,460,"#7B4FD6")
s+=moon(590,70,18)+stars([(80,60),(150,120),(470,50),(640,170)])
s+='<line x1="30" y1="410" x2="650" y2="410"/>'
s+='<rect x="100" y="300" width="230" height="50" rx="10" fill="#FFF6E5"/><line x1="115" y1="350" x2="115" y2="408"/><line x1="315" y1="350" x2="315" y2="408"/>'
s+=f'<path d="M232,198 C214,224 214,280 228,304 L270,304 C282,280 280,224 262,198 Z" fill="{SHIRT}"/>'
s+='<circle cx="247" cy="160" r="34" fill="#fff"/>'
s+='<path d="M232,156 q6,-6 12,0" stroke-width="3.5"/><path d="M254,156 q6,-6 12,0" stroke-width="3.5"/>'
s+='<ellipse cx="252" cy="178" rx="7" ry="8" fill="#fff" stroke-width="3.5"/>'
# leg down, bare foot on floor
s+='<path d="M258,304 L338,308 L342,396"/>'
s+='<ellipse cx="356" cy="402" rx="22" ry="9" fill="#FFE3C7"/>'
# leg raised, foot up
s+='<path d="M262,300 L360,282 L420,242"/>'
s+='<ellipse cx="438" cy="232" rx="24" ry="11" fill="#FFE3C7" transform="rotate(-30 438 232)"/>'
# arms reaching to shoe
s+='<path d="M244,222 L330,250 L470,214"/><path d="M256,226 L344,236 L470,214"/>'
# tiny shoe in hand
s+=f'<path d="M462,200 L496,198 C506,198 508,214 498,214 L462,216 Z" fill="{RED}"/>'
# relief sparkles
for (x1,y1,x2,y2) in [(430,196,424,180),(458,250,472,262),(410,262,398,276),(380,388,370,374),(384,414,398,420)]:
    s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="5"/>'
# other tiny shoe on floor
s+=f'<path d="M420,404 L448,402 C456,402 458,412 450,412 L420,413 Z" fill="{RED}"/>'
s+=TAIL; open(OUT+"easy-method-tight-shoes.svg","w").write(s)

# ---- Second batch (chapters after The Easy Method) ----
def man(x,y,face="flat",shirt=SHIRT):
    """Head centered at (x,y); returns head + torso. Torso runs to y+150; hips at (x-4,y+150)/(x+14,y+150)."""
    o=f'<path d="M{x-16},{y+38} C{x-32},{y+64} {x-32},{y+124} {x-18},{y+152} L{x+20},{y+152} C{x+30},{y+124} {x+28},{y+64} {x+14},{y+38} Z" fill="{shirt}"/>'
    o+=f'<circle cx="{x}" cy="{y}" r="34" fill="#fff"/>'
    if face=="flat":
        o+=dot(x-6,y-6)+dot(x+10,y-6)+f'<line x1="{x-4}" y1="{y+14}" x2="{x+10}" y2="{y+14}" stroke-width="3.5"/>'
    elif face=="happy":
        o+=f'<path d="M{x-12},{y-6} q5,-6 10,0" stroke-width="3.5"/><path d="M{x+6},{y-6} q5,-6 10,0" stroke-width="3.5"/><path d="M{x-6},{y+10} q8,9 16,0" stroke-width="3.5"/>'
    elif face=="squeeze":
        o+=f'<path d="M{x-12},{y-10} l9,4 l-9,4" stroke-width="3.5"/><path d="M{x+18},{y-10} l-9,4 l9,4" stroke-width="3.5"/><path d="M{x-6},{y+14} l4,-3 l4,3 l4,-3 l4,3" stroke-width="3"/>'
    elif face=="blank":
        o+=dot(x-4,y-8)+dot(x+12,y-8)+f'<path d="M{x},{y+12} q5,2 10,0" stroke-width="3.5"/>'
    return o

def batch2(OUT):
    # E. The punt (The Empty House)
    s=head(680,440,"#2FB36A")
    for x in (120,260,400,540):
        s+=f'<line x1="{x}" y1="20" x2="{x}" y2="420" stroke="#fff" stroke-width="4" opacity="0.55"/>'
    s+='<line x1="30" y1="410" x2="650" y2="410" stroke="#fff"/>'
    s+=man(170,170,"happy")
    s+='<path d="M166,322 L150,408"/><path d="M184,320 L240,300 L262,268"/>'
    s+='<path d="M156,215 L110,250"/><path d="M184,215 L232,236"/>'
    s+=f'<path d="M270,262 Q380,120 486,110" stroke="#fff" stroke-width="4" stroke-dasharray="4 14"/>'
    s+=f'<g transform="rotate(25 520 120)">{monster(520,150,"dangle",0.95,stink=False)}</g>'
    for (x1,y1,x2,y2) in [(470,70,450,60),(468,100,446,98),(476,130,456,138)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="5"/>'
    s+=TAIL; open(OUT+"empty-house-punt.svg","w").write(s)

    # F. Carrying his dinner up (The Empty House)
    s=head(680,460,"#FF8C42")
    s+='<line x1="30" y1="420" x2="650" y2="420"/>'
    steps="M90,420"
    x,y=90,420
    for i in range(8):
        x+=0; y-=34; steps+=f" L{x},{y}"; x+=46; steps+=f" L{x},{y}"
    s+=f'<path d="{steps} L{x},420 Z" fill="#FFF6E5"/>'
    # door at top with the monster
    s+=f'<rect x="470" y="40" width="110" height="108" fill="#5A3E9B"/><rect x="470" y="40" width="110" height="108"/>'
    s+=monster(522,146,"bang",0.7)
    # man on the stairs with a plate
    s+=man(300,150,"flat")
    s+='<path d="M296,302 L280,352 L276,386"/><path d="M314,302 L346,318 L350,352"/>'
    s+='<path d="M290,196 L338,212 L370,196"/><path d="M308,200 L346,206 L370,196"/>'
    s+='<ellipse cx="392" cy="192" rx="38" ry="10" fill="#fff"/>'
    s+=f'<path d="M370,188 q22,-24 44,0 Z" fill="{RED}"/>'
    for dx in (378,394,410):
        s+=f'<path d="M{dx},166 c-5,-6 5,-10 0,-16" stroke="#fff" stroke-width="3"/>'
    s+=TAIL; open(OUT+"empty-house-dinner-upstairs.svg","w").write(s)

    # G. The path across the lawn (The Flesh)
    s=head(680,420,"#7FD3FF")
    s+='<path d="M0,170 L680,150 L680,392 Q680,420 652,420 L28,420 Q0,420 0,392 Z" fill="#43B85C" stroke="none"/>'
    s+='<path d="M0,170 L680,150"/>'
    s+='<path d="M60,410 C200,360 300,300 420,230 C480,196 560,172 640,160" stroke="#9C6B3C" stroke-width="34" opacity="0.95"/>'
    s+='<path d="M60,410 C200,360 300,300 420,230 C480,196 560,172 640,160" stroke="#C8925A" stroke-width="22"/>'
    s+='<rect x="540" y="70" width="90" height="84" fill="#FFF6E5"/><path d="M528,74 L585,32 L642,74 Z" fill="#FF5A5F"/><rect x="574" y="112" width="20" height="42" fill="#5A3E9B"/>'
    for (x,y) in [(110,300),(150,260),(500,300),(560,350),(260,390),(620,260)]:
        s+=f'<path d="M{x},{y} l4,-12 M{x+8},{y} l0,-14 M{x+16},{y} l-4,-12" stroke="#1E7A36" stroke-width="3.5"/>'
    s+=man(300,198,"flat")
    s+='<path d="M296,350 L280,376"/><path d="M314,350 L336,372"/><path d="M284,236 L262,286"/><path d="M314,236 L340,284"/>'
    s=s.replace(man(300,198,"flat"), f'<g transform="translate(300,300) scale(0.5) translate(-300,-300)">{man(300,198,"flat")}<path d="M296,350 L270,430"/><path d="M314,350 L350,428"/><path d="M286,236 L250,300"/><path d="M314,236 L350,296"/></g>')
    s=s.replace('<path d="M296,350 L280,376"/><path d="M314,350 L336,372"/><path d="M284,236 L262,286"/><path d="M314,236 L340,284"/>','')
    s+=TAIL; open(OUT+"flesh-path-across-the-lawn.svg","w").write(s)

    # H. Grandfather's watch as a hammer (The Flesh)
    s=head(680,440,"#FFD23F")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="470" y="60" width="60" height="350" fill="#C8925A"/><line x1="485" y1="80" x2="485" y2="390" stroke-width="2.5"/><line x1="512" y1="120" x2="512" y2="370" stroke-width="2.5"/>'
    s+='<line x1="430" y1="232" x2="470" y2="232" stroke-width="6"/><line x1="430" y1="222" x2="430" y2="242" stroke-width="6"/>'
    s+=man(220,170,"blank")
    s+='<path d="M216,322 L196,408"/><path d="M234,322 L262,408"/>'
    s+='<path d="M206,214 L186,262 L180,300"/><path d="M234,214 L300,236 L352,222"/>'
    # watch with chain in hand
    s+='<path d="M352,222 L380,226" stroke-width="3" stroke-dasharray="2 5"/>'
    s+=f'<circle cx="404" cy="230" r="24" fill="#F4C542"/><circle cx="404" cy="230" r="17" fill="#fff" stroke-width="3"/>'
    s+='<line x1="404" y1="230" x2="404" y2="218" stroke-width="3"/><line x1="404" y1="230" x2="413" y2="234" stroke-width="3"/>'
    s+='<path d="M396,216 L404,226 L398,238 L408,246" stroke="#141414" stroke-width="2"/>'
    for (x1,y1,x2,y2) in [(432,196,444,180),(440,262,454,276),(420,190,420,172)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+='<path d="M370,170 q16,-22 36,-14" stroke-width="3"/><path d="M402,152 l6,4 l-7,3" stroke-width="3"/>'
    s+=TAIL; open(OUT+"flesh-watch-as-a-hammer.svg","w").write(s)

    # I. The car alarm (The Little Monster)
    s=head(680,420,"#FF5A5F")
    s+='<line x1="30" y1="380" x2="650" y2="380"/>'
    s+=f'<path d="M330,330 L330,290 Q332,270 356,266 L400,232 Q410,224 430,224 L520,224 Q540,224 552,236 L586,266 Q620,270 624,292 L624,330 Z" fill="#2F6BFF"/>'
    s+='<path d="M410,262 L432,238 L470,238 L470,262 Z" fill="#BFE3FF"/><path d="M486,262 L486,238 L530,238 L556,262 Z" fill="#BFE3FF"/>'
    s+='<circle cx="380" cy="332" r="26" fill="#333"/><circle cx="380" cy="332" r="10" fill="#ddd"/><circle cx="572" cy="332" r="26" fill="#333"/><circle cx="572" cy="332" r="10" fill="#ddd"/>'
    s+=f'<circle cx="610" cy="284" r="8" fill="{YEL}"/><circle cx="342" cy="284" r="8" fill="{YEL}"/>'
    for r in (0,1,2):
        s+=f'<path d="M{470-r*0},{196-r*22} q20,-12 40,0" stroke="#fff" stroke-width="5"/>'
    s+=f'<path d="M640,250 q12,30 0,60" stroke="#fff" stroke-width="5"/><path d="M314,250 q-12,30 0,60" stroke="#fff" stroke-width="5"/>'
    s+=man(170,160,"squeeze")
    s+='<path d="M166,312 L150,378"/><path d="M184,312 L206,378"/>'
    s+='<path d="M152,206 L136,170 L146,140"/><path d="M188,206 L206,170 L196,140"/>'
    s+=TAIL; open(OUT+"little-monster-car-alarm.svg","w").write(s)

def batch3(OUT):
    # J. The dragon in his head (Introduction, after "It is the whole dragon")
    s=head(720,520,"#FFB13B")
    s+='<line x1="30" y1="480" x2="690" y2="480"/>'
    s+=('<path d="M260,250 C206,250 196,190 242,176 C232,120 296,96 326,124 C346,70 426,64 452,110 '
        'C486,60 576,76 578,130 C646,128 670,200 624,226 C656,270 596,310 554,290 C526,330 446,330 426,296 '
        'C386,322 306,316 298,280 C274,290 246,276 260,250 Z" fill="#fff"/>')
    s+='<circle cx="236" cy="296" r="14" fill="#fff"/><circle cx="216" cy="328" r="9" fill="#fff"/>'
    D="#7B4FD6"
    s+=f'<path d="M332,250 C300,246 280,236 266,216 L254,228 L258,204 L280,212 C292,226 310,234 336,236" fill="{D}"/>'
    s+=f'<path d="M392,214 L344,118 L374,140 L392,104 L416,140 L438,120 L448,210 Z" fill="#5A3E9B"/>'
    s+=f'<ellipse cx="400" cy="246" rx="72" ry="38" fill="{D}"/>'
    s+=f'<path d="M444,228 C468,204 488,176 512,156 L540,176 C514,196 494,226 468,256 Z" fill="{D}"/>'
    s+=f'<path d="M508,150 C520,132 560,128 578,142 L594,152 L572,158 L594,168 L570,176 C552,184 522,180 508,168 Z" fill="{D}"/>'
    s+='<path d="M576,152 l-6,8 l-4,-8 M584,158 l-4,8 l-5,-7" stroke="#fff" stroke-width="2.5"/>'
    s+=f'<path d="M520,136 L512,110 L534,130 M540,132 L540,104 L556,130" fill="#5A3E9B"/>'
    s+=dot(548,146,4.5)+'<path d="M536,136 l20,4" stroke-width="4"/>'
    s+=f'<path d="M598,160 C614,146 626,150 640,140 C632,156 640,164 628,176 C620,170 608,172 598,166 Z" fill="{RED}" stroke="{RED}"/>'
    s+=f'<path d="M604,160 C614,154 620,156 628,152 C624,160 626,164 620,170 Z" fill="{YEL}" stroke="none"/>'
    s+='<path d="M360,280 l-4,22 l-8,2 M392,284 l0,22 l-8,2 M430,282 l4,22 l-6,2 M456,274 l8,20 l-6,4" stroke-width="5"/>'
    # the man, sword up, sweating
    s+=man(170,320,"blank")
    s+='<path d="M166,472 L150,478"/>'
    s+='<path d="M166,472 L156,478"/>'
    s=s.replace('<path d="M166,472 L150,478"/><path d="M166,472 L156,478"/>','<path d="M166,472 L150,478"/><path d="M184,472 L200,478"/>')
    s+='<path d="M156,366 L132,330"/><path d="M184,366 L214,348 L232,330"/>'
    s+='<line x1="232" y1="330" x2="268" y2="250" stroke="#B9C2CC" stroke-width="8"/><line x1="222" y1="324" x2="244" y2="336" stroke-width="6"/>'
    s+='<path d="M204,296 q6,10 0,14 q-6,-4 0,-14 Z" fill="#7FD3FF" stroke-width="2.5"/>'
    # the real thing, at his feet
    s+=monster(300,478,"bang",0.75,stink=True)
    s+=TAIL; open(OUT+"intro-the-dragon-in-his-head.svg","w").write(s)

    # K. Press it and he was never there (The Button)
    s=head(720,480,"#1B2459")
    s+=moon(640,70,18)+stars([(80,60),(170,110),(500,50),(690,160),(330,40)])
    s+='<line x1="30" y1="440" x2="690" y2="440" stroke="#fff"/>'
    s+='<rect x="90" y="290" width="230" height="150" fill="#FFF6E5"/><line x1="90" y1="358" x2="320" y2="358"/>'+dot(205,324,5)
    s+=clock(104,250)
    s+='<rect x="210" y="272" width="80" height="18" fill="#D9D9D9"/><ellipse cx="250" cy="272" rx="40" ry="9" fill="#D9D9D9"/>'
    s+=f'<path d="M220,272 C220,250 280,250 280,272 Z" fill="{RED}"/>'
    # finger pressing
    s+='<path d="M250,252 L250,200 Q250,180 270,176 L330,166" fill="none"/>'
    s+='<ellipse cx="250" cy="250" rx="9" ry="6" fill="#fff"/>'
    for (x1,y1,x2,y2) in [(206,250,190,236),(294,250,310,236),(250,226,250,226)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="6"/>'
    # the back room upstairs: empty, a puff where he was
    s+='<rect x="400" y="120" width="260" height="190" fill="#FFF6E5"/><line x1="400" y1="310" x2="660" y2="310" stroke-width="7"/>'
    s+=('<path d="M480,290 C460,290 456,266 474,260 C470,236 500,226 512,240 C520,218 556,218 562,240 '
        'C580,230 604,246 594,266 C612,272 606,294 586,292 Z" fill="#fff" stroke-dasharray="10 8"/>')
    for (x1,y1,x2,y2) in [(470,220,458,204),(540,206,540,186),(610,222,624,206),(450,276,432,280),(620,282,640,284)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="6"/>'
    s+=TAIL; open(OUT+"button-press-it.svg","w").write(s)

def legs(x,y,spread=18):
    return f'<path d="M{x-4},{y} L{x-spread},{y+86}"/><path d="M{x+14},{y} L{x+14+spread},{y+86}"/>'

def batch4(OUT):
    W,H=680,440
    # 1. The cream and the rash (What Am I Giving Up?)
    s=head(W,H,"#FF8FB1")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(300,150,"squeeze")+legs(300,302)
    s+=f'<path d="M286,196 L250,250 L262,270"/><path d="M316,196 L360,236 L330,262"/>'
    for (x,y) in [(250,232),(258,250),(266,214),(354,230),(340,246),(276,208),(300,226),(286,262),(318,280),(296,300)]:
        s+=f'<circle cx="{x}" cy="{y}" r="5" fill="{RED}" stroke="none"/>'
    s+=f'<rect x="318" y="248" width="30" height="16" rx="4" fill="#fff" transform="rotate(-30 333 256)"/><rect x="314" y="262" width="8" height="10" fill="{SHIRT}" transform="rotate(-30 318 267)"/>'
    for i,(x,y,r) in enumerate([(470,330,-10),(520,350,15),(560,320,-25),(500,390,5),(590,380,30),(440,385,-20)]):
        s+=f'<g transform="rotate({r} {x} {y})"><rect x="{x-22}" y="{y-9}" width="44" height="18" rx="4" fill="#fff"/><rect x="{x+22}" y="{y-5}" width="9" height="10" fill="{SHIRT}"/></g>'
    s+=f'<path d="M352,130 q6,10 0,14 q-6,-4 0,-14 Z" fill="#7FD3FF" stroke-width="2.5"/>'
    s+=TAIL; open(OUT+"giving-up-cream-and-rash.svg","w").write(s)

    # 2. The dropped coat (Getting Your Time Back)
    s=head(W,H,"#9AA9C2")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="120" y="300" width="440" height="50" rx="10" fill="#FFF6E5"/><line x1="140" y1="350" x2="140" y2="408"/><line x1="540" y1="350" x2="540" y2="408"/>'
    s+=f'<path d="M210,300 C230,278 300,282 360,290 C400,286 450,288 480,296 L470,302 L216,304 Z" fill="{SHIRT}"/>'
    s+='<ellipse cx="180" cy="290" rx="34" ry="14" fill="#fff"/>'
    s+='<path d="M166,286 l10,0 M184,286 l10,0" stroke-width="3"/><path d="M172,296 q6,2 12,0" stroke-width="3"/>'
    s+='<path d="M480,298 L560,300 L590,330 M470,300 L540,306 L560,336"/><path d="M300,300 L280,344 M330,300 L340,346"/>'
    for (x,y) in [(240,250),(270,236),(300,250)]:
        s+=f'<text x="{x}" y="{y}" font-family="sans-serif" font-size="0">.</text>'
    s+='<path d="M230,250 q10,-10 20,0 M262,232 q10,-10 20,0" stroke="#fff" stroke-width="3"/>'
    s+=TAIL; open(OUT+"time-the-dropped-coat.svg","w").write(s)

    # 3. The bank account somebody dips into (What It's Doing to You)
    s=head(W,H,"#5FD08A")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<ellipse cx="360" cy="300" rx="120" ry="84" fill="#FF8FB1"/><ellipse cx="478" cy="292" rx="22" ry="26" fill="#FF8FB1"/>'
    s+=dot(474,286,4)+dot(486,286,4)+'<path d="M320,222 L330,198 L350,218" fill="#FF8FB1"/><line x1="330" y1="222" x2="380" y2="222" stroke-width="7"/>'
    s+='<path d="M290,380 L290,408 M420,380 L420,408 M260,370 L256,404 M450,370 L454,404" stroke-width="6"/>'
    s+=dot(410,268,5)+'<path d="M402,252 l14,4" stroke-width="3.5"/>'
    s+=f'<path d="M560,60 C520,90 470,150 372,216"/><path d="M372,216 l-12,-4 l2,14 Z" fill="#fff"/>'
    s+=f'<circle cx="376" cy="200" r="10" fill="{YEL}"/><circle cx="350" cy="170" r="9" fill="{YEL}"/><circle cx="330" cy="140" r="8" fill="{YEL}"/>'
    s+='<path d="M372,216 q-6,-10 6,-12" stroke-width="3"/>'
    s+=TAIL; open(OUT+"costs-the-bank-account.svg","w").write(s)

    # 4. Arm-wrestling yourself (Two Wills)
    s=head(W,H,"#FFB13B")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="250" y="270" width="180" height="20" fill="#C8925A"/><line x1="270" y1="290" x2="270" y2="408"/><line x1="410" y1="290" x2="410" y2="408"/>'
    s+=man(170,170,"squeeze")+legs(170,322)
    s+=man(510,170,"squeeze")+legs(510,322)
    s+='<path d="M186,226 L290,262 L330,220"/><path d="M494,226 L390,262 L350,220"/><circle cx="340" cy="216" r="12" fill="#fff"/>'
    for (x1,y1,x2,y2) in [(320,186,312,170),(360,186,368,170),(340,180,340,162)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+=f'<path d="M206,128 q6,10 0,14 q-6,-4 0,-14 Z" fill="#7FD3FF" stroke-width="2.5"/><path d="M476,128 q6,10 0,14 q-6,-4 0,-14 Z" fill="#7FD3FF" stroke-width="2.5"/>'
    s+=TAIL; open(OUT+"two-wills-arm-wrestling.svg","w").write(s)

    # 5. Two weeks without toast (Every Man in the Trap)
    s=head(W,H,"#7FD3FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="330" y="250" width="220" height="20" fill="#C8925A"/><line x1="350" y1="270" x2="350" y2="408"/><line x1="530" y1="270" x2="530" y2="408"/>'
    s+='<ellipse cx="450" cy="246" rx="50" ry="10" fill="#fff"/>'
    s+=f'<path d="M424,240 C420,214 436,206 450,212 C464,206 480,214 476,240 Z" fill="#E8B66B"/><path d="M432,236 C430,220 440,216 450,220 C460,216 470,220 468,236 Z" fill="#F6D89A" stroke-width="3"/>'
    for dx in (436,452,468):
        s+=f'<path d="M{dx},196 c-5,-6 5,-10 0,-16" stroke="#fff" stroke-width="3"/>'
    s+=man(220,170,"squeeze")+legs(220,322)
    s+='<path d="M206,216 L178,262 L190,300"/><path d="M236,216 L262,262 L248,300"/>'
    s+=f'<path d="M256,128 q6,10 0,14 q-6,-4 0,-14 Z" fill="#fff" stroke-width="2.5"/><path d="M180,124 q6,10 0,14 q-6,-4 0,-14 Z" fill="#fff" stroke-width="2.5"/>'
    s+='<path d="M268,150 L410,224" stroke-dasharray="6 10" stroke-width="3"/>'
    s+=TAIL; open(OUT+"every-man-toast.svg","w").write(s)

    # 6. The buffet (The Collector and the Customer)
    s=head(W,H,"#FFD23F")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(190,190,"squeeze")+legs(190,342)
    s+='<path d="M176,236 L196,296 L240,300"/><path d="M206,236 L240,280 L300,300"/>'
    for i in range(7):
        y=296-i*24; dx=(i%2)*8-4+70
        s+=f'<ellipse cx="{200+dx}" cy="{y}" rx="44" ry="9" fill="#fff"/><path d="M{176+dx},{y-4} q24,-20 48,0" fill="{[RED,LIME,"#E8B66B",SHIRT,"#FF8C42",LIME,RED][i]}"/>'
    s+=man(480,190,"happy",shirt="#5A3E9B")+legs(480,342)
    s+='<path d="M466,236 L450,280 L486,292"/><path d="M496,236 L520,290"/>'
    s+=f'<ellipse cx="490" cy="290" rx="34" ry="8" fill="#fff"/><path d="M474,287 q16,-14 32,0" fill="{LIME}"/>'
    s+=TAIL; open(OUT+"collector-the-buffet.svg","w").write(s)

    # 7. Would you want to be the car? (The Test Drive)
    s=head(W,H,"#7B4FD6")
    s+='<line x1="30" y1="380" x2="650" y2="380" stroke="#fff"/>'
    s+=f'<path d="M150,330 L150,290 Q152,270 176,266 L220,232 Q230,224 250,224 L340,224 Q360,224 372,236 L406,266 Q440,270 444,292 L444,330 Z" fill="{RED}"/>'
    s+='<path d="M232,262 L254,238 L290,238 L290,262 Z" fill="#fff"/><path d="M306,262 L306,238 L350,238 L376,262 Z" fill="#fff"/>'
    s+=dot(272,252,5)+dot(330,252,5)+'<path d="M262,240 l16,6 M340,240 l-16,6" stroke-width="3"/>'
    s+='<path d="M286,300 q14,-10 28,0" stroke-width="4"/>'
    s+=f'<path d="M262,262 q-4,14 2,20" stroke="#7FD3FF" stroke-width="4"/>'
    s+='<circle cx="200" cy="332" r="26" fill="#333"/><circle cx="200" cy="332" r="10" fill="#ddd"/><circle cx="392" cy="332" r="26" fill="#333"/><circle cx="392" cy="332" r="10" fill="#ddd"/>'
    s+=man(560,170,"flat")+'<path d="M556,322 L540,378"/><path d="M574,322 L596,378"/>'
    s+='<path d="M546,216 L510,250 L470,254"/><path d="M574,216 L600,260"/>'
    s+=f'<circle cx="458" cy="256" r="9" fill="{YEL}"/><path d="M450,256 L430,256 M436,256 l0,6 M442,256 l0,6" stroke-width="4"/>'
    s+=TAIL; open(OUT+"test-drive-the-car.svg","w").write(s)

    # 8. The diving board (Should I Avoid Temptation?)
    s=head(W,H,"#7FD3FF")
    s+=f'<path d="M0,300 L680,300 L680,412 Q680,440 652,440 L28,440 Q0,440 0,412 Z" fill="#2F9BFF" stroke="none"/>'
    s+='<path d="M0,300 L680,300" stroke="#fff"/>'
    s+='<path d="M60,330 q20,-10 40,0 M300,350 q20,-10 40,0 M520,330 q20,-10 40,0" stroke="#fff" stroke-width="4"/>'
    s+='<rect x="40" y="240" width="60" height="60" fill="#ddd"/><rect x="60" y="270" width="220" height="14" fill="#fff"/>'
    s+=man(240,110,"squeeze")
    s+='<path d="M236,262 L228,268 L236,270 M254,262 L262,268 L254,270"/>'
    s+='<path d="M226,156 L196,190 L206,214"/><path d="M254,156 L284,190 L276,214"/>'
    for (x1,y1,x2,y2) in [(216,262,206,256),(270,262,280,256),(200,232,190,226),(286,232,296,226)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke-width="3"/>'
    s+=f'<path d="M276,70 q6,10 0,14 q-6,-4 0,-14 Z" fill="#fff" stroke-width="2.5"/><path d="M200,66 q6,10 0,14 q-6,-4 0,-14 Z" fill="#fff" stroke-width="2.5"/>'
    s+=TAIL; open(OUT+"temptation-diving-board.svg","w").write(s)

    # 9. The bird out of the broken snare (The Moment You Know)
    s=head(W,H,"#7FD3FF")
    s+='<path d="M0,360 L680,360 L680,412 Q680,440 652,440 L28,440 Q0,440 0,412 Z" fill="#43B85C" stroke="none"/><path d="M0,360 L680,360"/>'
    s+='<circle cx="560" cy="90" r="40" fill="#FFD23F" stroke="none"/>'
    s+='<path d="M150,360 L190,330 L230,360 M170,346 L210,346 M180,330 L176,360" stroke="#9C6B3C" stroke-width="5"/><path d="M230,360 L270,344 M120,360 L150,348" stroke="#9C6B3C" stroke-width="5"/>'
    s+='<path d="M196,326 l10,-10 M206,330 l14,-4" stroke="#9C6B3C" stroke-width="4"/>'
    s+=f'<path d="M392,186 L360,176 L366,196 Z" fill="{RED}"/>'
    s+=f'<ellipse cx="420" cy="180" rx="40" ry="24" fill="{RED}"/>'
    s+=f'<circle cx="462" cy="160" r="18" fill="{RED}"/>'+dot(466,156,3.5)
    s+=f'<path d="M478,158 l16,4 l-15,6 Z" fill="{YEL}"/>'
    s+=f'<path d="M408,174 C400,130 430,110 452,118 C440,140 436,160 432,176 Z" fill="#FF8FB1"/>'
    s+='<path d="M380,176 l-30,10 M376,190 l-34,4 M380,162 l-28,0" stroke="#fff" stroke-width="4"/>'
    s+='<path d="M210,320 Q300,250 390,180" stroke="#fff" stroke-width="3" stroke-dasharray="4 12"/>'
    s+=TAIL; open(OUT+"moment-the-broken-snare.svg","w").write(s)

    # 10. Let it ring (Let It Ring)
    s=head(W,H,"#FF8C42")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<path d="M150,410 L150,250 Q150,200 200,200 L300,200 Q350,200 350,250 L350,410" fill="#5A3E9B"/><rect x="130" y="290" width="240" height="70" rx="20" fill="#7B4FD6"/>'
    s+=man(250,190,"happy")
    s+='<path d="M246,342 L330,350 L340,408 M264,342 L340,340 L360,404"/>'
    s+='<path d="M236,236 L206,290 L240,300"/><path d="M266,236 L300,280 L290,300"/>'
    s+=f'<rect x="200" y="290" width="70" height="20" rx="4" fill="{SHIRT}"/>'.replace(SHIRT,"#FFF6E5")
    s+='<rect x="470" y="300" width="100" height="110" fill="#FFF6E5"/>'
    s+=f'<path d="M480,300 L486,270 Q520,256 554,270 L560,300 Z" fill="{INK}"/><path d="M482,268 Q520,240 558,268" stroke-width="10" stroke="{INK}"/>'
    for (d,r) in [(0,40),(0,60)]:
        s+=f'<path d="M{520-r},{250-r*0.4} q{r},-{r*0.7} {2*r},0" stroke="#fff" stroke-width="5"/>'
    s+='<path d="M456,240 l-12,-8 M584,240 l12,-8" stroke="#fff" stroke-width="5"/>'
    s+=TAIL; open(OUT+"let-it-ring-armchair.svg","w").write(s)

    # 11. The men still on the ship (The Men Still on the Ship)
    s=head(W,H,"#7FD3FF")
    s+='<path d="M0,250 L680,250 L680,330 L0,330 Z" fill="#2F9BFF" stroke="none"/>'
    s+='<path d="M0,330 L680,330 L680,412 Q680,440 652,440 L28,440 Q0,440 0,412 Z" fill="#F6D89A" stroke="none"/><path d="M0,330 Q340,318 680,330"/>'
    s+=f'<path d="M110,262 L430,262 L400,290 L140,290 Z" fill="#9C6B3C" transform="rotate(-6 270 276)"/>'
    s+='<path d="M90,272 q40,-12 80,0 q40,12 80,0 q40,-12 80,0 q40,12 80,0 q40,-12 80,0" stroke="#fff" stroke-width="5"/>'
    s+=f'<line x1="260" y1="262" x2="250" y2="150" stroke-width="6"/><path d="M252,160 L330,200 L256,236 Z" fill="#fff"/>'
    for x in (170,210,320,360):
        s+=f'<circle cx="{x}" cy="244" r="8" fill="#fff"/><line x1="{x}" y1="252" x2="{x}" y2="262" stroke-width="4"/>'
    s+=man(540,250,"flat")+'<path d="M536,402 L520,430"/><path d="M554,402 L572,430"/>'
    s+='<path d="M526,296 L504,336"/><path d="M554,296 L590,250 L600,226"/>'
    s+=TAIL; open(OUT+"ship-men-still-aboard.svg","w").write(s)

# ---- Fifth batch (later chapters). Run with:  python3 tools/draw_illustrations.py images/illustrations/ ----
def sofa(W=None):
    o=f'<rect x="120" y="226" width="440" height="80" rx="24" fill="#5A3E9B"/>'
    return o
def batch5(OUT):
    W,H=680,440
    HAIR="#9C6B3C"; SKIN="#FFE3C7"
    def phone(x,y,up):
        if up:
            return f'<rect x="{x}" y="{y}" width="26" height="46" rx="5" fill="{INK}"/><rect x="{x+4}" y="{y+5}" width="18" height="36" rx="2" fill="{GLOW}" stroke="none"/>'
        return f'<rect x="{x}" y="{y}" width="26" height="46" rx="5" fill="#3b3b3b"/><circle cx="{x+8}" cy="{y+8}" r="3" fill="{INK}" stroke-width="2"/>'
    def couch_scene(bg,up):
        s=head(W,H,bg)
        s+='<line x1="30" y1="410" x2="650" y2="410"/>'
        s+='<rect x="130" y="210" width="420" height="110" rx="30" fill="#5A3E9B"/>'
        s+=man(250,150,"happy" if up else "flat")
        # wife: hair behind head, yellow top
        s+=f'<path d="M{430-38},150 C{430-40},100 {430+40},100 {430+36},150 L{430+36},180 L{430-38},180 Z" fill="{HAIR}"/>'
        s+=man(430,150,"flat",YEL)
        s+=f'<path d="M{430-36},138 C{430-30},108 {430+30},108 {430+34},140 C{430+10},126 {430-16},128 {430-36},138 Z" fill="{HAIR}"/>'
        s+='<rect x="130" y="296" width="420" height="80" rx="22" fill="#7B4FD6"/>'
        s+='<rect x="100" y="250" width="44" height="126" rx="18" fill="#5A3E9B"/><rect x="536" y="250" width="44" height="126" rx="18" fill="#5A3E9B"/>'
        s+=phone(325,282,up).replace('y="282"','y="282"')
        s+='<path d="M238,356 L226,408"/><path d="M262,356 L282,408"/><path d="M418,356 L408,408"/><path d="M442,356 L460,408"/>'
        if up:
            s+='<path d="M406,206 L362,262 L346,284"/>'  # her hand resting, relaxed, not reaching
        else:
            s+='<path d="M406,206 L366,252 L350,280"/>'
            for (x1,y1,x2,y2) in [(258,206,244,190),(276,218,278,194),(292,236,312,222)]:
                s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="6"/>'
        return s+TAIL
    # 1. The Locked Door: phone face down, his chest jumps
    open(OUT+"locked-door-phone-face-down.svg","w").write(couch_scene("#FF8C42",False))
    # 2. Now: the same couch, phone face up, he hasn't given it a thought
    open(OUT+"now-phone-face-up.svg","w").write(couch_scene("#33C3D6",True))

    # 3. Beware of Cutting Down: a smaller meal is still a meal
    s=head(W,H,"#2EC4B6")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="60" y="330" width="560" height="22" rx="8" fill="#9C6B3C"/><line x1="110" y1="352" x2="110" y2="408"/><line x1="570" y1="352" x2="570" y2="408"/>'
    s+=monster(340,330,"dangle",1.5,stink=False)
    s+='<ellipse cx="340" cy="332" rx="190" ry="34" fill="#fff"/><ellipse cx="340" cy="332" rx="140" ry="22" fill="#FFF6E5" stroke-width="3.5"/>'
    s+=f'<ellipse cx="344" cy="330" rx="9" ry="6" fill="#D9A55B" stroke-width="3.5"/>'
    s+=TAIL; open(OUT+"cutting-down-one-crumb.svg","w").write(s)

    # 4. The First Weeks: the old bell rings and he lets it
    s=head(W,H,"#3A2A7A")
    s+=moon(600,70,18)+stars([(70,60),(160,110),(430,50),(650,170),(300,40)])
    s+='<line x1="30" y1="410" x2="650" y2="410" stroke="#fff"/>'
    s+='<rect x="60" y="320" width="380" height="60" rx="10" fill="#FFF6E5"/><line x1="80" y1="380" x2="80" y2="408"/><line x1="420" y1="380" x2="420" y2="408"/>'
    s+=f'<rect x="76" y="270" width="110" height="54" rx="18" fill="{YEL}"/>'
    s+='<circle cx="130" cy="268" r="34" fill="#fff"/>'+dot(122,262)+dot(140,262)+'<line x1="122" y1="282" x2="138" y2="282" stroke-width="3.5"/>'
    s+=f'<path d="M170,300 C170,276 200,276 230,282 L430,282 C440,282 440,334 430,334 L170,334 Z" fill="{SHIRT}"/>'
    s+='<rect x="470" y="330" width="130" height="78" rx="8" fill="#FFF6E5"/><line x1="488" y1="408" x2="488" y2="408"/>'
    s+=f'<path d="M505,330 C505,276 565,276 565,330 Z" fill="{YEL}"/><circle cx="535" cy="272" r="7" fill="{YEL}"/><circle cx="535" cy="338" r="7" fill="{YEL}"/>'
    for (x1,y1,x2,y2) in [(494,290,476,278),(488,312,466,312),(576,290,594,278),(582,312,604,312)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="#fff" stroke-width="5"/>'
    s+=TAIL; open(OUT+"first-weeks-the-bell.svg","w").write(s)

    # 5. If You Slip: clipped the eleventh, kept running
    s=head(W,H,"#6BCB77")
    s+='<line x1="30" y1="412" x2="650" y2="412"/><line x1="30" y1="428" x2="650" y2="428" stroke="#fff" stroke-width="3"/>'
    def hurdle(x): return f'<path d="M{x},412 L{x},340 M{x+70},412 L{x+70},340"/><rect x="{x-6}" y="326" width="82" height="16" rx="4" fill="#fff"/>'
    for x in (70,180): s+=hurdle(x)
    s+=f'<rect x="300" y="396" width="84" height="16" rx="4" fill="#fff" transform="rotate(-8 340 404)"/><path d="M384,408 L412,396 M300,404 L286,388"/>'
    s+=man(500,110,"flat")
    s+='<path d="M486,262 L450,330 L468,404"/><path d="M506,262 L560,310 L600,396"/>'
    s+='<path d="M486,170 L462,206 L478,236"/><path d="M510,170 L540,200 L526,232"/>'
    s+='<path d="M440,200 l-26,0 M436,230 l-34,0 M440,260 l-26,0" stroke="#fff" stroke-width="4"/>'
    s+=TAIL; open(OUT+"slip-hurdles-clipped-the-eleventh.svg","w").write(s)

    # 6. Do Not Negotiate: how many times he has to knock
    s=head(W,H,"#00A6A6")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<rect x="400" y="100" width="170" height="310" rx="8" fill="{YEL}"/><rect x="420" y="130" width="130" height="110" rx="6" stroke-width="3.5"/><rect x="420" y="262" width="130" height="120" rx="6" stroke-width="3.5"/>'
    s+='<circle cx="414" cy="270" r="9" fill="#fff"/>'
    s+=man(220,150,"flat")+legs(220,302,20)
    s+='<path d="M206,196 L186,250 L170,290"/><path d="M234,196 L330,210 L392,196"/>'
    s+=f'<circle cx="396" cy="194" r="11" fill="{SKIN}"/>'
    s+='<path d="M418,170 l12,-10 M420,200 l16,0 M418,230 l12,10" stroke="#fff" stroke-width="5"/>'
    for i in range(6):
        x=432+i*18
        s+=f'<line x1="{x}" y1="296" x2="{x}" y2="350" stroke="#fff" stroke-width="3.5"/>'
    s+='<line x1="426" y1="342" x2="534" y2="304" stroke="#fff" stroke-width="3.5"/>'
    s+=TAIL; open(OUT+"negotiate-knocking-on-the-door.svg","w").write(s)

    # 7. Can I Compartmentalize?: he won't stay in his room
    s=head(W,H,"#FF9F1C")
    s+='<rect x="20" y="110" width="640" height="280" fill="#FFF6E5" stroke="none"/><line x1="20" y1="390" x2="660" y2="390"/><line x1="20" y1="110" x2="660" y2="110"/>'
    for x in (350,490):
        s+=f'<rect x="{x}" y="180" width="90" height="210" rx="4" fill="#9C6B3C"/><circle cx="{x+72}" cy="290" r="5" fill="{YEL}"/>'
    s+=f'<rect x="60" y="180" width="110" height="210" rx="4" fill="{INK}"/><path d="M60,180 L22,196 L22,392 L60,390 Z" fill="#9C6B3C"/><circle cx="34" cy="290" r="4" fill="{YEL}"/>'
    for (x,y) in [(196,380),(232,372),(268,380)]:
        s+=f'<ellipse cx="{x}" cy="{y}" rx="11" ry="5" fill="{LIME}"/>'
    s+=monster(310,384,"dangle",1.05,stink=False)
    s+=TAIL; open(OUT+"compartment-down-the-hall.svg","w").write(s)

    # 8. The Man Led by a Woman: the lever sticking out of him
    s=head(W,H,"#FF6B6B")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(330,140,"flat",SHIRT)+'<path d="M322,292 L296,340 L270,406"/><path d="M342,292 L384,330 L420,402"/>'
    s+='<path d="M318,190 L292,224 L306,252"/><path d="M344,190 L370,228 L356,256"/>'
    s+=f'<path d="M306,226 L190,120" stroke-width="12"/><path d="M306,226 L190,120" stroke="{YEL}" stroke-width="5"/><circle cx="186" cy="116" r="14" fill="{RED}"/>'
    s+=f'<path d="M0,20 L90,70 L150,104 L136,126 L70,100 L0,70 Z" fill="#3b3b3b"/><circle cx="168" cy="102" r="16" fill="{SKIN}"/>'
    s+='<path d="M472,200 l36,0 M476,240 l44,0 M472,280 l36,0" stroke="#fff" stroke-width="4"/>'
    s+=TAIL; open(OUT+"led-by-woman-the-lever.svg","w").write(s)

    # 9. The Back Door: fruit juice and cola, same sugar
    s=head(W,H,"#FFE066")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<path d="M140,190 L260,190 L248,408 L152,408 Z" fill="#fff"/><path d="M144,230 L256,230 L248,408 L152,408 Z" fill="#FFA630"/>'
    s+=f'<path d="M410,170 Q410,160 430,160 L500,160 Q520,160 520,170 L520,408 L410,408 Z" fill="{RED}"/><rect x="410" y="250" width="110" height="60" fill="#fff" stroke-width="3.5"/><ellipse cx="465" cy="162" rx="55" ry="9" fill="#D9D9D9"/>'
    for (x,y) in [(170,376),(204,376),(187,344)]+[(60+0,0)][:0]:
        pass
    def cubes(x):
        return "".join(f'<rect x="{cx}" y="{cy}" width="30" height="30" rx="4" fill="#fff" stroke-width="4" transform="rotate({r} {cx+15} {cy+15})"/>' for (cx,cy,r) in [(x,376,-4),(x+34,376,5),(x+17,344,-6)])
    s+=cubes(266)+cubes(536)
    s+=TAIL; open(OUT+"back-door-juice-and-cola.svg","w").write(s)

# ---- Sixth batch (Introduction to chapter 4). ----
def batch6(OUT):
    W,H=680,440
    SKIN="#FFE3C7"; HAIR="#9C6B3C"
    # 1. Can You Be Trusted?: the soldier who shows up drunk
    s=head(W,H,"#5C7AEA")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<rect x="470" y="170" width="120" height="240" fill="#fff"/><path d="M470,170 L530,110 L590,170 Z" fill="{RED}"/>'
    s+=f'<rect x="470" y="250" width="120" height="40" fill="{RED}" stroke="none"/><rect x="470" y="170" width="120" height="240" fill="none"/>'
    s+='<rect x="500" y="300" width="60" height="110" fill="#3b3b3b"/>'
    # drunk soldier, leaning
    s+='<g transform="rotate(-12 260 400)">'
    s+=man(260,150,"blank","#4E7A12")
    s+=f'<path d="M224,138 C224,100 296,100 296,138 Z" fill="#4E7A12"/><rect x="220" y="134" width="80" height="8" rx="3" fill="#4E7A12"/>'
    s+='<path d="M246,302 L222,408"/><path d="M270,302 L306,404"/>'
    s+='<path d="M246,196 L216,240 L234,270"/><path d="M276,196 L318,230 L338,206"/>'
    s+=f'<rect x="330" y="180" width="26" height="46" rx="6" fill="#7A3E12" transform="rotate(25 343 203)"/><rect x="338" y="160" width="10" height="26" rx="3" fill="#7A3E12" transform="rotate(25 343 203)"/>'
    s+='</g>'
    s+=f'<circle cx="190" cy="100" r="7" fill="{YEL}" stroke="none"/><circle cx="330" cy="86" r="7" fill="{YEL}" stroke="none"/><circle cx="262" cy="64" r="7" fill="{YEL}" stroke="none"/>'
    # two worried small soldiers far right-back
    for x in (610,):
        pass
    s+=TAIL; open(OUT+"trusted-soldier-on-duty-drunk.svg","w").write(s)

    # 2. Can You Be Trusted?: a grown man, a Little Monster the size of a house cat
    s=head(W,H,"#FF8FB1")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<path d="M80,410 L80,270 Q80,230 120,230 L220,230 Q260,230 260,270 L260,410 Z" fill="#7B4FD6"/>'
    s+=man(150,190,"squeeze","#6B7A8F")
    s+=f'<path d="M110,290 L100,360 M190,290 L200,360" />'
    s+=f'<path d="M126,236 L108,214 L126,226 M180,236 L198,214 L178,228"/>'
    s+=monster(430,400,"tantrum",1.5,stink=False)
    # cat for size
    s+=f'<ellipse cx="560" cy="380" rx="42" ry="24" fill="#FFA630"/><circle cx="598" cy="356" r="19" fill="#FFA630"/><path d="M586,342 L588,322 L600,338 M606,340 L616,324 L614,346" fill="#FFA630"/>'
    s+=dot(592,354,3)+dot(606,354,3)+'<path d="M522,372 q-30,-30 -8,-52" stroke-width="7" stroke="#FFA630"/><path d="M522,372 q-30,-30 -8,-52" stroke-width="3"/>'
    s+=TAIL; open(OUT+"trusted-cat-sized-monster.svg","w").write(s)

    # 3. The Easy Method: the foot of the mountain
    s=head(W,H,"#9AD0FF")
    s+=f'<path d="M20,410 L330,60 L640,410 Z" fill="#8F7BD6"/><path d="M330,60 L290,110 L320,104 L338,124 L360,100 L388,112 Z" fill="#fff"/>'
    s+='<path d="M150,396 L470,350 L190,306 L440,266 L240,230 L400,196 L300,150" stroke="#F6D89A" stroke-width="7"/>'
    s+='<line x1="30" y1="412" x2="650" y2="412"/>'
    s+=man(110,230,"squeeze")+legs(110,382,16).replace('M','M',1)
    s+=f'<rect x="118" y="256" width="46" height="60" rx="10" fill="{RED}"/>'
    s+='<path d="M96,276 L122,350"/><path d="M122,278 L170,320"/>'
    s+=f'<path d="M84,214 q-12,10 -4,24 q8,-6 4,-24 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"easy-method-foot-of-the-mountain.svg","w").write(s)

    # 4. The Easy Method: tell a boy he can't have the cookie
    s=head(W,H,"#7FD3FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="330" y="150" width="300" height="16" rx="5" fill="#9C6B3C"/><line x1="360" y1="166" x2="360" y2="210"/><line x1="600" y1="166" x2="600" y2="210"/>'
    s+=f'<circle cx="480" cy="86" r="62" fill="#D9A55B"/>'
    for (x,y) in [(450,64),(500,52),(520,96),(468,110),(430,100),(496,128)]:
        s+=f'<circle cx="{x}" cy="{y}" r="8" fill="#5A3E1A"/>'
    s+=man(200,230,"squeeze")
    s+=f'<path d="M184,368 L172,408"/><path d="M206,368 L224,408"/>'
    s+='<path d="M186,270 L240,210 L300,150"/><path d="M210,270 L274,222 L330,166"/>'
    s+=f'<rect x="196" y="300" width="14" height="60" fill="none" stroke="none"/>'
    s+=TAIL; open(OUT+"easy-method-the-cookie.svg","w").write(s)

    # 5. The Easy Method: the bait and what's on the hook
    s=head(W,H,"#1FA2D8")
    s+='<path d="M0,70 Q85,50 170,70 T340,70 T510,70 T680,70 L680,60 L0,60 Z" fill="#fff" stroke="none"/>'
    s+='<line x1="460" y1="0" x2="460" y2="250" stroke="#fff" stroke-width="4"/>'
    s+=f'<path d="M460,250 L460,300 Q460,332 430,332 Q408,332 408,308" stroke-width="7"/><path d="M408,308 L398,290" stroke-width="7"/>'
    s+=f'<path d="M452,262 q18,10 4,22 q-14,12 4,24" stroke="#FF8FA3" stroke-width="12"/><path d="M452,262 q18,10 4,22 q-14,12 4,24" stroke="{INK}" stroke-width="2"/>'
    s+=f'<ellipse cx="200" cy="300" rx="80" ry="46" fill="#FFA630"/><path d="M120,300 L80,262 L80,338 Z" fill="#FFA630"/><path d="M200,256 L220,226 L246,262 Z" fill="#FFA630"/>'
    s+=f'<path d="M262,284 Q290,300 262,320 Z" fill="#fff" stroke-width="4"/>'+dot(244,288,5)
    s+='<path d="M170,270 q-14,30 0,60 M200,262 q-14,38 0,76" stroke-width="3.5"/>'
    s+='<path d="M60,160 q10,-10 20,0 M110,380 q8,-8 16,0" stroke="#fff" stroke-width="4"/>'
    s+=TAIL; open(OUT+"easy-method-bait-and-hook.svg","w").write(s)

    # 6. Who Is Telling You This: the ordinary evening
    s=head(W,H,"#FF8C42")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="90" y="220" width="300" height="100" rx="30" fill="#5A3E9B"/>'
    s+=man(240,150,"blank")
    s+='<rect x="90" y="296" width="300" height="80" rx="22" fill="#7B4FD6"/><rect x="66" y="250" width="40" height="126" rx="16" fill="#5A3E9B"/><rect x="374" y="250" width="40" height="126" rx="16" fill="#5A3E9B"/>'
    s+='<path d="M226,356 L216,408"/><path d="M254,356 L274,408"/>'
    s+='<path d="M230,196 L210,250 L246,262"/><path d="M256,196 L290,240 L262,262"/>'
    s+=f'<rect x="232" y="252" width="42" height="22" rx="8" fill="{INK}"/>'
    s+='<rect x="430" y="330" width="210" height="16" rx="5" fill="#9C6B3C"/><line x1="450" y1="346" x2="450" y2="408"/><line x1="620" y1="346" x2="620" y2="408"/>'
    s+='<path d="M446,262 L458,330 L492,330 L504,262 Z" fill="#FFA630" fill-opacity="0.85"/><rect x="446" y="256" width="58" height="10" rx="4" fill="#fff" fill-opacity="0.8"/>'
    s+='<path d="M520,330 L526,284 L580,284 L586,330 Z" fill="#D9A55B"/><path d="M528,286 l6,-20 l8,14 l6,-18 l8,18 l6,-14 l6,18 l8,-16 l4,18" fill="#FFD23F"/>'
    s+=f'<path d="M594,330 C594,290 640,290 640,330 Z" fill="#E2A24E"/><rect x="594" y="318" width="46" height="12" fill="#6BCB77"/><path d="M594,330 L640,330 L640,336 L594,336 Z" fill="#E2A24E"/>'
    s+=f'<rect x="530" y="230" width="36" height="52" rx="4" fill="#fff"/><circle cx="548" cy="248" r="8" fill="#9C6B3C"/><circle cx="548" cy="266" r="8" fill="#9C6B3C"/>'.replace('<rect x="530" y="230" width="36" height="52" rx="4" fill="#fff"/>','')
    s+=TAIL; open(OUT+"who-the-ordinary-evening.svg","w").write(s)

    # 7. Who Is Telling You This: thirteen ways to be anxious
    s=head(W,H,"#B388EB")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(340,200,"squeeze")+legs(340,352,16)
    s+=f'<path d="M326,246 L296,300 L328,320"/><path d="M352,246 L384,300 L350,320"/>'
    s+=f'<rect x="326" y="296" width="30" height="46" rx="5" fill="{INK}"/><rect x="330" y="301" width="22" height="36" rx="2" fill="{GLOW}" stroke="none"/>'
    s+=f'<path d="M300,174 q-14,10 -6,26 q10,-8 6,-26 Z" fill="#4FB3FF" stroke-width="2"/><path d="M384,170 q14,10 6,26 q-10,-8 -6,-26 Z" fill="#4FB3FF" stroke-width="2"/>'
    import math
    pts=[(90,70),(190,48),(300,40),(410,40),(520,52),(600,90),(60,170),(630,180),(72,270),(618,276),(130,340),(560,350),(240,360)]
    for (x,y) in pts[:13]:
        s+=f'<ellipse cx="{x}" cy="{y}" rx="36" ry="22" fill="#fff"/><path d="M{x-8},{y+18} l{-6 if x>340 else 6},14 l{14 if x>340 else -14},-12" fill="#fff"/>'
        s+=f'<circle cx="{x-12}" cy="{y}" r="3" fill="{INK}" stroke="none"/><circle cx="{x}" cy="{y}" r="3" fill="{INK}" stroke="none"/><circle cx="{x+12}" cy="{y}" r="3" fill="{INK}" stroke="none"/>'
    s+=TAIL; open(OUT+"who-thirteen-ways-to-be-anxious.svg","w").write(s)

    # 8. The Button: he'd break the nightstand
    s=head(W,H,"#1B2459")
    s+=moon(600,70,18)+stars([(80,60),(160,110),(470,50),(640,150),(300,40)])
    s+='<line x1="30" y1="410" x2="650" y2="410" stroke="#fff"/>'
    s+=man(130,150,"squeeze")+legs(130,302,18)
    s+='<path d="M118,196 L106,250 L90,290"/><path d="M144,196 L240,170 L320,214"/>'
    s+=f'<circle cx="324" cy="218" r="11" fill="{SKIN}"/>'
    s+='<rect x="280" y="290" width="260" height="22" rx="6" fill="#FFF6E5" transform="rotate(4 410 300)"/>'
    s+='<path d="M300,314 L296,408 M520,318 L534,404" stroke-width="7"/><rect x="340" y="320" width="130" height="50" rx="6" fill="#FFF6E5" transform="rotate(2 400 340)"/>'
    s+=f'<path d="M310,290 C310,256 350,256 350,290 Z" fill="{RED}" transform="translate(-4,10)"/>'
    s+=f'<rect x="440" y="206" width="70" height="44" rx="7" fill="{INK}" stroke="#fff" transform="rotate(-18 475 228)"/>'
    s+=f'<path d="M560,230 L540,280 L580,262 Z" fill="{YEL}" transform="rotate(30 560 250)"/>'
    for (x1,y1,x2,y2) in [(260,300,238,284),(262,326,236,336),(380,276,392,250),(430,284,452,262)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="6"/>'
    s+=TAIL; open(OUT+"button-he-would-break-the-nightstand.svg","w").write(s)

# ---- Seventh batch (chapters 4 to 7: The Empty House to The Flesh). ----
def house_front(x,y,w=300,h=300,body="#FFF6E5",roof=RED,door="#5A3E9B"):
    o=f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{body}"/>'
    o+=f'<path d="M{x-20},{y} L{x+w/2},{y-120} L{x+w+20},{y} Z" fill="{roof}"/>'
    return o
def plate(x,y,rx=34,ry=9): return f'<ellipse cx="{x}" cy="{y}" rx="{rx}" ry="{ry}" fill="#fff"/>'
def batch7(OUT):
    W,H=680,440
    # 1. The Empty House: he waits on the front step, his room still ready upstairs
    s=head(W,H,"#7FD3FF")
    s+=f'<circle cx="590" cy="70" r="34" fill="{YEL}" stroke="none"/>'
    s+='<rect x="30" y="380" width="620" height="40" fill="#6BCB77" stroke="none"/><line x1="30" y1="380" x2="650" y2="380"/>'
    s+=house_front(150,150,320,230)
    s+='<rect x="190" y="180" width="80" height="70" fill="#BFE3FF"/><line x1="230" y1="180" x2="230" y2="250"/>'
    # upstairs window: the room kept ready, a little made bed
    s+='<rect x="350" y="180" width="90" height="70" fill="#FFD23F"/><rect x="362" y="222" width="66" height="20" rx="5" fill="#FF8FB1"/><rect x="364" y="212" width="20" height="12" rx="4" fill="#fff"/>'
    s+='<rect x="282" y="276" width="62" height="104" fill="#5A3E9B"/>'+dot(332,330,4.5)
    s+='<rect x="262" y="372" width="102" height="14" fill="#C9B79C"/><rect x="250" y="386" width="126" height="14" fill="#C9B79C"/>'
    # the sulking monster on the step with a tiny suitcase
    s+=monster(326,374,"dangle",0.9,stink=True)
    s+=f'<rect x="392" y="348" width="44" height="34" rx="6" fill="{RED}"/><path d="M404,348 q10,-14 20,0" stroke-width="4"/>'
    s+=TAIL; open(OUT+"empty-house-front-step.svg","w").write(s)

    # 2. The Empty House: back inside with a bigger appetite and a stack of new plates
    s=head(W,H,"#FFD23F")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="120" y="300" width="440" height="20" rx="6" fill="#9C6B3C"/><line x1="150" y1="320" x2="150" y2="408"/><line x1="530" y1="320" x2="530" y2="408"/>'
    # tall wobbly stack of empty plates
    for i in range(9):
        s+=plate(430+(i%3-1)*3,292-i*16,44,11)
    for i in range(4):
        s+=plate(510+(i%2)*3,292-i*16,30,8)
    # monster banging a fork and spoon, tantrum, on a chair
    s+='<path d="M196,300 L196,180 Q245,150 294,180 L294,300 Z" fill="#7B4FD6"/>'
    s+=monster(245,300,"bang",1.1,stink=True)
    s+=f'<line x1="196" y1="294" x2="186" y2="254" stroke-width="5"/><path d="M180,252 l0,-16 M186,252 l0,-16 M192,252 l0,-16" stroke-width="3"/>'
    s+=f'<line x1="294" y1="294" x2="304" y2="254" stroke-width="5"/><ellipse cx="306" cy="244" rx="8" ry="11" fill="#fff"/>'
    for (x1,y1,x2,y2) in [(160,200,140,186),(330,196,350,180),(150,240,128,244),(340,236,362,238)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+=TAIL; open(OUT+"empty-house-stack-of-plates.svg","w").write(s)

def batch8(OUT):
    W,H=680,440
    # 1. Why Is It Difficult to Stop?: he says no, and his own thumb unlocks the phone
    s=head(W,H,"#1B2459")
    s+=moon(600,70,18)+stars([(80,60),(170,40),(470,50),(640,160),(330,30)])
    s+='<line x1="30" y1="410" x2="650" y2="410" stroke="#fff"/>'
    s+=man(250,170,"squeeze")+legs(250,322,18)
    for dx in (-60,60):
        s+=f'<path d="M{250+dx},150 q{dx//6},20 0,40" stroke="#fff" stroke-width="4"/>'
    s+='<path d="M236,216 L210,280 L236,310"/>'
    s+='<path d="M266,216 L340,236 L400,196"/>'
    s+=f'<rect x="392" y="140" width="46" height="78" rx="8" fill="{INK}" transform="rotate(12 415 179)"/><rect x="398" y="148" width="34" height="62" rx="3" fill="{GLOW}" stroke="none" transform="rotate(12 415 179)"/>'
    s+=f'<circle cx="402" cy="196" r="11" fill="#FFE3C7"/>'
    for (x1,y1,x2,y2) in [(456,150,480,138),(458,180,486,182),(450,212,474,226)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="5"/>'
    s+=TAIL; open(OUT+"difficult-thumb-unlocks-the-phone.svg","w").write(s)

    # 2. Why Is It Difficult to Stop?: a stone in his pocket all day
    s=head(W,H,"#6BCB77")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    for x in (90,170):
        s+=f'<rect x="{x}" y="120" width="60" height="290" fill="#BFE3FF"/>'
    s+=f'<rect x="520" y="90" width="110" height="320" fill="#BFE3FF"/>'
    s+='<g transform="rotate(8 340 400)">'
    s+=man(330,150,"blank","#4A4A68")
    s+='<path d="M326,302 L300,404"/><path d="M344,302 L376,404"/>'
    s+=f'<path d="M318,196 L290,260"/><rect x="262" y="256" width="58" height="40" rx="6" fill="#9C6B3C"/>'
    s+='<path d="M348,196 L370,258"/>'
    s+='</g>'
    s+=f'<path d="M352,262 C330,262 330,330 362,340 C400,350 420,300 402,270 C392,254 370,258 352,262 Z" fill="#9A9A9A"/>'
    s+='<path d="M366,282 q10,-6 18,4 M360,312 q12,4 20,-4" stroke-width="3"/>'
    s+=f'<path d="M300,120 q-14,10 -6,26 q10,-8 6,-26 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"difficult-stone-in-his-pocket.svg","w").write(s)

    # 3. Why Is It Difficult to Stop?: worse things in a dentist's waiting room
    s=head(W,H,"#9AD0FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="30" y="150" width="620" height="16" fill="#FFF6E5"/><line x1="30" y1="150" x2="650" y2="150"/><line x1="30" y1="166" x2="650" y2="166"/>'
    s+=monster(470,150,"bang",0.75)
    for (x1,y1,x2,y2) in [(410,176,396,196),(470,178,470,202),(530,176,544,196)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="5"/>'
    # chairs
    for x in (120,420):
        s+=f'<rect x="{x}" y="320" width="130" height="18" rx="6" fill="#FFA630"/><rect x="{x}" y="250" width="18" height="88" rx="6" fill="#FFA630"/><line x1="{x+20}" y1="338" x2="{x+20}" y2="408"/><line x1="{x+120}" y1="338" x2="{x+120}" y2="408"/>'
    s+=man(200,214,"happy")
    s+='<path d="M196,366 L240,370 L250,408"/><path d="M214,366 L262,360 L274,408"/>'
    s+=f'<path d="M186,262 L210,300"/><path d="M216,262 L240,300"/><rect x="190" y="282" width="70" height="46" rx="4" fill="#fff" transform="rotate(-8 225 305)"/><line x1="225" y1="284" x2="227" y2="326" stroke-width="3" transform="rotate(-8 225 305)"/>'
    # the drill on a tray in the back
    s+=f'<rect x="520" y="230" width="90" height="10" rx="4" fill="#ccc"/><line x1="565" y1="240" x2="565" y2="408"/><path d="M540,230 L540,200 L580,190" stroke-width="5"/>'
    s+=TAIL; open(OUT+"difficult-dentist-waiting-room.svg","w").write(s)

def batch9(OUT):
    W,H=680,440
    # 1. A Master, Not a Habit: the light switch on the wrong wall
    s=head(W,H,"#FFA630")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="60" y="40" width="250" height="370" fill="#FFF6E5"/><rect x="370" y="40" width="250" height="370" fill="#FFE3C7"/>'
    s+=f'<rect x="520" y="200" width="30" height="46" rx="5" fill="#fff"/><rect x="530" y="210" width="10" height="18" rx="3" fill="{INK}"/>'
    s+=man(250,190,"squeeze")+legs(250,342,16)
    s+='<path d="M236,236 L200,200 L176,214"/>'
    s+='<path d="M264,236 L300,290"/>'
    s+=f'<circle cx="172" cy="216" r="12" fill="#FFE3C7"/>'
    for (x1,y1,x2,y2) in [(150,190,134,176),(146,216,126,216),(150,242,134,256)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+=f'<path d="M560,180 q20,-20 30,0" stroke="{INK}" stroke-width="4"/>'
    s+=TAIL; open(OUT+"master-the-light-switch.svg","w").write(s)

    # 2. A Master, Not a Habit: the pipsqueak on a throne, served on a tray
    s=head(W,H,"#B388EB")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<path d="M420,410 L420,200 L450,150 L480,190 L510,140 L540,190 L570,150 L600,200 L600,410 Z" fill="{RED}"/>'
    s+=f'<rect x="440" y="300" width="140" height="30" rx="6" fill="{YEL}"/>'
    s+=monster(510,300,"bang",1.0,stink=True)
    s+=f'<path d="M490,236 L496,214 L506,228 L514,208 L522,228 L532,214 L536,236 Z" fill="{YEL}" stroke-width="3.5"/>'
    s+=man(220,170,"blank")+legs(220,322,16)
    s+='<path d="M206,216 L250,270 L300,262"/><path d="M234,216 L280,250 L320,248"/>'
    s+=f'<rect x="290" y="240" width="90" height="10" rx="4" fill="#ccc"/><path d="M304,240 C304,206 366,206 366,240 Z" fill="#ddd"/><circle cx="335" cy="204" r="5" fill="#ddd"/>'
    s+=f'<path d="M170,150 q-14,10 -6,26 q10,-8 6,-26 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"master-the-pipsqueak-king.svg","w").write(s)

    # 3. The Flesh: he steps into the shower, and upstairs the banging starts
    s=head(W,H,"#7FD3FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="30" y="140" width="620" height="16" fill="#FFF6E5"/><line x1="30" y1="140" x2="650" y2="140"/><line x1="30" y1="156" x2="650" y2="156"/>'
    s+=monster(330,140,"bang",0.75)
    for (x1,y1,x2,y2) in [(270,166,256,186),(330,168,330,192),(390,166,404,186)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="5"/>'
    s+='<rect x="380" y="200" width="200" height="210" fill="#E6F6FF"/><path d="M380,200 L380,410" stroke-width="5"/>'
    s+='<path d="M560,180 L560,215 L520,215" stroke-width="6"/><circle cx="512" cy="222" r="14" fill="#ccc"/>'
    for (x,y) in [(500,250),(520,270),(490,290),(530,300),(510,320),(486,340)]:
        s+=f'<line x1="{x}" y1="{y}" x2="{x-4}" y2="{y+14}" stroke="#4FB3FF" stroke-width="4"/>'
    s+=f'<path d="M120,410 L120,300 Q120,280 140,280 L180,280 L180,410" fill="#fff"/>'
    s+=man(300,236,"blank","#fff")
    s+='<path d="M296,388 L280,408 M314,388 L330,408" stroke-width="5"/>'
    s+='<path d="M286,282 L258,330"/><path d="M314,282 L380,300"/>'
    s+=f'<path d="M262,226 q-12,8 -6,22 q9,-7 6,-22 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"flesh-the-shower-cue.svg","w").write(s)

def tough(tx,ty,col,sc=1.0,extra=""):
    """A bigger, 'tougher' little spirit: squat body, unibrow scowl, tiny flexed arms, still cute."""
    o=f'<g transform="translate({tx},{ty}) scale({sc})">'
    # flexing arms with tiny biceps
    o+=f'<path d="M-34,-30 Q-50,-36 -48,-56" /><circle cx="-46" cy="-50" r="7" fill="{col}"/><circle cx="-48" cy="-60" r="6" fill="{col}"/>'
    o+=f'<path d="M34,-30 Q50,-36 48,-56" /><circle cx="46" cy="-50" r="7" fill="{col}"/><circle cx="48" cy="-60" r="6" fill="{col}"/>'
    o+=f'<path d="M-36,-6 C-40,-44 -22,-70 0,-70 C22,-70 40,-44 36,-6 C33,4 -33,4 -36,-6 Z" fill="{col}"/>'
    o+='<path d="M-6,-69 q2,-12 7,-3 q4,-11 8,1" stroke-width="4"/>'
    # unibrow scowl, small eyes, pouty mouth
    o+='<path d="M-20,-50 L-2,-44 L2,-44 L20,-50" stroke-width="5"/>'
    o+=dot(-10,-38,4)+dot(10,-38,4)
    o+='<path d="M-8,-20 q8,-7 16,0" stroke-width="4"/>'
    o+=f'<ellipse cx="-14" cy="2" rx="10" ry="6" fill="{col}"/><ellipse cx="14" cy="2" rx="10" ry="6" fill="{col}"/>'
    o+=extra
    return o+'</g>'

def batch10(OUT):
    W,H=680,440
    # 1. The Empty House: the spirit comes back with seven tougher pals
    s=head(W,H,"#FFD23F")
    s+='<rect x="30" y="300" width="620" height="120" fill="#6BCB77" stroke="none"/><line x1="30" y1="300" x2="650" y2="300"/>'
    s+=house_front(560,180,90,120)
    s+='<rect x="590" y="240" width="32" height="60" fill="#5A3E9B"/>'
    cols=["#FF7A59","#7B4FD6","#2FB3A8","#FF5FA2","#4F7BFF","#E8A33D","#8B5E3C"]
    shades='<path d="M-30,-56 L30,-56" stroke="#141414" stroke-width="8"/><rect x="-22" y="-46" width="18" height="12" rx="3" fill="#141414"/><rect x="4" y="-46" width="18" height="12" rx="3" fill="#141414"/>'
    plaster='<rect x="8" y="-32" width="18" height="9" rx="2" fill="#fff" transform="rotate(-20 17 -28)"/>'
    band='<rect x="-38" y="-24" width="76" height="8" fill="#fff" stroke-width="3"/>'
    back=[(150,300,1.15,cols[1],''),(260,296,1.2,cols[2],band),(370,300,1.15,cols[4],'')]
    front=[(100,404,1.35,cols[0],plaster),(215,410,1.4,cols[3],shades),(330,406,1.35,cols[5],''),(445,410,1.4,cols[6],band)]
    for (x,y,sc,c,e) in back+front:
        s+=tough(x,y,c,sc,e)
    # the original Little Monster struts in front of them with a tiny flag, like he's in charge
    s+=monster(560,400,"bang",0.8,stink=True)
    s+=f'<line x1="596" y1="372" x2="596" y2="310"/><path d="M596,310 L630,322 L596,336 Z" fill="{RED}"/>'
    s+=TAIL; open(OUT+"empty-house-seven-tough-spirits.svg","w").write(s)

    # 2. The Empty House: swept and tidy, his room kept ready, door open
    s=head(W,H,"#FF8FB1")
    s+='<rect x="60" y="60" width="560" height="350" fill="#FFF6E5"/><line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="460" y="150" width="110" height="260" fill="#5A3E9B"/><path d="M460,150 L420,170 L420,400 L460,410 Z" fill="#fff"/>'
    s+='<rect x="110" y="320" width="200" height="40" rx="8" fill="#FF8FB1"/><rect x="100" y="290" width="20" height="120" rx="6" fill="#9C6B3C"/><rect x="118" y="304" width="56" height="22" rx="8" fill="#fff"/><line x1="130" y1="360" x2="130" y2="408"/><line x1="300" y1="360" x2="300" y2="408"/>'
    s+=f'<rect x="150" y="150" width="90" height="70" fill="{YEL}"/><path d="M162,190 q15,-20 30,0 q15,-20 30,0" stroke-width="3"/>'
    s+='<line x1="372" y1="160" x2="396" y2="380" stroke-width="7" stroke="#9C6B3C"/><path d="M380,370 L360,408 L420,408 L410,368 Z" fill="#E8A33D"/>'
    for (x,y) in [(250,396),(330,398),(200,394)]:
        s+=f'<path d="M{x},{y} l6,-10 l6,10 l-6,-4 Z" fill="#fff" stroke-width="2"/>'
    for (x,y) in [(100,100),(560,110),(330,90)]:
        s+=f'<path d="M{x},{y-12} L{x+3},{y-3} L{x+12},{y} L{x+3},{y+3} L{x},{y+12} L{x-3},{y+3} L{x-12},{y} L{x-3},{y-3} Z" fill="{YEL}" stroke-width="2.5"/>'
    s+=TAIL; open(OUT+"empty-house-swept-and-ready.svg","w").write(s)

    # 3. The Empty House: look first (the man studies the pouting pipsqueak through a magnifying glass)
    s=head(W,H,"#9AD0FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(230,170,"blank")+legs(230,322,16)
    s+='<path d="M216,216 L190,280"/><path d="M246,216 L320,250 L360,262"/>'
    s+='<line x1="360" y1="262" x2="388" y2="282" stroke-width="8" stroke="#9C6B3C"/><circle cx="420" cy="306" r="40" fill="#E6F6FF" fill-opacity="0.7" stroke-width="7"/>'
    s+=monster(470,408,"dangle",1.0,stink=True)
    s+=TAIL; open(OUT+"empty-house-look-first.svg","w").write(s)

def batch11(OUT):
    W,H=680,440
    # 2. The Flesh: a hijacking, and the plane lands nowhere
    s=head(W,H,"#F6C26B")
    s+=f'<circle cx="580" cy="70" r="36" fill="{YEL}" stroke="none"/>'
    s+='<path d="M30,360 Q170,340 330,360 T650,350 L650,410 L30,410 Z" fill="#E8A33D"/>'
    s+='<path d="M120,330 l0,-50 M120,300 l-14,-10 M120,310 l14,-12" stroke-width="5" stroke="#4E7A12"/>'
    s+='<g transform="rotate(12 360 220)">'
    s+='<path d="M200,220 Q200,190 240,190 L470,190 Q520,190 530,220 Q520,250 470,250 L240,250 Q200,250 200,220 Z" fill="#fff"/>'
    s+=f'<path d="M330,190 L300,120 L340,120 L390,190 Z" fill="{SHIRT}"/><path d="M330,250 L300,310 L340,310 L390,250 Z" fill="{SHIRT}"/><path d="M220,190 L200,150 L230,150 L250,190 Z" fill="{SHIRT}"/>'
    for x in (300,340,380,420):
        s+=f'<circle cx="{x}" cy="215" r="9" fill="{GLOW}"/>'
    s+=f'<path d="M470,200 Q500,200 515,218 L470,218 Z" fill="{GLOW}"/>'
    s+='</g>'
    s+=monster(488,236,"bang",0.42,stink=False)
    for (x1,y1,x2,y2) in [(560,240,590,236),(556,262,586,270)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+=TAIL; open(OUT+"flesh-the-hijacked-plane.svg","w").write(s)

    # 3. The Little Monster: one diet, one small belly
    s=head(W,H,"#2FB3A8")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=monster(340,378,"bang",1.5,stink=True)
    s+=f'<ellipse cx="340" cy="366" rx="32" ry="17" fill="{LIME}" stroke-width="4"/>'
    s+=plate(110,392,62,14)+f'<rect x="92" y="352" width="36" height="34" rx="6" fill="{INK}" transform="rotate(-70 110 369)"/><rect x="98" y="358" width="24" height="22" rx="3" fill="{GLOW}" stroke="none" transform="rotate(-70 110 369)"/>'
    s+=plate(240,398,62,14)+'<path d="M208,384 Q240,360 272,384 Q240,408 208,384 Z" fill="#fff"/><circle cx="240" cy="384" r="9" fill="'+SHIRT+'"/>'+dot(240,384,4)
    s+=plate(440,398,62,14)+'<path d="M412,384 q-6,-22 16,-22 q6,-16 26,-6 q20,-6 22,14 q14,8 -2,18 Z" fill="#fff"/>'
    s+=plate(570,392,62,14)+f'<path d="M546,380 l12,-14 l12,14 l12,-14 l12,14" stroke="{RED}" stroke-width="5"/>'
    s+=TAIL; open(OUT+"little-monster-one-small-belly.svg","w").write(s)

    # 4. The Little Monster: licking the photograph on the menu
    s=head(W,H,"#FF8C42")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="250" y="80" width="230" height="300" rx="10" fill="#FFF6E5" transform="rotate(-6 365 230)"/>'
    s+='<g transform="rotate(-6 365 230)"><rect x="280" y="110" width="170" height="120" fill="#BFE3FF"/>'+plate(365,200,62,14)+'<path d="M325,196 C320,160 410,160 405,196 Z" fill="#B5542B"/><path d="M340,180 q25,-10 50,0" stroke="#fff" stroke-width="3"/>'
    for y in (260,286,312,338):
        s+=f'<line x1="290" y1="{y}" x2="440" y2="{y}" stroke-width="4" stroke="#bbb"/>'
    s+='</g>'
    s+=monster(200,330,"dangle",1.3,stink=True)
    s+='<path d="M210,300 q40,-40 90,-110" stroke="#FF8FA3" stroke-width="12"/><path d="M210,300 q40,-40 90,-110" stroke-width="2"/>'
    s+=TAIL; open(OUT+"little-monster-licking-the-menu.svg","w").write(s)

    # 5. The Little Monster: the firefighter who lit the fire (works back to front)
    s=head(W,H,"#1B2459")
    s+='<line x1="30" y1="410" x2="650" y2="410" stroke="#fff"/>'
    s+='<rect x="380" y="200" width="200" height="210" fill="#FFF6E5"/><path d="M360,200 L480,110 L600,200 Z" fill="#9C6B3C"/>'
    s+='<rect x="440" y="260" width="70" height="60" fill="#FFD23F"/>'
    s+=f'<path d="M450,260 q10,-40 20,-10 q8,-40 24,-6 q10,-30 14,16 Z" fill="{RED}"/><path d="M462,260 q6,-20 12,-4 q6,-20 14,2 Z" fill="{YEL}"/>'
    s+=monster(220,404,"bang",1.2,stink=False)
    s+=f'<path d="M184,336 L190,316 L250,316 L256,336 Z" fill="{RED}"/><rect x="176" y="334" width="88" height="10" rx="4" fill="{RED}"/>'
    s+=f'<line x1="170" y1="396" x2="150" y2="340" stroke-width="5"/><path d="M146,338 q4,-16 8,0 Z" fill="{RED}" stroke-width="2"/>'
    s+=f'<path d="M272,390 Q330,380 360,320" stroke="#4FB3FF" stroke-width="10"/><path d="M360,320 l10,-14" stroke="#4FB3FF" stroke-width="4"/>'
    s+=TAIL; open(OUT+"little-monster-firefighter-with-a-match.svg","w").write(s)

    # 6. But It Feels Good: the bird on the giant plaster egg
    s=head(W,H,"#9AD0FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<ellipse cx="190" cy="380" rx="90" ry="24" fill="#C9A26B"/>'
    for (x,y) in [(160,372),(190,376),(220,372)]:
        s+=f'<ellipse cx="{x}" cy="{y}" rx="14" ry="18" fill="#BFE3FF"/>'
    s+='<ellipse cx="450" cy="300" rx="130" ry="110" fill="#FFF6E5"/>'
    for (x,y,r) in [(400,260,16),(480,240,12),(500,320,18),(420,340,12),(450,290,9),(540,280,10)]:
        s+=f'<circle cx="{x}" cy="{y}" r="{r}" fill="{SHIRT}" stroke="none"/>'
    s+='<g transform="rotate(-35 520 190)"><ellipse cx="520" cy="190" rx="34" ry="24" fill="#FF7A59"/><circle cx="548" cy="172" r="16" fill="#FF7A59"/><path d="M562,170 L580,176 L562,180 Z" fill="'+YEL+'"/>'+dot(552,168,3.5)+'<path d="M500,186 q-14,-20 -26,-8" fill="#FF7A59"/><path d="M510,212 L506,232 M528,212 L530,232" stroke-width="4"/></g>'
    for (x1,y1,x2,y2) in [(590,230,610,250),(596,200,620,206)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{INK}" stroke-width="4"/>'
    s+=TAIL; open(OUT+"feels-good-the-plaster-egg.svg","w").write(s)

    # 7. But It Feels Good: nobody sneaks a glass of orange juice
    s=head(W,H,"#1B2459")
    s+=moon(600,70,18)+stars([(80,60),(170,40),(470,50),(330,30)])
    s+='<line x1="30" y1="410" x2="650" y2="410" stroke="#fff"/>'
    s+='<rect x="430" y="170" width="160" height="240" rx="10" fill="#E6F6FF"/><path d="M430,170 L380,190 L380,400 L430,410 Z" fill="#fff"/>'
    s+=f'<path d="M430,180 L120,400 L590,400 Z" fill="{YEL}" fill-opacity="0.55" stroke="none"/>'
    s+=man(240,170,"squeeze")+'<path d="M236,322 L210,400 L196,404"/><path d="M254,322 L282,396 L296,392"/>'
    s+='<path d="M262,230 L310,250 L330,226"/><path d="M234,220 L190,190 L176,160"/>'
    s+='<rect x="320" y="190" width="26" height="40" rx="3" fill="#FFA630" fill-opacity="0.9"/><rect x="320" y="186" width="26" height="8" fill="#fff" stroke-width="3"/>'
    s+=f'<path d="M168,162 q-6,-8 2,-12 q10,4 4,12" stroke-width="3"/>'
    s+=TAIL; open(OUT+"feels-good-sneaking-orange-juice.svg","w").write(s)

    # 8. But It Feels Good: the price goes up, the portion goes down
    s=head(W,H,"#B388EB")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="80" y="300" width="520" height="18" rx="6" fill="#9C6B3C"/><line x1="110" y1="318" x2="110" y2="408"/><line x1="570" y1="318" x2="570" y2="408"/>'
    s+=plate(250,290,110,22)+f'<circle cx="250" cy="284" r="6" fill="#B5542B"/>'
    s+='<path d="M440,286 L440,60 L520,60 L520,286" fill="#fff"/>'
    for y in range(80,280,22):
        s+=f'<line x1="452" y1="{y}" x2="{500 if y%44 else 490}" y2="{y}" stroke-width="3" stroke="#999"/>'
    s+=f'<path d="M440,286 l10,-10 l10,10 l10,-10 l10,10 l10,-10 l10,10 l10,-10 l10,10" fill="#fff"/>'
    s+=man(150,170,"squeeze")
    s+='<path d="M164,216 L200,262 L232,276"/><line x1="232" y1="276" x2="246" y2="282" stroke-width="3"/>'
    s+=f'<path d="M118,150 q-14,10 -6,26 q10,-8 6,-26 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"feels-good-tiny-portion-long-bill.svg","w").write(s)

def tree(x,y,fruit=True):
    o=f'<rect x="{x-14}" y="{y-150}" width="28" height="150" fill="#9C6B3C"/>'
    o+=f'<circle cx="{x}" cy="{y-200}" r="80" fill="#4FAF4F"/><circle cx="{x-60}" cy="{y-160}" r="44" fill="#4FAF4F"/><circle cx="{x+60}" cy="{y-160}" r="44" fill="#4FAF4F"/>'
    if fruit:
        for (dx,dy) in [(-30,-220),(20,-240),(40,-180),(-50,-170),(0,-190),(70,-150),(-75,-140)]:
            o+=f'<circle cx="{x+dx}" cy="{y+dy}" r="11" fill="{RED}"/>'
    return o

def batch12(OUT):
    W,H=680,440
    # 1. Crossing the Red Line: the tug of war, and you're the rope
    s=head(W,H,"#7FD3FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(340,170,"squeeze")+legs(340,322,14)
    s+='<path d="M90,316 L320,300" stroke="#C9A26B" stroke-width="9"/><path d="M360,300 L560,350" stroke="#C9A26B" stroke-width="9"/>'
    s+='<path d="M90,316 L320,300 M360,300 L560,350" stroke-width="2"/>'
    s+='<path d="M326,216 L300,250 L320,296"/><path d="M354,216 L380,250 L360,296"/>'
    s+=monster(580,404,"bang",1.0,stink=True)
    s+='<path d="M60,330 C40,300 70,280 90,300 C110,280 140,300 120,330 L90,370 Z" fill="#FF5FA2"/>'
    s+=dot(80,316,3.5)+dot(102,316,3.5)+'<path d="M82,334 q10,6 20,0" stroke-width="3"/><path d="M80,370 L72,404 M100,370 L108,404" stroke-width="4"/>'
    for (x1,y1,x2,y2) in [(300,120,286,104),(340,110,340,90),(380,120,394,104)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+=TAIL; open(OUT+"red-line-tug-of-war.svg","w").write(s)

    # 2. Crossing the Red Line: toes on the red line
    s=head(W,H,"#FFD23F")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<line x1="400" y1="380" x2="400" y2="420" stroke="{RED}" stroke-width="12"/><rect x="380" y="396" width="270" height="14" fill="{RED}" fill-opacity="0.3" stroke="none"/>'
    s+=man(350,180,"blank")+'<path d="M346,332 L380,404 L398,404"/><path d="M364,332 L392,398 L404,398"/>'
    s+='<path d="M336,226 L316,290"/><path d="M366,226 L388,290"/>'
    s+=monster(240,404,"bang",0.9,stink=True)
    s+='<path d="M282,360 L312,330" stroke-width="5"/>'
    s+=TAIL; open(OUT+"red-line-toes-on-the-line.svg","w").write(s)

    # 3. Crossing the Red Line: the medicine that does everything (there's no such medicine)
    s=head(W,H,"#B388EB")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<rect x="250" y="130" width="180" height="270" rx="26" fill="#FFA630"/><rect x="270" y="90" width="140" height="50" rx="8" fill="#fff"/>'
    s+='<rect x="275" y="190" width="130" height="150" rx="10" fill="#fff"/>'
    s+=f'<circle cx="310" cy="230" r="16" fill="{YEL}"/>'+moon(370,232,16)
    s+=f'<path d="M296,300 l14,-24 l14,24 Z" fill="{SHIRT}"/><path d="M356,276 l14,24 l14,-24 Z" fill="{SHIRT}"/>'
    s+=f'<path d="M210,110 L470,420" stroke="{RED}" stroke-width="14"/>'
    s+=TAIL; open(OUT+"red-line-no-such-medicine.svg","w").write(s)

    # 4. Good News, Twice: the camping trip, sleeping like a log
    s=head(W,H,"#1B2459")
    s+=moon(590,70,20)+stars([(80,60),(170,40),(470,50),(330,30),(250,90)])
    s+='<rect x="30" y="360" width="620" height="50" fill="#2E6B3A" stroke="none"/><line x1="30" y1="360" x2="650" y2="360" stroke="#fff"/>'
    s+=f'<path d="M150,360 L300,150 L450,360 Z" fill="{RED}"/><path d="M300,150 L270,360 L330,360 Z" fill="#7a1f1a"/>'
    s+='<rect x="210" y="320" width="180" height="34" rx="16" fill="'+SHIRT+'"/><circle cx="196" cy="334" r="22" fill="#fff"/><path d="M186,330 q5,4 10,0 M200,330 q5,4 10,0" stroke-width="3"/>'
    for (x,y,f) in [(380,200,22),(410,170,28),(446,136,34)]:
        s+=f'<text x="{x}" y="{y}" font-family="sans-serif" font-weight="bold" font-size="{f}" fill="#fff" stroke="none">z</text>'
    s+=f'<path d="M530,360 l12,-30 l12,30 Z" fill="#FFA630"/><path d="M536,346 q6,-26 12,0" fill="{YEL}" stroke="none"/>'
    s+=TAIL; open(OUT+"good-news-the-camping-trip.svg","w").write(s)

    # 5. Good News, Twice: home again, and he's banging before you've unpacked
    s=head(W,H,"#FF8C42")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="30" y="150" width="620" height="16" fill="#FFF6E5"/><line x1="30" y1="150" x2="650" y2="150"/><line x1="30" y1="166" x2="650" y2="166"/>'
    s+=monster(420,150,"bang",0.8)
    for (x1,y1,x2,y2) in [(360,176,346,196),(420,178,420,202),(480,176,494,196)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{YEL}" stroke-width="5"/>'
    s+='<rect x="90" y="220" width="100" height="190" fill="#5A3E9B"/>'
    s+=man(280,240,"blank")+'<path d="M276,392 L262,408 M294,392 L306,408" stroke-width="5"/>'
    s+=f'<path d="M296,286 L330,330"/><rect x="320" y="320" width="80" height="60" rx="8" fill="{RED}"/><path d="M342,320 q18,-16 36,0" stroke-width="4"/>'
    s+='<path d="M264,286 L240,330"/>'
    s+=TAIL; open(OUT+"good-news-home-again.svg","w").write(s)

    # 6. Good News, Twice: grass grows back
    s=head(W,H,"#9AD0FF")
    s+=f'<circle cx="590" cy="70" r="34" fill="{YEL}" stroke="none"/>'
    s+='<path d="M30,250 L650,250 L650,410 L30,410 Z" fill="#6BCB77"/>'
    s+='<path d="M80,410 C200,360 300,330 380,300 C460,270 560,262 640,256 L640,270 C560,278 470,290 390,318 C310,346 220,380 120,410 Z" fill="#B98A55" fill-opacity="0.45"/>'
    for (x,y) in [(150,388),(200,372),(250,356),(300,338),(350,320),(400,304),(450,290),(500,280),(550,272),(600,266)]:
        s+=f'<path d="M{x},{y} l-6,-14 M{x},{y} l0,-18 M{x},{y} l6,-14" stroke="#2E8B3A" stroke-width="4"/>'
    for (x,y,c) in [(230,330,"#FF5FA2"),(420,280,YEL),(520,300,"#fff"),(330,370,"#FF5FA2")]:
        s+=f'<circle cx="{x}" cy="{y}" r="9" fill="{c}"/><circle cx="{x}" cy="{y}" r="3" fill="#FFA630" stroke="none"/>'
    s+=TAIL; open(OUT+"good-news-grass-grows-back.svg","w").write(s)

    # 7. Good News, Twice: nobody ever got an apple by clenching his teeth
    s=head(W,H,"#FFF0B3")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=tree(470,410,True)
    s+=man(170,180,"squeeze")+legs(170,332,16)
    s+='<path d="M156,226 L124,200 L118,170"/><path d="M186,226 L218,200 L224,170"/>'
    s+=f'<circle cx="118" cy="166" r="12" fill="#FFE3C7"/><circle cx="224" cy="166" r="12" fill="#FFE3C7"/>'
    for (x1,y1,x2,y2) in [(120,120,110,100),(170,108,170,86),(220,120,230,100)]:
        s+=f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{RED}" stroke-width="5"/>'
    s+=f'<path d="M136,160 q-14,10 -6,26 q10,-8 6,-26 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"good-news-clenched-teeth-no-apple.svg","w").write(s)

def mousetrap(x,y,w=240):
    o=f'<rect x="{x}" y="{y}" width="{w}" height="26" rx="4" fill="#E2B56B"/>'
    o+=f'<path d="M{x+40},{y} L{x+40},{y-70} L{x+w-30},{y-70} L{x+w-30},{y}" stroke-width="6" stroke="#999"/>'
    o+=f'<path d="M{x+w-90},{y} L{x+w-70},{y-26} L{x+w-40},{y-6} Z" fill="{YEL}"/>'
    for (cx,cy) in [(x+w-72,y-12),(x+w-58,y-10)]:
        o+=f'<circle cx="{cx}" cy="{cy}" r="3" fill="#E2A600" stroke="none"/>'
    return o
def batch13(OUT):
    W,H=680,440
    # 1. The quiet trap: the bait is your own, and everyone says it isn't a trap
    s=head(W,H,"#7FD3FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=mousetrap(220,384,260)
    for (x,c) in [(90,"#FF7A59"),(590,"#2FB3A8")]:
        s+=man(x,200,"happy",c)+legs(x,352,14)
        s+=f'<path d="M{x-14},246 L{x-40},290"/><path d="M{x+14},246 L{x+30},200 L{x+30},178"/>'
        s+=f'<rect x="{x+22}" y="168" width="16" height="22" rx="6" fill="#FFE3C7"/><rect x="{x+26}" y="150" width="8" height="22" rx="4" fill="#FFE3C7"/>'
    s+=TAIL; open(OUT+"master-the-quiet-trap.svg","w").write(s)

    # 2. The quiet trap: he quits on his worst day and stacks a second misery on the first
    s=head(W,H,"#5C6B8A")
    s+='<ellipse cx="330" cy="40" rx="170" ry="30" fill="#8A93A8"/>'
    for i in range(14):
        x=200+i*20; y=80+(i*29)%60
        s+=f'<line x1="{x}" y1="{y}" x2="{x-6}" y2="{y+20}" stroke="#BFE3FF" stroke-width="4"/>'
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(330,230,"squeeze")+'<path d="M326,382 L306,408 M344,382 L364,408"/>'
    s+=f'<path d="M310,276 L284,196"/><path d="M350,276 L376,196"/>'
    s+=f'<rect x="270" y="130" width="120" height="60" rx="4" fill="#C9A26B" transform="rotate(-6 330 160)"/><rect x="280" y="72" width="100" height="56" rx="4" fill="#B98A55" transform="rotate(7 330 100)"/>'
    s+=TAIL; open(OUT+"master-two-boxes-in-the-rain.svg","w").write(s)

    # 3. The quiet trap: 'when things calm down', and the calendar pages fly away
    s=head(W,H,"#FFD23F")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="70" y="300" width="250" height="60" rx="20" fill="#7B4FD6"/><rect x="60" y="270" width="36" height="110" rx="14" fill="#5A3E9B"/><rect x="300" y="270" width="36" height="110" rx="14" fill="#5A3E9B"/>'
    s+=man(190,226,"blank")+'<path d="M180,370 L170,408 M206,370 L220,408"/>'
    s+='<path d="M176,272 L150,320"/><path d="M204,272 L230,320"/>'
    s+=f'<rect x="420" y="250" width="110" height="130" rx="6" fill="#fff"/><rect x="420" y="250" width="110" height="28" fill="{RED}"/>'
    for (x,y,r) in [(470,190,-20),(520,140,15),(580,100,-30),(610,60,20),(440,120,30)]:
        s+=f'<g transform="rotate({r} {x} {y})"><rect x="{x-26}" y="{y-30}" width="52" height="60" rx="4" fill="#fff"/><rect x="{x-26}" y="{y-30}" width="52" height="12" fill="{RED}"/></g>'
    s+=TAIL; open(OUT+"master-calendar-pages-fly.svg","w").write(s)

    # 4. The quiet trap: it winds him up, one guilty night at a time
    s=head(W,H,"#FF8FB1")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(270,190,"squeeze")+legs(270,342,16)
    s+='<path d="M256,236 L230,300"/><path d="M286,236 L312,300"/>'
    s+=f'<rect x="310" y="262" width="60" height="12" rx="4" fill="#999"/><path d="M370,236 C400,226 400,300 370,300 C350,300 352,240 370,236 Z" fill="#ccc"/><path d="M370,236 C340,226 340,300 370,300" fill="none"/>'
    s+=f'<path d="M350,240 q-20,-16 -10,-36 M352,300 q-20,16 -6,34" stroke="{RED}" stroke-width="4"/>'
    s+='<rect x="400" y="330" width="110" height="80" fill="#C9A26B"/><line x1="400" y1="330" x2="510" y2="410" stroke-width="3"/>'
    s+=monster(452,330,"bang",0.9,stink=True)
    s+='<path d="M412,320 L388,290" stroke-width="5"/>'
    s+=f'<path d="M234,176 q-14,10 -6,26 q10,-8 6,-26 Z" fill="#4FB3FF" stroke-width="2"/>'
    s+=TAIL; open(OUT+"master-wind-up-key.svg","w").write(s)

    # 5. The two causes: the men who walked out, faintly puzzled they ever bothered
    s=head(W,H,"#6BCB77")
    s+=f'<circle cx="590" cy="70" r="34" fill="{YEL}" stroke="none"/>'
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=mousetrap(70,384,200)
    s+=man(440,190,"happy")+'<path d="M436,342 L410,408"/><path d="M454,342 L490,404"/>'
    s+='<path d="M454,236 L480,180 L458,152"/><path d="M426,236 L400,290"/>'
    s+=f'<path d="M462,110 q0,-24 20,-24 q20,0 16,18 q-4,12 -16,16 l0,10" stroke-width="5"/>'+dot(482,140,4)
    s+=TAIL; open(OUT+"master-walked-out-puzzled.svg","w").write(s)

def blob(tx,ty,sc=1.0,stink=True):
    """The Little Monster's body only (no face), for custom faces."""
    o=f'<g transform="translate({tx},{ty}) scale({sc})">'
    if stink:
        for dx in (-20,0,20):
            o+=f'<path d="M{dx},-66 c-7,-9 7,-15 0,-24 c-7,-9 7,-15 0,-24" stroke="{STINK}" stroke-width="4"/>'
    o+=f'<path d="M-30,-8 C-34,-38 -19,-56 0,-56 C19,-56 34,-38 30,-8 C27,2 -27,2 -30,-8 Z" fill="{LIME}"/>'
    o+='<path d="M-4,-55 q1,-12 6,-3 q3,-11 7,1" stroke-width="4"/>'
    return o
def sexy_monster(tx,ty,sc=1.0,phone=True):
    """The Little Monster trying to look sexy: duck lips, lashes, hip cocked, belly popping out."""
    o=blob(tx,ty,sc)
    # half-closed 'sultry' eyes with lashes
    for ex in (-11,11):
        o+=f'<path d="M{ex-8},-36 q8,-7 16,0" fill="#fff"/><path d="M{ex-8},-36 q8,4 16,0" fill="#fff"/>'
        o+=dot(ex,-35,2.6)
        o+=f'<path d="M{ex-8},-37 l-4,-5 M{ex-3},-40 l-2,-6 M{ex+3},-40 l1,-6 M{ex+8},-37 l4,-5" stroke-width="2.5"/>'
    # big duck lips
    o+='<path d="M-12,-20 q6,-9 12,-3 q6,-6 12,3 q-6,10 -12,6 q-6,4 -12,-6 Z" fill="#FF4F8B" stroke-width="3"/>'
    o+='<line x1="-10" y1="-19" x2="10" y2="-19" stroke-width="2"/>'
    # belly bulging out over 'sucked in' line
    o+='<path d="M-14,-6 q14,14 28,0" stroke-width="3"/>'
    # cocked hip: one leg straight, one bent
    o+=f'<ellipse cx="-12" cy="6" rx="6" ry="9" fill="{LIME}"/><ellipse cx="14" cy="2" rx="9" ry="5" fill="{LIME}" transform="rotate(-25 14 2)"/>'
    # hand on hip
    o+='<path d="M-28,-22 q-14,6 -6,16"/>'
    if phone:
        o+='<path d="M28,-26 L40,-56"/>'
        o+=f'<rect x="34" y="-82" width="16" height="28" rx="4" fill="{INK}"/><circle cx="42" cy="-60" r="2" fill="#fff" stroke="none"/>'
    return o+'</g>'
def batch14(OUT):
    W,H=680,440
    # 1. The Dirty House: the cat lady can't smell it; the visitor holds his nose
    s=head(W,H,"#FFB86B")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="60" y="300" width="230" height="60" rx="20" fill="#8E5BD6"/><rect x="50" y="270" width="34" height="110" rx="14" fill="#6C42A8"/><rect x="266" y="270" width="34" height="110" rx="14" fill="#6C42A8"/>'
    s+=man(175,236,"happy","#FF5A8A")+'<path d="M165,386 L150,408 M190,386 L205,408"/>'
    s+='<path d="M162,280 L130,300"/><path d="M190,280 L222,300"/>'
    s+=f'<rect x="200" y="210" width="44" height="30" rx="8" fill="#fff"/><path d="M222,210 q-6,-12 0,-18 M232,210 q6,-12 0,-18" stroke="#c9a" stroke-width="3"/>'
    def cat(x,y,c):
        o=f'<ellipse cx="{x}" cy="{y}" rx="26" ry="18" fill="{c}"/><circle cx="{x+22}" cy="{y-16}" r="14" fill="{c}"/>'
        o+=f'<path d="M{x+12},{y-26} l2,-12 l8,8 M{x+26},{y-28} l6,-10 l4,12" fill="{c}"/>'
        o+=dot(x+18,y-18,2.4)+dot(x+28,y-18,2.4)+f'<path d="M{x-26},{y} q-16,-10 -8,-26" />'
        return o
    s+=cat(380,392,"#888")+cat(110,252,"#F2A33A")+cat(460,392,"#222")+cat(320,392,"#F2A33A")
    for (x,y) in [(400,330),(470,330),(330,330),(120,200)]:
        s+=f'<path d="M{x},{y} c-7,-9 7,-15 0,-24 c-7,-9 7,-15 0,-24" stroke="{STINK}" stroke-width="5"/>'
    s+=man(570,200,"squeeze","#2FB3A8")+legs(570,352,14)
    s+='<path d="M556,246 L540,214 L566,206"/><path d="M584,246 L612,296"/>'
    s+=f'<path d="M520,150 q-6,-10 2,-16" stroke="#4FB3FF" stroke-width="3"/>'
    s+=TAIL; open(OUT+"dirty-house-cat-lady-sniffs.svg","w").write(s)

    # 2. The shock ladder: each rung a bigger gasp; the audience on top yawns
    s=head(W,H,"#7FD3FF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<path d="M250,410 L330,40 M350,410 L430,40" stroke-width="7"/>'
    for i in range(8):
        y=380-i*44; x1=250+(410-y)*80/370; x2=x1+100
        s+=f'<line x1="{x1}" y1="{y}" x2="{x2}" y2="{y}" stroke-width="6"/>'
    # gasping face at the bottom
    s+='<circle cx="150" cy="340" r="34" fill="#fff"/>'+dot(140,330,5)+dot(160,330,5)+'<ellipse cx="150" cy="356" rx="9" ry="12" fill="#5a1414"/>'
    s+=f'<path d="M110,300 l-14,-14 M150,292 l0,-20 M190,300 l14,-14" stroke="{RED}" stroke-width="5"/>'
    # middle: shrug
    s+='<circle cx="480" cy="230" r="30" fill="#fff"/>'+dot(472,224)+dot(488,224)+'<line x1="472" y1="242" x2="490" y2="242" stroke-width="3.5"/>'
    # top: yawning, phone in hand
    s+='<circle cx="560" cy="90" r="32" fill="#fff"/><path d="M546,80 l10,0 M566,80 l10,0" stroke-width="3.5"/><ellipse cx="561" cy="104" rx="8" ry="10" fill="#5a1414"/>'
    s+='<text x="590" y="60" font-family="Arial" font-weight="bold" font-size="22" fill="#141414" stroke="none">z z</text>'
    s+=TAIL; open(OUT+"dirty-house-the-shock-ladder.svg","w").write(s)

    # 3. Lot lingers: a big hand from outside the frame drags him by the wrist toward the gate
    s=head(W,H,"#FF7A59")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    for (x,h) in [(40,180),(110,240),(180,150),(250,210)]:
        s+=f'<rect x="{x}" y="{410-h}" width="60" height="{h}" fill="#8A3B2A"/>'
        for wy in range(410-h+20,390,40):
            s+=f'<rect x="{x+12}" y="{wy}" width="12" height="16" fill="{YEL}" stroke-width="3"/><rect x="{x+36}" y="{wy}" width="12" height="16" fill="{YEL}" stroke-width="3"/>'
        for k in range(3):
            s+=f'<path d="M{x+30},{410-h-10-k*0} c-10,-20 10,-30 0,-50" stroke="{YEL}" stroke-width="5"/>' if k==0 else ''
    s+=man(390,200,"flat","#C9A26B")+'<path d="M386,352 L370,408"/><path d="M404,352 L380,406"/>'
    s+='<path d="M376,246 L330,260"/><path d="M404,246 L470,226"/>'
    s+='<path d="M470,226 L640,200" stroke-width="22" stroke="#FFE3C7"/><path d="M470,226 L640,200" stroke-width="5" fill="none"/>'
    s+='<circle cx="476" cy="226" r="16" fill="#FFE3C7"/>'
    s+=f'<path d="M370,180 q-20,-10 -26,-30" stroke="#4FB3FF" stroke-width="3"/>'
    s+='<path d="M300,250 q-20,10 -40,0" stroke-width="4"/>'
    s+=TAIL; open(OUT+"dirty-house-lot-lingers.svg","w").write(s)

    # 4. Fresh air: door flung open, man steps in, sniffs, recoils
    s=head(W,H,"#6BCB77")
    s+=f'<circle cx="590" cy="70" r="34" fill="{YEL}" stroke="none"/>'
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=house_front(80,170,300,240)
    s+='<rect x="190" y="290" width="80" height="120" fill="#2a1a3a"/><path d="M270,290 L320,300 L320,410 L270,410 Z" fill="#5A3E9B"/>'
    for (x,y) in [(210,290),(240,280),(150,250)]:
        s+=f'<path d="M{x},{y} c-7,-9 7,-15 0,-24 c-7,-9 7,-15 0,-24" stroke="{STINK}" stroke-width="5"/>'
    s+=man(470,210,"squeeze")+'<path d="M466,362 L440,408"/><path d="M484,362 L520,404"/>'
    s+='<path d="M456,256 L444,222 L462,214"/><path d="M486,256 L526,236"/>'
    s+=f'<path d="M420,190 l-20,-6 M422,206 l-22,4" stroke="{RED}" stroke-width="4"/>'
    s+=TAIL; open(OUT+"dirty-house-door-open-fresh-air.svg","w").write(s)

    # 5. Mud on purpose: a grinning boot stamps muddy prints across a cream carpet
    s=head(W,H,"#FFD23F")
    s+='<rect x="40" y="300" width="600" height="110" rx="10" fill="#FFF6E5"/>'
    for (x,y) in [(90,360),(170,340),(250,370),(330,345),(410,372)]:
        s+=f'<ellipse cx="{x}" cy="{y}" rx="30" ry="14" fill="#6B4423" stroke="none"/><ellipse cx="{x+28}" cy="{y}" rx="10" ry="12" fill="#6B4423" stroke="none"/>'
    s+='<path d="M470,120 L470,300 L600,300 Q630,300 630,270 L630,250 Q600,230 540,230 L540,120 Z" fill="#7a4a2a"/>'
    s+='<path d="M470,300 L630,300" stroke-width="10"/>'
    s+='<circle cx="505" cy="170" r="20" fill="#fff"/><circle cx="525" cy="170" r="20" fill="#fff"/>'+dot(508,172)+dot(528,172)
    s+='<path d="M490,206 q30,26 60,0" fill="#fff"/>'
    s+=f'<path d="M560,320 l20,20 M600,320 l10,24 M520,322 l-6,26" stroke="#6B4423" stroke-width="6"/>'
    s+=TAIL; open(OUT+"mud-boots-on-the-carpet.svg","w").write(s)

    # 6. Would you pay him? A man spits on the family photo and holds out his hand
    s=head(W,H,"#5C6B8A")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="90" y="120" width="130" height="160" rx="6" fill="#E2B56B"/><rect x="106" y="136" width="98" height="128" fill="#FFF6E5"/>'
    s+='<circle cx="140" cy="186" r="16" fill="#fff"/><circle cx="172" cy="182" r="18" fill="#fff"/><path d="M128,264 q12,-50 24,0 M158,264 q14,-56 28,0" fill="#FF8FB1"/>'
    s+='<path d="M200,170 q10,6 4,14" stroke="#4FB3FF" stroke-width="4"/>'
    s+=man(330,190,"flat","#222")+legs(330,342,16)
    s+='<path d="M302,180 q-30,-10 -60,-6" stroke="#4FB3FF" stroke-width="3" stroke-dasharray="6 8"/>'
    s+='<path d="M344,236 L400,250 L430,240"/>'
    s+='<path d="M430,240 q14,-4 18,6 q-8,8 -20,4" fill="#FFE3C7"/>'
    s+=f'<rect x="470" y="300" width="70" height="38" rx="4" fill="#6BCB77"/><text x="488" y="326" font-family="Arial" font-weight="bold" font-size="20" fill="#141414" stroke="none">$20</text>'
    s+=man(560,200,"blank")+legs(560,352,14)
    s+='<path d="M546,246 L520,300"/><path d="M574,246 L600,300"/>'
    s+=f'<path d="M600,140 q0,-24 20,-24 q20,0 16,18 q-4,12 -16,16 l0,10" stroke-width="5"/>'+dot(620,170,4)
    s+=TAIL; open(OUT+"mud-would-you-pay-him.svg","w").write(s)

    # 7. The monster at the awards show: devil-horn top hat, flames, and nobody cares
    s=head(W,H,"#2B1B4F")
    s+='<rect x="100" y="320" width="480" height="90" fill="#8E5BD6"/><line x1="100" y1="320" x2="580" y2="320"/>'
    for x in range(130,560,60):
        s+=f'<path d="M{x},320 q-14,-40 6,-70 q4,30 18,18 q10,30 -4,52 Z" fill="{RED}"/><path d="M{x+6},318 q-4,-20 6,-34 q6,18 -2,34 Z" fill="{YEL}" stroke="none"/>'
    s+=monster(340,300,"bang",1.3,stink=True)
    s+=f'<rect x="306" y="190" width="68" height="40" fill="{RED}"/><rect x="292" y="226" width="96" height="10" rx="4" fill="{RED}"/>'
    s+=f'<path d="M314,192 q-14,-22 -2,-34 q0,16 12,20 Z M366,192 q14,-22 2,-34 q0,16 -12,20 Z" fill="{RED}"/>'
    s+='<circle cx="560" cy="80" r="26" fill="#fff"/><path d="M548,74 l8,0 M564,74 l8,0" stroke-width="3"/><ellipse cx="560" cy="92" rx="6" ry="8" fill="#5a1414"/>'
    s+='<text x="592" y="60" font-family="Arial" font-weight="bold" font-size="20" fill="#fff" stroke="none">z z</text>'
    s+=TAIL; open(OUT+"mud-the-monster-at-the-awards.svg","w").write(s)

    # 8. The Little Monster's duck-face selfie in a bathroom mirror
    s=head(W,H,"#FF8FB1")
    s+='<rect x="40" y="330" width="600" height="80" fill="#FFF6E5"/><line x1="40" y1="330" x2="640" y2="330"/>'
    s+='<rect x="380" y="70" width="230" height="250" rx="16" fill="#BFE3FF"/><path d="M400,110 l40,-30 M420,140 l60,-50" stroke="#fff" stroke-width="6"/>'
    s+=sexy_monster(240,300,2.2)
    s+='<g transform="translate(495,300) scale(-1.4,1.4)">'+sexy_monster(0,0,1.0,phone=True).replace('<g transform="translate(0,0) scale(1.0)">','<g>')+'</g>'
    s+=TAIL; open(OUT+"why-monster-duck-face-selfie.svg","w").write(s)

    # 9. The Little Monster's pin-up pose on a velvet chaise, with flies circling
    s=head(W,H,"#C93B6B")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<path d="M140,330 Q140,280 200,290 L520,300 Q560,300 560,340 L560,370 L140,370 Z" fill="#7B1E45"/><line x1="170" y1="370" x2="170" y2="404"/><line x1="530" y1="370" x2="530" y2="404"/>'
    s+=sexy_monster(340,292,1.9,phone=False)
    for (x,y) in [(250,120),(430,100),(470,160),(220,180)]:
        s+=f'<circle cx="{x}" cy="{y}" r="6" fill="{INK}" stroke="none"/><ellipse cx="{x-6}" cy="{y-7}" rx="6" ry="4" fill="#fff" stroke-width="2"/><ellipse cx="{x+6}" cy="{y-7}" rx="6" ry="4" fill="#fff" stroke-width="2"/>'
    s+=f'<path d="M240,110 q40,-30 80,0 q40,30 80,-10" stroke-dasharray="4 8" stroke-width="2"/>'
    s+=TAIL; open(OUT+"why-monster-pinup.svg","w").write(s)

    # 10. Scroll on: a calm man flicks past the picture with a thumb, the monster upstairs sulks
    s=head(W,H,"#33C3D6")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(220,190,"happy")+legs(220,342,16)
    s+='<path d="M234,236 L280,220 L300,196"/><path d="M206,236 L180,290"/>'
    s+=f'<rect x="282" y="140" width="56" height="96" rx="10" fill="{INK}"/><rect x="288" y="150" width="44" height="76" rx="4" fill="#fff"/>'
    s+=f'<path d="M298,170 l24,0 M298,184 l24,0 M298,198 l16,0" stroke-width="3"/><path d="M310,250 l0,-20 m-8,8 l8,-8 l8,8" stroke="{RED}" stroke-width="4"/>'
    s+='<rect x="430" y="120" width="190" height="150" fill="#FFF6E5"/><line x1="430" y1="270" x2="620" y2="270" stroke-width="7"/>'
    s+=monster(525,262,"dangle",1.05,stink=True)
    s+='<rect x="490" y="250" width="70" height="12" rx="6" fill="#fff"/>'
    s+=TAIL; open(OUT+"why-scroll-on.svg","w").write(s)

    # 11. "That's a boot": a man on the couch points at a TV where a muddy boot stomps across the screen
    s=head(W,H,"#9B7BFF")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<rect x="380" y="110" width="250" height="160" rx="12" fill="{INK}"/><rect x="394" y="124" width="222" height="132" fill="#FFF6E5"/>'
    s+='<line x1="505" y1="270" x2="505" y2="300"/><line x1="460" y1="300" x2="550" y2="300" stroke-width="6"/>'
    s+='<path d="M470,150 L470,230 L560,230 Q580,230 580,212 L580,200 Q560,190 520,190 L520,150 Z" fill="#7a4a2a"/>'
    for (x,y) in [(420,244),(450,236)]:
        s+=f'<ellipse cx="{x}" cy="{y}" rx="14" ry="6" fill="#6B4423" stroke="none"/>'
    s+=f'<path d="M488,170 q10,10 20,0" stroke-width="3"/>'+dot(492,162,3)+dot(506,162,3)
    s+=sofa().replace('x="120" y="226" width="440"','x="40" y="300" width="290"')
    s+='<rect x="40" y="300" width="290" height="70" rx="22" fill="#FF7A59"/><rect x="30" y="270" width="34" height="110" rx="14" fill="#D9573B"/><rect x="306" y="270" width="34" height="110" rx="14" fill="#D9573B"/>'
    s+=man(180,230,"happy")+'<path d="M170,380 L160,408 M196,380 L210,408"/>'
    s+='<path d="M194,276 L260,240 L330,226"/><path d="M166,276 L130,320"/>'
    s+='<text x="150" y="150" font-family="Arial" font-weight="bold" font-size="26" fill="#141414" stroke="none">That\'s a boot.</text>'
    s+=TAIL; open(OUT+"why-pay-thats-a-boot.svg","w").write(s)

# ---- Fifteenth batch (The Flesh: six bent goods; The Bent Gift: one flesh). Run: python3 tools/draw_illustrations.py images/illustrations/ 15 ----
def batch15(OUT):
    W,H=680,440
    HAIR="#9C6B3C"; SKIN="#FFE3C7"
    def sweat(x,y): return f'<path d="M{x},{y} q-8,12 0,16 q8,-4 0,-16 Z" fill="#4FB3FF" stroke-width="2.5"/>'
    def sparks(lst,col=YEL,w=5): return "".join(f'<line x1="{a}" y1="{b}" x2="{c}" y2="{d}" stroke="{col}" stroke-width="{w}"/>' for a,b,c,d in lst)
    def proud(x,y):
        # head tilted back, eyes shut smugly, nose up
        o=f'<circle cx="{x}" cy="{y}" r="34" fill="#fff"/>'
        o+=f'<path d="M{x-14},{y-8} q6,-5 12,0" stroke-width="3.5"/><path d="M{x+6},{y-10} q6,-5 12,0" stroke-width="3.5"/>'
        o+=f'<path d="M{x+18},{y+2} l14,-10 l-10,14" fill="#fff" stroke-width="3.5"/><path d="M{x-6},{y+16} q10,4 18,-4" stroke-width="3.5"/>'
        return o

    # 1. Pride: drives the wrong way rather than ask; a man holds out a map
    s=head(W,H,"#FFA630")
    s+='<rect x="30" y="330" width="620" height="80" fill="#5A5A6E"/>'
    for x in range(60,640,90): s+=f'<line x1="{x}" y1="370" x2="{x+40}" y2="370" stroke="#fff" stroke-width="5"/>'
    # sign pointing back the way he came
    s+='<line x1="110" y1="330" x2="110" y2="170"/><path d="M60,150 L160,150 L160,200 L60,200 L40,175 Z" fill="#2FB36A"/><path d="M70,175 L140,175 M70,175 l16,-12 M70,175 l16,12" stroke="#fff" stroke-width="6"/>'
    # car heading right
    s+=f'<path d="M260,320 L260,270 Q262,250 290,248 L330,210 Q340,200 360,200 L440,200 Q462,200 474,216 L500,248 L540,250 Q564,252 566,276 L566,320 Z" fill="{RED}"/>'
    s+='<path d="M340,214 L440,214 Q452,214 460,226 L480,248 L320,248 Z" fill="#BFE3FF"/>'
    s+='<circle cx="310" cy="324" r="26" fill="#333"/><circle cx="310" cy="324" r="9" fill="#ccc"/><circle cx="510" cy="324" r="26" fill="#333"/><circle cx="510" cy="324" r="9" fill="#ccc"/>'
    s+=proud(400,222).replace('r="34"','r="26"')
    s+=sweat(372,200)+sweat(430,192)
    # helpful man with map on the sidewalk, right
    s+=man(612,206,"happy","#2FB36A")
    s+='<path d="M608,358 L600,406"/><path d="M624,358 L634,406"/>'
    s+='<path d="M598,250 L572,276"/><rect x="532" y="262" width="52" height="40" fill="#FFF6E5" transform="rotate(-10 558 282)"/><path d="M540,276 l12,10 l12,-8 l12,10" stroke="#FF3B30" stroke-width="3" transform="rotate(-10 558 282)"/>'
    s+=TAIL; open(OUT+"flesh-pride-wont-ask.svg","w").write(s)

    # 2. Greed: alone on a pile of coins, his truck dead, nobody coming
    s=head(W,H,"#7BC8F6")
    s+='<line x1="30" y1="400" x2="650" y2="400"/>'
    s+=f'<path d="M80,400 Q120,250 230,230 Q340,250 380,400 Z" fill="{YEL}"/>'
    for (x,y) in [(150,360),(200,330),(260,350),(230,290),(300,380),(180,385),(320,330)]:
        s+=f'<ellipse cx="{x}" cy="{y}" rx="16" ry="8" fill="#FFB800" stroke-width="3"/>'
    s+=man(230,120,"squeeze")
    s+='<path d="M210,180 Q180,220 214,236"/><path d="M250,180 Q280,220 246,236"/>'
    s+=f'<path d="M206,214 Q230,190 256,214 Q270,260 230,262 Q192,260 206,214 Z" fill="#2FB36A"/><path d="M220,214 l20,0" stroke-width="3"/>'
    s+=f'<ellipse cx="230" cy="238" rx="10" ry="6" fill="{YEL}" stroke-width="3"/>'
    # broken truck
    s+=f'<path d="M430,370 L430,300 L500,300 L520,260 L580,260 L600,300 L620,300 L620,370 Z" fill="#8E5BD6"/>'
    s+='<rect x="530" y="270" width="40" height="28" fill="#BFE3FF"/>'
    s+='<circle cx="470" cy="374" r="22" fill="#333"/><circle cx="590" cy="374" r="22" fill="#333"/>'
    for dx in (450,480,510):
        s+=f'<path d="M{dx},296 c-12,-14 12,-24 0,-40 c-12,-14 12,-24 0,-40" stroke="#fff" stroke-width="8" opacity="0.9"/>'
    s+=f'<path d="M640,240 q-16,-16 -30,0 q-16,-16 -30,0" stroke="{INK}" stroke-width="3"/>'
    s+=TAIL; open(OUT+"flesh-greed-on-the-pile.svg","w").write(s)

    # 3. Envy: scowling over the fence at the neighbor's new truck
    s=head(W,H,"#9AD0FF")
    s+='<rect x="30" y="360" width="620" height="50" fill="#6BCB77" stroke="none"/><line x1="30" y1="410" x2="650" y2="410"/>'
    # neighbor's shiny truck
    s+=f'<path d="M330,340 L330,260 L420,260 L446,212 L530,212 L556,260 L600,262 L600,340 Z" fill="{RED}"/>'
    s+='<rect x="456" y="222" width="70" height="34" fill="#BFE3FF"/><path d="M466,250 l18,-20 M486,250 l14,-16" stroke="#fff" stroke-width="5"/>'
    s+='<circle cx="380" cy="344" r="24" fill="#333"/><circle cx="380" cy="344" r="8" fill="#ccc"/><circle cx="556" cy="344" r="24" fill="#333"/><circle cx="556" cy="344" r="8" fill="#ccc"/>'
    s+=sparks([(340,236,326,222),(360,226,360,206),(612,250,630,240),(610,276,632,280)],"#fff",5)
    # happy neighbor waving
    s+=man(620,140,"happy",YEL)+'<path d="M634,180 L660,130 M606,184 L600,240"/>'
    # fence and the envious man peeking
    s+='<g>'
    s+='<circle cx="190" cy="206" r="40" fill="#C7F05A"/>'
    s+='<path d="M166,196 L186,204 M214,196 L194,204" stroke-width="4.5"/>'+dot(180,212)+dot(200,212)
    s+='</g>'
    for x in range(60,300,40):
        s+=f'<path d="M{x},400 L{x},236 L{x+17},220 L{x+34},236 L{x+34},400 Z" fill="#C98B4F"/>'
    s+='<line x1="50" y1="280" x2="304" y2="280" stroke-width="6"/><line x1="50" y1="360" x2="304" y2="360" stroke-width="6"/>'
    s+=f'<path d="M156,236 q8,-12 16,0" fill="#C7F05A" stroke-width="3.5"/><path d="M208,236 q8,-12 16,0" fill="#C7F05A" stroke-width="3.5"/>'
    s+=TAIL; open(OUT+"flesh-envy-over-the-fence.svg","w").write(s)

    # 4. Anger: a hole in the drywall and an arm in a cast
    s=head(W,H,"#FF8FB1")
    s+='<rect x="30" y="30" width="620" height="340" fill="#FFF6E5" stroke="none"/><line x1="30" y1="370" x2="650" y2="370"/><line x1="30" y1="410" x2="650" y2="410"/>'
    s+=f'<path d="M420,160 L446,138 L470,150 L496,132 L512,162 L540,170 L524,198 L534,226 L502,228 L486,254 L462,234 L432,242 L430,212 L404,196 Z" fill="#3b2a20"/>'
    s+='<path d="M404,196 L370,190 M446,138 L436,104 M540,170 L578,158 M486,254 L494,290 M534,226 L566,244" stroke-width="3"/>'
    for (x,y) in [(450,400),(472,392),(500,402)]:
        s+=f'<rect x="{x}" y="{y-8}" width="14" height="10" fill="#fff" stroke-width="2.5" transform="rotate(20 {x} {y})"/>'
    s+=man(250,170,"blank")
    s+=sweat(220,140)
    s+='<path d="M246,322 L232,406"/><path d="M262,322 L282,406"/>'
    s+='<path d="M236,216 L214,280 L222,316"/>'
    s+=f'<path d="M232,206 L300,252" stroke="#4FB3FF" stroke-width="6"/><path d="M270,212 L300,252" stroke="#4FB3FF" stroke-width="6"/>'
    s+=f'<rect x="258" y="232" width="84" height="34" rx="14" fill="#fff" transform="rotate(-8 300 250)"/>'
    s+='<path d="M276,240 l4,16 M300,238 l4,16 M322,236 l4,16" stroke-width="2.5"/>'
    s+=f'<rect x="120" y="390" width="40" height="14" rx="4" fill="{INK}"/><rect x="124" y="392" width="32" height="8" fill="{RED}" stroke="none"/>'
    s+=TAIL; open(OUT+"flesh-anger-the-drywall.svg","w").write(s)

    # 5. Sloth: melted into the couch; the kid waits in the doorway with a ball
    s=head(W,H,"#FFD23F")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+='<rect x="70" y="70" width="140" height="120" fill="#BFE3FF"/><line x1="140" y1="70" x2="140" y2="190"/><line x1="70" y1="130" x2="210" y2="130"/><circle cx="110" cy="100" r="16" fill="#FFA630"/>'
    s+='<rect x="510" y="110" width="120" height="300" fill="#FFF6E5"/>'
    # kid with ball
    s+='<circle cx="570" cy="240" r="24" fill="#fff"/>'+dot(563,236)+dot(578,236)+'<path d="M562,254 q8,-6 16,0" stroke-width="3"/>'
    s+=f'<path d="M556,264 C546,286 548,320 556,336 L586,336 C594,320 594,286 584,264 Z" fill="{RED}"/>'
    s+='<path d="M562,336 L556,404"/><path d="M580,336 L588,404"/>'
    s+=f'<circle cx="572" cy="300" r="20" fill="#FF8FB1"/><path d="M552,300 h40" stroke-width="3"/>'
    s+='<path d="M558,280 L558,300 M586,280 L586,300"/>'
    # couch with melted man
    s+='<rect x="120" y="260" width="330" height="90" rx="26" fill="#5A3E9B"/><rect x="100" y="230" width="40" height="130" rx="16" fill="#7B4FD6"/><rect x="430" y="230" width="40" height="130" rx="16" fill="#7B4FD6"/>'
    s+=f'<path d="M200,300 C200,262 236,250 270,262 L360,286 C380,292 380,318 360,322 L210,330 Z" fill="{SHIRT}"/>'
    s+='<ellipse cx="190" cy="282" rx="36" ry="30" fill="#fff"/>'+dot(182,276)+dot(202,276)+'<path d="M174,273 h16 M194,273 h16" stroke-width="3.5"/><line x1="184" y1="296" x2="198" y2="296" stroke-width="3"/>'
    s+='<path d="M360,318 L430,330 L470,404 M350,322 L412,348 L436,404"/>'
    s+=f'<rect x="262" y="270" width="40" height="22" rx="10" fill="{INK}"/>'
    s+=f'<path d="M300,232 L340,228 L338,270 L304,272 Z" fill="{RED}"/><path d="M312,246 l14,0" stroke="#fff" stroke-width="3"/>'
    s+='<line x1="140" y1="360" x2="140" y2="404"/><line x1="430" y1="360" x2="430" y2="404"/>'
    s+=TAIL; open(OUT+"flesh-sloth-the-couch.svg","w").write(s)

    # 6. Gluttony: a tower of wing bones and a face that tastes nothing
    s=head(W,H,"#6BCB77")
    s+='<line x1="30" y1="410" x2="650" y2="410"/>'
    s+=man(300,150,"blank")
    s+=f'<path d="M282,176 q-6,8 2,12 M318,174 q8,6 2,12" stroke="#D9573B" stroke-width="5"/>'
    s+='<rect x="80" y="290" width="520" height="24" rx="6" fill="#C98B4F"/><line x1="120" y1="314" x2="120" y2="406"/><line x1="560" y1="314" x2="560" y2="406"/>'
    s+='<ellipse cx="440" cy="288" rx="90" ry="14" fill="#fff"/>'
    def bone(x,y,r):
        return f'<g transform="rotate({r} {x} {y})"><rect x="{x-26}" y="{y-5}" width="52" height="10" rx="5" fill="#FFF6E5" stroke-width="3"/><circle cx="{x-26}" cy="{y-4}" r="5" fill="#FFF6E5" stroke-width="2.5"/><circle cx="{x-26}" cy="{y+4}" r="5" fill="#FFF6E5" stroke-width="2.5"/><circle cx="{x+26}" cy="{y-4}" r="5" fill="#FFF6E5" stroke-width="2.5"/><circle cx="{x+26}" cy="{y+4}" r="5" fill="#FFF6E5" stroke-width="2.5"/></g>'
    rows=[(5,276),(4,256),(4,236),(3,216),(2,196),(1,176)]
    k=0
    for n,y in rows:
        for j in range(n):
            x=440+(j-(n-1)/2)*36
            s+=bone(x,y,[-18,12,-6,22,-25,8][k%6]); k+=1
    s+='<path d="M286,194 L240,250 L262,282"/>'
    s+='<path d="M316,194 L350,236 L330,210"/>'
    s+=f'<path d="M318,190 Q330,170 352,176 Q368,188 356,206 Q340,220 324,212 Z" fill="#D9573B"/>'
    s+=f'<ellipse cx="180" cy="286" rx="50" ry="10" fill="#fff"/><path d="M146,282 Q180,250 214,282 Z" fill="#D9573B"/>'
    s+=TAIL; open(OUT+"flesh-gluttony-the-ninth-wing.svg","w").write(s)

    # 7. The Bent Gift: one flesh. A man and his wife walk hand in hand toward a lit home
    s=head(W,H,"#FF7A59")
    s+=f'<circle cx="560" cy="120" r="52" fill="{YEL}" stroke="none"/>'
    s+='<rect x="30" y="360" width="620" height="50" fill="#2FB36A" stroke="none"/><line x1="30" y1="410" x2="650" y2="410"/>'
    s+=house_front(470,250,150,150).replace("","") if False else ""
    s+='<rect x="440" y="230" width="170" height="140" fill="#FFF6E5"/><path d="M420,236 L525,160 L630,236 Z" fill="#5A3E9B"/>'
    s+=f'<rect x="575" y="168" width="22" height="40" fill="{RED}"/><path d="M586,160 c-10,-12 10,-20 0,-34 c-10,-12 10,-20 0,-34" stroke="#fff" stroke-width="5"/>'
    s+=f'<rect x="505" y="300" width="40" height="70" fill="{RED}"/><rect x="458" y="260" width="34" height="30" fill="{YEL}"/><rect x="560" y="260" width="34" height="30" fill="{YEL}"/>'
    s+='<path d="M380,380 Q460,374 520,372" stroke="#FFF6E5" stroke-width="10" opacity="0.8"/>'
    # him (back three-quarter: just walking right)
    s+=man(200,190,"happy")+'<path d="M194,342 L172,406"/><path d="M212,342 L240,406"/>'
    s+='<path d="M186,236 L166,300"/>'
    # her: hair, dress
    s+=f'<path d="M{310-38},190 C{310-40},140 {310+40},140 {310+36},190 L{310+40},236 L{310-40},236 Z" fill="{HAIR}"/>'
    s+=f'<path d="M{296},228 C{280},260 {270},320 {262},352 L{360},352 C{352},320 {340},260 {326},228 Z" fill="{YEL}"/>'
    s+=f'<circle cx="310" cy="190" r="34" fill="#fff"/><path d="M{310-36},178 C{310-30},148 {310+30},148 {310+34},180 C{310+10},166 {310-16},168 {310-36},178 Z" fill="{HAIR}"/>'
    s+=f'<path d="M298,186 q5,-6 10,0" stroke-width="3.5"/><path d="M314,186 q5,-6 10,0" stroke-width="3.5"/><path d="M302,202 q8,9 16,0" stroke-width="3.5"/>'
    s+='<path d="M296,352 L290,406"/><path d="M324,352 L334,406"/>'
    s+='<path d="M334,240 L360,300"/>'
    # hands joined between them
    s+='<path d="M214,236 L256,282"/><path d="M290,240 L262,282"/><circle cx="259" cy="284" r="9" fill="#fff"/>'
    s+=f'<path d="M250,120 c-10,-14 -30,-4 -20,12 l20,18 l20,-18 c10,-16 -10,-26 -20,-12 Z" fill="{RED}"/>'
    s+=TAIL; open(OUT+"bent-gift-one-flesh.svg","w").write(s)

# ---- Sixteenth batch (The Back Door: rolled by hand beside a factory cigarette) ----
def batch16(OUT):
    W,H=680,440
    s=head(W,H,"#33C3D6")
    s+='<rect x="30" y="360" width="620" height="22" rx="8" fill="#9C6B3C"/><line x1="70" y1="382" x2="70" y2="408"/><line x1="610" y1="382" x2="610" y2="408"/>'
    # hand-rolled: lumpy, crooked paper, twisted end, loose tobacco, a few shreds on the table
    s+='<path d="M70,330 C80,310 120,322 160,314 C200,306 240,318 282,312 L300,322 L286,332 L300,344 C260,356 220,346 180,352 C140,358 100,348 72,354 Z" fill="#FFF3D6"/>'
    s+='<path d="M120,322 C124,334 118,344 124,350 M196,312 C200,326 192,340 198,350" stroke-width="3"/>'
    s+='<path d="M70,334 C60,336 58,350 70,352" fill="#C2410C" stroke-width="4"/>'
    s+='<path d="M296,324 l22,-8 M300,334 l24,2 M296,344 l20,12" stroke="#7A4A1A" stroke-width="4"/>'
    s+='<path d="M170,368 q8,-6 14,0 M232,372 q8,-6 14,0" stroke="#7A4A1A" stroke-width="4"/>'
    s+='<path d="M64,300 q-14,-18 0,-34 q14,-16 0,-34" stroke="#fff" stroke-width="7"/><path d="M64,300 q-14,-18 0,-34 q14,-16 0,-34" stroke="#bbb" stroke-width="3"/>'
    # factory: straight, white, orange filter with gold band
    s+='<rect x="372" y="320" width="170" height="40" rx="4" fill="#fff"/><rect x="542" y="320" width="100" height="40" rx="6" fill="#FFA630"/>'
    s+=f'<rect x="536" y="320" width="12" height="40" fill="{YEL}"/><line x1="580" y1="324" x2="580" y2="356" stroke-width="3"/><line x1="598" y1="324" x2="598" y2="356" stroke-width="3"/>'
    s+='<rect x="364" y="320" width="14" height="40" rx="4" fill="#C2410C"/>'
    s+='<path d="M386,300 q-14,-18 0,-34 q14,-16 0,-34" stroke="#fff" stroke-width="7"/><path d="M386,300 q-14,-18 0,-34 q14,-16 0,-34" stroke="#bbb" stroke-width="3"/>'
    # the lure: a fishing line and hook set in the filter
    s+='<line x1="618" y1="0" x2="618" y2="232" stroke="#fff" stroke-width="4"/>'
    s+=f'<path d="M618,232 L618,300 Q618,336 594,336 Q574,336 574,318" stroke-width="7"/><path d="M574,318 L564,304" stroke-width="7"/>'
    s+=TAIL; open(OUT+"back-door-rolled-and-factory-cigarettes.svg","w").write(s)

if __name__=="__main__":
    which=sys.argv[2:] or ["5","6","7","8","9","10","11","12","13","14","15","16"]
    for b in which: globals()["batch"+b](OUT)
