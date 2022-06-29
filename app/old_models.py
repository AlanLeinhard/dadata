from re import S
from flask import url_for, g

from datetime import datetime
from flask_login import UserMixin
from flask_security import RoleMixin
from app import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship


from app import db


class roles_users(db.Model):
    __tablename__ = 'roles_user'
    id = db.Column(db.Integer, primary_key=True)
    desc = db.Column(db.String)
    user_id = db.Column(db.Integer(), db.ForeignKey("user.id"))
    role_id = db.Column(db.Integer(), db.ForeignKey("roles.id"))


class Role(db.Model, RoleMixin):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))
    users = relationship("User", secondary="roles_user",
                         back_populates='roles')

    def __str__(self):
        return self.name


class User(db.Model, UserMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, unique=True, primary_key=True)
    name = db.Column(db.String)
    username = db.Column(db.String, unique=True)
    email = db.Column(db.String, unique=True)
    password = db.Column(db.String)
    created_on = db.Column(db.DateTime(), default=datetime.utcnow)
    updated_on = db.Column(
        db.DateTime(), default=datetime.utcnow, onupdate=datetime.utcnow)
    # Нужен для security!
    active = db.Column(db.Boolean())
    # Для получения доступа к связанным объектам
    roles = relationship("Role", secondary="roles_user",
                         back_populates='users')

    # Flask - Login
    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    # Flask-Security
    def has_role(self, *args):
        return set(args).issubset({role.name for role in self.roles})

    def get_id(self):
        return self.id

    # Required for administrative interface
    def __unicode__(self):
        return self.username

    def set_password(self, password):
        self.password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)


# Отвечает за сессию пользователей. Запрещает доступ к роутам, перед которыми указано @login_required
# @login_manager.user_loader
# def load_user(user_id):
#     if db.session["user_id"]:
#         user = User.query.filter_by(username=db.session["user_id"]).first()
#     else:
#         user = {"name": "Guest"}  # Make it better, use an anonymous User instead

#     g.user = user
#     return db.session.query(User).get(user_id)

class Post(db.Model):
    __tablename__ = 'post'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    desc = db.Column(db.String, nullable=False)
    body = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)

    @property
    def update_url(self):
        return url_for("site.update", id=self.id)

    @property
    def delete_url(self):
        return url_for("site.delete", id=self.id)


class Item(db.Model):
    __tablename__ = 'item'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    desc = db.Column(db.String, nullable=False)
    url_serv = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)
    click = db.Column(db.Integer)
    active = db.Column(db.Boolean())

    def __repr__(self):
        return self.title


class Project(db.Model):
    __tablename__ = 'project'
    id = db.Column(db.Integer, primary_key=True)
    author_id = db.Column(db.Integer, nullable=False)
    title = db.Column(db.String(100), nullable=False)
    created = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    desc = db.Column(db.String, nullable=False)
    url_serv = db.Column(db.String, nullable=False)
    image = db.Column(db.LargeBinary)
    click = db.Column(db.Integer)
    active = db.Column(db.Boolean())

    def __repr__(self):
        return self.title


class Region(db.Model):
    __tablename__ = 'fias_region'
    AOGUID = db.Column(db.Integer, primary_key=True)
    REGIONCODE = db.Column(db.String(2), nullable=False)
    REGIONNAME = db.Column(db.String(36), nullable=False)
    UPDATEDATE = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    STARTDATE = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    ENDDATE = db.Column(
        db.DateTime, nullable=False, server_default=db.func.current_timestamp()
    )
    ISACTUAL = db.Column(db.Integer, nullable=False)
    ISACTIVE = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.title


