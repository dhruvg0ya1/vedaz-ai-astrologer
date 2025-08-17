import streamlit as st
import datetime
import random
from geopy.geocoders import Nominatim
import ephem
import pytz
import requests
import json

st.set_page_config(
    page_title="Vedaz AI Astrologer",
    page_icon="🔮",
    layout="wide"
)

def get_rashi(birth_date):
    month = birth_date.month
    day = birth_date.day
    
    if (month == 4 and day >= 14) or (month == 5 and day <= 14):
        return "Mesha"
    elif (month == 5 and day >= 15) or (month == 6 and day <= 14):
        return "Vrishabha"
    elif (month == 6 and day >= 15) or (month == 7 and day <= 14):
        return "Mithuna"
    elif (month == 7 and day >= 15) or (month == 8 and day <= 14):
        return "Karka"
    elif (month == 8 and day >= 15) or (month == 9 and day <= 14):
        return "Simha"
    elif (month == 9 and day >= 15) or (month == 10 and day <= 14):
        return "Kanya"
    elif (month == 10 and day >= 15) or (month == 11 and day <= 14):
        return "Tula"
    elif (month == 11 and day >= 15) or (month == 12 and day <= 14):
        return "Vrishchika"
    elif (month == 12 and day >= 15) or (month == 1 and day <= 14):
        return "Dhanus"
    elif (month == 1 and day >= 15) or (month == 2 and day <= 12):
        return "Makara"
    elif (month == 2 and day >= 13) or (month == 3 and day <= 14):
        return "Kumbha"
    else:
        return "Meena"

def get_western_zodiac(birth_date):
    month = birth_date.month
    day = birth_date.day
    
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "Aries"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "Taurus"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return "Gemini"
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return "Cancer"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "Leo"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "Virgo"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return "Libra"
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return "Scorpio"
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return "Sagittarius"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "Capricorn"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "Aquarius"
    else:
        return "Pisces"

