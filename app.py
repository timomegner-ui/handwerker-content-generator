import os
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

st.set_page_config(
    page_title="Handwerker Content Generator",
    page_icon="🔨",
    layout="centered"
)

st.title("🔨 Handwerker Content Generator")
st.write(
    "Erstellt Social-Media-Content + fertige AI-Video-Prompts "
    "für Handwerker, Zimmerer, Dachdecker und lokale Betriebe."
)

branche = st.selectbox(
    "Branche",
    [
        "Zimmermann",
        "Dachdecker",
        "Maler",
        "Elektriker",
        "Sanitär",
        "Gartenbau",
        "Fliesenleger",
        "Tischler",
        "Allgemeines Handwerk"
    ]
)

topic = st.text_input(
    "Thema / Angebot",
    placeholder="z.B. freie Kapazitäten für Dachstuhl und Innenausbau"
)

platform = st.selectbox(
    "Plattform",
    ["Instagram", "TikTok", "LinkedIn", "Facebook"]
)

tone = st.selectbox(
    "Ton",
    [
        "Professionell",
        "Modern",
        "Locker",
        "Luxuriös",
        "Direkt",
        "Emotional",
        "Bodenständig"
    ]
)

target_group = st.text_input(
    "Zielgruppe",
    placeholder="z.B. Hausbesitzer, Bauherren, lokale Kunden"
)

goal = st.selectbox(
    "Ziel",
    ["Mehr Anfragen", "Mehr Reichweite", "Mehr Vertrauen", "Mehr Terminbuchungen"]
)

region = st.text_input(
    "Region / Stadt",
    placeholder="z.B. Villingen, Freiburg, Stuttgart oder 78052"
)

video_style = st.selectbox(
    "Video-Stil für AI-Prompts",
    [
        "Realistisch",
        "Cinematic",
        "Drohnenaufnahme",
        "Social Media Ad",
        "Vorher-Nachher",
        "Werkstatt / Behind the Scenes"
    ]
)

if st.button("Content generieren"):
    if not topic:
        st.warning("Bitte gib ein Thema ein.")
    else:
        prompt = f"""
        Du bist ein erfahrener Social-Media-Marketing-Experte für Handwerksbetriebe
        und ein Experte für AI-Video-Prompts für Kling AI, Runway und ähnliche Tools.

        Erstelle Content für:
        Branche: {branche}
        Thema: {topic}
        Plattform: {platform}
        Ton: {tone}
        Zielgruppe: {target_group}
        Ziel: {goal}
        Region/Stadt/PLZ: {region}
        Gewünschter Video-Stil: {video_style}

        Regeln für den Social-Media-Text:
        - Schreibe natürlich und nicht nach KI
        - Keine Floskeln wie "Traumprojekt wartet"
        - Keine Jahreszahlen in Hashtags
        - Keine übertriebenen Versprechen
        - Kurz, klar und verkaufsstark
        - Fokus auf echte Kundenanfragen
        - Schreibe auf Deutsch
        - Schreibe bodenständig, seriös und handwerklich
        - Falls eine Region angegeben wurde: nutze sie natürlich, z.B. "in Ihrer Nähe", "aus der Region" oder "rund um {region}"
        - Verwende keine PLZ unnatürlich mitten im Satz
        - Wenn die Region nur eine PLZ ist, nutze Formulierungen wie "aus Ihrer Region" oder "in Ihrer Nähe"

        Regeln für AI-Video-Prompts:
        - Schreibe die AI-Video-Prompts auf Englisch
        - Die Prompts sollen für Kling AI oder Runway geeignet sein
        - Realistisch, hochwertig, modern
        - Fokus auf Handwerk, Baustelle, Werkzeuge, Holz, Team, saubere Arbeit
        - Keine unrealistischen Szenen
        - Keine Logos oder Markennamen
        - Keine lesbaren Texte im Video
        - Jeder Prompt soll eine klare Szene beschreiben
        - Jeder Prompt soll Kamerabewegung, Lichtstimmung und Stil enthalten

        Gib die Antwort exakt in dieser Struktur aus:

        ## Hooks
        1.
        2.
        3.
        4.
        5.

        ## Caption kurz
        ...

        ## Caption emotional
        ...

        ## Caption professionell
        ...

        ## CTAs
        1.
        2.
        3.

        ## Hashtags
        ...

        ## Reel-Ideen
        1.
        2.
        3.

        ## AI Video Prompts für Kling / Runway

        ### Prompt 1
        ...

        ### Prompt 2
        ...

        ### Prompt 3
        ...

        ## Reel-Aufbau
        0-2 Sek: Hook
        2-6 Sek: Szene 1
        6-10 Sek: Szene 2
        10-15 Sek: CTA
        """

        with st.spinner("Generiere Content und Video-Prompts..."):
            response = client.responses.create(
                model="gpt-4.1-mini",
                input=prompt
            )

        result = response.output_text

        st.success("Fertig!")
        st.subheader("Ergebnis")
        st.markdown(result)

        st.download_button(
            label="Ergebnis als Text herunterladen",
            data=result,
            file_name="handwerker_content_mit_video_prompts.txt",
            mime="text/plain"
        )