import ENV
from .database_model import *
import mysql.connector
from .database_model import _DB 
from typing import Tuple, Dict, overload, Union

_db_config = {
    'user': ENV.get("AWS_DB_ADMIN"),
    'password': ENV.get("AWS_DB_PASSWORD"),
    'host': ENV.get("AWS_DB_HOST"),
    'port': ENV.get("AWS_DB_PORT"),
    'database': ENV.get("AWS_DB_DATABASE")
}
DB = _DB(_db_config)

@overload
def query(Q:str) -> mysql.connector.cursor: ...
@overload
def query(Q:str,args:Optional[Union[Dict[Any,Any],Tuple]]) -> mysql.connector.cursor: ...

def query(Q:str,args:Optional[Union[Dict[Any,Any],Tuple]] = None) -> mysql.connector.cursor:
    cursor = DB.cnx.cursor()
    if (args is None):
        cursor.execute(Q)
    else:
        cursor.execute(Q,args)
    return cursor

