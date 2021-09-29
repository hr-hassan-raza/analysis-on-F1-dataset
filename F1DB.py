import pandas as pd

def readData():

    circuits = pd.read_csv('./f1db_csv/circuits.csv')
    lapTimes = pd.read_csv('./f1db_csv/lap_times.csv')
    races = pd.read_csv('./f1db_csv/races.csv')
    drivers = pd.read_csv('./f1db_csv/drivers.csv')
    constructors = pd.read_csv('./f1db_csv/constructors.csv')
    piStops = pd.read_csv('./f1db_csv/pit_stops.csv')
    results = pd.read_csv('./f1db_csv/results.csv')

    return circuits, lapTimes,races,drivers,constructors,piStops,results

## Adding foreign keys and creating relationships
def createRelationships():

    circuits, lapTimes,races,drivers,constructors,piStops,results = readData()

    results.fastestLapSpeed[results.fastestLapSpeed=='\\N'] = 0
    drivers["fullName"] = drivers["forename"] + str(' ') + drivers["surname"]
    piStops['milliseconds_pitstops'] = piStops['milliseconds']
    colsUse = ['circuitId', 'raceId']
    results = results.merge(races[colsUse], left_on='raceId', right_on='raceId')
    colsUse = ['driverId', 'fullName']
    results = results.merge(drivers[colsUse], left_on='driverId', right_on='driverId')
    colsUse = ['raceId', 'milliseconds_pitstops']
    results = results.merge(piStops[colsUse], left_on='raceId', right_on='raceId')
    
    return circuits, lapTimes,races,drivers,constructors,piStops,results

def writeToDatabase(conn):

    circuits, lapTimes,races,drivers,constructors,piStops,results = createRelationships()

    namesData = ['circuits', 'lapTimes', 'races','drivers','constructors','piStops' ,'results']
    DataFrames = [circuits, lapTimes, races,drivers,constructors,piStops,results]

    for i in range(len(namesData)):
        DataFrames[i].to_sql(namesData[i], conn, if_exists='replace', index=False)

def makeJson(conn):

    namesData = ['circuits', 'lapTimes', 'races','drivers','constructors','piStops' ,'results']

    for i in range(len(namesData)):
        qurry = 'SELECT * FROM ' + str(namesData[i])
        #print(qurry)
        df = pd.read_sql_query(qurry, conn)
        path = str('./JasonFiles/'+namesData[i]+ '.json')
        #print(path)
        df.to_json(path)