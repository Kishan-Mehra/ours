import streamlit as st

# App Configuration
st.set_page_config(page_title="OUR PRODUCT", page_icon="🌐", layout="wide")

# Custom CSS for Modern Styling with Smooth Scroll
st.markdown(
    """
    <style>
    html {
        scroll-behavior: smooth;
    }
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;600&display=swap');

    /* Base Styles */
    body {
        font-family: 'Inter', sans-serif;
        background-color: #f7f8fa;
        margin: 0;
        padding: 0;
        scroll-behavior: smooth; /* Added for smooth scrolling */
    }

    h1, h2, h3 {
        font-family: 'Inter', sans-serif;
    }

    /* Fullscreen Sections */
    .section {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100vh;
        padding: 20px;
    }

    /* Header Section */
    .header {
        background: linear-gradient(135deg, #4A154B, #612E74);
        color: white;
        text-align: center;
        padding: 0 20px;
        border-radius: 15px;
    }

    .header h1 {
        font-size: 56px;
        margin-bottom: 20px;
    }

    .header p {
        font-size: 22px;
        margin-bottom: 40px;
    }

    .header .cta {
        display: inline-block;
        padding: 15px 30px;
        font-size: 18px;
        color: white;
        background-color: #36C5F0;
        border-radius: 5px;
        text-decoration: none;
        transition: background 0.3s ease;
        cursor: pointer; /* Added to show it's clickable */
    }

    .header .cta:hover {
        background-color: #2A9FD8;
    }

    /* Features Section */
    .features {
        background-color: white;
        text-align: center;
        border-radius: 15px;
        padding: 20px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
    }

    .features h2 {
        font-size: 48px;
        color: #333;
        margin-bottom: 20px;
    }

    .features .feature-item {
        margin: 20px auto;
        max-width: 600px;
        font-size: 18px;
        color: #555;
    }

    /* Pricing Section */
    .pricing {
        background-color: #f3f3f3;
        text-align: center;
        border-radius: 15px;
    }

    .pricing h2 {
        font-size: 48px;
        color: #333;
        margin-bottom: 20px;
    }

    .pricing .price-card {
        display: inline-block;
        margin: 10px;
        padding: 20px;
        background-color: white;
        border-radius: 8px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        max-width: 300px;
        transition: transform 0.3s ease;
    }

    .pricing .price-card:hover {
        transform: scale(1.05);
    }

    .pricing .price-card h3 {
        font-size: 24px;
        color: #333;
        margin-bottom: 10px;
    }

    .pricing .price-card p {
        font-size: 18px;
        color: #555;
        margin-bottom: 20px;
    }

    /* Footer */
    .footer {
        background: linear-gradient(135deg, #4A154B, #612E74);
        color: white;
        text-align: center;
        padding: 40px 20px;
        border-radius: 15px;
    }

    .footer p {
        font-size: 16px;
        margin: 0;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Embed HTML with Smooth Scroll JavaScript
st.markdown(
    """
    <div class="header section">
        <div>
            <h1>Welcome to Your Professional SaaS</h1>
            <p>Effortless collaboration, seamless communication, and a modern design.</p>
            <a href="#pricing" class="cta" onclick="smoothScrollToPricing()">Explore Pricing</a>
        </div>
    </div>

    <div id="features" class="features section">
        <div>
            <h2>Why Choose Us?</h2>
            <div class="feature-item">🚀 Powerful Tools to Enhance Productivity</div>
            <div class="feature-item">🔒 Secure Communication Channels</div>
            <div class="feature-item">🌐 Scalable and Reliable Infrastructure</div>
        </div>
    </div>

    <div id="pricing" class="pricing section">
        <div>
            <h2>Pricing Plans</h2>
            <div class="price-card">
                <h3>Free Plan</h3>
                <p>$0/month</p>
                <p>Basic Features</p>
            </div>
            <div class="price-card">
                <h3>Pro Plan</h3>
                <p>$10/month</p>
                <p>Advanced Features</p>
            </div>
            <div class="price-card">
                <h3>Enterprise</h3>
                <p>Custom Pricing</p>
                <p>Complete Package</p>
            </div>
        </div>
    </div>

    <div class="footer section">
        <p>&copy; 2024 InfiniteWorld.org. All Rights Reserve To This Website.</p>
    </div>

    <script>
    function smoothScrollToPricing() {
        document.getElementById('pricing').scrollIntoView({
            behavior: 'smooth'
        });
    }
    </script>
    """,
    unsafe_allow_html=True,
)