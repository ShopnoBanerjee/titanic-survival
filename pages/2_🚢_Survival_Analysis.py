import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv("titanic/train.csv")


st.markdown('''
            # Survival vs. Age:
            Analyzing survival rates across different age groups reveals how age impacted the likelihood of survival. One can examine if there was a preference for saving children and elderly passengers during the evacuation process, potentially indicating a "women and children first" policy.
            ''')




age_data = df['Age']

fig2, ax = plt.subplots(figsize=(8, 6))

primary_color = "#4E4D81"
secondary_background_color = "#5F3DC9"
graph_background_color = "#8BC2BF"

fig2.patch.set_facecolor(graph_background_color)


ax.hist(age_data, bins=20, color=primary_color, edgecolor='black')

ax.set_title('Distribution of Age')
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')

st.pyplot(fig2,use_container_width=True)




st.markdown('''
            # Survival vs Class:
            Analyzing survival rates among different passenger classes illuminates the role of socio-economic status in survival. First-class passengers may have had better access to lifeboats and evacuation assistance compared to second and third-class passengers.
            
            ''')

# Define data
pclass_survived = df[df['Survived'] == 1]['Pclass'].value_counts().sort_index()
pclass_not_survived = df[df['Survived'] == 0]['Pclass'].value_counts().sort_index()

pclass_counts = pd.DataFrame({'Survived': pclass_survived, 'Not Survived': pclass_not_survived}).fillna(0)

fig1, ax = plt.subplots(figsize=(5, 3))

primary_color = "#61bdb8"
secondary_background_color = "#153737"
graph_background_color = "#8BC2BF"

fig1.patch.set_facecolor(graph_background_color)

pclass_counts.plot(kind='bar', ax=ax, color=[primary_color, secondary_background_color], alpha=0.7, edgecolor='black')


ax.set_title('Survival by Passenger Class')
ax.set_xlabel('Passenger Class')
ax.set_ylabel('Number of Passengers')
ax.set_xticks(range(len(pclass_counts)))
ax.set_xticklabels(pclass_counts.index, rotation=0)
ax.legend(title='Outcome')

st.pyplot(fig1,use_container_width=True)




st.markdown('''
            # Survival vs. Embarkation Port:
            Comparing survival rates based on the embarkation port sheds light on whether passengers from certain ports had better chances of survival. Factors such as socio-economic status and demographics of passengers from different ports may influence survival rates.
            ''')



embarked_survived = df[df['Survived'] == 1]['Embarked'].value_counts()
embarked_not_survived = df[df['Survived'] == 0]['Embarked'].value_counts()

embarked_counts = pd.DataFrame({'Survived': embarked_survived, 'Not Survived': embarked_not_survived}).fillna(0)

fig3, ax = plt.subplots(figsize=(6, 4))

primary_color = "#4E4D81"
secondary_background_color = "#5F3DC9"
graph_background_color = "#8BC2BF"

fig3.patch.set_facecolor(graph_background_color)

embarked_counts.plot(kind='bar', ax=ax, color=[primary_color, secondary_background_color], alpha=0.8, edgecolor='black')

# Add titles and labels using the axis object
ax.set_title('Survival by Port of Embarkation')
ax.set_xlabel('Port of Embarkation')
ax.set_ylabel('Number of Passengers')
ax.set_xticklabels(embarked_counts.index, rotation=0)
ax.legend(title='Outcome')

# Show the plot
st.pyplot(fig3,use_container_width=True)






st.markdown('''
            # Survival vs. Total Family Size:
            Analyzing survival rates based on total family size (including both relatives and non-relatives traveling together) can help determine if passengers traveling with larger families had better or worse chances of survival. Factors such as assistance in finding and boarding lifeboats, coordination during evacuation, and willingness to prioritize family members may influence survival rates. 
            ''')



df["total_family"] = df["SibSp"] + df["Parch"] 

# Prepare the data for plotting
total_family_survived = df[df['Survived'] == 1]['total_family'].value_counts().sort_index()
total_family_not_survived = df[df['Survived'] == 0]['total_family'].value_counts().sort_index()

# Create a DataFrame with counts
total_family_counts = pd.DataFrame({'Survived': total_family_survived, 'Not Survived': total_family_not_survived}).fillna(0)

# Create figure and axis objects
fig4, ax = plt.subplots(figsize=(6, 4))

primary_color = "#4E4D81"
secondary_background_color = "#5F3DC9"
graph_background_color = "#8BC2BF"

fig4.patch.set_color(graph_background_color)

# Plot the data
total_family_counts.plot(kind='bar', ax=ax, color=[primary_color, secondary_background_color], alpha=0.7, edgecolor='black')

# Add titles and labels using the axis object
ax.set_title('Survival by Total Family Size')
ax.set_xlabel('Total Family Size (SibSp + Parch)')
ax.set_ylabel('Number of Passengers')
ax.set_xticklabels(total_family_counts.index, rotation=0)
ax.legend(title='Outcome')

# Show the plot
st.pyplot(fig4,use_container_width=True)




























