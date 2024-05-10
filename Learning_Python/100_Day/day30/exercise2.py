#  The code will crash and give you a KeyError

# Use what you've learnt about exception handling to prevent the program from crashing.


# eval() function will create a list of dictionaries using the input
facebook_posts = eval(input())

total_likes = 0
# TODO: Catch the KeyError exception
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
    except KeyError:
        pass
    
    

print(total_likes)