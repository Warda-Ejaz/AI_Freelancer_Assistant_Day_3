import streamlit as st
import pandas as pd
import plotly.express as px
import time
import re

st.set_page_config(page_title="AI Freelancer Assistant Pro - Day 3", layout="wide", page_icon="🚀")

# CSS for Pro UI
st.markdown("""
<style>
   .stButton>button { border-radius: 10px; background: linear-gradient(90deg, #4F46E5, #7C3AED); color: white; font-weight: bold; }
   .stTabs [data-baseweb="tab-list"] { gap: 24px; }
   .stMetric { background-color: #F3F4F6; padding: 10px; border-radius: 8px; }
</style>
""", unsafe_allow_html=True)

# Session State = Database Tables
if 'gig_descriptions' not in st.session_state: st.session_state.gig_descriptions = []
if 'pricing_history' not in st.session_state: st.session_state.pricing_history = []
if 'ai_credits' not in st.session_state: st.session_state.ai_credits = 200

def generate_gig_description(inputs):
    time.sleep(1) # AI wala feel
    desc = f"""**I will {inputs['service']} for you | {inputs['experience']} Level Expert**

Are you looking for a professional {inputs['service'].lower()} expert? You are at the right place!

**Why me?**
✅ {inputs['experience']} years of experience
✅ Skills: {inputs['skills']}
✅ {inputs['revisions']} Revisions included
✅ Delivery in {inputs['delivery']} days

**Gig Features:**
{inputs['features']}

Let's get started on your project today!"""

    keywords = f"{inputs['service']}, {inputs['skills'].replace(', ', ', ')}, freelance {inputs['service'].lower()}, {inputs['experience']} expert"

    faqs = f"""Q: Do you provide revisions?
A: Yes, I offer {inputs['revisions']} free revisions.

Q: What is the delivery time?
A: Standard delivery is {inputs['delivery']} days."""

    return desc, keywords, faqs

def calculate_price(rate, hours, complexity, urgency, tax):
    base = rate * hours
    comp_mult = {"Simple": 1.0, "Medium": 1.3, "Complex": 1.7}[complexity]
    urg_mult = {"Normal": 1.0, "Urgent +25%": 1.25, "Super Urgent +50%": 1.5}[urgency]

    subtotal = base * comp_mult * urg_mult
    tax_amount = subtotal * (tax/100)
    total = subtotal + tax_amount

    market_avg = rate * 1.2 * hours
    tip = "Increase your hourly rate by $5 if complexity is 'Complex'." if complexity == "Complex" else "Add portfolio samples to justify higher rates."

    return base, subtotal, tax_amount, total, market_avg, tip

st.title("🚀 AI Freelancer Assistant Pro - Day 3")
st.caption("Gig Description & Smart Pricing Module")

tab1, tab2, tab3 = st.tabs(["📊 Dashboard", "📝 Gig Description Generator", "💰 Smart Pricing Calculator"])

with tab1:
    st.subheader("Business Analytics")
    c1, c2, c3, c4 = st.columns(4)
    c1.metric("Gigs Created", len(st.session_state.gig_descriptions))
    c2.metric("Pricing Quotes", len(st.session_state.pricing_history))
    c3.metric("AI Credits Left", st.session_state.ai_credits)
    c4.metric("Avg Quote", f"${pd.DataFrame(st.session_state.pricing_history)['Total'].mean():.0f}" if st.session_state.pricing_history else "$0")

    if st.session_state.gig_descriptions or st.session_state.pricing_history:
        data = pd.DataFrame({
            "Type": ["Gigs"] * len(st.session_state.gig_descriptions) + ["Quotes"] * len(st.session_state.pricing_history)
        })
        fig = px.pie(data, names="Type", title='Activity Distribution')
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Generate your first Gig or Quote to see analytics.")

with tab2:
    st.subheader("AI Gig Description Generator")
    if st.session_state.ai_credits < 15: st.warning("Low AI Credits! 15 credits needed per gig.")

    with st.form("gig_form"):
        c1, c2, c3 = st.columns(3)
        service = c1.selectbox("Service Category", ["AI Bot Development", "Web Scraping", "Data Analysis", "Streamlit App", "Logo Design"])
        experience = c2.selectbox("Experience Level", ["Beginner", "Intermediate", "Expert"])
        delivery = c3.slider("Delivery Time - Days", 1, 30, 5)

        skills = st.text_input("Your Skills", "Python, Streamlit, AI, LangChain")
        features = st.text_area("Key Features", "Fast delivery, 24/7 support, Custom solution")
        revisions = st.selectbox("Revisions Included", ["1", "3", "Unlimited"])

        if st.form_submit_button("✨ Generate AI Gig + SEO + FAQ", use_container_width=True):
            if st.session_state.ai_credits >= 15 and service and skills:
                inputs = {"service":service, "skills":skills, "experience":experience, "delivery":delivery, "features":features, "revisions":revisions}
                desc, keywords, faqs = generate_gig_description(inputs)

                st.session_state.gig_descriptions.append({"Service": service, "Desc": desc[:50]+"..."})
                st.session_state.ai_credits -= 15

                st.success("Gig Generated Successfully!")
                st.text_area("AI Generated Description", desc, height=200)
                st.text_input("SEO Keywords", keywords)
                st.text_area("FAQ Suggestions", faqs, height=100)
                st.download_button("📥 Download Gig.txt", desc, f"gig_{re.sub(r'[^A-Za-z0-9]+', '_', service)}.txt")
            else:
                st.error("Fill all fields + Check AI Credits.")

with tab3:
    st.subheader("Smart Pricing Calculator")
    c1, c2 = st.columns(2)
    rate = c1.number_input("Hourly Rate $", 5, 200, 25)
    hours = c2.number_input("Estimated Hours", 1, 500, 20)

    c3, c4, c5 = st.columns(3)
    complexity = c3.selectbox("Project Complexity", ["Simple", "Medium", "Complex"])
    urgency = c4.selectbox("Urgency", ["Normal", "Urgent +25%", "Super Urgent +50%"])
    tax = c5.slider("Tax % Optional", 0, 30, 10)

    if st.button("💵 Calculate Smart Price", use_container_width=True):
        base, subtotal, tax_amt, total, market, tip = calculate_price(rate, hours, complexity, urgency, tax)

        st.session_state.pricing_history.append({"Rate": rate, "Hours": hours, "Total": total})

        st.subheader("💰 AI Price Breakdown")
        col1, col2, col3, col4 = st.columns(4)
        col1.metric("Base Price", f"${base:.2f}")
        col2.metric("After Complexity + Urgency", f"${subtotal:.2f}")
        col3.metric("Tax Amount", f"${tax_amt:.2f}")
        col4.metric("Suggested Price", f"${total:.2f}", delta=f"Market Avg: ${market:.0f}")

        st.info(f"**AI Market Analysis:** Market average for this work is ~${market:.0f}")
        st.success(f"**Service Improvement Tip:** {tip}")
