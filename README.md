# City ranking based on daily AQI  <img src='https://user-images.githubusercontent.com/83420459/228736537-fbd32ab5-ac73-41c8-8e9c-f4669557061c.png' width='50'>


India, currently is operating over 300+ stations over 150+ cities across the country. The Central Pollution Control Board (CPCB) facilitates in daily assessment of Air Quality Index (AQI) based on the guildiness set by the Goverment of India. In this reagrds, as on today (03-01-2022) on a daily basis AQI of 100+ cities are reported. In the year 2015, The country has approxiametly 35 stations covering over 20 cities and ranking could be carried out manually on the basis of daily AQI bulletin released. Considering the upgradiation in CAAQMS network over the larger geographical extent of the country, performing the conventional techniques is challenging as it is laborous and time consuming with gretaer risk of human error. To resolve this issue, a python based code was developed.
...
## Basics behind the analysis
The Central Pollution COntrol Board (CPCB), Government of India releases daily AQI bulletin dispalying the AQI status for all the cities with operational Continnous Ambient Air Quality Monitoring Station (CAAQMS). The bulletin is revised on daily basis in the CPCB website after 4.00 PM. The archeives AQI bulletin may be [accessed here](https://cpcb.nic.in/AQI_Bulletin.php). The AQI information provided in the bulletin are analysed on daily basis to asecertain the performance of the cities in India. This may sound simple and actually is. The downloaded daily AQI bulletin is converted to dataframe and are sorted in descending order on the basis of AQI value and thereby allocating highest to lowest ranks. The actuall catch is, if two or more cities are identified with same AQI value, then these cities are assigned with the same rank. 

## Code
The code can be [accessed here](https://github.com/moorthynair/City-ranking-based-on-AQI/blob/main/Ranking_based_on_AQI_code.py). The entire process from downloading the bulletin to ranking the cities as per the AQI levels are automated. There exist 03 basic user input, a) Date (YYYYMMDD format); b) provide the path to download the bulleting pdf file; c)List of specific city of interest (The final analysis provides the rank of all the cities mentioned in the daily AQI bulletin. However in case of exracting the ranks of specific city of interest, the list of those may be provided).

To perform anaysis on the latest AQI bulltein, make sure the bulletin is released by the federal agency. [Access here](https://cpcb.nic.in/aqi_report.php) to check the status of latest AQI bulletin available. The latest bulletin is released in the CPCB website after 4.00PM daily. 5.00PM woluld be an ideal time to run the code for analysing the latest report. In case of unavaibality of AQI bulletin for the set date, a warning message shall pop up terminating the entire run

## What does the outputs/results contain?
The output parent dataframe with file name **'final_file'** is generated. The contains the City names, Air Quality status (ie., Good, Satisfactory, Moderate, Poor, Very Poor, Severe); Index value (ie., AQI), crticial pollutants identified, No of monitoring stations and the national level city rank based on AQI for the user defined date. For user defined city/cities information, the output dataframe named **'city_ranking'** is generated containing all the above mentioned information.

## LICENSE
The work is licensed under [MIT LICENSE](https://github.com/moorthynair/City-ranking-based-on-AQI/blob/main/LICENSE)
