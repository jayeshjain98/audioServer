import database_services.operation.bd_databaseconfiguration as cfg
from psycopg2 import pool

db_connection_pool=pool.SimpleConnectionPool(cfg.min_connection,
	cfg.max_connection,
	database=cfg.database,
	user=cfg.db_user,
	password=cfg.db_password,
	host=cfg.host,
	port=cfg.port)