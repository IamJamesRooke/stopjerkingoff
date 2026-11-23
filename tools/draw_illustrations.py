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
    o+='<circle cx="-10" cy="-35" r="9" fill="#fff"/><circle cx="10" cy="-35" r="9" fill="#fff"/>'
    if pose=="dangle":
        o+=dot(-8,-33)+dot(12,-33)
        o+='<path d="M-19,-46 L-4,-41"/><path d="M19,-46 L4,-41"/><path d="M-6,-21 q6,-5 12,0" stroke-width="4"/>'
        o+='<path d="M-22,-12 Q0,-2 16,-9"/><path d="M22,-12 Q0,-2 -16,-9"/>'
        o+=f'<ellipse cx="-11" cy="6" rx="6" ry="8" fill="{LIME}"/><ellipse cx="11" cy="6" rx="6" ry="8" fill="{LIME}"/>'
    else:
        o+=dot(-8,-36)+dot(8,-36)
        o+='<path d="M-20,-48 L-4,-41"/><path d="M20,-48 L4,-41"/><path d="M-9,-17 q9,-9 18,0" stroke-width="4"/>'
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
