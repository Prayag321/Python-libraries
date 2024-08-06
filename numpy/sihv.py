name_dict ={
  'Shiv': 6,
  'Prayag': -1,
  'Deven': -3,
  'Ayush': 17,
  'Neelesh': 8
}
# dec

val = name_dict.values()
keys = name_dict.keys()
new_dict = {}
for key in keys:
  if name_dict[key] % 2 == 0:
    new_dict[key]=name_dict[key]
print(sorted(new_dict))
