from sqlalchemy import MetaData, Table, Column, String, Integer, Date, ForeignKey


metadata = MetaData()


group = Table(
    "group_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False)
)


child = Table(
    "child_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_id", Integer, ForeignKey("group_data.id"), nullable=False),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("sex", String, nullable=False),
    Column("birthday", Date, nullable=False)
)

educator = Table(
    "educator_data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("group_id", Integer, ForeignKey("group_data.id"), nullable=False),
    Column("first_name", String, nullable=False),
    Column("last_name", String, nullable=False),
    Column("sex", String, nullable=False),
    Column("birthday", Date, nullable=False)
)
