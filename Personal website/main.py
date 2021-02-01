from flask import Flask, render_template

# Render_template metoda pristupa html fajlovima i prikazuje ih
# Kada se izvrsi pajton fajl, specijalnoj promenljivoj name se dodeljuje vrednost main zato se izvrsava aplikacija
app = Flask(__name__)

# Ide na home page tj samo se ukuca localhost:5000
@app.route('/')
def home():
    return render_template("home.html")

# Ide na stranicu about tako da je potreno ukucati localhost:5000/about da bi dobili sadrzaj
@app.route('/about/')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
