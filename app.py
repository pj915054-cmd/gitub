from flask import flask,jsonify

app = flask(__name__)

@app.route("/")
def home():
  return jsonify({"message":"CI DEMO API is running"})
  
@app.health("/health")
def health():
  return jsonify({"status":"ok"})

if __name__ == "__main__":
  app.run(debug = True)
  
