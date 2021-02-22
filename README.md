# Communicate Data Findings

## GoBike System analysis

### Project Overview

This repo contains an explaratory data analysis for the GoBike system for bike sharing in SF. It contains data files form June 2018 to May 2019 with a record of more than 2 millions. The analysis amid at exploring trends in data regarding trip durations, seasons and months. This analysis is done through three level: univariate analysis, bivariate analysis and multivariate analysis. The data contains various and interesting infromation from age and gender to trip duration and start and end time of trip. I only extract 10% of the datasets not all of them due to memory usage performance. Ages in the dataset are ranging from 18 to 56 takes around 95% of the users in dataset.

### Exploratory Data Analysis Conlclusion

The dataset includes:

- The dataset has a length of 113327 rows and 12 columns.
- ID number for each bicycle.
- Trip duration in seconds.
- Start and end time
- The beginning and end station, latitude, longitude and station name.
- The year the user was born.
- The gender of the user.

There was some cleaning needed to the dataset. This included:

- Dropping NaNs in birth year and gender, outliers in age column and `other` category in `member_gender` column.
- Change data types, including times to datetimes, done in `pd.read_csv()`.
- Extract months, days of the week and hour from start_time.
- Create new columns analysis purposes; `age` and `age_groups`.

### Explanatory Data Analysis Conlclusion

To sum up, the analysis ends up that the longest trip durations are in the summer specifically in August. Winter, in Sep and Jan, comes in the second place, while spring months come with shortest trip durations across the year. Unlike the bar chart, `Average of duration trip per season in minutes`, it shows the longest median duratoin trip is in spring, the heatmap suggests the summer as longest duration trips take palce in this season. The second heatmap also prove the same fact that the summer has the peak duration of trips with high frequency in Wednesdays. The trip durations take more or less that 10 minutes.

### Explanatory Data Analysis Insights

After doing this analysis, I highly recommend paying more attention to advertising. The data is rich with a lot of infromation that can help in more spread and contribution for this kind of safe, clean and cheap kind of transporation. Also, the gender factor can be a very chanllenging factor to develop since males are much more suprior to using GoBike which is not something to worry about, but I think inviting females for bikesharing would be benefecial for woman health, releasing depression and stress which in return contributes to their relationship with their families and spouses.
