#!/usr/bin/env python
# coding: utf-8

# In[94]:


import plotly.graph_objects as go
import numpy as np
import streamlit as st

st.set_page_config(layout="wide")
st.title("Pickleball Club of Tysons Price Analysis")




# In[95]:


INDIVIDUAL_MONTHLY = 79
FAMILY_MONTHLY = 179
MEMBER_DOUBLES_RES = 8
VISITOR_DOUBLES_RES = 16
REGISTRATION_FEE = 35

st.sidebar.write("## Club Pricing")
st.sidebar.text(f"""
Individual Membership Monthly Fee: *${INDIVIDUAL_MONTHLY}*
Family Membership Monthly Fee: *${FAMILY_MONTHLY}*
One Time Registration Fee: *${REGISTRATION_FEE}*

Reservation Fee Per Hour Per Person for Doubles Game (Member): *${MEMBER_DOUBLES_RES}*
Reservation Fee Per Hour Per Person or Doubles Game (Non-Member): *${VISITOR_DOUBLES_RES}*
""")

col1, col2, col3, col4 = st.columns(4)
# In[96]:


games_per_month = st.slider("Number of Games We Would Play Per Month", min_value=1, max_value=30)
hours_per_game = st.slider("Number of Hours Per Game", min_value=1, max_value=3)
num_months = st.slider("Number of Months", min_value=1, max_value=24, value=12)


# In[97]:


# Individual Membership
def calculate_individual(num_months):
    cost =  (INDIVIDUAL_MONTHLY * num_months) + (MEMBER_DOUBLES_RES * games_per_month * hours_per_game * num_months) + REGISTRATION_FEE
    return cost


# In[98]:


# Family Membership
def calculate_family(num_months):    
    family_member_cost = (FAMILY_MONTHLY * num_months) + (MEMBER_DOUBLES_RES * games_per_month * hours_per_game * num_months) + REGISTRATION_FEE
    family_per_person = float(family_member_cost / 3)
    return family_per_person

def calculate_family_total(num_months):    
    family_member_cost = (FAMILY_MONTHLY * num_months) + (MEMBER_DOUBLES_RES * games_per_month * hours_per_game * num_months) + REGISTRATION_FEE
    family_per_person = float(family_member_cost / 3)
    return family_member_cost    


# In[99]:


# Visitor Rate
def calculate_visitor(num_months):
    visitor_cost = (VISITOR_DOUBLES_RES * games_per_month * hours_per_game * num_months)
    return visitor_cost


# ## Visualization

# In[100]:


x = [i for i in range(1, num_months + 1)]

y_individual = list(map(calculate_individual, x))

y_family = list(map(calculate_family, x))

y_family_total = list(map(calculate_family_total, x))

y_visitor = list(map(calculate_visitor, x))


# col1.metric(label="Individual Membership Monthly Base", value=f"${calculate_individual(1)}")
# col2.metric(label="Family Membership Monthly Base (per person)", value=f"${calculate_family(1):.2f}")
# col3.metric(label="Family Membership Monthly Base (Total)", value=f"${calculate_family_total(1)}")
# col4.metric(label="Non-Member Monthly Base", value=f"${calculate_visitor(1)}")


# In[101]:


# --- Create the Plotly Figure ---
fig = go.Figure()

# Add Individual Users trace (mode changed to 'lines')
fig.add_trace(go.Scatter(
    x=x,
    y=y_individual,
    mode='lines+markers', # Changed from 'lines+markers' to 'lines'
    name='Individual Membership',
    line=dict(color='deepskyblue', width=3) # Markers removed
))

# Add Family Users trace (mode changed to 'lines')
fig.add_trace(go.Scatter(
    x=x,
    y=y_family,
    mode='lines+markers', # Changed from 'lines+markers' to 'lines'
    name='Family Plan Per Person',
    line=dict(color='lightcoral', width=3) # Markers removed
))

fig.add_trace(go.Scatter(
    x=x,
    y=y_family_total,
    mode='lines+markers', # Changed from 'lines+markers' to 'lines'
    name='Family Plan Total (3 People)',
    line=dict(color='lightblue', width=3) # Markers removed
))

# Add Visitor Users trace (mode changed to 'lines')
fig.add_trace(go.Scatter(
    x=x,
    y=y_visitor,
    mode='lines+markers', # Changed from 'lines+markers' to 'lines'
    name='Visitor (Non-Member)',
    line=dict(color='lightgreen', width=3) # Markers removed
))

# --- Customize the Plot Layout ---
fig.update_layout(
    title={
        'text': f"Pickleball Club Projected Prices Per Month| Assuming We Play {games_per_month}, {hours_per_game}-Hour Games Per Month",
        'y':0.95,
        'x':0.5,
        'xanchor': 'center',
        'yanchor': 'top'
    },
    xaxis_title="Month Number",
    yaxis_title="Price Per Person ($)",
    hovermode="x unified", # Shows all y-values for a given x on hover
    legend_title="User Type",
    font=dict(
        family="Inter, sans-serif",
        size=14
    ),
    template="plotly_dark",
    margin=dict(l=40, r=40, t=80, b=40) # Adjust margins
)


st.plotly_chart(fig)

# In[ ]:




