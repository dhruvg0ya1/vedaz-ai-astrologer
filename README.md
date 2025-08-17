
# Vedaz AI Astrologer

An intelligent Vedic astrology application that provides personalized astrological insights based on Indian astrology principles. This app combines traditional Vedic wisdom with modern AI (LLM integration) to deliver accurate readings based on Rashi, Nakshatra, and planetary positions.

## Features

* **Vedic Birth Chart Analysis** : Generate detailed astrological profiles using Indian astrology system
* **Rashi (Moon Sign) Detection** : Automatic calculation of Vedic moon sign with personality traits
* **Nakshatra Analysis** : Birth star influence on personality and life path according to Vedic tradition
* **Lunar Phase Analysis** : Moon phase influence on mind and emotional patterns
* **AI-Powered Q&A** : Advanced LLM integration (Groq Llama-3) for contextual, personalized responses
* **Intelligent Fallback** : Rule-based system ensures functionality even without API access
* **Dharmic Guidance** : AI responses based on Vedic principles and Sanskrit wisdom
* **Indian Context** : Specifically designed for Indian users with cultural relevance

## Quick Start

### Prerequisites

* Python 3.8 or higher
* pip package manager

### Installation

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd vedaz-ai-astrologer
   ```
2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the application**
   ```bash
   streamlit run app.py
   ```
4. **Open your browser**
   * The app will automatically open at `http://localhost:8501`
   * If it doesn't open automatically, navigate to the URL shown in your terminal

## LLM Integration Setup (Optional)

For enhanced AI-powered responses, you can integrate with Groq's Llama-3 model:

### **Quick Setup:**

