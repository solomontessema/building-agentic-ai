from flask import Flask, render_template, request, send_from_directory
import os

app = Flask(__name__, template_folder="templates")

# Serve root-level assets like style.css and script.js
@app.route('/<path:filename>')
def serve_root_assets(filename):
    return send_from_directory(app.root_path, filename)

# Serve images from the img/ directory
@app.route('/img/<path:filename>')
def serve_images(filename):
    return send_from_directory(os.path.join(app.root_path, 'img'), filename)

@app.route("/", methods=["GET", "POST"])
def index():
    response = None
    if request.method == "POST":
        query = request.form.get("query")
        if query:
            from agents.base_agent import agent
            response = agent.run(query)
    return render_template("index.html", response=response)

if __name__ == "__main__":
    app.run(debug=True)
