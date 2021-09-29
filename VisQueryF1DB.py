import seaborn as sns
import matplotlib.pyplot as plt 
def showTopDrivers(df, s, a):
    print(a)
    topTen = (df.sort_values([a], ascending=False)).head(10)
    print(s,topTen)
    fig_dims = (20, 6)
    fig, ax = plt.subplots(figsize=fig_dims)
    plt.title(s)
    sns.set_theme(style="whitegrid")
    ax = sns.barplot(x="fullName", y=a, data=topTen)
    return ax

def FastestTrend(df):
    df.fastestLapSpeed[df.fastestLapSpeed=='\\N'] = 0
    df1 = df.loc[df['circuitId'] == 1]
    df2 = df.loc[df['circuitId'] == 6]
    df3 = df.loc[df['circuitId'] == 4]
    df4 = df.loc[df['circuitId'] == 10]
    fig_dims = (20, 6)
    fig, axs = plt.subplots(2,2,figsize=fig_dims)
    fig.suptitle('Pit Stops trend in circuit 1,6,4,8')
    axs[0][0].plot(df1['fastestLapSpeed'],  "-r", label = "circuitId 1 ",)
    axs[0][1].plot(df2['fastestLapSpeed'], '-g', label = "circuitId 6")
    axs[1][0].plot(df3['fastestLapSpeed'], '-y',label = "circuitId 4")
    axs[1][1].plot(df4['fastestLapSpeed'], '-b',label = "circuitId 8")
    fig.legend()
def PitstopTrend(df):
    df.milliseconds_pitstops[df.milliseconds_pitstops=='\\N'] = 0
    df1 = df.loc[df['constructorId'] == 1]
    df2 = df.loc[df['constructorId'] == 6]
    df3 = df.loc[df['constructorId'] == 4]
    df4 = df.loc[df['constructorId'] == 10]
    #print(df1)
    #print(df2)
    fig_dims = (20, 6)
    fig, axs = plt.subplots(2,2,figsize=fig_dims)
    fig.suptitle('Pit Stops trend in circuit 1,6,4,8')
    axs[0][0].plot(df1['milliseconds_pitstops'],'-r', label = "constructorId 1")
    axs[0][1].plot(df2['milliseconds_pitstops'], '-g',label = "constructorId 6")
    axs[1][0].plot(df3['milliseconds_pitstops'], '-y',label = "constructorId 4")
    axs[1][1].plot(df4['milliseconds_pitstops'], '-b',label = "constructorId 8")
    fig.legend()