1. **Get Free API Key** : Visit [Groq Console](https://console.groq.com/) and create account
2. **Create secrets file** :

```bash
   mkdir .streamlitecho 'GROQ_API_KEY = "your_api_key_here"' > .streamlit/secrets.toml
```

1. **Restart app** : The AI will now provide contextual, personalized responses

### **Without API Key:**

* App works perfectly with intelligent rule-based responses
* All features remain functional
* Shows info message about AI enhancement option

## How to Use

### Step 1: Enter Birth Details

* **Full Name** : Your complete name
* **Birth Date (Janma Tithi)** : Select your birth date from the calendar
* **Birth Time (Janma Samay)** : Choose your birth time (if unknown, default noon is used)
* **Birth Place (Janma Sthan)** : Enter your birth city and state in India

### Step 2: Generate Vedic Analysis

* Click "Generate Vedic Analysis"
* Wait for the ancient wisdom consultation to complete
* Review your personalized Vedic astrological insights

### Step 3: Ask Questions (AI-Powered)

* Use the text area to ask any question about your life
* **AI Enhancement** : With API key, get contextual responses based on your astrological profile
* **Smart Fallback** : Works without API using intelligent rule-based responses
* Topics can include: love/marriage, career, health, family, spirituality, etc.
* Click "Seek Vedic Guidance" for personalized AI-powered responses based on Vedic principles

## Technical Details

### Core Technologies

* **Streamlit** : Web application framework
* **PyEphem** : Astronomical calculations for moon phases and planetary positions
* **Geopy** : Location geocoding for birth place coordinates
* **PyTZ** : Timezone handling for accurate calculations
* **Groq API** : LLM integration for intelligent question answering (optional)
* **Llama-3-8B** : Advanced language model for contextual responses

### Vedic Astrology Components

* **Rashi Calculator** : Determines Vedic moon sign based on birth date
* **Nakshatra Detector** : Calculates birth star constellation
* **Lunar Phase Analysis** : Determines moon phase at birth time with Vedic interpretation
* **LLM Integration** : Advanced AI system for personalized, contextual responses
* **Intelligent Fallback** : Rule-based system ensures functionality without API access
* **Dharmic Guidance Database** : Comprehensive Vedic principles and Sanskrit knowledge

### File Structure

```
vedaz-ai-astrologer/
├── app.py              # Main application file
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── .gitignore         # Git ignore rules
```

## Configuration

### Environment Setup

No additional configuration required. The app uses default settings optimized for Indian astrology calculations.

### Customization Options

* Modify Rashi traits in the `rashi_traits` dictionary
* Add new Nakshatra meanings in the `nakshatra_meanings` dictionary
* Adjust Vedic response templates in the `response_templates` dictionary
* Customize UI colors and styling in the Streamlit markdown sections

## Dependencies

| Package   | Version | Purpose                               |
| --------- | ------- | ------------------------------------- |
| streamlit | 1.28.0  | Web interface framework               |
| geopy     | 2.4.0   | Location geocoding                    |
| pyephem   | 4.1.4   | Astronomical calculations             |
| pytz      | 2023.3  | Timezone handling                     |
| requests  | 2.31.0  | API communication for LLM integration |

## Deployment

### Local Development

```bash
streamlit run app.py
```

### Streamlit Cloud

1. Push code to GitHub repository
2. Connect repository to Streamlit Cloud
3. Deploy automatically from main branch

### Other Platforms

* **Heroku** : Add `Procfile` with `web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0`
* **Docker** : Create Dockerfile with Python base image and requirements installation

## Features Explained

### Vedic Birth Chart Analysis

The app calculates your Rashi (Vedic moon sign) based on your birth date and provides personality insights rooted in traditional Indian astrological interpretations.

### Nakshatra System

Uses the 27 Nakshatra system to provide deeper personality analysis. Each Nakshatra governs specific traits and karmic patterns according to Vedic tradition.

### AI-Powered Vedic Responses

The system uses advanced LLM integration (Groq Llama-3) to analyze your questions and provide contextually relevant responses based on your Vedic astrological profile. The AI incorporates:

* Your specific Rashi, Nakshatra, and lunar phase data
* Traditional dharmic principles and Sanskrit wisdom
* Cultural sensitivity for Indian context
* Practical guidance based on Vedic traditions

 **Intelligent Fallback** : If API access is unavailable, the system seamlessly switches to a sophisticated rule-based response system, ensuring the app always provides meaningful guidance.

### Indian Cultural Context

Responses include references to:

* Hindu festivals and traditions
* Sanskrit terminology
* Dharmic principles
* Ayurvedic concepts
* Spiritual practices
* Indian family values

## API Reference

### Core Functions

#### `get_rashi(birth_date)`

Returns Vedic Rashi (moon sign) based on birth date using sidereal zodiac

#### `get_nakshatra(birth_date)`

Calculates the birth Nakshatra (lunar mansion) from 27 Vedic constellations

#### `get_moon_phase(birth_date)`

Determines moon phase at birth time with Vedic lunar calendar names

#### `generate_ai_response(question, rashi, nakshatra, moon_phase, name)`

Generates personalized Vedic astrological response using LLM integration or intelligent fallback system

#### `get_coordinates(location)`

Geocodes birth location for astronomical calculations

## Vedic Astrology Concepts

### Rashi System

* Uses sidereal zodiac (Nirayana system)
* 12 Rashis with Sanskrit names
* Based on moon's position at birth time

### Nakshatra System

* 27 lunar mansions covering 360 degrees
* Each Nakshatra spans 13°20'
* Governs personality traits and destiny

### Lunar Phases

* Uses traditional Indian lunar calendar names
* Includes Purnima, Amavasya, and other phases
* Affects mental and emotional patterns

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/vedic-enhancement`)
3. Commit your changes (`git commit -am 'Add new Vedic feature'`)
4. Push to the branch (`git push origin feature/vedic-enhancement`)
5. Create a Pull Request

## Troubleshooting

### Common Issues

**App won't start**

* Check Python version (3.8+ required)
* Install requirements: `pip install -r requirements.txt`

**Location not found**

* Use format: "City, State, India" (e.g., "Mumbai, Maharashtra, India")
* Check internet connection for geocoding

**Astronomical calculations fail**

* Ensure birth date is valid
* Check system clock is correct

**AI responses seem generic**

* Add your Groq API key in `.streamlit/secrets.toml` for personalized AI responses
* Without API key, app uses intelligent rule-based responses (still functional)

**API integration not working**

* Check your internet connection
* Verify API key is correct in secrets file
* App automatically falls back to rule-based system if API fails

## Advanced Features

### LLM Integration Details

* **Model** : Groq Llama-3-8B for fast, accurate responses
* **Context Awareness** : AI considers user's complete astrological profile
* **Prompt Engineering** : Specialized prompts for Vedic astrology guidance
* **Response Optimization** : Limited to 100 words for concise, actionable advice
* **Cultural Sensitivity** : AI trained to provide culturally appropriate Indian context

### Deployment Configurations

#### **For Development:**

```bash
# Without API key
streamlit run app.py

# With API key
echo 'GROQ_API_KEY = "your_key"' > .streamlit/secrets.toml
streamlit run app.py
```

#### **For Production:**

Set environment variable or use Streamlit Cloud secrets management for API key storage.

## Cultural Sensitivity

This application is built with respect for Indian traditions and Vedic wisdom. It aims to provide guidance based on ancient knowledge while acknowledging that astrology should complement, not replace, practical decision-making. The AI integration ensures responses remain culturally appropriate and dharmic in nature.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

* Built with Streamlit for rapid web development
* Astronomical calculations powered by PyEphem
* Location services by Geopy and OpenStreetMap
* Inspired by ancient Vedic astrological traditions
* Designed specifically for Indian cultural context
* Created for Vedaz AI Expert internship program

## Support

For questions or issues:

1. Check the troubleshooting section
2. Open an issue on GitHub
3. Review the documentation

---

*Built with devotion using ancient Vedic knowledge | Powered by Vedaz AI | Sarve Bhavantu Sukhinah - May all beings be happy*
