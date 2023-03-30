# City ranking based on daily AQI  <img src='https://user-images.githubusercontent.com/83420459/228736537-fbd32ab5-ac73-41c8-8e9c-f4669557061c.png' width='50'>


India, currently is operating over 300+ stations over 150+ cities across the country. The Central Pollution Control Board (CPCB) facilitates in daily assessment of Air Quality Index based on the guildiness set by the Goverment of India. In this reagrds, as on today (03-01-2022) on a daily basis AQI of 100+ cities are reported. In the year 2015, The country has approxiametly 35 stations covering over 20 cities and ranking could be carried out manually on the basis of daily AQI bulletin released. Considering the upgradiation in CAAQMS network over the larger geographical extent of the country, performing the conventional techniques is challenging as it is laborous and time consuming with gretaer risk of human error. To resolve this issue, a python based code was developed.
...
## Basics behind the analysis
The Central Pollution COntrol Board (CPCB), Government of India releases daily AQI bulletin dispalying the AQI status for all the cities with operational Continnous Ambient Air Quality Monitoring Station (CAAQMS). The bulletin is revised on daily basis in the CPCB website after 4.00 PM. The archeives AQI bulletin may be [accessed here](https://cpcb.nic.in/AQI_Bulletin.php). The AQI information provided in the bulletin are analysed on daily basis to asecertain the performance of the cities in India. This may sound simple and actually is. The downloaded daily AQI bulletin is converted to dataframe and are sorted in descending order on the basis of AQI value and thereby allocating highest to lowest ranks. The actuall catch is, if two or more cities are identified with same AQI value, then these cities are assigned with the same rank. 

## Code
The code can be [accessed here](https://github.com/moorthynair/City-ranking-based-on-AQI/blob/main/Ranking_based_on_AQI_code.py). The entire process from downloading the bulletin to ranking the cities as per the AQI levels are automated. There exist 2 basic user input, a)provide the path to download the bulleting pdf file; b)List of specific city of interset (The final analysis provides the rank of all the cities mentioned in the daily AQI bulletin. However in case of exracting the ranks of specific city the list of those may be provided). 

## Discalimer
The code is only suitable of performing analysis on the latest [daily AQI bulletin](https://cpcb.nic.in/aqi_report.php) available and not the archieves. You may download the archeive bulletin file seperately and run the same analysis. 

##LICENSE
The work is licensed under [MIT LICENSE](https://github.com/moorthynair/City-ranking-based-on-AQI/blob/main/LICENSE)