class ADDROBJ(db.Model):
    __tablename__ = 'ADDROBJ'
    ID = db.Column(db.Integer, primary_key=True)
    AOGUID = db.Column(db.String(36), nullable=False)
    FORMALNAME = db.Column(db.String(120), nullable=False)
    REGIONCODE = db.Column(db.String(2), nullable=False)
    AUTOCODE = db.Column(db.String(1), nullable=False)
    AREACODE = db.Column(db.String(3), nullable=False)
    CITYCODE = db.Column(db.String(3), nullable=False)
    CTARCODE = db.Column(db.String(3), nullable=False)
    PLACECODE = db.Column(db.String(3), nullable=False)
    PLANCODE = db.Column(db.String(4), nullable=False)
    STREETCODE = db.Column(db.String(4), nullable=False)
    EXTRCODE = db.Column(db.String(4), nullable=False)
    SEXTCODE = db.Column(db.String(3), nullable=False)
    OFFNAME = db.Column(db.String(120), nullable=False)
    POSTALCODE = db.Column(db.String(6), nullable=False)
    IFNSFL = db.Column(db.String(4), nullable=False)
    TERRIFNSFL = db.Column(db.String(4), nullable=False)
    IFNSUL = db.Column(db.String(4), nullable=False)
    TERRIFNSUL = db.Column(db.String(4), nullable=False)
    OKATO = db.Column(db.String(11), nullable=False)
    OKTMO = db.Column(db.String(11), nullable=False)
    UPDATEDATE = db.Column(db.Date, nullable=False)
    SHORTNAME = db.Column(db.String(10), nullable=False)
    AOLEVEL = db.Column(db.Integer, nullable=False)
    PARENTGUID = db.Column(db.String(36), nullable=False)
    AOID = db.Column(db.String(36), nullable=False)
    PREVID = db.Column(db.String(36), nullable=False)
    NEXTID = db.Column(db.String(36), nullable=False)
    CODE = db.Column(db.String(17), nullable=False)
    PLAINCODE = db.Column(db.String(15), nullable=False)
    ACTSTATUS = db.Column(db.Integer, nullable=False)
    LIVESTATUS = db.Column(db.Integer, nullable=False)
    CENTSTATUS = db.Column(db.Integer, nullable=False)
    OPERSTATUS = db.Column(db.Integer, nullable=False)
    CURRSTATUS = db.Column(db.Integer, nullable=False)    
    STARTDATE = db.Column(db.Date, nullable=False)
    ENDDATE = db.Column(db.Date, nullable=False)
    NORMDOC = db.Column(db.String(36), nullable=False)
    CADNUM = db.Column(db.String(36), nullable=False)
    DIVTYPE = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return self.title


class STEAD(db.Model):
    __tablename__ = 'STEAD'
    ID = db.Column(db.Integer, primary_key=True)
    STEADGUID = db.Column(db.String(36), nullable=False)
    NUMBER = db.Column(db.String(36), nullable=False)
    REGIONCODE = db.Column(db.String(2), nullable=False)
    POSTALCODE = db.Column(db.String(6), nullable=False)
    IFNSFL = db.Column(db.String(4), nullable=False)
    TERRIFNSFL = db.Column(db.String(4), nullable=False)
    IFNSUL = db.Column(db.String(4), nullable=False)
    TERRIFNSUL = db.Column(db.String(4), nullable=False)
    OKATO = db.Column(db.String(11), nullable=False)
    OKTMO = db.Column(db.String(11), nullable=False)
    UPDATEDATE = db.Column(db.Date, nullable=False)
    PARENTGUID = db.Column(db.String(36), nullable=False)
    STEADID = db.Column(db.String(36), nullable=False)
    PREVID = db.Column(db.String(36), nullable=False)
    NEXTID = db.Column(db.String(36), nullable=False)
    LIVESTATUS = db.Column(db.Integer, nullable=False)
    OPERSTATUS = db.Column(db.Integer, nullable=False)  
    STARTDATE = db.Column(db.Date, nullable=False)
    ENDDATE = db.Column(db.Date, nullable=False)
    NORMDOC = db.Column(db.String(36), nullable=False)
    CADNUM = db.Column(db.String(36), nullable=False)
    DIVTYPE = db.Column(db.Integer, nullable=False)
    

    def __repr__(self):
        return self.title


class HOUSE(db.Model):
    __tablename__ = 'HOUSE'
    ID = db.Column(db.Integer, primary_key=True)
    POSTALCODE = db.Column(db.String(6), nullable=False)
    IFNSFL = db.Column(db.String(4), nullable=False)
    TERRIFNSFL = db.Column(db.String(4), nullable=False)
    IFNSUL = db.Column(db.String(4), nullable=False)
    TERRIFNSUL = db.Column(db.String(4), nullable=False)
    OKATO = db.Column(db.String(11), nullable=False)
    OKTMO = db.Column(db.String(11), nullable=False)
    UPDATEDATE = db.Column(db.DateTime, nullable=False)
    HOUSENUM = db.Column(db.String(20), nullable=False)
    ESTSTATUS = db.Column(db.Integer, nullable=False)
    BUILDNUM = db.Column(db.String(50), nullable=False)
    STRUCNUM = db.Column(db.String(50), nullable=False)
    STRSTATUS = db.Column(db.Integer, nullable=False)
    HOUSEID = db.Column(db.String(36), nullable=False)
    HOUSEGUID = db.Column(db.String(36), nullable=False)
    AOGUID = db.Column(db.String(36), nullable=False)
    STARTDATE = db.Column(db.Date, nullable=False)
    ENDDATE = db.Column(db.Date, nullable=False)
    STATSTATUS = db.Column(db.Integer, nullable=False)  
    NORMDOC = db.Column(db.String(36), nullable=False)
    COUNTER = db.Column(db.Integer, nullable=False) 
    CADNUM = db.Column(db.String(100), nullable=False)
    DIVTYPE = db.Column(db.Integer, nullable=False)


    def __repr__(self):
        return self.title


