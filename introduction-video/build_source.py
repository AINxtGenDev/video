"""Generate the five editable HyperFrames scenes from a compact brand brief."""
from pathlib import Path
import json

PROJECT = Path(__file__).resolve().parent
COMPS = PROJECT / 'compositions'
COMPS.mkdir(exist_ok=True)

COMMON = '''
@font-face{font-family:Manrope;src:url("assets/fonts/Manrope-var.woff2") format("woff2");font-weight:200 800;font-style:normal;font-display:block}
@font-face{font-family:Montserrat;src:url("assets/fonts/Montserrat-400.woff2") format("woff2");font-weight:400;font-style:normal;font-display:block}
*{box-sizing:border-box;margin:0;padding:0}
#root{position:absolute;inset:0;overflow:hidden;font-family:Manrope,sans-serif;color:#2E3134}
.scene-content{position:absolute;inset:0;background:#F3EEE8}
.photo-box{position:absolute;overflow:hidden;background:#EFF4EE}
.photo-pan{position:absolute;inset:0}
.media{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.title{position:absolute;left:34px;width:412px;font-size:40px;font-weight:700;line-height:1.14;letter-spacing:-1.3px}
.accent{color:#5E6F5B}
.rule{position:absolute;left:34px;height:1px;width:412px;background:#9CAF95;transform-origin:left center}
.small{font-size:18px;line-height:1.45;font-weight:400}
.label{font-family:Montserrat,sans-serif;font-size:16px;line-height:1.4;font-weight:400}
'''

def media(scene, image, duration, offset, box):
    return f'''<div class="photo-box" style="{box}" data-layout-allow-overflow data-layout-allow-overlap>
      <div id="{scene}-pan" class="photo-pan">
        <img id="{scene}-image" class="clip media editorial-media" data-start="0" data-duration="{duration}" data-track-index="2" src="assets/{image}" alt="Innenraummotiv der Website" />
        <video id="{scene}-wan" class="clip media wan-media" data-start="0" data-duration="{duration}" data-track-index="3" data-media-start="{offset}" muted playsinline preload="auto" src="assets/wan-room.mp4"></video>
      </div>
    </div>'''

def scene(name, duration, body, animation, extra=''):
    html = f'''<!doctype html><html lang="de"><body><template>
<style>{COMMON}\n{extra}</style>
<div id="root" data-composition-id="{name}" data-width="480" data-height="854" data-duration="{duration}">
 <div id="{name}-motion" class="scene-content">{body}</div>
</div>
<script>
{{ const tl=gsap.timeline({{paused:true}});
{animation}
window.__timelines=window.__timelines||{{}};
window.__timelines["{name}"]=tl;
}}
</script></template></body></html>'''
    (COMPS / f'{name}.html').write_text(html)

scene('hook',5,
    media('hook','living.webp',5,0,'left:0;top:0;width:480px;height:484px')+'''
    <h1 class="title" style="top:520px"><span id="hook-first">Schöne Räume.</span><br><span id="hook-second" class="accent">Klarer Alltag.</span></h1>
    <div id="hook-rule" class="rule" style="top:650px"></div>
    <p id="hook-note" class="small" style="position:absolute;left:34px;top:678px">Raumgestaltung &amp; Ordnungscoaching</p>''',
    '''tl.fromTo("#hook-pan",{scale:1,x:0},{scale:1.045,x:-5,duration:4.85,ease:"none"},0);
tl.fromTo("#hook-second",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},1.6);
tl.fromTo("#hook-rule",{scaleX:0},{scaleX:1,duration:0.7,ease:"power2.out"},2.7);
tl.fromTo("#hook-note",{opacity:0},{opacity:1,duration:0.5,ease:"power2.out"},3.15);''')

