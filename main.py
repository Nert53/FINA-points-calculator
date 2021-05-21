#Vojtěch Nerh 8. O - 2021 GJJ

from flask import Flask, url_for, render_template, request, jsonify
import xml.dom.minidom

app = Flask(__name__)

#přiřazení xml dokumentu s data o WR
document = xml.dom.minidom.parse("static\data.xml")

@app.route("/")
def home():
    return render_template("main.html")

@app.route("/process", methods=["POST"])
def process():

    #importování údajů ze select tagů a input tagu
    time = request.form["time"]
    distance = request.form["distance"]
    style = request.form["style"]
    course = request.form["course"]
    gender = request.form["gender"]

    records = document.getElementsByTagName("record")

    for record in records:
        discipline = record.getElementsByTagName("discipline")[0]

        distance_xml = discipline.getElementsByTagName("length")[0].childNodes[0].nodeValue
        stroke_xml = discipline.getElementsByTagName("stroke")[0].childNodes[0].nodeValue
        course_xml = discipline.getElementsByTagName("course")[0].childNodes[0].nodeValue
        gender_xml = discipline.getElementsByTagName("gender")[0].childNodes[0].nodeValue

        if distance_xml == distance and stroke_xml == style and course_xml == course and gender_xml == gender:
                
            #informace o plavci
            athlete = record.getElementsByTagName("athlete")[0]
            athlete_name = athlete.getElementsByTagName("holder_name")[0].childNodes[0].nodeValue
            athlete_nationality = athlete.getElementsByTagName("holder_nationality")[0].childNodes[0].nodeValue

            #informace o rekordu
            performance = record.getElementsByTagName("performance")[0]
            wr_time = performance.getElementsByTagName("time")[0].childNodes[0].nodeValue
            wr_year = performance.getElementsByTagName("year")[0].childNodes[0].nodeValue

            #úprava formátu času WR
            split_wr_time = wr_time.split(":")
            edited_wr_time = int(split_wr_time[0]) * 60 + int(split_wr_time[1]) + int(split_wr_time[2]) * 0.01

            #úprava formátu času plavce
            time_split = time.split(":")
            edited_time = int(time_split[0]) * 60 + int(time_split[1]) + int(time_split[2]) * 0.01

            points = int(1000 * ((edited_wr_time/edited_time)**3))
            
            break

    #jestliže neexistuj proměná points příkaz se nevykoná (neboli nebyly zvoleny existující disciplíny např. 800m prsa)
    if "points" in locals():
        return jsonify({"tim" : time, "point" : points, "ath_nam" : athlete_name, "ath_nat" : athlete_nationality, "wr_t" : wr_time, "wr_y" : wr_year})
    else:
        return jsonify({"error" : "Data are not valid!"})
if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0")

