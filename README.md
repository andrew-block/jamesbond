# jamesbond

<img src="https://cdn.worldvectorlogo.com/logos/james-bond-007-1.svg" alt="alt text" width="250" height="300">

# About
**jamesbond** 🔫🍸👙🇬🇧 is a Python tabular data package that displays information/metrics about the James Bond films in a pandas dataframe. This package can be used for visualization and machine learning. 


# Getting started
You can install easily from PyPi


## Installation
```
pip install jamesbond
```
## Usage
Pull James Bond movie metrics into a pandas data frame using the ```load_jamesbond``` method:

```
from jamesbond import jamesbond

df = jamesbond.load_jamesbond()

df.head(10)
```

# Content

| ```Column```            | ```Dtype```   | ```Description```                                                                                |
| :---              | :---    | :---                                                                                       |
| **```Year```**    | ```int64```   | ```Release year of the movie.```                                                                |
| **```Movie```**   | ```object```  | ```The movie title.```                                                                     |
| **```Bond```**              | ```object```  | ```Actor who played James Bond.```                                                             |
| **```Director```**          | ```object```  | ```Director of the movie.```                                                                    |
| **```Composer```**          | ```object```  | ```Composer of the movie.```                                                                   |
| **```Writer```**           | ```object```  | ```Writer of the movie.```                                                                     |
| **```Cinematographer```**   | ```object```  | ```Cinematographer of the movie.```                                                          |
| **```Depicted_Film_Loc```** | ```object```  | ```Depicted location(s) of the movie.```                                                      |
| **```Shooting_Loc```**      | ```object```  | ```Shooting location(s) of the move.```                                                          |
| **```Bond_Car_MFG```**      | ```object```  | ```The manufacturer of the bond car.```                                                          |
| **```Bond_Girl_Nat```**     | ```object```  | ```The nationality of the bond girl(s).```                                                       |
| **```US_Gross```**          | ```int64```   | ```The films U.S gross earnings.```                                                              |
| **```US_Adj```**            | ```int64```   | ```The films U.S gross earnings adjusted based on 2013.```                                       |
| **```World_Gross```**       | ```int64```   | ```The films worldwide gross earnings.```                                                        |
| **```World_Adj```**         | ```int64```   | ```The films worldwide gross earnings adjusted based on 2013.```                                 |
| **```Budget```**            | ```int64```   | ```The films budget.```                                                                          |
| **```Budget_Adj```**        | ```int64```   | ```The films budget adjust based on 2013.```                                                     |
| **```Film_Length```**       | ```int64```   | ```The length of the movie.```                                                                   |
| **```Avg_User_IMDB```**     | ```float64``` | ```The average user rating from IMDB.```                                                         |
| **```Avg_User_Rtn_Tom```**  | ```float64``` | ```The average user rating from Rotten Tomatoes.```                                              |
| **```Conquests```**         | ```int64```   | ```The number of bond girls in the movie.```                                                     |
| **```Martinis```**          | ```int64```   | ```The number of martinis Bond consumed in the movie.```                                         |
| **```BJB```**               | ```int64```   | ```The number of times bond stated "Bond, James Bond."```                                         |
| **```Kills_Bond```**        | ```int64```   | ```The number of people Bond killed.```                                                          |
| **```Kills_Others```**      | ```int64```   | ```The number of people killed by someone other than bond.```                                    |
| **```Top_100```**           | ```int64```   | ```A flag where 1 represents the title song made Billboard/UK top 100 song, 0 mean it didn't.``` |
| **```Video_Game```**        | ```int64```   | ```A flag where 1 represents the title was made into a video game, 0 means it didn't.```         |

# References
This package leverages and adds to Derek S. Young and his [HoRM](https://rdrr.io/cran/HoRM/man/JamesBond.html) package

Derek S. Young (2017). Handbook of Regression Methods. CRC Press/Taylor & Francis Group. Boca Raton, FL.
