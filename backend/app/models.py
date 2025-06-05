# app/models.py

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Process(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), nullable=False)
    priority = db.Column(db.String(20), nullable=False)
    timestamp = db.Column(db.String(50), nullable=False)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "priority": self.priority,
            "timestamp": self.timestamp
        }