class ROOM(db.Model):
    __tablename__ = 'ROOM'
    ID = db.Column(db.Integer, primary_key=True)
    ROOMID = db.Column(db.String(36), nullable=False)
    ROOMGUID = db.Column(db.String(36), nullable=False)
    HOUSEGUID = db.Column(db.String(36), nullable=False)
    REGIONCODE = db.Column(db.String(2), nullable=False)
    FLATNUMBER = db.Column(db.String(50), nullable=False)
    FLATTYPE = db.Column(db.Integer, nullable=False)
    ROOMNUMBER = db.Column(db.String(50), nullable=False)
    ROOMTYPEID = db.Column(db.Integer, nullable=False)
    POSTALCODE = db.Column(db.String(6), nullable=False)
    UPDATEDATE = db.Column(db.DateTime, nullable=False)
    PREVID = db.Column(db.String(36), nullable=False)
    NEXTID = db.Column(db.String(36), nullable=False)
    STARTDATE = db.Column(db.Date, nullable=False)
    ENDDATE = db.Column(db.Date, nullable=False)
    LIVESTATUS = db.Column(db.Integer, nullable=False)  #STEAD
    STATSTATUS = db.Column(db.Integer, nullable=False)  
    NORMDOC = db.Column(db.String(36), nullable=False)
    CADNUM = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.title


class NORDOC(db.Model):
    __tablename__ = 'NORDOC'
    ID = db.Column(db.Integer, primary_key=True)
    NORMDOCID = db.Column(db.String(36), nullable=False)
    DOCNAME = db.Column(db.String(255), nullable=False)
    DOCDATE = db.Column(db.Date, nullable=False)
    DOCNUM = db.Column(db.String(20), nullable=False)
    DOCTYPE = db.Column(db.Integer, nullable=False)
    DOCIMGID = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return self.title


class SOCRBASE(db.Model):
    __tablename__ = 'SOCRBASE'
    ID = db.Column(db.Integer, primary_key=True)
    LEVEL = db.Column(db.String(5), nullable=False)
    SCNAME = db.Column(db.String(10), nullable=False)
    SOCRNAME = db.Column(db.String(50), nullable=False)
    KOD_T_ST = db.Column(db.String(4), nullable=False)

    def __repr__(self):
        return self.title


class CURENTST(db.Model):
    __tablename__ = 'CURENTST'
    ID = db.Column(db.Integer, primary_key=True)
    CURENTSTID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.title


class ACTSTAT(db.Model):
    __tablename__ = 'ACTSTAT'
    ID = db.Column(db.Integer, primary_key=True)
    ACTSTATID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.title


class OPERSTAT(db.Model):
    __tablename__ = 'OPERSTAT'
    ID = db.Column(db.Integer, primary_key=True)
    OPERSTATID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.title


class CENTERST(db.Model):
    __tablename__ = 'CENTERST'
    ID = db.Column(db.Integer, primary_key=True)
    CENTERSTID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return self.title


class HSTSTAT(db.Model):
    __tablename__ = 'HSTSTAT'
    ID = db.Column(db.Integer, primary_key=True)
    HOUSESTID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return self.title


class ESTSTAT(db.Model):
    __tablename__ = 'ESTSTAT'
    ID = db.Column(db.Integer, primary_key=True)
    ESTSTATID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(20), nullable=False)
    SHORTNAME = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.title


class STRSTAT(db.Model):
    __tablename__ = 'STRSTAT'
    ID = db.Column(db.Integer, primary_key=True)
    STRSTATID = db.Column(db.Integer, nullable=False)
    NAME = db.Column(db.String(20), nullable=False)
    SHORTNAME = db.Column(db.String(20), nullable=False)

    def __repr__(self):
        return self.title



# Отвечает за сессию пользователей. Запрещает доступ к роутам, перед которыми указано @login_required
@login_manager.user_loader
def load_user(user_id):
    return db.session.query(User).get(user_id)