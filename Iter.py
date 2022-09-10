from iter_class import FlatIterator
from generator_class import flat_generator




nested_list = [
	[['a',1,3], 'b', 'c'],
	['d', 'e', 'f', 'h', False],
	[1, 2, None],
]

flat_list = [item for item in FlatIterator(nested_list)]

print(flat_list)

for item in  flat_generator(nested_list):
	print(item)