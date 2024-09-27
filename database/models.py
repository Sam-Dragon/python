from sqlalchemy import Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, Mapped

Base = declarative_base()

ID_SEQ = Sequence("id_seq", start=1)


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(Integer, ID_SEQ, primary_key=True, index=True,
                                    default=ID_SEQ.next_value())
    email: Mapped[str] = mapped_column(String(100), unique=True)
    password: Mapped[str] = mapped_column(String(100))
    name: Mapped[str] = mapped_column(String(1000))
