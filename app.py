import streamlit as st
import pandas as pd
import os
import plotly.express as px
from src.predict import make_prediction, get_study_goal
from datetime import datetime

st.set_page_config(
    page_title="Student Productivity AI", 
    layout="wide", 
    page_icon="✍️" # You can change the emoji too!
)

# --- SESSION STATE FOR HISTORY ---
if 'history' not in st.session_state:
    st.session_state.history = []

# --- CUSTOM STYLING ---
st.markdown("""
    <style>
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; border: 1px solid #e6e9ef; }
    [data-testid="stMetricValue"] { color: #1f77b4; }
    </style>
    """, unsafe_allow_html=True)

# --- SIDEBAR HISTORY ---
with st.sidebar:
    st.header("📜 Session History")
    if st.session_state.history:
        for i, entry in enumerate(reversed(st.session_state.history[-5:])):
            st.info(f"Score: **{entry['score']}%** | {entry['time']}")
        if st.button("Clear Session"):
            st.session_state.history = []
            st.rerun()
    
    st.divider()
    log_file = "productivity_history.csv"
    if os.path.exists(log_file):
        with open(log_file, "rb") as file:
            st.download_button(label="📥 Download Full History (CSV)", data=file, file_name="productivity_log.csv", mime="text/csv")

st.title("✍️ Student Productivity AI")
st.markdown("---")

col1, col2 = st.columns([1, 1.2], gap="large")

with col1:
    st.header("🕒 Daily Activity Log")
    study_hours = st.slider("📚 Study Hours", 0.0, 24.0, 4.0, 0.5)
    sleep_hours = st.slider("😴 Sleep Hours", 0.0, 24.0, 7.0, 0.5)
    
    with st.expander("📱 Digital Usage (0-24 hrs each)", expanded=False):
        social = st.slider("Social Media", 0.0, 24.0, 1.0, 0.5)
        youtube = st.slider("YouTube", 0.0, 24.0, 1.0, 0.5)
        gaming = st.slider("Gaming", 0.0, 24.0, 0.0, 0.5)
        total_screen = social + youtube + gaming

    with st.expander("🧘 Health & Academics", expanded=False):
        exercise_mins = st.number_input("Exercise (Minutes)", 0, 1440, 30, 5)
        exercise_hrs = exercise_mins / 60.0
        breaks_count = st.number_input("Breaks Per Day", 0, 50, 5)
        breaks_hrs = breaks_count * 0.25 
        coffee = st.number_input("Coffee Intake (mg)", 0, 1000, 100, 50)
        attendance = st.slider("Attendance %", 0, 100, 85)
        stress = st.select_slider("Stress Level", options=[1, 2, 3, 4, 5], value=2)
        focus = st.slider("Focus Score (1-100)", 1, 100, 70)
        assignments = st.number_input("Assignments Completed", 0, 20, 2)
        final_grade = st.slider("Current Grade Avg %", 0, 100, 75)

    total_time_used = study_hours + sleep_hours + total_screen + exercise_hrs + breaks_hrs
    
    st.divider()
    if total_time_used > 24.0:
        st.error(f"❌ **Time Paradox!** Activities add up to **{total_time_used:.2f} hours**.")
        can_predict = False
    elif total_time_used == 0:
        st.info("Adjust sliders to see your prediction.")
        can_predict = False
    else:
        st.success(f"✅ **{total_time_used:.2f} / 24 hours** accounted for.")
        can_predict = True

    if can_predict:
        with st.expander("📊 View Your Time Distribution", expanded=True):
            remaining_time = max(0, 24 - total_time_used)
            chart_data = pd.DataFrame({
                "Activity": ["Study", "Sleep", "Screens", "Exercise", "Breaks", "Unallocated"],
                "Hours": [study_hours, sleep_hours, total_screen, exercise_hrs, breaks_hrs, remaining_time]
            })
            fig = px.pie(chart_data, values='Hours', names='Activity', hole=0.4,
                         color_discrete_map={"Study":"#2ecc71", "Screens":"#e74c3c", "Sleep":"#3498db", "Unallocated":"#ecf0f1"},
                         color_discrete_sequence=px.colors.qualitative.Pastel)
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)

