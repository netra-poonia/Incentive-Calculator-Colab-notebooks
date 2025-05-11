import streamlit as st
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import truncnorm

st.title("Loan Simulation : ")

st.sidebar.header("Simulation Controls")
ats = st.sidebar.slider("Average Ticket Size (₹L)", 6.0, 12.0, 8.0, 0.1)
high_pct = st.sidebar.slider("Target % Loans > ₹10L", 10, 50, 20, 1)

N = 10000
lower, upper = 5, 20
std = 2.5
mean = ats

a, b = (lower - mean) / std, (upper - mean) / std
data = truncnorm.rvs(a, b, loc=mean, scale=std, size=N)

actual_ats = np.mean(data)
actual_pct_above_10L = np.mean(data > 10) * 100

col1, col2 = st.columns(2)
col1.metric("Simulated ATS (₹L)", f"{actual_ats:.2f}")
col2.metric("% Loans > ₹10L", f"{actual_pct_above_10L:.1f}%")

fig, ax = plt.subplots(figsize=(10, 5))
sns.kdeplot(data, fill=True, ax=ax, bw_adjust=0.5, color="skyblue")
ax.set_title("Loan Amount Distribution", fontsize=16)
ax.set_xlabel("Loan Amount (₹L)")
ax.set_ylabel("Density")
ax.grid(True)

st.pyplot(fig)