scene('portrait',7,'''
    <div class="photo-box" style="left:80px;top:72px;width:320px;height:384px" data-layout-allow-overflow>
      <div id="portrait-pan" class="photo-pan"><img id="portrait-photo" class="clip media" data-start="0" data-duration="7" data-track-index="2" src="assets/claudia.webp" alt="Originalporträt von Claudia Plessl" /></div>
    </div>
    <p id="portrait-prefix" class="label" style="position:absolute;left:34px;top:486px">MAG.</p>
    <h2 id="portrait-name" class="title" style="top:510px;font-size:37px">Claudia Plessl</h2>
    <div id="portrait-rule" class="rule" style="top:570px"></div>
    <p id="portrait-role" class="small" style="position:absolute;left:34px;top:594px;font-size:20px">Interior Design<br>Professional Organizing</p>
    <p id="portrait-region" class="label" style="position:absolute;left:34px;top:677px;color:#5E6F5B">Wien &amp; Niederösterreich</p>''',
    '''tl.fromTo("#portrait-pan",{scale:1},{scale:1.025,duration:6.8,ease:"none"},0);
tl.fromTo("#portrait-prefix, #portrait-name",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},0.6);
tl.fromTo("#portrait-rule",{scaleX:0},{scaleX:1,duration:0.65,ease:"power2.out"},1.65);
tl.fromTo("#portrait-role",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},2.2);
tl.fromTo("#portrait-region",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},4.0);''',
    '.scene-content{background:#EFF4EE}')

scene('order',6,
    media('order','order.webp',6,5,'left:34px;top:80px;width:412px;height:412px')+'''
    <h2 class="title" style="top:532px"><span>Ordnung,</span><br><span id="order-second" class="accent">die bleibt</span></h2>
    <div id="order-rule" class="rule" style="top:656px"></div>
    <p id="order-note" class="small" style="position:absolute;left:34px;top:682px">Mehr Übersicht. Mehr Leichtigkeit.</p>''',
    '''tl.fromTo("#order-pan",{scale:1.045,y:-5},{scale:1,y:0,duration:5.8,ease:"none"},0);
tl.fromTo("#order-second",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},1.5);
tl.fromTo("#order-rule",{scaleX:0},{scaleX:1,duration:0.65,ease:"power2.out"},2.9);
tl.fromTo("#order-note",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},3.5);''')

scene('design',6,
    media('design','living.webp',6,11,'left:34px;top:80px;width:412px;height:412px')+'''
    <h2 class="title" style="top:532px"><span>Räume mit</span><br><span id="design-second" class="accent">Persönlichkeit</span></h2>
    <div id="design-rule" class="rule" style="top:656px"></div>
    <p id="design-note" class="small" style="position:absolute;left:34px;top:682px">Passend zu Ihnen und Ihrem Alltag.</p>''',
    '''tl.fromTo("#design-pan",{scale:1,x:4},{scale:1.05,x:-4,duration:5.8,ease:"none"},0);
tl.fromTo("#design-second",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},1.5);
tl.fromTo("#design-rule",{scaleX:0},{scaleX:1,duration:0.65,ease:"power2.out"},2.9);
tl.fromTo("#design-note",{opacity:0},{opacity:1,duration:0.55,ease:"power2.out"},3.5);''')

