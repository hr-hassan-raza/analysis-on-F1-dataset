# analysis-on-F1-dataset

1) Justifications 
Task 1
The first part of task 1 required to find out how many points has each driver scored. In order to this we call PointsEachDriverScore(conn) which returns the dataframe which contains full names and points each driver scored. To get top ten drivers who scored most points we call function showTopDrivers(df,s, "points"). This function also shows visualization of top ten drivers who have scored most points over the years
 

The second part of task 1 was to find out in how many races do each driver participate. For this we call function RacesDriver(conn) which returns dataframe which contains count of races each driver has participated over the years.
 

Task 2

Task 2 required to visualize the trend of fastest lap speed over the years per circuit. To visualize it we call function fastestLap(conn) which gives the fastest lap speed in each circuit over the years. The visualization is shown below in figure 5. The trend of fastest lap speed is not regular. It first raises than falls down. The visualization only shows the top ten circuits and there trend of fastest lap speed over the years.
 
Task 3

Task 3 required to visualize the the trend of pit stop times over the years per constructor in a given circuit.  I have made visualization of four The visualization shows that there is irregular trend in time of pit stops of different constructors.
