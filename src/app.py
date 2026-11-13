"""
Starter Streamlit demo for the CIVE70111 coursework.

Run it from the repository root:

    streamlit run src/app.py

The app works out of the box: if it cannot find your saved model it trains a
small placeholder on made-up data, so you can see the interface before you
have a model of your own. Replace the placeholder with your real model:

1. In your notebook, fit a scikit-learn model (a Pipeline that includes your
   scaler is easiest, because then the app needs no separate scaling step).
2. Save it with joblib, one file per plant, using the names below:

       import joblib
       joblib.dump(model, "models/power_model_plant1.joblib")
       joblib.dump(model, "models/power_model_plant2.joblib")

3. Make sure FEATURES below lists the columns your model was trained on, in
   the same order and with the same names.

Optional: save your operating-condition classifier the same way as
models/condition_model_plant1.joblib (and plant2). The app will then also show
the predicted condition and its probability.

This is a placeholder app. Everything below is yours to change. Add sliders,
plots, a model selector or a page that replays a day from the test set -
whatever helps you present your work in the demo. For inspiration on what is
possible, browse the Streamlit gallery: https://streamlit.io/gallery
"""

from pathlib import Path

import joblib
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st
from sklearn.linear_model import LinearRegression

# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

MODELS_DIR = Path(__file__).resolve().parent.parent / "models"

# Input columns, in the order your model expects them.
FEATURES = ["IRRADIATION", "AMBIENT_TEMPERATURE", "MODULE_TEMPERATURE"]

PLANTS = {"Plant 1": "plant1", "Plant 2": "plant2"}


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------

def placeholder_model():
    """A stand-in regression model trained on made-up data. Not a real result."""
    rng = np.random.default_rng(0)
    n = 500
    irradiation = rng.uniform(0, 1.2, n)
    ambient = rng.uniform(20, 35, n)
    module = ambient + 25 * irradiation + rng.normal(0, 2, n)
    dc_power = 12000 * irradiation * (1 - 0.004 * (module - 25)) + rng.normal(0, 300, n)
    X = pd.DataFrame(np.column_stack([irradiation, ambient, module]), columns=FEATURES)
    return LinearRegression().fit(X, dc_power)


@st.cache_resource
def _load_file(path, modified):
    # `modified` is part of the cache key, so a retrained model is reloaded.
    return joblib.load(path)


def load_model(kind, plant):
    """Load models/<kind>_<plant>.joblib, or return None if it does not exist."""
    path = MODELS_DIR / f"{kind}_{plant}.joblib"
    if path.exists():
        return _load_file(str(path), path.stat().st_mtime)
    return None


# ---------------------------------------------------------------------------
# Page
# ---------------------------------------------------------------------------

st.set_page_config(page_title="Solar power demo", layout="wide")
st.title("Solar power forecasting demo")

# Delete this notice once the app has been made your own.
st.info(
    "**This is a placeholder app.** It is a starting point provided with the "
    "project template, showing how to load a saved model, take inputs and "
    "plot a prediction. Replace it with your own design for your demo. "
    "For inspiration on what Streamlit can do, browse the "
    "[Streamlit gallery](https://streamlit.io/gallery)."
)

with st.expander("How to host this app online (optional)"):
    st.markdown(
        """
You can host the app for free on
[Streamlit Community Cloud](https://streamlit.io/cloud), which deploys it
straight from your GitHub repository.

1. Push your repository to GitHub, including `src/app.py`, `requirements.txt`
   and the model files in `models/`.
2. Sign in at [share.streamlit.io](https://share.streamlit.io) with your
   GitHub account.
3. Click **Create app**, choose your repository and branch, set the main
   file path to `src/app.py`, and click **Deploy**.
4. Every push to that branch updates the app automatically.

Things to know:

- **Your repository is private, so the app is private too.** Only you can
  see it until you invite viewers with the **Share** button. Each account
  can have one private app at a time.
- **The hosted app can only read files committed to your repository**, such
  as saved models in `models/`. Anything you have only on your computer is
  missing (GitHub rejects single files over 100 MB).
- **The app sleeps after 12 hours without visitors.** Open it before your
  presentation and click *Yes, get this app back up!* if you see it.
- Running locally with `streamlit run src/app.py` is fine for the
  presentation. Hosting is optional.

Full instructions:
[Deploy your app](https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app).
"""
    )

with st.sidebar:
    st.header("Inputs")
    plant_label = st.selectbox("Plant", list(PLANTS))
    irradiation = st.slider("Irradiation", 0.0, 1.2, 0.6, 0.01)
    ambient = st.slider("Ambient temperature (°C)", 15.0, 40.0, 27.0, 0.5)
    module = st.slider("Module temperature (°C)", 15.0, 70.0, 45.0, 0.5)

plant = PLANTS[plant_label]
power_model = load_model("power_model", plant)
if power_model is None:
    st.warning(
        f"No saved model found at models/power_model_{plant}.joblib, "
        "so this page is using a placeholder trained on made-up data. "
        "See the instructions at the top of src/app.py."
    )
    power_model = placeholder_model()

inputs = pd.DataFrame([[irradiation, ambient, module]], columns=FEATURES)

# --- Prediction -----------------------------------------------------------

left, right = st.columns(2)

with left:
    st.subheader("Predicted DC power")
    prediction = float(power_model.predict(inputs)[0])
    st.metric("DC power (kW)", f"{prediction:,.0f}")

    condition_model = load_model("condition_model", plant)
    if condition_model is not None:
        st.subheader("Predicted operating condition")
        label = condition_model.predict(inputs)[0]
        st.metric("Condition", str(label))
        if hasattr(condition_model, "predict_proba"):
            probabilities = condition_model.predict_proba(inputs)[0]
            st.dataframe(
                pd.DataFrame({"class": condition_model.classes_, "probability": probabilities}),
                hide_index=True,
            )

# --- How the prediction responds to irradiation ---------------------------

with right:
    st.subheader("Response to irradiation")
    sweep = pd.DataFrame({
        "IRRADIATION": np.linspace(0, 1.2, 100),
        "AMBIENT_TEMPERATURE": ambient,
        "MODULE_TEMPERATURE": module,
    })[FEATURES]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(sweep["IRRADIATION"], power_model.predict(sweep), label="model")
    ax.scatter([irradiation], [prediction], color="black", zorder=3, label="current input")
    ax.set_xlabel("Irradiation")
    ax.set_ylabel("Predicted DC power (kW)")
    ax.legend()
    st.pyplot(fig)
    st.caption("Temperatures are held at the slider values while irradiation varies.")
