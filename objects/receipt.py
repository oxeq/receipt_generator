from sqlalchemy import Integer, String, Boolean
from sqlalchemy.orm import Mapped, mapped_column
from objects.db import db


class ReceiptInfo(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)

    # id транкзакции на интерхабе
    transaction_id: Mapped[str] = mapped_column(String, nullable=False)

    # время транкзакции timestamp
    date: Mapped[int] = mapped_column(Integer, nullable=False)

    # логин стима
    steam_login: Mapped[str] = mapped_column(String, nullable=False)

    # сумма к зачислению в копейках
    sum: Mapped[int] = mapped_column(Integer, nullable=False)
