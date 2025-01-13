import streamlit as st
import base64

# Set page configuration
st.set_page_config(page_title="CLEARVIEW: Interactive Air Quality Insights", layout="wide")

# Function to encode image to Base64
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Encode background image
background_base64 = encode_image("b.jpg")  # Change this to your image path

# Add custom CSS for background image and layout
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("data:image/png;base64,{background_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
            margin: 0;
            padding: 0;
            height: 100vh;
            overflow: hidden; /* Disable body scrolling */
        }}
        .stApp {{
            position: absolute;
            top: 50%;
            left: 10%;
            transform: translateY(-50%);
            max-width: 1200px;
            height: 700px;
            background: rgba(211, 211, 211, 0.7);
            padding: 30px;
            border-radius: 12px;
            border: 1px solid #ccc;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.3);
        }}
        h1, h2, h3 {{
            color: #333;
            font-weight: 600;
            animation: fadeInText 2s ease-in-out;
        }}
        .cta-button {{
            background-color: #4CAF50;
            color: white;
            padding: 15px 30px;
            border-radius: 10px;
            text-align: center;
            cursor: pointer;
            font-size: 20px;
            font-weight: bold;
            box-shadow: 0px 3px 5px rgba(0, 0, 0, 0.2);
        }}
        .cta-button:hover {{
            background-color: #45a049;
        }}
        @keyframes fadeInText {{
            0% {{ opacity: 0; }}
            100% {{ opacity: 1; }}
        }}
        .center-button {{
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
        }}
    </style>
    """,
    unsafe_allow_html=True,
)



# Hero Section with CTA button
st.markdown(
    """
    <div style="text-align:center; margin-bottom:20px;">
        <h1>CLEARVIEW: Interactive Air Quality Insights</h1>
        
    </div>
    """, unsafe_allow_html=True
)

# Streamlit button for redirection in the sidebar
if st.sidebar.button('Explore Air Quality Data'):
    # Display the link after the button is clicked
    st.sidebar.markdown(
        """
        <div style="text-align:center; margin-top:20px;">
            <a href="https://www.data.gov.in/catalog/real-time-air-quality-index" target="_blank">Click here to explore the Air Quality Data</a>
        </div>
        """, unsafe_allow_html=True
    )
if st.sidebar.button('AQI Calculator'):
    # Display the link after the button is clicked
    st.sidebar.markdown(
        """
        <div style="text-align:center; margin-top:20px;">
            <a href="https://www.airnow.gov/aqi/aqi-calculator/" target="_blank">Click here to AQI Calculator</a>
        </div>
        """, unsafe_allow_html=True
    )
# Introduction to Air Quality Insights

st.subheader("Overview")
st.markdown(""" 
    <div style="text-align: justify;">
        CLEARVIEW is a cutting-edge platform that provides real-time and historical air quality insights, helping you stay informed about the air you breathe. We monitor key pollutants like
        PM2.5, PM10, NO2, SO2, and O3 and provide accurate readings of the Air Quality Index (AQI) for your location. 
        Whether you're concerned about pollution levels in your city or planning outdoor activities, CLEARVIEW gives you the tools to understand air quality and its potential impact on your health.
        With CLEARVIEW, you can track trends, understand the health risks associated with different AQI levels, and take the necessary steps to protect yourself and your family. Our mission
        is to provide accessible, easy-to-understand air quality data so you can make informed decisions and improve your well-being, no matter where you live.
    </div>
""", unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; margin-top:20px;">
        <iframe width=100%" height="350" src="https://www.youtube.com/embed/d538jQc-pCM" frameborder="0" allow="accelerometer; autoplay; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    </div>
""", unsafe_allow_html=True)


st.subheader("Average of Gases")
background_base64 = encode_image("C:/Users/DELL/OneDrive/Desktop/p/a.png")

st.markdown(f"""
    <div style="text-align:center; margin-top:5px;">
        <img src="data:image/png;base64,{background_base64}" width="1000" style="border:2px solid black; border-radius:10px;">
    </div>
""", unsafe_allow_html=True)



