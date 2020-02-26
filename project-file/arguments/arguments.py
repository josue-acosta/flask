user_list = [ "anastasia.net", "deco-with-christ.org"]

def print_websites(x, y):
	print(f"There websites are: {x}, {y}")

print_websites(user_list[0], user_list[1])
print_websites(*user_list)



user_dictionary = {
	"first": "anastasia.net",
	"second": "deco-with-christ.org",
	"third": {
		"wisokyburgh": "wisokyburgh.com"
	}
}

def print_user_website(first, second, third):
	print(f"{first}, {second}, {third}")

print_user_website(user_dictionary["first"], user_dictionary["second"], user_dictionary["third"]["wisokyburgh"])
print_user_website(**user_dictionary)