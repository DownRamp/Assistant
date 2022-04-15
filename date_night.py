try:
    from googlesearch import search
except ImportError:
    print("No module named 'google' found")
 
def check_dislikes(no_list, url):
    print("dislike")
    for i in no_list:
        if i in url:
            return True
    return False

def fetch_dislikes():
    print()

def save_dislikes():
    print("save")

# to search
location = "Toronto"
want = "Date ideas"
query = location + " " + want
 
url_list = []
no_list = ["putting", "golf"]
list_complete = False
curr_stop = 10
curr_start = 0
while len(url_list) < 10:
    
    for j in search(query, tld="co.in", lang='en', num=10, start=curr_start, stop=curr_stop, pause=2):
        if check_dislikes(no_list, j):
            continue
        else:
            url_list.append(j)
    curr_stop+=10
    curr_start+=10

for i in url_list:
    print(i)
    # pick the ones you like
    # pick the ones you don't
    # add an additional filter with don't likes
    check = input("Was this helpful?(y/n)")
    if check == "n":
        specific_word = input("Was there a specific reason?(y/n) ")
        if(specific_word == "y"):
            value = input("Enter reason: ")
            save_dislikes(value)
        else:
            save_dislikes(i)

