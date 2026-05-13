import streamlit as st
import pandas as pd
import plotly.express as px
import random
from datetime import datetime

# Page Config
st.set_page_config(
    page_title="CrisisShield AI",
    page_icon="🛡️",
    layout="wide"
)

# Load Data
df = pd.read_csv("sample_incidents.csv")

# Safety check for address column
if "address" not in df.columns:
    df["address"] = "Address not available"

df["address"] = df["address"].fillna("Address not available")


# Styling
st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #07111f 0%, #0f172a 55%, #111827 100%);
    color: #e5e7eb;
}

html, body, [class*="css"] {
    color: #e5e7eb !important;
}

h1, h2, h3, h4 {
    color: #ffffff !important;
    font-weight: 800 !important;
}

p, label, div, span {
    color: #e5e7eb !important;
}

.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
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

.stButton button {
    background: linear-gradient(135deg, #dc2626, #ef4444);
    color: white !important;
    border-radius: 12px;
    padding: 12px 24px;
    border: none;
    font-weight: 800;
    box-shadow: 0 8px 25px rgba(239,68,68,0.35);
}

.stTextInput input {
    background-color: #111827 !important;
    color: white !important;
    border: 1px solid #334155 !important;
    border-radius: 12px !important;
    padding: 12px !important;
}

[data-testid="stDataFrame"] {
    background: #111827;
    border-radius: 16px;
    padding: 10px;
    border: 1px solid #334155;
}

[data-testid="stExpander"] {
    background: #111827;
    border-radius: 16px;
    border: 1px solid #334155;
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
        return "Activate cyber incident response, isolate affected systems, and protect critical services."
    elif incident == "Hospital Disruption":
        return "Switch to backup systems, notify medical leadership, and prioritize patient safety."
    elif incident == "Misinformation":
        return "Verify information, issue official public communication, and monitor social channels."
    elif severity >= 9:
        return "Dispatch emergency response immediately and activate command center."
    elif severity >= 7:
        return "Send field response teams and monitor escalation."
    return "Monitor situation closely and verify additional reports."


# Add AI fields
df["risk_level"] = df["severity"].apply(calculate_risk)
df["ai_confidence"] = df["severity"].apply(confidence_score)
df["recommended_action"] = df.apply(recommend_action, axis=1)


# Header Branding
st.markdown("""
# 🛡️ CrisisShield AI
### Emergency Command Intelligence Platform  
**Developed by Shaikh Irfan | Cybersecurity Researcher | IEEE Member**

AI-powered disaster response, cyber incident coordination, infrastructure protection, and emergency intelligence.
""")


# System Status Bar
st.markdown(f"""
<div style="
    background:linear-gradient(135deg,#111827,#1e293b);
    padding:16px 24px;
    border-radius:16px;
    border:1px solid #334155;
    margin-bottom:24px;
    display:flex;
    justify-content:space-between;
    align-items:center;
    box-shadow:0 8px 24px rgba(0,0,0,0.25);
">

<div style="color:#22c55e;font-weight:700;">
● AI Monitoring Active
</div>

<div style="color:#22c55e;font-weight:700;">
● System Operational
</div>

<div style="color:#38bdf8;font-weight:600;">
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
</div>

</div>
""", unsafe_allow_html=True)


# Tabs
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "🚨 Command Center",
    "🗺️ Incident Map",
    "🤖 AI Recommendations",
    "💬 AI Analyst Assistant",
    "📋 Executive Summary"
])


