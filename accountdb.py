import asyncio
import asyncpg

class AccountDB():
    def __init__(self):
        self.ac = []
        self.ev = []

    def GetAc(self, name, password):
        print('GA')
        asyncio.get_event_loop().run_until_complete(self.GetAcA(name, password))

    def ApAc(self, name, password):
        print('AA')
        asyncio.get_event_loop().run_until_complete(self.ApAcA(name, password))

    def GetEv(self, id):
        print('GE')
        asyncio.get_event_loop().run_until_complete(self.GetEvA(id))

    def ApEv(self, title, description, town, link, typee, con, id_creator):
        print('AE')
        asyncio.get_event_loop().run_until_complete(self.ApEvA(title, description, town, link, typee, con, id_creator))

    def GetAllEv(self):
        print('GAE')
        asyncio.get_event_loop().run_until_complete(self.GetAllEvA())

    def GetEvU(self, id):
        print('GAE')
        asyncio.get_event_loop().run_until_complete(self.GetEvUA(id))

    def GetEvC(self, id):
        print('GAE')
        asyncio.get_event_loop().run_until_complete(self.GetEvCA(id))

    def RegEv(self, id_event, id_user):
        print('GAE')
        asyncio.get_event_loop().run_until_complete(self.RegEvA(id_event, id_user))

    async def GetAcA(self, name, password):
        print('GAA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('GAA2')
        res = await conn.fetch('''
            SELECT *
            FROM users 
            WHERE name = $1 and password = $2
            ''', name, password)
        print('GAA3')
        print(res)
        if res != []:
            self.ac = res[0]
            print(self.ac)
        await conn.close()

    async def ApAcA(self, name, password):
        print('AAA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('AAA2')
        res = await conn.fetch('''
            SELECT 
            COUNT(*)
            FROM users
            WHERE name = $1
            ''', name)
        print('AA3')
        if res[0][0] == 0:
            await conn.execute('''
                INSERT INTO users(name, password) VALUES
                ($1, $2)
                ''', name, password)

        print(res)
        await conn.close()

    async def GetEvA(self, id):
        print('GEA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('GEA2')
        res = await conn.fetch('''
            SELECT *
            FROM events 
            WHERE id = $1
            ''', id)
        print('GEA3')
        print(res)
        await conn.close()

    async def ApEvA(self, title, description, town, link, typee, con, id_creator):
        l = list()

        print('AEA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('AEA2')

        await conn.execute('''
            INSERT INTO events(title, description, town, link, typee, connect, id_creator) VALUES
            ($1, $2, $3, $4, $5, $6, $7)
            ''', title, description, town, link, typee, con, str(id_creator))

        print('AEA3')

        res = await conn.fetch('''
            SELECT eventsc
            FROM users 
            WHERE id = $1
            ''', id_creator)
        print(len(res))
        print(res)
        if str(res[0][0]) != 'None':
            print(res[0][0])
            evc = int(res[0][0]) + 1
        else:
            evc = 1

        await conn.execute('''
            UPDATE users 
            SET eventsc = $1 WHERE id = $2
            ''', evc, id_creator)

        ev_id = await conn.fetch('''
            SELECT id
            FROM events 
            WHERE title = $1 and description = $2 and town = $3 and link = $4 and typee = $5 and connect = $6 and id_creator = $7
            ''', title, description, town, link, typee, con, str(id_creator))

        res = await conn.fetch('''
            SELECT id_eventsc
            FROM users 
            WHERE id = $1
            ''', id_creator)
        print(res)
        print(res[0][0])
        if res[0][0] != []:
            for i in res:
                l.append(i[0][0])
        l.append(str(ev_id[0][0]))
        print(l)
        await conn.execute('''
            UPDATE users 
            SET id_eventsc = $1 WHERE id = $2
            ''', l, id_creator)
        await conn.close()

    async def GetAllEvA(self):
        print('GAEA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('GAEA2')
        res = await conn.fetch('''
            SELECT *
            FROM events
            ''')
        print('GAEA3')
        print(res)
        self.ev = res
        await conn.close()

    async def GetEvUA(self, id):
        print('GEUA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('GAEA2')
        id_events = await conn.fetch('''
            SELECT id_eventsu
            FROM users
            WHERE id = $1
            ''', id)

        print('GAEA321')
        self.ev = []
        print(id_events)
        print(id_events[0])
        print(id_events[0][0])
        if id_events[0][0] != None:
            for i in id_events[0][0]:
                print('J  ', i)
                res = await conn.fetch('''
                    SELECT *
                    FROM events
                    WHERE id = $1
                    ''', int(i))
                self.ev.append(res)

            print(res)

        await conn.close()

    async def GetEvCA(self, id):
        print('GECA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('GAEA2')
        id_events = await conn.fetch('''
            SELECT id_eventsc
            FROM users
            WHERE id = $1
            ''', id)

        print('GAEA3')
        self.ev = []
        if id_events[0][0] != None:
            for i in id_events[0][0]:
                print('J  ', i)
                res = await conn.fetch('''
                    SELECT *
                    FROM events
                    WHERE id = $1
                    ''', int(i))
                self.ev.append(res)

            print(res)

        await conn.close()

    async def RegEvA(self, id_event, id_user):
        l = list()

        print('AEA1')
        conn = await asyncpg.connect('postgres://ihrqjpfx:dfotcLNv_Evt3aGnEfQ-J_s6LV_I2j8g@flora.db.elephantsql.com/ihrqjpfx')
        print('AEA2')

        res = await conn.fetch('''
                    SELECT eventsu
                    FROM users 
                    WHERE id = $1
                    ''', id_user)
        print(len(res))
        print(res)
        if str(res[0][0]) != 'None':
            print(res[0][0])
            evc = int(res[0][0]) + 1
        else:
            evc = 1

        await conn.execute('''
                    UPDATE users 
                    SET eventsu = $1 WHERE id = $2
                    ''', evc, id_user)

        res = await conn.fetch('''
                    SELECT id_eventsu
                    FROM users 
                    WHERE id = $1
                    ''', id_user)
        print(res)
        print(res[0][0])
        if res[0][0] != None:
            for i in res:
                l.append(i[0][0])
        l.append(str(id_event))
        print(l)
        await conn.execute('''
                    UPDATE users 
                    SET id_eventsu = $1 WHERE id = $2
                    ''', l, id_user)

        await conn.close()