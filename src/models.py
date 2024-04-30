from sqlalchemy import MetaData, Table, Column, VARCHAR, Integer, Date, ForeignKey


metadata = MetaData()


group = Table(
    "group",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", VARCHAR(50), nullable=False)
)


child = Table(
    "child",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_id", Integer, ForeignKey("group.id", ondelete="CASCADE"), nullable=False),
    Column("first_name", VARCHAR(15), nullable=False),
    Column("last_name", VARCHAR(15), nullable=False),
    Column("sex", VARCHAR(1), nullable=False),
    Column("birthday", Date, nullable=False)
)

educator = Table(
    "educator",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_id", Integer, ForeignKey("group.id", ondelete="CASCADE"), nullable=False),
    Column("first_name", VARCHAR(15), nullable=False),
    Column("last_name", VARCHAR(15), nullable=False),
    Column("sex", VARCHAR(1), nullable=False),
    Column("birthday", Date, nullable=False)
)
