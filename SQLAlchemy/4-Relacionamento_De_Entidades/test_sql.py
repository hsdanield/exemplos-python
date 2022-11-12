from infra.configs.connection import DBConnectionHandler
from infra.entities.country import Country
from sqlalchemy import text
from sqlalchemy import inspect

country_table = inspect(Country).local_table
print(country_table)

# db_conn = DBConnectionHandler()
# engine = db_conn.get_engine()

# class CountryTest:
#     table_name = "tb_country"
#     schema = "dev"


# with engine as db:
# #     result = db.execute(
# #         f"""
# #             SELECT `AUTO_INCREMENT`
# #             FROM  INFORMATION_SCHEMA.TABLES
# #             WHERE TABLE_SCHEMA = '{schema}'
# #             AND   TABLE_NAME   = '{table}';
# #         """
# #     )
# #     print(result.all())
