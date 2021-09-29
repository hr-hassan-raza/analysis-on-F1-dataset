import pandas as pd
import sqlite3

#How many points has each driver scored?
def PointsEachDriverScore(conn):
    conn = sqlite3.connect('F1ResultsDb.db')
    qurry = '''select
        [fullName],
        sum(points) points
    from
        results
    Group by [fullName]
    '''
    df = pd.read_sql_query(qurry, conn)
    return df
##In how many races do each driver participate?
def RacesDriver(conn):
    queery = '''
    select fullName, count(distinct raceId)
    from results
    group by fullName
    '''
    df = pd.read_sql_query(queery, conn)
    return df
##What is the trend of fastest lap speed over the years per circuit?
def fastestLap(conn):
    Q = 'SELECT circuitId, fastestLapSpeed FROM results' 
    df = pd.read_sql_query(Q, conn)
    return df
## What is the trend of pit stop times over the years per constructor in a given circuit? 
def PiStops(conn):
    querry = 'SELECT constructorId, milliseconds_pitstops FROM results'
    df = pd.read_sql_query(querry, conn)
    return df