with col2:
    st.header("🔬 AI Analysis")
    enable_simulation = st.toggle("🚀 Enable Data-Driven 'What-If' Scenarios")
    
    if st.button("Predict Productivity 🚀", use_container_width=True, disabled=not can_predict):
        user_input = {
            'study_hours_per_day': study_hours, 'sleep_hours': sleep_hours,
            'phone_usage_hours': total_screen, 'social_media_hours': social,
            'youtube_hours': youtube, 'gaming_hours': gaming,
            'breaks_per_day': breaks_count, 'coffee_intake_mg': coffee,
            'exercise_minutes': exercise_mins, 'assignments_completed': assignments,
            'attendance_percentage': attendance, 'stress_level': stress,
            'focus_score': focus, 'final_grade': final_grade
        }
        
        score = make_prediction(user_input)
        current_time = datetime.now().strftime("%H:%M:%S")
        st.session_state.history.append({"score": score, "time": current_time})

        st.metric("Productivity Score", f"{score}%")
        
        # --- 1. SMART STATUS & DYNAMIC INSIGHTS ---
        if score >= 90:
            st.success("🌟 Status: Elite Performance (Mastery Level)")
        elif score >= 75:
            st.info("📈 Status: Strong (High Efficiency)")
        elif score >= 50:
            st.warning("⚖️ Status: Balanced (Room for Growth)")
        else:
            st.error("⚠️ Status: Critical (Burnout/Inefficiency Risk)")

        st.subheader("💡 Personalized AI Insights")
        insights = []

        # Only show insights for WEAK points
        if sleep_hours < 6.5:
            insights.append("😴 **Sleep Debt:** Your recovery is below 6.5h. The brain cannot consolidate memory effectively at this level.")
        if total_screen > (study_hours * 0.8) and total_screen > 2:
            insights.append(f"📱 **Digital Friction:** Screen time is competing with study time. Reducing this is your fastest path to a focus boost.")
        if focus < 60:
            insights.append("🎯 **Focus Quality:** Your focus score is low. Try 'Pomodoro' sessions to improve the intensity of your study hours.")
        if stress >= 4 and coffee > 300:
            insights.append("☕ **Caffeine-Stress Loop:** High caffeine may be masking fatigue and increasing your anxiety levels.")
        if exercise_mins < 20:
            insights.append("🏃 **Missing Catalyst:** Even 20m of movement increases BDNF (brain protein) for better learning.")

        # If everything is optimized
        if not insights:
            st.write("✨ **Peak Alignment:** Your current data suggests no significant behavioral bottlenecks. Maintain this consistency!")
        else:
            for insight in insights:
                st.write(insight)

        # --- 2. DATA-DRIVEN POTENTIAL IMPACT (Filter out 0% gains) ---
        if enable_simulation:
            st.divider()
            st.subheader("🧪 Strategic Gains")
            sim_cols = st.columns(2)
            found_sim = False

            # Test Screen Reduction (Only if there is screen time to cut)
            if total_screen >= 1.5:
                s1_input = user_input.copy()
                s1_input['phone_usage_hours'] -= 1.5
                s1_score = make_prediction(s1_input)
                if s1_score > score + 0.5:
                    sim_cols[0].write(f"📱 **Detox (-1.5h screens):** **{s1_score}%** (+{round(s1_score-score, 2)}%)")
                    found_sim = True

            # Test Sleep (Only if sleep is low)
            if sleep_hours < 7.5:
                s4_input = user_input.copy()
                s4_input['sleep_hours'] = 8.0
                s4_score = make_prediction(s4_input)
                if s4_score > score + 0.5:
                    sim_cols[1].write(f"😴 **Sleep Optimization:** **{s4_score}%** (+{round(s4_score-score, 2)}%)")
                    found_sim = True

            # Test Academic Push (Only if assignments are low)
            if assignments < 5:
                s3_input = user_input.copy()
                s3_input['assignments_completed'] += 2
                s3_score = make_prediction(s3_input)
                if s3_score > score + 0.5:
                    sim_cols[0].write(f"📝 **Task Completion (+2):** **{s3_score}%** (+{round(s3_score-score, 2)}%)")
                    found_sim = True

            if not found_sim:
                st.write("✅ All simulated parameters are already at their point of diminishing returns. You are maxing out your current potential!")

        # --- 3. THE CONDITIONAL ROADMAP ---
        # If user is ALREADY at 90%, change the Roadmap to a "Mastery" message
        st.divider()
        if score < 90:
            st.subheader("🎯 The Roadmap to 90%")
            goal = get_study_goal(user_input, 90)
            if goal and goal > study_hours:
                st.info(f"To cross the **90%** threshold, increase study intensity/time to **{goal} hours**.")
            else:
                st.write("Your study hours are sufficient. Focus on **Sleep** or **Focus Score** to hit 90% instead of just adding more hours.")
        else:
            st.subheader("🏆 Mastery Achieved")
            st.balloons()
            st.success(f"You have surpassed the 90% benchmark. Your current roadmap is **Maintenance**: Stay at this level for 7 days to turn these habits into a permanent lifestyle.")

        # --- CSV LOGGING (Remains same for integrity) ---
        log_file = "productivity_history.csv"
        new_entry = pd.DataFrame([user_input])
        new_entry['score'] = score
        new_entry['date'] = datetime.now().strftime("%Y-%m-%d %H:%M")
        if not os.path.isfile(log_file): new_entry.to_csv(log_file, index=False)
        else: new_entry.to_csv(log_file, mode='a', header=False, index=False)