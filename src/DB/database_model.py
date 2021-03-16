from pydantic import BaseModel
from typing import Optional, Dict, Any
import mysql.connector.connection as connection
import mysql.connector


class _DB(BaseModel):
    cnx: connection
    configuration:Dict[str, Any]
    def __init__(self,config:Dict[str, Any]):
        self.configuration = config
        self.cnx = mysql.connector.connect(**self.configuration)

    def connect(self, config:Optional[Dict[str, Any]] = None ):
        try:
            self.cnx.close()
        finally:
            if (config is not None):
                self.configuration = config
            self.cnx = mysql.connector.connect(**self.configuration)
    
    def close(self):
        self.cnx.close()