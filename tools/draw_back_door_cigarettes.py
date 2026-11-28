# Draws the cigarette drawing for The Back Door (hand-rolled beside factory-made), in the same style as
# tools/draw_illustrations.py. Kept in its own file so it doesn't collide with the batches there.
# Usage: python3 tools/draw_back_door_cigarettes.py images/illustrations/
import sys
INK="#141414"; LIME="#9BD13A"; STINK="#C7F05A"; SHIRT="#2F6BFF"; RED="#FF3B30"; YEL="#FFD23F"; GLOW="#BFE3FF"
SW=5
def head(w,h,bg):
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" width="{w}" height="{h}">
<defs><filter id="r" x="-3%" y="-3%" width="106%" height="106%"><feTurbulence type="fractalNoise" baseFrequency="0.03" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="2"/></filter></defs>
<rect width="{w}" height="{h}" rx="28" fill="{bg}"/>
<g filter="url(#r)" stroke="{INK}" stroke-width="{SW}" stroke-linecap="round" stroke-linejoin="round" fill="none">
'''
TAIL="</g></svg>\n"

def batch37(OUT):
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

if __name__=='__main__':
    batch37(sys.argv[1])
