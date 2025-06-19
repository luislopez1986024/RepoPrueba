DB_CONFIG = {
    'server': 'DESKTOP-BP8S587',
    'database': 'SistemaElectoral',
    'driver': 'ODBC Driver 17 for SQL Server',
    'trusted_connection': 'yes'
}

def get_connection_string():
    return (
        f"DRIVER={{{DB_CONFIG['driver']}}};"
        f"SERVER={DB_CONFIG['server']};"
        f"DATABASE={DB_CONFIG['database']};"
        f"Trusted_Connection={DB_CONFIG['trusted_connection']};"
    )