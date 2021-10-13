def remember_result(sum_func):
	last_result = None

	def sum_wrapper(*args):
		nonlocal last_result
		print(f"Last result = '{last_result}'")
		if isinstance(args[0], int):
			tmp = 0
			for i in args:
				tmp = tmp + i
			args = str(tmp)
		last_result = sum_func(*args)
		return last_result
	return sum_wrapper


@remember_result
def sum_list(*args):
	result = ""
	for item in args:
		result += item
	print(f"Current result = '{result}'")
	return result


sum_list("a", "b")
# "Last result = 'None'"
# "Current result = 'ab'"
sum_list("abc", "cde")
# "Last result = 'ab'"
# "Current result = 'abccde'"
sum_list(3, 4, 5)
# "Last result = 'abccde'"
# "Current result = '12'"
