import sqlite3
from peewee import *
from datetime import date

db = SqliteDatabase('athletes.db')

class Team(Model):
    name = CharField()

    class Meta:
        database = db

class Athlete(Model):
    name = CharField()
    year = CharField()

    class Meta:
        database = db

class Athlete_Team(Model):
    athlete = ForeignKeyField(Athlete, backref='athlete')
    team = ForeignKeyField(Team, backref='team')

    class Meta:
        database = db

class Coach(Model):
    name = CharField()

    class Meta:
        database = db

class Coach_Team(Model):
    team = ForeignKeyField(Team, backref='team')
    coach = ForeignKeyField(Coach, backref='coach')

    class Meta:
        database = db

class StrCoach(Model):
    name = CharField()

    class Meta:
        database = db

class StrCoach_Team(Model):
    team = ForeignKeyField(Team, backref='team')
    strcoach = ForeignKeyField(StrCoach, backref='strcoach')

    class Meta:
        database = db

class DataStream(Model):
    athlete = ForeignKeyField(Athlete, backref='datastream')
    date = DateTimeField(default='datetime.datetime(month, day, year, hour, minute)')

    class Meta:
        database = db

class RQuestionaire(DataStream):
    fatigue = SmallIntegerField()
    musclesoreness = SmallIntegerField()
    sleepquality = SmallIntegerField()
    stress = SmallIntegerField()
    wellnesssum = SmallIntegerField()

    class Meta:
        database = db

class TQuestionaire(DataStream):
    sessiontype = TextField()
    sessionduration = SmallIntegerField()
    breathlessness = SmallIntegerField()
    lowerbodyload = SmallIntegerField()
    upperbodyload = SmallIntegerField()
    overallexertion = SmallIntegerField()

    class Meta:
        database = db

class ForceDecks(DataStream):
    testtype = TextField()
    trialnum = IntegerField()
    rsi = DecimalField()
    si = DecimalField()
    jumpheight = DecimalField()
    activestiff = DecimalField()
    activestiffindex = DecimalField()
    conimpulse= DecimalField()
    conmeanforce = IntegerField()
    conmeanpowerbw = DecimalField()
    conmeanpower = IntegerField()
    conpeakvel = DecimalField()
    contacttime = DecimalField()
    cmdepth = DecimalField()
    dropheight = DecimalField()
    droplanding = DecimalField()
    eccconforceratio = DecimalField()
    eccimp = DecimalField()
    eccmeanforce = IntegerField()
    efectivedrop = DecimalField()
    flighttime = DecimalField()
    forcezerovel = IntegerField()
    starttopeakpwr = DecimalField()
    peakdriveforce = IntegerField()
    peaklandforce = DecimalField()
    peakpowerbw = DecimalField()
    peakpower = IntegerField()
    positiveimp = DecimalField()
    startconphase = DecimalField()
    velattakeoff = DecimalField()
    contacttrough = IntegerField()
    jhtolandrfd = DecimalField()
    jhtopeaklandforce = DecimalField()
    landnetpeak = DecimalField()
    landingrfd = IntegerField()
    meanlandaccel = DecimalField()
    meanlandpwr = DecimalField()
    meanlandvel = DecimalField()
    passivestiff = DecimalField()
    passivestiffindex = DecimalField()
    peakimpactforce = DecimalField()
    peaklandaccel = DecimalField()
    peaktakeoffaccel = DecimalField()

    class Meta:
        database = db

class FitFor90(DataStream):
    rpe = IntegerField()
    duration = IntegerField()
    load = IntegerField()
    category = TextField()
    type = TextField()

class JumpMat(DataStream):
    jumpheight = DecimalField()
    contacttime = DecimalField()

    class Meta:
        database = db

class GPS(DataStream):
    playerload = IntegerField()
    avghr = IntegerField()
    hrabove85 = IntegerField()
    impacts = IntegerField()
    distancepermin = DecimalField()
    highspeedrun = DecimalField()

    class Meta:
        database = db

db.connect('athletes.db')

db.create_tables([Team, Athlete, Athlete_Team, Coach, Coach_Team, StrCoach, \
StrCoach_Team, RQuestionaire, TQuestionaire, ForceDecks, FitFor90, JumpMat, GPS])

db.close()
