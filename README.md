# AI_Freelancer_Assistant_Day_3

A complete Streamlit-based SaaS tool for freelancers to generate high-converting Fiverr/Upwork gigs and calculate optimized project pricing using AI logic.

### ✨ Core Features

#### 1. **AI Gig Description Generator**
- **Inputs**: Service Category, Skills, Experience Level, Delivery Time, Features, Revisions
- **Outputs**: AI-Generated Gig Description, SEO Keywords, FAQ Suggestions
- **Download**: One-click `.txt` export for Fiverr/Upwork

#### 2. **Smart Pricing Calculator**
- **Inputs**: Hourly Rate, Estimated Hours, Project Complexity, Urgency, Tax %
- **Logic**: Dynamic multipliers for `Complexity` and `Urgency` + Tax calculation
- **Outputs**: Suggested Price, Market Analysis, Service Improvement Tips

#### 3. **Business Dashboard & Database**
- **Analytics**: Live metrics for Gigs Created, Quotes Generated, AI Credits Left
- **Visualization**: Interactive Plotly Pie Chart for activity distribution
- **Database**: In-memory storage using `st.session_state` for `Gig Descriptions` and `Pricing History`

### 🛠️ Tech Stack

| Category | Technology |
| --- | --- |
| **Framework** | Streamlit |
| **Data & Logic** | Python, Pandas |
| **Visualization** | Plotly Express |
| **State Mgmt** | Streamlit Session State |

### 🚀 Local Setup & Run

1. **Clone & Navigate**
    ```bash
    git clone <https://github.com/Warda-Ejaz/AI_Freelancer_Assistant_Day_3/edit/main>
    cd AI_FREELANCER_DAY_3
2. *Install Dependencies*
    pip install streamlit pandas plotly
3. *Launch the App*
    streamlit run app.py
App will run at `http://localhost:8501`

---
*Developed by:* Warda Ejaz
*Task:* Day 3 - Gig Description & Smart Pricing Module
*Program:*  AI Freelancer System 
