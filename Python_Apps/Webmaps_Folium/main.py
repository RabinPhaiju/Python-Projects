import folium

map = folium.Map(locations=[27.7127, 85.3214])

# add marker ---------------------------
fg = folium.FeatureGroup(name="My Map")
# fg.add_child(folium.CircleMarker(location=[27.712759, 85.321405], radius=6, fill_color='red', color='blue', fill_opaciy='0.9', popup="Here i am", icon=folium.Icon(color='red')))
# map.add_child(fg)

# multiple marker -----------------
# for coordinate in [[27.7,85.3],[27.7,85.2]]:
    # fg.add_child(folium.Marker(location=coordinate, popup="Here i am", icon=folium.Icon(color='red')))
# map.add_child(fg)

# read from csv file, using pandas and geopy (using [longitude and latitude])
# popup in add_child

# ----------------------------------------------------------------------------------
import mysql.connector # Error

con = mysql.connector.connect(
    user = "root",
    password = "",
    host = "localhost",
    database = "ffn"

)

cursor = con.cursor()

query = cursor.execute('select `lan` from register')
lan = cursor.fetchall()
query = cursor.execute('select `log` from register')
lon = cursor.fetchall()
query = cursor.execute('select `username` from register')
username = cursor.fetchall()


for lang, long, name in zip(lan, lon, username):
    fg.add_child(folium.Marker(location=[lang[0],long[0]], popup=name[0], icon=folium.Icon(color='red')))
map.add_child(fg)


# --------------------------------------------------

map.save("Map1.html")