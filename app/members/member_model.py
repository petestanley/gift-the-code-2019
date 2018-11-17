from flask_sqlalchemy import SQLAlchemy


builtin_list = list


db = SQLAlchemy()


def init_app(app):
    # Disable track modifications, as it unnecessarily uses memory.
    app.config.setdefault('SQLALCHEMY_TRACK_MODIFICATIONS', False)
    db.init_app(app)


def from_sql(row):
    """Translates a SQLAlchemy model instance into a dictionary"""
    data = row.__dict__.copy()
    data['id'] = row.id
    data.pop('_sa_instance_state')
    return data


# [START model]
class Member(db.Model):
    __tablename__ = 'transactions'

    id = db.Column(db.Integer, primary_key=True)
    trx_date = db.Column(db.Date)
    email = db.Column(db.String(255))
    mopoints = db.Column(db.Integer)
    posting_type = db.Column(db.String(255))

    def __repr__(self):
        return "<Member(email='%s', app=%s)" % (self.email, self.mopoints)
# [END model]


# [START create]
def create(data):
    member = Member(**data)
    db.session.add(member)
    db.session.commit()
    return from_sql(member)
# [END create]


# [START read]
def read(id):
    result = Member.query.get(id)
    if not result:
        return None
    return from_sql(result)
# [END read]


# [START update]
def update(data, id):
    member = Member.query.get(id)
    for k, v in data.items():
        setattr(member, k, v)
    db.session.commit()
    return from_sql(member)
# [END update]


def delete(id):
    Member.query.filter_by(id=id).delete()
    db.session.commit()
