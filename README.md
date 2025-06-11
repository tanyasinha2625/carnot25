# carnot25
Tractor vs Rain


Tractor vs Rain

Overview
This project looks at how tractor activity changes with rainfall across Maharashtra between April and June 2024. We’ll use daily tractor data (like engine hours, acres covered, GPS movement) and match it with rainfall data to see patterns—like whether tractors move more after rain, how regions differ, or if untimely rains disrupt work. The idea is to find interesting insights about how farming reacts to the weather.

What do we want to know?
Understand how rainfall impacts tractor usage (e.g., engine hours, acres).


Detect untimely rain events and their effect on farming behavior.


Compare patterns across regions (e.g., Marathwada vs Vidarbha).


Explore tractor mobility — do they migrate to where the rain goes?


Identify high-efficiency zones or interesting outliers.

Questions that we can answer
How does rainfall affect daily tractor activity?


Which regions are more rain-sensitive?


Are there untimely rainfall events disrupting operations?


Do tractors move across subdistricts in response to rain?


Which subdistricts show the most efficient usage?

Some directions for analysis 

We can choose to pursue these directions to understand the behaviour of tractors better, and try and correlate it with rainfall. Any other interesting things are also welcome :)
	
✅ 1. Daily Tractor Usage Trends
Goal: Track how farming activity evolves day-to-day across MH.
🔹 Do:
Aggregate by day: total/average acres, engine hours, farming hours.


📈 Plot: Line plots – acres vs day, engine hrs vs day.

✅ 2. Regional Usage Patterns
Goal: Compare activity levels across subdistricts and districts.
🔹 Do:
Aggregate totals by subdistrict, district.


🗺️ Plot: Choropleth – total acres per subdistrict.
 📊 Plot: Bar chart – top 10 districts by total activity.

✅ 3. Rainfall vs Tractor Activity
Goal: Understand how rain influences farming activity.
🔹 Do:
Merge rainfall data (district + day), compute correlation with acres, engine hrs.


📉 Plot: Scatter – rain_mm vs acres tilled.
 📈 Plot: Lag plot – rain[t-1] vs acres[t].

✅ 4. Regional Rainfall Sensitivity
Goal: Identify which regions respond more (or less) to rain.
🔹 Do:
Group by district: compute rain–activity correlation.


📊 Plot: Bar chart – correlation per district.
 🗺️ Plot: Choropleth – rain sensitivity across MH.

✅ 5. Untimely Rain Event Impact
Goal: Spot disruptions caused by off-season or excessive rainfall.
🔹 Do:
Define “untimely rain” (e.g., >20mm before sowing season), compare activity on those days.


📈 Plot: Timeline with rainfall spikes + drops in usage.
 📊 Plot: Boxplot – acres on untimely vs normal days.



