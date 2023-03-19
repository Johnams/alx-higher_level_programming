#!/usr/bin/python3
# Lists all cities of the database hbtn_0e_4_usa, ordered by city id.
# Usage: ./4-cities_by_state.py <mysql username> \
#                               <mysql password> \
#                               <database name>
import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("SELECT `c`.`id`, `c`.`name`, `s`.`name` \
            FROM `cities` as `c` \
            INNER JOIN `states` as `s` \
              ON `c`.`state_id` = `s`.`id` \
            ORDER BY `c`.`id`")
    [print(city) for city in c.fetchall()]
