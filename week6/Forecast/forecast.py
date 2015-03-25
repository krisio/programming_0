def forecast(days):

    rain_count = 0
    snow_count = 0
    sun_count = 0

    for day in days:
        
            if day == "snow":
            
                snow_count += 1

            elif day == "rain":
            
                rain_count += 1

            elif day == "sunshine":
            
                sun_count += 1

    if snow_count > rain_count and snow_count > sun_count:
	    return "snow"

    elif rain_count > snow_count and rain_count > sun_count:
	    return "rain"

    elif sun_count > snow_count and sun_count > rain_count:
	    return "sunshine"

    elif sun_count == snow_count and sun_count == rain_count:
	    return days[-1]

    elif sun_count == snow_count and sun_count > rain_count:
	    return "rain"

    elif snow_count == rain_count and rain_count > sun_count:
	    return "sunshine"

    elif sun_count == rain_count and rain_count > snow_count:
	    return "snow"

days = ["rain", "rain", "sunshine", "sunshine","snow"]

print(forecast(days))




    
