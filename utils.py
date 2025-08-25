def adjust_price(base, demand_mult, supply_mult, d_thresh=0.8, s_thresh=0.9):
    return base * max(demand_mult, d_thresh) * max(supply_mult, s_thresh)
