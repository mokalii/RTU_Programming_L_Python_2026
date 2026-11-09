
def average(values):
    if not values:
        return 0.0
    return sum(values)/len(values)

def largest_city(populations):
    if not populations:
        return ("",0)
    city=max(populations,key=populations.get)
    return (city,populations[city])

def smallest_city(populations):
    if not populations:
        return ("",0)
    city=min(populations,key=populations.get)
    return (city, populations[city])

def total_population(populations):
    return sum(populations.values())

if __name__=="__main__":
    temperatures=[3,5,4,6,2,7,3]
    city_population={"Riga":605000,"Daugavpils":78000,"Liepaja":67000,"Jelgava":55000,"Valmiera":23000}

    print(f"Average temperature: {average(temperatures):.1f}")
    largest=largest_city(city_population)
    smallest=smallest_city(city_population)
    print(f"Largest city: {largest[0]} - {largest[1]}")
    print(f"Smallest city: {smallest[0]} - {smallest[1]}")
    print(f"Total population: {total_population(city_population)}")