# COMMAND CENTER
# COMMAND CENTER
with tab1:

    st.markdown("""
    ## 🔴 Live Emergency Command Center
    Monitor emergency events, cyber disruptions, infrastructure risks,
    and public safety alerts from one operational dashboard.
    """)

    # KPI DATA
    total_incidents = len(df)
    critical_count = len(df[df["risk_level"] == "Critical"])
    high_count = len(df[df["risk_level"] == "High"])
    cyber_count = len(
        df[df["type"].isin(["Cyberattack", "Hospital Disruption"])]
    )

    # KPI CARDS
    st.markdown("## 📊 Operational Overview")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#111827,#1e293b);
            padding:22px;
            border-radius:18px;
            border:1px solid #334155;
            text-align:center;
        ">
            <h4 style="color:#93c5fd;">Total Incidents</h4>
            <h1 style="color:white;">{total_incidents}</h1>
            <p style="color:#22c55e;">Active Monitoring</p>
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#111827,#1e293b);
            padding:22px;
            border-radius:18px;
            border:1px solid #334155;
            text-align:center;
        ">
            <h4 style="color:#fca5a5;">Critical Incidents</h4>
            <h1 style="color:white;">{critical_count}</h1>
            <p style="color:#ef4444;">Immediate Attention</p>
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#111827,#1e293b);
            padding:22px;
            border-radius:18px;
            border:1px solid #334155;
            text-align:center;
        ">
            <h4 style="color:#fde68a;">High Risk Events</h4>
            <h1 style="color:white;">{high_count}</h1>
            <p style="color:#f59e0b;">Escalation Watch</p>
        </div>
        """, unsafe_allow_html=True)

    with col4:
        st.markdown(f"""
        <div style="
            background:linear-gradient(135deg,#111827,#1e293b);
            padding:22px;
            border-radius:18px;
            border:1px solid #334155;
            text-align:center;
        ">
            <h4 style="color:#86efac;">Cyber/Infra Events</h4>
            <h1 style="color:white;">{cyber_count}</h1>
            <p style="color:#22c55e;">System Health 92%</p>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)

    # INCIDENT EXPLORER
    st.markdown("### 🔎 Explore Incident Details")

    detail_view = st.selectbox(
        "Select a KPI category to view related incidents:",
        [
            "Total Incidents",
            "Critical Incidents",
            "High Risk Events",
            "Cyber/Infrastructure Events"
        ]
    )

    if detail_view == "Total Incidents":
        detail_df = df

    elif detail_view == "Critical Incidents":
        detail_df = df[df["risk_level"] == "Critical"]

    elif detail_view == "High Risk Events":
        detail_df = df[df["risk_level"] == "High"]

    else:
        detail_df = df[
            df["type"].isin(["Cyberattack", "Hospital Disruption"])
        ]

    st.dataframe(
        detail_df[
            [
                "type",
                "location",
                "address",
                "severity",
                "risk_level",
                "source",
                "recommended_action"
            ]
        ],
        use_container_width=True
    )

    st.markdown("<br>", unsafe_allow_html=True)

    # LIVE ALERT SIMULATOR
    st.markdown("""
    <div style="
        background:linear-gradient(135deg, #111827, #1e293b);
        padding:24px;
        border-radius:18px;
        border:1px solid #334155;
        margin-bottom:20px;
    ">
        <h3>⚡ Live Emergency Alert Simulator</h3>
        <p>
        Generate a simulated emergency alert to test AI triage,
        classification, and response routing.
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

        st.success(
            f"Generated {new_alert_type} alert in {new_location}"
        )

    st.markdown("## 🔴 Priority Incident Alerts")

    critical_df = df[df["risk_level"] == "Critical"]

    for _, row in critical_df.iterrows():

        with st.container(border=True):

            col_a, col_b = st.columns([4, 1])

            with col_a:
                st.markdown(
                    f"### 🚨 {row['type']} — {row['location']}"
                )

            with col_b:
                st.markdown(
                    f"""
                    <div style="
                        background:linear-gradient(
                            135deg,#7f1d1d,#991b1b
                        );
                        color:white;
                        padding:10px;
                        border-radius:12px;
                        text-align:center;
                        font-weight:700;
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
                    background:linear-gradient(
                        135deg,#0f766e,#115e59
                    );
                    color:#ecfeff;
                    padding:14px;
                    border-radius:14px;
                    margin-top:12px;
                ">
                <b>Recommended Action:</b><br>
                {row['recommended_action']}
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown("## 📌 Incident Feed")

    st.dataframe(df, use_container_width=True)


# INCIDENT MAP
with tab2:

    st.markdown("## 🗺️ Real-Time Incident Map")
    st.caption("Geospatial view of emergency, infrastructure, and cyber-related incidents.")

    map_fig = px.scatter_mapbox(
        df,
        lat="latitude",
        lon="longitude",
        hover_name="type",
        hover_data=[
            "location",
            "address",
            "severity",
            "risk_level",
            "source"
        ],
        color="risk_level",
        zoom=3,
        height=650
    )

    map_fig.update_layout(
        mapbox_style="carto-darkmatter",
        paper_bgcolor="#0f172a",
        plot_bgcolor="#0f172a",
        font_color="white",
        margin={"r": 0, "t": 0, "l": 0, "b": 0}
    )

    st.plotly_chart(map_fig, use_container_width=True)


# AI RECOMMENDATIONS
with tab3:

    st.markdown("## 🤖 AI Response Recommendations")
    st.caption("Operational recommendations generated from incident severity, source, and type.")

    for _, row in df.iterrows():

        with st.expander(
            f"{row['type']} in {row['location']} — {row['risk_level']} Risk"
        ):

            st.write("**Description:**", row["description"])
            st.write("**Address:**", row["address"])
            st.write("**Source:**", row["source"])
            st.write("**Severity:**", row["severity"])
            st.write("**AI Confidence:**", row["ai_confidence"])
            st.write("**Recommended Action:**", row["recommended_action"])


# AI ANALYST ASSISTANT
with tab4:

    st.markdown("## 💬 AI Emergency Analyst Assistant")

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
                cyber_df[["type", "location", "address", "severity", "risk_level", "recommended_action"]],
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

    st.markdown("## 📋 Executive Emergency Summary")

    st.markdown(f"""
    <div style="
        background:linear-gradient(135deg, #111827, #1e293b);
        padding:24px;
        border-radius:18px;
        border:1px solid #334155;
        box-shadow:0 8px 24px rgba(0,0,0,0.3);
        margin-bottom:20px;
    ">
        <h3 style="margin-top:0;">Operational Overview</h3>
        <p>
        CrisisShield AI is monitoring <b>{len(df)} active incidents</b> across multiple regions.
        The system identified <b>{critical_count} critical incidents</b> and
        <b>{cyber_count} cyber or hospital-related disruptions</b>.
        </p>
        <p>
        Highest concern: <b>critical infrastructure disruption</b>. Recommended response:
        activate emergency workflow, prioritize critical infrastructure, and coordinate field response.
        </p>
    </div>
    """, unsafe_allow_html=True)

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.markdown("### Key Findings")

        st.markdown(f"""
        <div style="
            background:#111827;
            padding:20px;
            border-radius:16px;
            border:1px solid #334155;
        ">
        ✅ Total incidents monitored: <b>{len(df)}</b><br><br>
        🔴 Critical incidents detected: <b>{critical_count}</b><br><br>
        🏥 Cyber or hospital disruptions: <b>{cyber_count}</b><br><br>
        ⚠️ Highest concern: <b>Critical infrastructure disruption</b><br><br>
        🚨 Recommended response: <b>Activate emergency workflow</b>
        </div>
        """, unsafe_allow_html=True)

        st.markdown("### Recommended Immediate Actions")

        st.markdown("""
        <div style="
            background:#111827;
            padding:20px;
            border-radius:16px;
            border:1px solid #334155;
        ">
        1. Activate emergency command center<br>
        2. Prioritize critical infrastructure protection<br>
        3. Dispatch coordinated field response teams<br>
        4. Increase cyber monitoring for healthcare and utility networks<br>
        5. Verify misinformation before public communication
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("### Risk Distribution")

        pie = px.pie(
            df,
            names="risk_level",
            hole=0.55,
            color="risk_level",
            color_discrete_map={
                "Critical": "#ef4444",
                "High": "#f59e0b",
                "Medium": "#38bdf8",
                "Low": "#22c55e"
            }
        )

        pie.update_layout(
            paper_bgcolor="#111827",
            plot_bgcolor="#111827",
            font_color="white",
            height=360,
            margin=dict(l=10, r=10, t=20, b=10),
            legend=dict(
                orientation="h",
                yanchor="bottom",
                y=-0.15,
                xanchor="center",
                x=0.5
            )
        )

        st.plotly_chart(pie, use_container_width=True)

    st.markdown("### Executive Interpretation")

    st.markdown("""
    <div style="
        background:#111827;
        padding:20px;
        border-radius:16px;
        border-left:5px solid #ef4444;
        border-top:1px solid #334155;
        border-right:1px solid #334155;
        border-bottom:1px solid #334155;
        margin-top:10px;
    ">
    CrisisShield AI provides emergency managers with a unified operational view of disaster,
    cyber, infrastructure, and misinformation events. The current incident picture suggests
    that response teams should prioritize life-safety operations, healthcare continuity,
    cyber containment, and infrastructure protection.
    </div>
    """, unsafe_allow_html=True)


# Footer
st.markdown("---")
st.markdown("""
### CrisisShield AI
**Developed by Shaikh Irfan | Cybersecurity Researcher | IEEE Member**  
Built for emergency intelligence, disaster response, cyber incident coordination, and critical infrastructure protection.
""")