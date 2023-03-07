from itemadapter import ItemAdapter
import mysql.connector

class WeatherPipeline:
    def __init__(self):
        self.conn=mysql.connector.connect(
           host='localhost',
           password='111111',
           username='root',
           database='weather'
       )
        self.cur=self.conn.cursor()

        self.cur.execute("""

        CREATE TABLE IF NOT EXISTS report (
            id int NOT NULL auto_increment, 
            city VARCHAR(255),
            temperature VARCHAR(255),
            conditions VARCHAR(255),
            visibility VARCHAR(255),
            wind VARCHAR(255),
            PRIMARY KEY (id)
        )        
        """)       
    def process_item(self, item, spider):
        # self.cur.execute (
        #     """
        #     INSERT INTO report ( city,temperature,conditions,visibility,wind) values (%s,%s,%s,%s,%s)               
        #     """,
        #     (
        #     item['city'],
        #     item['temperature'],
        #     item['conditions'],
        #     item['visibility'],
        #     item['wind'],
        #     )
        # )
        
        self.cur.execute (
            """
            UPDATE report SET temperature=%s, conditions=%s, visibility=%s, wind=%s where city=%s
            """,
            (            
            item['temperature'],
            item['conditions'],
            item['visibility'],
            item['wind'],
            item['city'], 
            )
        )
        self.conn.commit()
           
    def close_spider(self, spider):
        self.cur.close()
        self.conn.close()