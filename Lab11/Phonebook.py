import psycopg2
from config import load_config

def search(pattern):
    try:
        params = load_config()
        conn = psycopg2.connect(**params)
        cur = conn.cursor()

        # Явное указание типа TEXT
        cur.execute("SELECT * FROM search_phonebook(%s::TEXT);", (pattern,))

        rows = cur.fetchall()
        print(f"\n🔍 Search results for pattern '{pattern}':")
        for row in rows:
            print(f"ID: {row[0]}, Name: {row[1]}, Phone: {row[2]}")

        cur.close()
        conn.close()

    except (Exception, psycopg2.DatabaseError) as error:
        print(f"❌ Error: {error}")

if __name__ == '__main__':
    search("Ali")