# Key Metrics (AQI, PM2.5, CO2, etc.)
st.subheader("Key Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Air Quality Index (AQI)", value="55", delta="Up 5", help="Good air quality")
with col2:
    st.metric(label="PM2.5 (µg/m³)", value="12", delta="Down 2", help="Low pollution level")
with col3:
    st.metric(label="CO2 (ppm)", value="300", delta="Stable", help="Optimal air conditions")

# Adding the AQI Color Code Image under Key Metrics
st.subheader("AQI Colour Code")
st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <img src="https://www.deq.idaho.gov/wp-content/uploads/AQI-Page-Basics-for-Ozone-and-Particle-Pollution_5_7_20-1.png" width="1000" style="border:2px solid black; border-radius:10px;">
    </div>
""", unsafe_allow_html=True)

# Embedding the AQI Map (iframe)
st.subheader("Explore AQI Map")
st.markdown("""
    <div style="text-align:center; margin-top:30px;">
        <iframe src="https://aqicn.org/map/india/m/" width="100%" height="600" frameborder="0"></iframe>
    </div>
""", unsafe_allow_html=True)

# Features and Benefits Section
import streamlit as st

st.subheader("How It Works")
st.markdown("""
    <div style="text-align: justify;">
        Clearview Interactive Air Quality Insights works by aggregating and processing data from various sensors and APIs to provide both real-time and historical air quality information. It collects environmental data, including AQI, PM2.5, CO2, and other pollutants from sources like government databases and environmental monitoring stations. The collected data undergoes preprocessing to handle missing values, remove duplicates, and correct inconsistencies. Once cleaned, the data is structured into a star schema format, enabling efficient analysis and visualization. In Power BI, a user-friendly dashboard is developed with interactive elements such as filters and slicers, allowing users to explore AQI trends, regional comparisons, pollutant proportions, and historical changes. The dashboard incorporates various visualizations like line charts, bar charts, pie charts, and maps for a comprehensive understanding of air quality. By making the data accessible and interactive, Clearview empowers users to make informed decisions related to health, policy, and environmental sustainability.
    </div>
""", unsafe_allow_html=True)

st.subheader("Why It Matters")
st.markdown("""
    <div style="text-align: justify;">
        Good air quality is essential for your health. By monitoring air quality levels, you can take preventative steps to avoid harmful pollutants.
        Stay informed and protect yourself and your family from air pollution-related health issues.
    </div>
""", unsafe_allow_html=True)

params = st.query_params

# Page routing
if params.get("page") == "homes":
    st.title("Welcome to the Home Page")
    st.write("Explore all insights here.")
else:
    st.title("Call to Action: Explore Insights")
    st.markdown(
        """
        <div style="text-align:center; margin-top:30px;">
            <a href="/Home" style="text-decoration:none;">
                <button style="padding:10px 20px; font-size:16px; background-color:#007BFF; color:white; border:none; border-radius:5px; cursor:pointer;">
                    Get Started
                </button>
            </a>
        </div>
        """, unsafe_allow_html=True
    )
        
        
        
# Footer with additional resources and social media links
st.markdown(""" 
<div style="text-align:center; padding-top:30px;">
    <p><strong>Follow Us:</strong></p>
    <a href="https://facebook.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/5968/5968764.png" width="30">
            </a>
            <a href="https://twitter.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/3670/3670151.png" width="30">
            </a>
            <a href="https://linkedin.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/145/145807.png" width="30">
            </a>
            <a href="https://instagram.com" target="_blank">
                <img src="https://cdn-icons-png.flaticon.com/128/15707/15707749.png" width="30">
            </a>
</div>
""", unsafe_allow_html=True)

# Footer with privacy and contact info
st.markdown(""" 
<div style="text-align:center; padding-top:30px; font-size:14px;">
    <p><a href="https://www.yourwebsite.com/privacy" target="_blank">Privacy Policy</a> | <a href="https://www.yourwebsite.com/contact" target="_blank">Contact Us</a></p>
</div>
""", unsafe_allow_html=True)