def get_nakshatra(birth_date):
    nakshatras = [
        "Ashwini", "Bharani", "Krittika", "Rohini", "Mrigashira", "Ardra",
        "Punarvasu", "Pushya", "Ashlesha", "Magha", "Purva Phalguni", "Uttara Phalguni",
        "Hasta", "Chitra", "Swati", "Vishakha", "Anuradha", "Jyeshtha",
        "Mula", "Purva Ashadha", "Uttara Ashadha", "Shravana", "Dhanishta", "Shatabhisha",
        "Purva Bhadrapada", "Uttara Bhadrapada", "Revati"
    ]
    
    day_of_year = birth_date.timetuple().tm_yday
    nakshatra_index = (day_of_year * 27 // 365) % 27
    return nakshatras[nakshatra_index]

def get_moon_phase(birth_date):
    observer = ephem.Observer()
    moon = ephem.Moon()
    sun = ephem.Sun()
    
    observer.date = birth_date
    moon.compute(observer)
    sun.compute(observer)
    
    moon_lon = float(moon.hlon)
    sun_lon = float(sun.hlon)
    phase = (moon_lon - sun_lon) % (2 * 3.14159)
    
    if phase < 0.5:
        return "Amavasya (New Moon)"
    elif phase < 1.5:
        return "Shukla Pratipada"
    elif phase < 2.0:
        return "Shukla Saptami"
    elif phase < 2.5:
        return "Shukla Chaturdashi"
    elif phase < 3.5:
        return "Purnima (Full Moon)"
    elif phase < 4.5:
        return "Krishna Pratipada"
    elif phase < 5.5:
        return "Krishna Saptami"
    else:
        return "Krishna Chaturdashi"

def get_coordinates(location):
    try:
        geolocator = Nominatim(user_agent="vedic_astrologer_app")
        location_info = geolocator.geocode(location)
        if location_info:
            return location_info.latitude, location_info.longitude
        return None, None
    except:
        return None, None

def get_birth_chart_insights(name, birth_date, birth_time, location):
    rashi = get_rashi(birth_date)
    western_zodiac = get_western_zodiac(birth_date)
    nakshatra = get_nakshatra(birth_date)
    moon_phase = get_moon_phase(birth_date)
    
    rashi_traits = {
        "Mesha": ["dynamic", "leadership qualities", "ambitious", "sometimes impatient", "pioneering spirit"],
        "Vrishabha": ["stable", "practical", "determined", "appreciation for beauty", "strong-willed"],
        "Mithuna": ["intelligent", "communicative", "versatile", "curious nature", "adaptable"],
        "Karka": ["emotional", "caring", "intuitive", "protective", "family-oriented"],
        "Simha": ["confident", "generous", "natural leader", "creative", "dignified"],
        "Kanya": ["analytical", "perfectionist", "helpful", "organized", "detail-oriented"],
        "Tula": ["balanced", "diplomatic", "harmonious", "artistic", "fair-minded"],
        "Vrishchika": ["intense", "mysterious", "transformative", "passionate", "investigative"],
        "Dhanus": ["philosophical", "adventurous", "optimistic", "truth-seeking", "independent"],
        "Makara": ["disciplined", "ambitious", "practical", "responsible", "persevering"],
        "Kumbha": ["innovative", "humanitarian", "independent", "visionary", "unique"],
        "Meena": ["compassionate", "intuitive", "artistic", "spiritual", "empathetic"]
    }
    
    nakshatra_meanings = {
        "Ashwini": "healing abilities and quick action",
        "Bharani": "creativity and nurturing nature",
        "Krittika": "sharp intellect and determination",
        "Rohini": "artistic talents and material prosperity",
        "Mrigashira": "curiosity and search for knowledge",
        "Ardra": "transformation and emotional depth",
        "Punarvasu": "renewal and optimistic nature",
        "Pushya": "nourishing qualities and wisdom",
        "Ashlesha": "mystical abilities and intuition",
        "Magha": "ancestral connection and leadership",
        "Purva Phalguni": "creativity and enjoyment of life",
        "Uttara Phalguni": "generosity and helpful nature",
        "Hasta": "skillful hands and craftsmanship",
        "Chitra": "artistic expression and beauty",
        "Swati": "independence and flexibility",
        "Vishakha": "goal-oriented and determined",
        "Anuradha": "friendship and devotion",
        "Jyeshtha": "protective nature and seniority",
        "Mula": "getting to the root of matters",
        "Purva Ashadha": "invincibility and confidence",
        "Uttara Ashadha": "victory and achievement",
        "Shravana": "listening and learning abilities",
        "Dhanishta": "musical talents and prosperity",
        "Shatabhisha": "healing and mystical knowledge",
        "Purva Bhadrapada": "spiritual transformation",
        "Uttara Bhadrapada": "deep wisdom and compassion",
        "Revati": "prosperity and nurturing qualities"
    }
    
    traits = rashi_traits.get(rashi, ["unique", "special"])
    selected_traits = random.sample(traits, min(3, len(traits)))
    
    insights = f"""
    Namaste {name}! 🙏
    
    Based on your janma kundali, here is your vedic analysis:
    
    **🌙 Vedic Rashi (Moon Sign)**: {rashi}
    
    **⭐ Western Sun Sign**: {western_zodiac}
    
    **✨ Janma Nakshatra**: {nakshatra}
    
    **🌛 Moon Phase**: {moon_phase}
    
    **🔮 Core Personality**: As a {rashi} rashi individual, you possess {', '.join(selected_traits[:-1])} and {selected_traits[-1]} qualities.
    
    **⭐ Nakshatra Influence**: Your {nakshatra} nakshatra bestows you with {nakshatra_meanings.get(nakshatra, 'special qualities')}. This celestial mansion governs your deeper personality traits and karmic patterns.
    
    **🌙 Lunar Influence**: Being born during {moon_phase} indicates your mind and emotional nature are influenced by this lunar energy, affecting your intuition and subconscious patterns.
    
    **🪐 Current Planetary Period**: The cosmic energies suggest favorable time for {random.choice(['career advancement', 'spiritual growth', 'relationship harmony', 'financial prosperity', 'health improvement', 'education and learning'])}.
    
    **🕉️ Vedic Guidance**: Your dharmic path involves balancing your {selected_traits[0]} nature with developing {random.choice(['patience', 'compassion', 'wisdom', 'devotion', 'detachment'])}. Focus on {random.choice(['meditation', 'seva (service)', 'dharmic actions', 'spiritual practices', 'positive karma'])}.
    """
    
    return insights, rashi, nakshatra, moon_phase

def generate_ai_response(question, rashi, nakshatra, moon_phase, name):
    try:
        prompt = f"""You are an expert Vedic astrologer providing guidance to {name}. 

User's Astrological Profile:
- Rashi (Moon Sign): {rashi}
- Nakshatra (Birth Star): {nakshatra}
- Moon Phase at Birth: {moon_phase}

User's Question: "{question}"

Provide a concise, relevant Vedic astrology response (2-3 sentences) that:
1. References their astrological profile
2. Gives practical guidance based on Vedic principles
3. Uses respectful tone with occasional Sanskrit terms
4. Focuses on dharmic solutions

Keep response under 100 words and culturally appropriate for Indian context."""

        api_url = "https://api.groq.com/openai/v1/chat/completions"
        
        headers = {
            "Authorization": f"Bearer {st.secrets.get('GROQ_API_KEY', 'demo_key')}",
            "Content-Type": "application/json"
        }
        
        data = {
            "model": "llama3-8b-8192",
            "messages": [
                {"role": "system", "content": "You are a wise Vedic astrologer providing concise, culturally sensitive guidance."},
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 150,
            "temperature": 0.7
        }
        
        if st.secrets.get('GROQ_API_KEY'):
            response = requests.post(api_url, headers=headers, json=data, timeout=10)
            if response.status_code == 200:
                result = response.json()
                return result['choices'][0]['message']['content'].strip()
    
    except Exception as e:
        st.error(f"API Error: Using fallback response system")
    
    question_lower = question.lower()
    
    response_templates = {
        "love": [
            f"According to Vedic astrology, {name}, your {rashi} rashi indicates that Venus is favorably placed in your chart. Your {nakshatra} nakshatra suggests deep emotional connections are destined.",
            f"The cosmic energies show that your {rashi} nature attracts partners who complement your spiritual journey. The current planetary transits favor romantic relationships.",
            f"Your {nakshatra} nakshatra governs relationships through dharmic connections. Look for someone who shares your values and supports your spiritual growth, {name}."
        ],
        "career": [
            f"Jupiter's blessings are evident in your professional sector, {name}. Your {rashi} rashi indicates natural talents in fields that require {random.choice(['leadership', 'creativity', 'analysis', 'communication', 'service'])}.",
            f"The planetary positions suggest your {nakshatra} nakshatra brings success through {random.choice(['dedication', 'innovation', 'helping others', 'artistic expression', 'spiritual work'])}. Mars energizes your career house.",
            f"Your dharmic career path aligns with your {rashi} qualities. Consider fields related to {random.choice(['education', 'healthcare', 'technology', 'finance', 'arts', 'spirituality'])}."
        ],
        "money": [
            f"Goddess Lakshmi favors those who follow dharma, {name}. Your {rashi} nature attracts wealth through {random.choice(['honest work', 'creative endeavors', 'service to others', 'business ventures', 'investments'])}.",
            f"The {nakshatra} nakshatra indicates multiple sources of income. Your financial growth comes through patience and righteous means.",
            f"Mercury and Jupiter influence your wealth sectors positively. Your {rashi} practical nature will guide you to prosperous decisions in the coming months."
        ],
        "health": [
            f"Your {rashi} constitution requires attention to {random.choice(['digestive health', 'stress management', 'physical exercise', 'mental peace', 'spiritual practices'])}. Ayurvedic remedies will benefit you.",
            f"The {nakshatra} nakshatra governs your vitality. Include yoga, pranayama, and meditation in your daily routine for optimal health, {name}.",
            f"Planetary positions suggest focusing on {random.choice(['proper sleep', 'healthy diet', 'regular exercise', 'stress reduction', 'spiritual healing'])} for maintaining good health."
        ],
        "family": [
            f"Your {rashi} nature creates harmony in family relationships. The {nakshatra} nakshatra blesses you with strong family bonds and ancestral support.",
            f"Family karma is favorably placed in your chart, {name}. Your role is to be the {random.choice(['peacemaker', 'supporter', 'guide', 'protector', 'nurturer'])} in family matters.",
            f"The cosmic energies suggest family celebrations and positive events in the near future. Your {rashi} qualities strengthen family unity."
        ],
        "spiritual": [
            f"Your spiritual journey is guided by your {nakshatra} nakshatra, {name}. This is an auspicious time for {random.choice(['meditation', 'temple visits', 'studying scriptures', 'seva activities', 'guru guidance'])}.",
            f"The {rashi} rashi indicates natural spiritual inclinations. Your path involves {random.choice(['bhakti yoga', 'karma yoga', 'jnana yoga', 'raja yoga', 'devotional practices'])}.",
            f"Planetary positions favor spiritual growth. Consider regular practices like mantra chanting, reading Bhagavad Gita, or visiting sacred places."
        ]
    }
    
    if any(word in question_lower for word in ["love", "marriage", "relationship", "partner", "spouse", "shaadi"]):
        return random.choice(response_templates["love"])
    elif any(word in question_lower for word in ["career", "job", "work", "business", "naukri", "profession"]):
        return random.choice(response_templates["career"])
    elif any(word in question_lower for word in ["money", "wealth", "finance", "paisa", "income", "dhan"]):
        return random.choice(response_templates["money"])
    elif any(word in question_lower for word in ["health", "swasthya", "illness", "disease", "fitness"]):
        return random.choice(response_templates["health"])
    elif any(word in question_lower for word in ["family", "parents", "children", "parivar", "mata", "pita"]):
        return random.choice(response_templates["family"])
    elif any(word in question_lower for word in ["spiritual", "dharma", "karma", "god", "bhagwan", "meditation", "temple"]):
        return random.choice(response_templates["spiritual"])
    else:
        general_responses = [
            f"The cosmic energies surrounding your question are complex, {name}. Your {rashi} wisdom combined with {nakshatra} guidance suggests trusting your inner voice.",
            f"According to Vedic principles, this matter will resolve through dharmic action. Your {rashi} nature already knows the righteous path forward.",
            f"The planets indicate that patience and devotion will bring clarity to your situation. Your {nakshatra} nakshatra supports spiritual solutions.",
            f"Lord Krishna teaches us in Bhagavad Gita that we have the right to perform our actions, but not to the fruits of action. Your {rashi} duty is clear, {name}.",
            f"The answer lies within your heart chakra. Your {nakshatra} nakshatra connects you to divine guidance. Practice meditation for inner clarity."
        ]
        return random.choice(general_responses)

def main():
    st.markdown("""
    <div style='text-align: center; padding: 20px;'>
        <h1>🔮 Vedaz AI Astrologer ✨</h1>
        <p style='font-size: 18px; color: #666;'>Discover your cosmic blueprint through ancient Indian astrology</p>
        <p style='font-size: 14px; color: #888;'>Powered by Vedaz AI Technology</p>
    </div>
    """, unsafe_allow_html=True)
    
    if 'user_data' not in st.session_state:
        st.session_state.user_data = None
    
    with st.container():
        col1, col2 = st.columns([1, 1])
        
        with col1:
            st.markdown("### 📝 Your Janma Kundali Details")
            
            name = st.text_input("Full Name", placeholder="Enter your full name")
            birth_date = st.date_input("Birth Date (Janma Tithi)", min_value=datetime.date(1900, 1, 1), max_value=datetime.date.today())
            birth_time = st.time_input("Birth Time (Janma Samay)", value=datetime.time(12, 0))
            location = st.text_input("Birth Place (Janma Sthan)", placeholder="City, State, India")
            
            if st.button("🔮 Generate Vedic Analysis", type="primary"):
                if name and birth_date and location:
                    with st.spinner("🙏 Consulting ancient Vedic wisdom..."):
                        insights, rashi, nakshatra, moon_phase = get_birth_chart_insights(name, birth_date, birth_time, location)
                        st.session_state.user_data = {
                            'name': name,
                            'insights': insights,
                            'rashi': rashi,
                            'nakshatra': nakshatra,
                            'moon_phase': moon_phase
                        }
                else:
                    st.error("Please fill in all required fields")
        
        with col2:
            if st.session_state.user_data:
                st.markdown("### ⭐ Your Vedic Profile")
                st.markdown(st.session_state.user_data['insights'])
            else:
                st.markdown("""
                ### 🌟 What You Will Discover
                
                **🌙 Rashi Analysis**: Deep insights into your moon sign characteristics
                
                **⭐ Nakshatra Wisdom**: Your birth star's influence on personality and destiny
                
                **🌛 Lunar Influence**: How moon phases affect your mind and emotions
                
                **🕉️ Dharmic Guidance**: Cosmic directions for your spiritual journey
                
                **🪐 Current Planetary Periods**: What the celestial bodies indicate for you now
                """)
    
    if st.session_state.user_data:
        st.markdown("---")
        st.markdown("### 🙏 Ask the Divine")
        
        question = st.text_area(
            "What guidance do you seek from the cosmic forces?",
            placeholder="Ask about love, career, health, family, spirituality, or any concern...",
            height=100
        )
        
        if st.button("✨ Seek Vedic Guidance", type="secondary"):
            if question.strip():
                with st.spinner("🔮 Consulting the ancient wisdom..."):
                    response = generate_ai_response(
                        question, 
                        st.session_state.user_data['rashi'], 
                        st.session_state.user_data['nakshatra'],
                        st.session_state.user_data['moon_phase'], 
                        st.session_state.user_data['name']
                    )
                    
                    st.markdown("#### 🌟 Divine Response")
                    st.success(response)
            else:
                st.warning("Please enter your question first")
    
    st.markdown("---")
    st.markdown("""
    <div style='text-align: center; color: #666; font-size: 12px;'>
        Built with devotion using ancient Vedic knowledge 🕉️ | Powered by Vedaz AI ⚡ | Sarve Bhavantu Sukhinah - May all beings be happy 🌸
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()