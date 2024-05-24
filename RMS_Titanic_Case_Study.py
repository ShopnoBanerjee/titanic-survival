import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


st.markdown("# RMS Titanic")

st.write("The RMS Titanic, a British passenger liner operated by the White Star Line, embarked on its maiden voyage from Southampton to New York City on April 10, 1912. Heralded as a marvel of modern engineering and luxury, the Titanic tragically sank after colliding with an iceberg on April 15, 1912. This case study examines the design, voyage, disaster, aftermath, and legacy of the Titanic, highlighting critical lessons learned in maritime safety.")

st.image("RMS_Titanic_3.jpg",caption="The RMS Titanic",) 

st.markdown("# Design and Construction")
st.markdown("Constructed at the Harland and Wolff shipyard in Belfast, the Titanic was one of the largest and most luxurious ships of its time. It measured approximately 882 feet in length, with a gross tonnage of 46,328 tons, and featured 16 watertight compartments designed to keep the ship afloat even if multiple compartments were breached. The ship boasted numerous amenities, including opulent first-class cabins, a grand staircase, swimming pools, and restaurants")

st.markdown('''
            Despite its advanced design, several critical safety oversights were present:-Lifeboat Capacity: 
            - The Titanic carried only 20 lifeboats, sufficient for about 1,178 people, far fewer than the total number of passengers and crew on board
            - Watertight Compartments: The compartments were not sealed at the top, allowing water to spill from one to another, compromising the ship’s buoyancy.
            ''')

st.image("titanic-deck-plan-learning.jpg",caption="Titanic Deck Plan")


st.markdown('''
            # The Passengers 
            The passengers of the RMS Titanic represented a diverse mix of early 20th-century society, totaling approximately 2,224 people on board. They were divided into three main classes based on their accommodations:
            ''')
 
 
st.markdown('''
            ### Titanic Passenger Data
            ```
            S --> Southampton
            Q --> Queenstown
            C --> Cherbourg
            ```
            ''')
           
table = pd.read_csv("titanic/train.csv")
table = table[['Name','Sex','Age','Pclass','Fare','Embarked','Survived']]
table = table.rename(columns=({'Pclass':'Class'}))
st.dataframe(table)          


            
            
st.markdown('''
            ### First Class
            First-class passengers were among the wealthiest and most prominent individuals of the time. This group included influential businessmen, celebrities, and members of high society. They enjoyed luxurious accommodations and amenities, such as opulent cabins, gourmet dining, a swimming pool, and a grand staircase. 
            
            ### Second Class
            Second-class passengers were typically professionals, academics, and tourists. While their accommodations were less lavish than those of first class, they still enjoyed comfortable cabins and access to dining rooms, a library, and other amenities. Second-class passengers included Lawrence Beesley, a science teacher and journalist who survived the sinking and later wrote a memoir about his experience, and Reverend John Harper, a Baptist minister traveling to preach in America.
            
            ### Third Class (Steerage)
            Third-class passengers, or steerage, consisted primarily of immigrants seeking new opportunities in the United States. They came from various countries, including Ireland, Scandinavia, Eastern Europe, and the Middle East. These passengers traveled in more modest accommodations, often in shared dormitory-style rooms. Despite the less comfortable conditions, third-class passengers were provided with basic meals and communal spaces. Many of these passengers were families and young individuals hoping to start anew in America.
            ''')


#USING MATPLOTLIB (try not to as the other st.plot looks better) '''


st.markdown('''
            # The Maiden Voyage
            The Titanic set sail from Southampton on April 10, 1912, with stops at Cherbourg, France, and Queenstown (now Cobh), Ireland, before heading across the Atlantic towards New York City. The ship carried 2,224 passengers and crew, including some of the wealthiest people of the time, as well as emigrants seeking a new life in America.
            
            ### The Disaster
            On the night of April 14, 1912, the Titanic struck an iceberg at 11:40 PM ship's time. The collision caused significant damage to the ship's hull, breaching five of its watertight compartments. Despite efforts to avoid the iceberg, the ship’s side was ripped open, leading to a rapid influx of water.
            
            ```
            Red : Southampton,Queenstown,Cherbough
            Blue : Crash site
            Green : New York
            ```
            ''')




#titanic crash location

crash  = pd.DataFrame({
    "name" : ["crash site","Southampton","Queenstown","Cherbough","New York"],
    "lat" : [41.72583043,50.909698, 53.805806,49.630001, 40.730610,], 
    "lon" :  [-49.94082957,-1.404351, -3.047469,-1.620000, -73.935242 ],
    "color": [[0, 0, 255], [255, 0, 0], [255, 0, 0], [255, 0, 0],[0, 255, 0]]
    })

st.map(crash,color="color")

# st.markdown("# Aftermath"
#             "The Titanic sank at 2:20 AM on April 15, 1912. Of the 2,224 people aboard, more than 1,500 perished, making it one of the deadliest maritime disasters in history. The Carpathia, another passenger ship, arrived several hours later and rescued the 710 survivors."
#              "The disaster led to widespread public outcry and significant changes in maritime regulations:"
#              "- International Ice Patrol: Established to monitor icebergs in the North Atlantic and warn ships of potential dangers."
#              "- Lifeboat Regulations: New laws required ships to carry sufficient lifeboats for all passengers and crew."
#              "- Radio Communication: Improved regulations for continuous radio watch and distress signal protocols were implemented.""
#              )
             
st.markdown('''
            # Aftermath
            Despite its advanced design, several critical safety oversights were present:-Lifeboat Capacity:The Titanic sank at 2:20 AM on April 15, 1912. Of the 2,224 people aboard, more than 1,500 perished, making it one of the deadliest maritime disasters in history. The Carpathia, another passenger ship, arrived several hours later and rescued the 710 survivors.
            - International Ice Patrol: Established to monitor icebergs in the North Atlantic and warn ships of potential dangers.
            - Lifeboat Regulations: New laws required ships to carry sufficient lifeboats for all passengers and crew.
            - Radio Communication: Improved regulations for continuous radio watch and distress signal protocols were implemented.
            
            ''')

st.video("https://www.youtube.com/watch?v=bXlalGvxkaY")

