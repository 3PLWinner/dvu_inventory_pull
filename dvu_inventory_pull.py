import pandas as pd;
import psycopg2
import os
from datetime import datetime
import logging

logging.basicConfig(
    filename='app.log',
    filemode='a',
    level=logging.DEBUG
)

# Create a connection to the database
try:
    conn = psycopg2.connect("host='3plwinner.replica.wdgcorp.com' dbname='_9867200137_p' user='_9867200137' password='y5q549tXAUccq9bA'")
except Exception as err:
    logging.error(err)




try: 
    query = '''SELECT stor.description, item.item_code, inv.containerid, inv.qty_available, inv.qty_allocated, inv.qty_hold, inv.qty_quarantine, inv.qty_damaged, inv.qty_shipped 
    FROM dv_inventory inv 
    LEFT JOIN dv_item item ON inv.item_id = item.id 
    LEFT JOIN dv_storage stor ON inv.storage_id = stor.id 
    WHERE inv.containerid <> '' '''
    inventory_df = pd.read_sql(query, conn)
except Exception as err:
    logging.error(err)


current_path = os.path.abspath(os.getcwd())

time = datetime.now().strftime("%m-%d-%Y_%H_%M")

try:
    inventory_df = inventory_df.set_index("description")

    inventory_df.to_csv(current_path + "\\data\\DVU_inventory_"+time+".csv")
except Exception as err:
    logging.error(err)

conn.close()