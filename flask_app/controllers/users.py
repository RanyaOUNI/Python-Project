
@app.route('/blood_request')
def blood_request():
    every = Demand.get_all_demands_with_hospitals()
    return render_template("blood_request.html",every = every)