
PRICES=[12.5,9.9,15.0,22.3,5.0]
QUANTITIES=[2,5,1,3,4]

def item_totals(prices,quantities):
    return list(map(lambda p,q:p*q, prices, quantities))

def filter_above(totals,threshold=30):
    return list(filter(lambda x :x>threshold,totals))

def pair_up(prices,quantities):
    return list(zip(prices, quantities))

def item_totals_comp(prices ,quantities):
    return [p*q for p,q in zip(prices, quantities)]

def filter_above_comp(totals, threshold=30):
    return [x for x in totals if x > threshold]

if __name__=="__main__":
    totals=item_totals(PRICES,QUANTITIES)
    print("Totals:",totals)
    print("Totals > 30:", filter_above(totals))
    print("Price-quantity pairs:",pair_up(PRICES,QUANTITIES))
    print("Totals (comprehension):" ,item_totals_comp(PRICES,QUANTITIES))
    print("Totals > 30 (comprehension):",filter_above_comp(totals))
