import streamlit as st
import pandas as pd
import plotly.express as px
import random
import time
from streamlit_option_menu import option_menu

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
    background-color: #0f172a;
    color: white;
}

html, body, [class*="css"] {
    color: white !important;
}

h1, h2, h3, h4, h5, h6, p, label, div, span {
    color: white !important;
}

[data-testid="stMetricValue"] {
    color: white !important;
}

[data-testid="stMetricLabel"] {
    color: #cbd5e1 !important;
}

.alert-box {
    background-color: #7f1d1d;
    padding: 15px;
    border-radius: 10px;
    color: white;
    font-weight: bold;
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
st.title("🚨 CrisisShield AI")
st.caption("AI-Powered Emergency Intelligence Platform")

# Navigation Menu
selected = option_menu(
    menu_title=None,
    options=[
    "Command Center",
    "Incident Map",
    "AI Recommendations",
    "AI Analyst Assistant",
    "Executive Summary"
],
    icons=[
    "speedometer2",
    "geo-alt",
    "robot",
    "chat-dots",
    "clipboard-data"
],
    orientation="horizontal"
)

# COMMAND CENTER
if selected == "Command Center":

    st.subheader("🔴 Live Emergency Command Center")
    st.markdown("### ⚡ Live Alert Simulator")

    if st.button("Generate New Emergency Alert"):
        alert_types = ["Fire", "Flood", "Cyberattack", "Power Outage", "Hospital Disruption", "Misinformation", "Wildfire", "Earthquake"]
        alert_locations = ["Atlanta", "Miami", "New York", "Dallas", "Los Angeles", "Chicago", "San Francisco"]
        alert_sources = ["911", "Weather", "SOC", "Utility", "Social Media", "Satellite", "USGS"]

        new_alert_type = random.choice(alert_types)
        new_location = random.choice(alert_locations)
        new_source = random.choice(alert_sources)
        new_severity = random.randint(5, 10)

        st.error(f"🚨 NEW ALERT: {new_alert_type} reported in {new_location}")
        st.write(f"Severity: {new_severity}")
        st.write(f"Source: {new_source}")
        st.write("AI Status: Alert classified and routed to response queue.")

    critical_count = len(df[df["risk_level"] == "Critical"])
    high_count = len(df[df["risk_level"] == "High"])

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Incidents", len(df))
    col2.metric("Critical Incidents", critical_count)
    col3.metric("High Risk Incidents", high_count)

    st.markdown("### Priority Alerts")

    critical_df = df[df["risk_level"] == "Critical"]

    for _, row in critical_df.iterrows():

        st.markdown(
            f"""
            <div class="alert-box">
            {row['type']} detected in {row['location']}
            | Severity: {row['severity']}
            | AI Confidence: {row['ai_confidence']}
            </div>
            """,
            unsafe_allow_html=True
        )
        

        st.write(row["description"])
        st.write("Recommended Action:", row["recommended_action"])
        st.divider()

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
elif selected == "Incident Map":

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
elif selected == "AI Recommendations":

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
elif selected == "AI Analyst Assistant":

    st.subheader("🤖 AI Emergency Analyst Assistant")

    st.write("Ask a question about the current emergency situation.")

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
elif selected == "Executive Summary":

    st.subheader("📋 Executive Emergency Summary")

    summary = f"""
CrisisShield AI detected {len(df)} active emergency incidents across multiple regions.

Critical incidents include cyberattacks, wildfire escalation,
hospital disruption, and earthquake-related infrastructure damage.

AI analysis indicates elevated operational risk to healthcare systems,
public safety infrastructure, and emergency response coordination.

Recommended immediate actions:
- Activate emergency command center
- Prioritize critical infrastructure protection
- Dispatch coordinated field response teams
- Increase cyber monitoring for healthcare and utility networks
"""

    st.markdown(
        f"""
        <div style="
            background-color:#1e293b;
            padding:20px;
            border-radius:10px;
            color:white;
            border:1px solid #334155;
            white-space: pre-wrap;
            font-size:16px;
        ">
        {summary}
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
st.caption("CrisisShield AI | IEEE Response Quest Challenge Prototype")