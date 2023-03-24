import numpy as np
from weapon_catalog import wp_attributes

'''
	input: 
	wp_list = list of weapons with dps values

	power_skalar = change to overall powerlevel in every weapon 
	disregarding individual weapon buffs/nerfs

	output:
		new dict with scaled damage values

'''
#print(list(wp_attributes.keys()))
def scale_base_power(dict, power_skalar):
  for wp in list(dict.keys()):
    dict[wp]['base_dmg'] *= power_skalar
  return dict
#new = scale_base_power(wp_attributes, 1.15)
#print(new)
