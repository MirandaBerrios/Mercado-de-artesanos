-- USER SQL
ALTER USER "MERCADOARTESANOS"
DEFAULT TABLESPACE "USERS"
TEMPORARY TABLESPACE "TEMP"
ACCOUNT UNLOCK ;

-- QUOTAS
ALTER USER "MERCADOARTESANOS" QUOTA UNLIMITED ON "USERS";

-- ROLES
ALTER USER "MERCADOARTESANOS" DEFAULT ROLE "RESOURCE";

-- SYSTEM PRIVILEGES
