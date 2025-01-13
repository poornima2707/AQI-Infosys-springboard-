import streamlit as st
import base64
import os

# Set page configuration
st.set_page_config(page_title="Welcome Back!", layout="wide")

# Function to encode image to Base64 (with relative path handling)
def encode_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read()).decode()
        return encoded_string
    else:
        return None

# Encode background image (use relative path for portability)
background_image_path = "b.jpg"  # Update this with a relative path
background_base64 = encode_image(background_image_path)

# Add custom CSS for background image, layout, and styling
st.markdown(
    f"""
    <style>
        body {{
            background-image: url("data:image/png;base64,{background_base64}");
            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }}
        .stApp {{
            position: absolute;
            top: 50%;
            left: 10%;
            transform: translateY(-50%);
            max-width: 1200px;
            height: 700px; /* Adjust height */
            background: rgba(211, 211, 211, 0.6);
            padding: 5px; /* Reduce padding */
            border-radius: 8px; /* Slightly smaller border radius */
            border: 1px solid #ccc;
            box-shadow: 0px 3px 10px rgba(0, 0, 0, 0.2);
            overflow: hidden; /* Disable scrolling for the container */
            animation: slideUp 1s ease-out;
        }}
        .content {{
            display: flex;
            align-items: center;
            justify-content: space-between;
        }}
        .text-content {{
            width: 60%;
        }}
        .image-content {{
            width: 35%;
            display: flex;
            justify-content: center;
            align-items: center;
        }}
        .image-content img {{
            max-width: 100%;
            height: 650px;
            border-radius: 8px;
            box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.2);
        }}
    </style>
    """,
    unsafe_allow_html=True,
)

# Conclusion content with an image
image_path = "e.png"  # Replace with your image path
image_base64 = encode_image(image_path)

conclusion_content = f"""
<div class="content">
    <div class="text-content">
        <h2>📑 Conclusion:</h2>
        <ul>
            <li><strong>Key Findings:</strong>
                <ul>
                    <li>PM2.5, PM10, NO2, SO2, O3 levels and their health/environmental impacts.</li>
                    <li>Most polluted and cleanest states/cities identified.</li>
                    <li>AQI trends show pollution variations over time.</li>
                </ul>
            </li>
            <li><strong>Regional Comparison:</strong>
                <ul>
                    <li>Significant AQI differences across regions.</li>
                    <li>Performance influenced by industrial activity and emissions.</li>
                </ul>
            </li>
            <li><strong>Health and Environmental Implications:</strong>
                <ul>
                    <li>Pollution linked to respiratory, cardiovascular issues.</li>
                    <li>Environmental effects include reduced visibility and vegetation damage.</li>
                </ul>
            </li>
            <li><strong>Trend Analysis:</strong>
                <ul>
                    <li>Yearly/seasonal trends highlight improvement or deterioration.</li>
                    <li>Influenced by industrial activity, regulations, climate change.</li>
                </ul>
            </li>
            <li><strong>Recommendations:</strong>
                <ul>
                    <li>Stricter emission norms, promote public transport.</li>
                    <li>Raise public awareness about pollution effects.</li>
                </ul>
            </li>
            <li><strong>Future Scope:</strong>
                <ul>
                    <li>Improve data collection and dashboard updates for accurate insights.</li>
                </ul>
            </li>
        </ul>
    </div>
    <div class="image-content">
        <img src="data:image/png;base64,{image_base64}" alt="Conclusion Image">
    </div>
</div>
"""

# Add the Conclusion content to your Streamlit app
st.markdown(conclusion_content, unsafe_allow_html=True)
