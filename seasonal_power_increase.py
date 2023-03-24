import numpy as np

wp_list = {"a": 1, "b": 2}

'''
	input: 
	wp_list = list of weapons with dps values
	---> need to rewrite the function a bit to account for other 
	     metrics which remain unchanged

	power_skalar = change to overall powerlevel in every weapon 
	disregarding individual weapon buffs/nerfs

	output:
		new dict with scaled damage values

'''

def scale_base_power(dict, power_skalar):
  for wp in dict.keys():
    dict[f"{wp}"] *= power_skalar
  return dict

new = scale_base_power(wp_list, 1.15)
print(new)
