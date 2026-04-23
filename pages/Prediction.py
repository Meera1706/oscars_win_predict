import streamlit as st
import pickle
import numpy as np

st.title("🎯 Oscar Win Prediction ")

# -----------------------------
# Load model artifacts
# -----------------------------
model = pickle.load(open("model/model.pkl", "rb"))
scaler = pickle.load(open("model/scaler.pkl", "rb"))
columns = pickle.load(open("model/columns.pkl", "rb"))

# -----------------------------
# Inputs
# -----------------------------
st.subheader("🎬 Enter Movie Details")

year = st.number_input("Year of Film", 1900, 2030, 2000)

category = st.selectbox("Award Category", [
    "ACTOR IN A LEADING ROLE",
    "ACTOR IN A SUPPORTING ROLE",
    "ACTRESS IN A LEADING ROLE",
    "ACTRESS IN A SUPPORTING ROLE"
])

genre = st.selectbox("Genre", [
    "Drama", "Comedy", "Action", "Biography", "Romance"
])

actor_name = st.text_input("Actor / Actress Name")

# -----------------------------
# Helper Functions
# -----------------------------

def actor_score(name):
    """
    Simple heuristic:
    longer name -> assumed experienced actor (placeholder logic)
    """
    if not name:
        return 0.0
    
    length = len(name.strip())

    if length > 15:
        return 0.05
    elif length > 10:
        return 0.02
    else:
        return 0.0


def genre_adjustment(genre):
    weights = {
        "Drama": 0.10,
        "Biography": 0.08,
        "Romance": 0.03,
        "Comedy": -0.05,
        "Action": -0.08
    }
    return weights.get(genre, 0.0)


def build_input_vector(year, category, columns):
    """
    Build input aligned with trained features
    """
    input_data = np.zeros(len(columns))

    # Assume first column is year (as per your pipeline)
    input_data[0] = year

    # Set category columns dynamically
    for i, col in enumerate(columns):
        if category in col:
            input_data[i] = 1

    return input_data


# -----------------------------
# Prediction
# -----------------------------
if st.button("Predict"):

    try:
        # Build input
        input_data = build_input_vector(year, category, columns)

        # Scale
        input_scaled = scaler.transform([input_data])

        # Base model prediction
        base_prob = model.predict_proba(input_scaled)[0][1]

        # Adjustments
        g_adj = genre_adjustment(genre)
        a_adj = actor_score(actor_name)

        # Final probability
        final_prob = base_prob + g_adj + a_adj
        final_prob = max(0, min(1, final_prob))  # clamp between 0 and 1

        # -----------------------------
        # Display Results
        # -----------------------------
        st.subheader("📊 Prediction Results")

        st.write(f"**Model Probability:** {base_prob:.2f}")
        st.write(f"**Genre Impact:** {g_adj:+.2f}")
        st.write(f"**Actor Impact:** {a_adj:+.2f}")
        st.write(f"**Final Probability:** {final_prob:.2f}")

        # Risk Levels
        st.subheader("🎯 Interpretation")

        if final_prob > 0.7:
            st.success("🟢 High Chance of Winning")
        elif final_prob > 0.4:
            st.warning("🟡 Moderate Chance of Winning")
        else:
            st.error("🔴 Low Chance of Winning")

        # Confidence bar
        st.progress(final_prob)

        # Explanation
        st.subheader("🧠 Explanation")

        st.markdown("""
        - **Model Probability** → Output from trained ML model  
        - **Genre Impact** → Domain-based adjustment  
        - **Actor Impact** → Experience-based heuristic  
        - **Final Probability** → Combined estimate  
        """)

    except Exception as e:
        st.error(f"Error during prediction: {e}")