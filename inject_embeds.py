import urllib.parse
import re

html_path = r"c:\Users\User\Desktop\fukumachi website\index.html"

# Group 1: Everything Lasts EP [USHBA001]
# Unhidden Perspicacity (Not in original SC list, dropping or assuming from next?), Everything lasts, Hedonism, Seventh Sense.
# From the provided URLs:
# "Hedonism": https://soundcloud.com/novafuture/fukumachi-hedonism-full-track
# "Everything lasts": https://soundcloud.com/vault-sessions-collective/premiere-fukumachi-everything-lasts-ushba001 or grabthegroove one (using vault sessions)
# "Seventh Sense": https://soundcloud.com/bcco/bcco-premiere-fukumachi-seventh-sense-ushba001
# "Unhidden Perspicacity": NOT FOUND in original URL list. Added placeholder or omitted for now. I will use the available ones.

ep_everything_lasts = [
    "https://soundcloud.com/novafuture/fukumachi-hedonism-full-track?si=bc7a52069b7d41a2af78fc315993acb8",
    "https://soundcloud.com/vault-sessions-collective/premiere-fukumachi-everything-lasts-ushba001?si=9f5a490023584d94952aaf34be1e6a9e",
    "https://soundcloud.com/bcco/bcco-premiere-fukumachi-seventh-sense-ushba001?si=4dd107a17c944fe6b7596b5335141667",
    "https://soundcloud.com/grabthegroove/gtg-premiere-fukumachi-everything-lasts-ushba001?si=d2a2ad80c003485097726dbb502f591b"
]

# Group 2: Melting Point EP [FR030]
# Melting Point, Bass is Mood (remove dupe), Complex Surface, Plasencia.
ep_melting_point = [
    "https://soundcloud.com/vault-sessions-collective/premiere-fukumachi-melting-point-fr030?si=825dda7a30294eda813906da7b2339c8",
    "https://soundcloud.com/format-amsterdam/fukumachi-bass-is-mood?si=800784635bca4caf9eacd69ffd00a55c",
    "https://soundcloud.com/hate_music/premiere-fukumachi-complex-surface-fr030?si=99bdda4903b140bf85212a5bb97fa518",
    "https://soundcloud.com/format-amsterdam/fukumachi-plasencia-fr030?si=4d917f918aa141259963279ee2ca5a08"
]

# Group 3: Nautilus EP [FR027]
# Nautilus, Berlandieri, Gijoe, Ziggy Tap.
ep_nautilus = [
    "https://soundcloud.com/novafuture/fukumachi-nautilus-full-track?si=cbae992018594bae82f4142696c5d0be",
    "https://soundcloud.com/hate_music/premiere-fukumachi-berlandieri-fr027?si=8cb763f5aae24a159f5a4604b4810b4c",
    "https://soundcloud.com/vault-sessions-collective/premiere-fukumachi-gijoe-fr027?si=459b502806d7439b9f4b8404c8c7b217",
    "https://soundcloud.com/duplicityedinburgh/premiere-fukumachi-ziggy-tap-fr027?si=15d6b2ea1d1845279ca9afcbb2b4fa7d"
]

# Group 4: VA Participations (Everything else from the original 27, minus duplicates & EPs)
ep_urls_flattened = set(ep_everything_lasts + ep_melting_point + ep_nautilus)

original_sc_tracks = [
    "https://soundcloud.com/fukumachi/fukumachi-into-the-void?si=a9e2189a86a548b8881f73a6840e46c9",
    "https://soundcloud.com/vault-sessions-collective/premiere-fukumachi-sakura-emerald025?si=3f6cd6e1a2a54edd806b9b00168ae1cb",
    "https://soundcloud.com/duplicityedinburgh/premiere-fukumachi-patagonia-boerdeva?si=751331256a48493db5a1a29a543485e2",
    "https://soundcloud.com/duplicityedinburgh/premiere-fukumachi-jimsher-comova01?si=9c6126225c8246518b2892a412222161",
    "https://soundcloud.com/markedamsterdam/fukumachi-japan-sea-prtl-wrx?si=7e2bf3790c5043e281a0cc97e35aabba",
    "https://soundcloud.com/markedamsterdam/fukumachi-asymmetric-radiance?si=be9d7dad2fec4acdac42eb6a23f7c6ec",
    "https://soundcloud.com/lostinether/lost-in-ether-p-r-e-m-i-e-r-e-boy-in-nature-club-function-fukumachi-remixic-trax?si=6263310d7f2148ce8a8d291ff5701c36",
    "https://soundcloud.com/differentsoundofficial/ds-premiere-fukumachi-waves-anima-002?si=45e0f50f6923471fa794a105a4a86b18",
    "https://soundcloud.com/vault-sessions-collective/premiere-kaiobarssalos-blind-fukumachi-remix-kysh-ep03?si=b00544b675374e3abdb9b82f02d518df",
    "https://soundcloud.com/markedamsterdam/fukumachi-existence-anima?si=c8a60408e7de4499b1fba90df2112c5a",
    "https://soundcloud.com/markedamsterdam/fukumachi-craftsmans-legacy-safe-space?si=206d14d8447a44d3bd3313fd0b09e80c",
    "https://soundcloud.com/vault-sessions-collective/premiere-juan-sanchez-fonkyzeit-fukumachi-remix-atdep007?si=53ad893a03664def8bc6a569c46a7e60",
    "https://soundcloud.com/aktivv/premiere-fukumachi-leviathan-om025?si=3906c10f28a94dab9d1d5bd65b4aa31e",
    "https://soundcloud.com/kollektivsynergie/syn-premier-fukumachi-no-excuse-analtd012ca?si=b7953a6ff6af4c788a9c0063506c4d06"
]

def generate_sc_html(url):
    encoded_url = urllib.parse.quote(url.split("?")[0]) # Drop duplicate query params
    return f'''<div class="embed-wrapper">
    <iframe width="100%" height="166" scrolling="no" frameborder="no" allow="autoplay"
        src="https://w.soundcloud.com/player/?url={encoded_url}&color=%23ff5500&auto_play=false&hide_related=false&show_comments=true&show_user=true&show_reposts=false&show_teaser=true"></iframe>
</div>'''

def generate_section(title, urls):
    content = f'<h3>{title}</h3>\\n'
    for url in urls:
        content += generate_sc_html(url) + "\\n"
    return content

final_sc_html = ""
final_sc_html += generate_section("Everything Lasts EP [USHBA001]", ep_everything_lasts)
final_sc_html += generate_section("Melting Point EP [FR030]", ep_melting_point)
final_sc_html += generate_section("Nautilus EP [FR027]", ep_nautilus)
final_sc_html += generate_section("VA Participations", original_sc_tracks)

with open(html_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace SC Tracks and completely remove Music Videos section
# The regex looks for <div class="embed-container soundcloud-embeds"> all the way to the end of <div class="releases-grid">
pattern = r'(<div class="releases-grid">\s*<!-- SoundCloud Tracks -->\s*<div class="embed-container soundcloud-embeds">).*?(</div>\s*</div>\s*</section>)'
replacement = r'\g<1>\n' + final_sc_html + r'</div>\n</div>\n</div>\n</section>'
content = re.sub(pattern, replacement, content, flags=re.DOTALL)

with open(html_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Injected grouped EPs and VAs successfully, removed Music Videos.")
