import pandas as pd;
import psycopg2
import os
from datetime import datetime

# Create a connection to the database
conn = psycopg2.connect("host='3plwinner.replica.wdgcorp.com' dbname='_9867200137_p' user='_9867200137' password='y5q549tXAUccq9bA'")

try: 
    query = '''SELECT stor.description, item.item_code, inv.containerid, inv.qty_available, inv.qty_allocated, inv.qty_hold, inv.qty_quarantine, inv.qty_damaged, inv.qty_shipped 
    FROM dv_inventory inv 
    LEFT JOIN dv_item item ON inv.item_id = item.id 
    LEFT JOIN dv_storage stor ON inv.storage_id = stor.id 
    WHERE inv.containerid <> '' '''
    inventory_df = pd.read_sql(query, conn)
except Exception as err:
    print(err)


current_path = os.path.abspath(os.getcwd())

time = datetime.now().strftime("%H:%M:%S")

inventory_df.to_csv(current_path + "DVU_inventory_"+time+".csv")

conn.close()