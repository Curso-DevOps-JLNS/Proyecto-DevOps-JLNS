from app import create_app
from app.models import db  # ⬅️ IMPORTANTE

app = create_app()

if __name__ == "__main__":
    with app.app_context():
        db.create_all()  # ⬅️ CREAR TABLAS SI NO EXISTEN
    app.run(host="0.0.0.0", port=5000)
