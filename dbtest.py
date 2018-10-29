import sqlite3
from peewee import *
from datetime import date
from athlete_db import DataStream
from athlete_db import RQuestionaire
from athlete_db import Athlete
from athlete_db import ForceDecks
from athlete_db import Athlete_Team
from athlete_db import Team


db = SqliteDatabase('athletes.db')

db.connect('athletes.db')


query = (RQuestionaire.select().join(Athlete).join(Athlete_Team).join(Team).where(\
RQuestionaire.date.between('8/21/18 6:10', '8/22/18 7:10')))
for entry in query:
    tag = Athlete.get(Athlete.id == entry.athlete_id)
    print(tag.name, entry.date, entry.stress)


query2 = (TQuestionaire.select().join(Athlete).join(Athlete_Team).join(Team).where(\
TQuestionaire.date.between('8/01/18 6:10', '8/22/18 7:10')))
for entry in query2:
    tag = Athlete.get(Athlete.id == entry.athlete_id)
    print(tag.name, entry.date, entry.sessiontype, entry.sessionduration)

query3 = (ForceDecks.select().join(Athlete).join(Athlete_Team).join(Team).where(\
ForceDecks.date.between('04/17/2018 10:00', '04/17/2018 11:50')))
for entry in query3:
    tag = Athlete.get(Athlete.id == entry.athlete_id)
    print(tag.name, entry.date, entry.testtype, entry.trialnum, entry.rsi, \
    entry.jumpheight, entry.peakpower, entry.conimpulse, entry.eccconforceratio)
