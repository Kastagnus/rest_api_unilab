from MyProject.application import app
from MyProject.db import db


@app.before_first_request
def create_table():
    db.create_all()

if __name__ == "__main__":

    db.init_app(app)
    app.run(debug=True, port=5100)

