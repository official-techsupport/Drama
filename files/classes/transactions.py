from files.helpers.const import KOFI_TOKEN

if KOFI_TOKEN:
	from sqlalchemy import *
	from files.__main__ import Base

	class Transaction(Base):

		__tablename__ = "transactions"
		id = Column(String, primary_key=True)
		created_utc = Column(Integer)
		type = Column(String)
		amount = Column(Integer)
		email = Column(String)
		claimed = Column(Boolean)

		def __repr__(self):
			return f"<Transaction(id={self.id})>"