scene('contact',6,'''
    <p id="contact-label" class="label" style="position:absolute;left:34px;top:96px;color:#5E6F5B">SCHÖN, WENN WIR UNS KENNENLERNEN.</p>
    <div style="position:absolute;left:85px;top:177px;width:310px;height:167px" data-layout-allow-overflow>
      <img id="contact-logo" class="clip" data-start="0" data-duration="6" data-track-index="2" src="assets/logo.webp" alt="Claudia Plessl — Original-Logo" style="position:absolute;inset:0;width:100%;height:100%;object-fit:contain" />
    </div>
    <div id="contact-rule" class="rule" style="top:394px"></div>
    <h2 id="contact-cta" class="title" style="top:430px;font-size:35px">Reden wir über<br><span class="accent">Ihren Raum.</span></h2>
    <p id="contact-domain" style="position:absolute;left:34px;top:566px;font-size:28px;font-weight:700;color:#5E6F5B">claudiaplessl.at</p>
    <p id="contact-invite" class="small" style="position:absolute;left:34px;top:623px">Kostenloses Erstgespräch</p>
    <p id="contact-disclosure" class="label" style="position:absolute;left:34px;top:722px;font-size:13px;color:#575A5D">Innenraumbilder: KI-generiert</p>''',
    '''tl.fromTo("#contact-rule",{scaleX:0},{scaleX:1,duration:0.65,ease:"power2.out"},0.45);
tl.fromTo("#contact-cta",{opacity:0},{opacity:1,duration:0.5,ease:"power2.out"},1.05);
tl.fromTo("#contact-domain",{opacity:0},{opacity:1,duration:0.5,ease:"power2.out"},2.0);
tl.fromTo("#contact-invite",{opacity:0},{opacity:1,duration:0.45,ease:"power2.out"},2.7);
tl.fromTo("#contact-disclosure",{opacity:0},{opacity:1,duration:0.45,ease:"power2.out"},3.4);''')

shots=[('hook',0,5),('portrait',5,7),('order',12,6),('design',18,6),('contact',24,6)]
variables=[{'id':'variant','type':'enum','label':'Filmvariante','default':'editorial','options':[{'value':'editorial','label':'Website-Bildwelt'},{'value':'wan','label':'Alibaba Wan 3.0'}]}]
hosts='\n'.join(f'<div id="{name}" class="clip" data-composition-id="{name}" data-composition-src="compositions/{name}.html" data-start="{start}" data-duration="{duration}" data-width="480" data-height="854" data-track-index="{i%2}" data-track-kind="graphics"></div>' for i,(name,start,duration) in enumerate(shots))
index=f'''<!doctype html>
<html lang="de" data-composition-variables='{json.dumps(variables)}'>
<head><meta charset="UTF-8"><meta name="viewport" content="width=480,height=854">
<title>Claudia Plessl — Vorstellung</title>
<script src="https://cdn.jsdelivr.net/npm/gsap@3.15.0/dist/gsap.min.js"></script>
<style>html,body{{margin:0;width:480px;height:854px;overflow:hidden;background:#F3EEE8}}*{{box-sizing:border-box}}#root{{position:relative;width:480px;height:854px;background:#F3EEE8;overflow:hidden}}.clip{{position:absolute;inset:0;width:100%;height:100%}}.stage-ground{{position:absolute;inset:0;background:#F3EEE8}}</style>
</head><body>
<div id="root" data-composition-id="main" data-start="0" data-duration="30" data-width="480" data-height="854" data-fps="30">
<div class="stage-ground"></div>
{hosts}
<audio id="music" class="clip" data-start="0" data-duration="30" data-track-index="8" data-volume="1" src="assets/music-soft.wav"></audio>
</div>
<script>
const tl=gsap.timeline({{paused:true}});
const values=window.__hyperframes?.getVariables?.() || {{variant:"editorial"}};
const wan=values.variant==="wan";
tl.set(".editorial-media",{{opacity:wan?0:1}},0);
tl.set(".wan-media",{{opacity:wan?1:0}},0);
window.__timelines=window.__timelines||{{}};
window.__timelines["main"]=tl;
// <seams:auto>
// </seams:auto>
</script></body></html>'''
(PROJECT/'index.html').write_text(index)
ledger={'fps':30,'seams':[{'id':f'{shots[i-1][0]}-to-{name}','cut':start,'technique':'cut-the-curve LEFT','exit':{'selector':f'#{shots[i-1][0]}-motion','axis':'x','dir':-1,'dur':0.32},'entry':{'selector':f'#{name}-motion','axis':'x','dir':-1,'dur':0.32,'travel':10}} for i,(name,start,duration) in enumerate(shots) if i]}
(PROJECT/'ledger.json').write_text(json.dumps(ledger,indent=2)+'\n')
print('Generated five scenes and the root composition, 480x854, 30 seconds.')
