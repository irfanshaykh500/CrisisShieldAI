import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time
from streamlit_option_menu import option_menu
from datetime import datetime

st.caption(
    f"Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
)

# Load Data
df = pd.read_csv("sample_incidents.csv")

# Page Config
st.set_page_config(
    page_title="CrisisShield AI",
    page_icon="🚨",
    layout="wide"
)

# Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #07111f 0%, #0f172a 50%, #111827 100%);
    color: #e5e7eb;
}

html, body, [class*="css"] {
    color: #e5e7eb !important;
}

h1 {
    color: #ffffff !important;
    font-size: 46px !important;
    font-weight: 900 !important;
}

h2, h3, h4 {
    color: #ffffff !important;
    font-weight: 800 !important;
}

p, label, div, span {
    color: #e5e7eb !important;
}

[data-testid="stMetric"] {
    background: linear-gradient(135deg, #111827, #1e293b);
    padding: 22px;
    border-radius: 18px;
    border: 1px solid #334155;
    box-shadow: 0 10px 30px rgba(0,0,0,0.35);
}

[data-testid="stMetricValue"] {
    color: #ffffff !important;
    font-size: 32px !important;
    font-weight: 900 !important;
}

[data-testid="stMetricLabel"] {
    color: #93c5fd !important;
    font-weight: 700 !important;
}

[data-testid="stDataFrame"] {
    background: #111827;
    border-radius: 16px;
    padding: 10px;
    border: 1px solid #334155;
}

.stButton button {
    background: linear-gradient(135deg, #dc2626, #ef4444);
    color: white !important;
    border-radius: 12px;
    padding: 12px 24px;
    border: none;
    font-weight: 800;
    box-shadow: 0 8px 25px rgba(239,68,68,0.35);
}

.stButton button:hover {
    background: linear-gradient(135deg, #b91c1c, #dc2626);
}

[data-testid="stExpander"] {
    background: #111827;
    border-radius: 16px;
    border: 1px solid #334155;
    box-shadow: 0 8px 24px rgba(0,0,0,0.3);
}

.stTabs [data-baseweb="tab-list"] {
    gap: 12px;
    background: #0f172a;
    padding: 12px;
    border-radius: 16px;
    border: 1px solid #334155;
}

.stTabs [data-baseweb="tab"] {
    background: #1e293b;
    color: #e5e7eb;
    border-radius: 12px;
    padding: 12px 20px;
    font-weight: 700;
}

.stTabs [aria-selected="true"] {
    background: linear-gradient(135deg, #dc2626, #ef4444) !important;
    color: white !important;
}

.stTextInput input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

hr {
    border-color: #334155;
}

</style>
""", unsafe_allow_html=True)

# Functions
def calculate_risk(severity):
    if severity >= 9:
        return "Critical"
    elif severity >= 7:
        return "High"
    elif severity >= 5:
        return "Medium"
    return "Low"

def confidence_score(severity):
    if severity >= 9:
        return "96%"
    elif severity >= 7:
        return "88%"
    elif severity >= 5:
        return "76%"
    return "65%"

def recommend_action(row):
    incident = row["type"]
    severity = row["severity"]

    if incident == "Cyberattack":
        return "Activate cyber incident response and isolate affected systems."
    elif incident == "Hospital Disruption":
        return "Switch to backup systems and prioritize patient safety."
    elif incident == "Misinformation":
        return "Verify information and issue official public communication."
    elif severity >= 9:
        return "Dispatch emergency response immediately."
    elif severity >= 7:
        return "Send field response teams and monitor escalation."
    return "Monitor situation closely."

# Add AI fields
df["risk_level"] = df["severity"].apply(calculate_risk)
df["ai_confidence"] = df["severity"].apply(confidence_score)
df["recommended_action"] = df.apply(recommend_action, axis=1)

# Header
st.markdown("""
# 🛡️ CrisisShield AI
### Emergency Command Intelligence Platform  
**Developed by Shaikh Irfan | Cybersecurity Researcher | IEEE Member**

AI-powered disaster response, cyber incident coordination, infrastructure protection, and emergency intelligence.
""")

# Navigation Menu
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚨 Command Center",
    "🗺️ Incident Map",
    "🤖 AI Recommendations",
    "💬 AI Analyst Assistant",
    "📋 Executive Summary"
])
# COMMAND CENTER
with tab1:

    st.markdown("""
## 🔴 Live Emergency Command Center
Monitor emergency events, cyber disruptions, infrastructure risks, and public safety alerts from one operational dashboard.
""")
    st.markdown("""
    <div style="
        background:linear-gradient(135deg, #111827, #1e293b);
        padding:24px;
        border-radius:18px;
        border:1px solid #334155;
        box-shadow:0 10px 30px rgba(0,0,0,0.35);
        margin-bottom:20px;
    ">
        <h3 style="margin-top:0; color:#ffffff;">
        ⚡ Live Emergency Alert Simulator
        </h3>
        <p style="color:#cbd5e1; margin-bottom:0;">
        Generate a simulated emergency alert to test AI triage, classification, and response routing.
        </p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("🚨 Generate Simulated Emergency Alert"):

        alert_types = [
            "Cyberattack",
            "Hospital Disruption",
            "Wildfire",
            "Flood",
            "Power Outage",
            "Misinformation",
            "Earthquake"
        ]

        alert_locations = [
            "Atlanta",
            "Miami",
            "New York",
            "Dallas",
            "Los Angeles",
            "Chicago",
            "San Francisco"
        ]

        alert_sources = [
            "SOC Monitoring",
            "911 Dispatch",
            "Weather Feed",
            "Utility Provider",
            "Social Media Intelligence",
            "Satellite Feed",
            "USGS Alert"
        ]

        new_alert_type = random.choice(alert_types)
        new_location = random.choice(alert_locations)
        new_source = random.choice(alert_sources)
        new_severity = random.randint(6, 10)

        if new_severity >= 9:
            new_risk = "Critical"
        elif new_severity >= 7:
            new_risk = "High"
        else:
            new_risk = "Medium"

        st.markdown(
            f"""
            <div style="
                background:#fff7ed;
                padding:22px;
                border-left:6px solid #f97316;
                border-radius:14px;
                box-shadow:0 8px 20px rgba(15,23,42,0.08);
                margin-bottom:20px;
            ">
                <h3 style="margin-top:0; color:#9a3412;">
                🚨 New Emergency Alert Generated
                </h3>
                <p><b>Incident Type:</b> {new_alert_type}</p>
                <p><b>Location:</b> {new_location}</p>
                <p><b>Source:</b> {new_source}</p>
                <p><b>Severity Score:</b> {new_severity}/10</p>
                <p><b>Risk Level:</b> {new_risk}</p>
                <p><b>AI Routing Status:</b> Classified, prioritized, and routed to emergency response queue.</p>
            </div>
            """,
            unsafe_allow_html=True
        )
    critical_count = len(df[df["risk_level"] == "Critical"])
    high_count = len(df[df["risk_level"] == "High"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Incidents", len(df))
    col2.metric("Critical Incidents", critical_count)
    col3.metric("High Risk Incidents", high_count)

    

    critical_df = df[df["risk_level"] == "Critical"]

    for _, row in critical_df.iterrows():

         with st.container(border=True):

            col_a, col_b = st.columns([4, 1])

            with col_a:
                st.markdown(f"### 🚨 {row['type']} — {row['location']}")

            with col_b:
                st.markdown(
    f"""
    <div style="
        background:linear-gradient(135deg,#7f1d1d,#991b1b);
        color:white;
        padding:10px 18px;
        border-radius:12px;
        text-align:center;
        font-weight:700;
        width:120px;
        margin-left:auto;
    ">
    {row['risk_level']}
    </div>
    """,
    unsafe_allow_html=True
)

            st.write(f"**Description:** {row['description']}")
            st.write(f"**Address:** {row['address']}")

            st.write(
                f"**Severity:** {row['severity']}/10 | "
                f"**AI Confidence:** {row['ai_confidence']} | "
                f"**Source:** {row['source']}"
            )

            st.markdown(
    f"""
    <div style="
        background:linear-gradient(135deg,#0f766e,#115e59);
        color:#ecfeff;
        padding:14px 18px;
        border-radius:14px;
        border-left:4px solid #14b8a6;
        margin-top:12px;
        font-weight:500;
    ">
    <b>Recommended Action:</b><br>
    {row['recommended_action']}
    </div>
    """,
    unsafe_allow_html=True
)
           
    st.subheader("Incident Feed")
    st.dataframe(df, use_container_width=True)

    chart = px.bar(
        df,
        x="type",
        y="severity",
        title="Incident Severity Analysis"
    )

    st.plotly_chart(chart, use_container_width=True)

# INCIDENT MAP
with tab2:

    st.subheader("🗺️ Real-Time Incident Map")

    map_fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="type",
        hover_data=[
            "location",
            "severity",
            "risk_level",
            "source"
        ],
        zoom=3,
        height=600
    )

    map_fig.update_layout(mapbox_style="open-street-map")
    map_fig.update_layout(
        margin={"r":0,"t":0,"l":0,"b":0}
    )

    st.plotly_chart(map_fig, use_container_width=True)

# AI RECOMMENDATIONS
with tab3:

    st.subheader("🤖 AI Response Recommendations")

    for _, row in df.iterrows():

        with st.expander(
            f"{row['type']} in {row['location']} — {row['risk_level']} Risk"
        ):

            st.write("Description:", row["description"])
            st.write("Source:", row["source"])
            st.write("Severity:", row["severity"])
            st.write("AI Confidence:", row["ai_confidence"])
            st.write(
                "Recommended Action:",
                row["recommended_action"]
            )
# AI ANALYST ASSISTANT
with tab4:

    st.subheader("🤖 AI Emergency Analyst Assistant")

    st.info(
    "Ask the AI Analyst Assistant about incident priority, cyber threats, response actions, or executive summaries."
)

    user_question = st.text_input(
        "Example: What is the highest risk incident?"
    )

    if user_question:

        question = user_question.lower()

        critical_df = df[df["risk_level"] == "Critical"]
        cyber_df = df[df["type"].isin(["Cyberattack", "Hospital Disruption"])]

        if "highest" in question or "dangerous" in question or "critical" in question:
            top_incident = df.sort_values(by="severity", ascending=False).iloc[0]

            st.success(
                f"The highest risk incident is {top_incident['type']} in {top_incident['location']} "
                f"with severity {top_incident['severity']}."
            )

            st.write("Recommended Action:", top_incident["recommended_action"])

        elif "cyber" in question or "hospital" in question:
            st.warning(
                f"CrisisShield AI found {len(cyber_df)} cyber or hospital-related incidents."
            )

            st.dataframe(
                cyber_df[["type", "location", "severity", "risk_level", "recommended_action"]],
                use_container_width=True
            )

        elif "summary" in question or "summarize" in question:
            st.info(
                f"CrisisShield AI is monitoring {len(df)} incidents. "
                f"{len(critical_df)} are critical. "
                f"{len(cyber_df)} involve cyber or hospital disruption."
            )

        elif "action" in question or "recommend" in question or "response" in question:
            st.write("""
Recommended response priority:
1. Activate emergency command center.
2. Prioritize critical incidents.
3. Protect healthcare and utility infrastructure.
4. Verify misinformation before public communication.
5. Dispatch field teams based on severity and location.
""")

        else:
            st.write("""
I can help answer:
- What is the highest risk incident?
- Summarize the situation.
- What cyber incidents exist?
- What action should responders take?
""")
# EXECUTIVE SUMMARY
with tab5:

    st.subheader("📋 Executive Emergency Summary")

    summary = """
<h3 style='margin-top:0;'>Operational Overview</h3>

CrisisShield AI detected <b>8 active emergency incidents</b> across multiple regions.

Critical incidents currently include:
<ul>
<li>Cyberattacks affecting operational systems</li>
<li>Wildfire escalation risks</li>
<li>Hospital infrastructure disruption</li>
<li>Earthquake-related infrastructure damage</li>
</ul>

AI analysis indicates elevated operational risk to:
<ul>
<li>Healthcare systems</li>
<li>Public safety infrastructure</li>
<li>Emergency response coordination</li>
</ul>

<h3>Recommended Immediate Actions</h3>

<ul>
<li>Activate emergency command center</li>
<li>Prioritize critical infrastructure protection</li>
<li>Dispatch coordinated field response teams</li>
<li>Increase cyber monitoring for healthcare and utility networks</li>
</ul>
"""
    st.markdown(
    f"""
    <div style="
        background:linear-gradient(135deg, #111827, #1e293b);
        padding:28px;
        border-radius:18px;
        border:1px solid #e2e8f0;
        box-shadow:0 8px 24px rgba(15,23,42,0.08);
        color:#0f172a;
        font-size:16px;
        line-height:1.6;
    ">

    <h3 style="margin-top:0; margin-bottom:12px;">
    Operational Overview
    </h3>

    <p style="margin-bottom:14px;">
    CrisisShield AI detected <b>8 active emergency incidents</b> across multiple regions.
    </p>

    <p style="margin-bottom:8px;">
    Critical incidents currently include:
    </p>

    <ul style="margin-top:0; margin-bottom:14px; padding-left:22px;">
        <li style="margin-bottom:6px;">Cyberattacks affecting operational systems</li>
        <li style="margin-bottom:6px;">Wildfire escalation risks</li>
        <li style="margin-bottom:6px;">Hospital infrastructure disruption</li>
        <li style="margin-bottom:6px;">Earthquake-related infrastructure damage</li>
    </ul>

    <p style="margin-bottom:8px;">
    AI analysis indicates elevated operational risk to:
    </p>

    <ul style="margin-top:0; margin-bottom:14px; padding-left:22px;">
        <li style="margin-bottom:6px;">Healthcare systems</li>
        <li style="margin-bottom:6px;">Public safety infrastructure</li>
        <li style="margin-bottom:6px;">Emergency response coordination</li>
    </ul>

    <h3 style="margin-top:10px; margin-bottom:8px;">
    Recommended Immediate Actions
    </h3>

    <ul style="margin-top:0; margin-bottom:0; padding-left:22px;">
        <li style="margin-bottom:6px;">Activate emergency command center</li>
        <li style="margin-bottom:6px;">Prioritize critical infrastructure protection</li>
        <li style="margin-bottom:6px;">Dispatch coordinated field response teams</li>
        <li>Increase cyber monitoring for healthcare and utility networks</li>
    </ul>

    </div>
    """,
    unsafe_allow_html=True
)

    st.write("""
CrisisShield AI analyzes emergency, cyber, infrastructure,
and misinformation reports to help response teams prioritize action
during fast-moving crisis situations.
""")

    st.markdown("### Key Findings")

    st.write(f"- Total incidents monitored: {len(df)}")

    st.write(
        f"- Critical incidents detected: {len(df[df['risk_level'] == 'Critical'])}"
    )

    st.write(
        f"- Cyber or hospital disruptions: {len(df[df['type'].isin(['Cyberattack', 'Hospital Disruption'])])}"
    )

    st.write("- Highest concern: critical infrastructure disruption.")
    st.write("- Recommended response: activate emergency workflow.")

    pie = px.pie(
        df,
        names="risk_level",
        title="Risk Distribution"
    )

    st.plotly_chart(pie, use_container_width=True)

st.markdown("---")
st.markdown("""
---
### CrisisShield AI
**Developed by Shaikh Irfan | Cybersecurity Researcher | IEEE Member**  
Built for emergency intelligence, disaster response, cyber incident coordination, and critical infrastructure protection.
""")