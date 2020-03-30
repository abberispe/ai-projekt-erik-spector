import gpt_2_simple as gpt2
import os
import requests

sess = gpt2.start_tf_sess()

gpt2.load_gpt2(sess)

def check_if_post_exist(string): # Används så att boten inte lägger ut något som redan finns på subredditen LifeProTips
    with open('data.txt') as f:
        datafile = f.readlines()
    for line in datafile:
        if string in line:
            return True
    return False

def generate_text():
    print("Generating text...")
    raw_text = gpt2.generate(sess, return_as_list=True)[0] # Skapar många olika posts
    posts = raw_text.split("\n")
    print("POSTS:", posts)
    eligible_posts = []
    for post in posts:
        if post[0:4] == "LPT:" and "*****" in post and not check_if_post_exist(post): # Tittar om titeln innehåller "LPT:", att det finns en seperator mellan titel och body (*****) och att posten inte existerar i datan
            eligible_posts.append(post.split("*****")) # Lägger in alla godkända posts i en lista
    if len(eligible_posts) == 0: # Om inga godkända posts finns, så kör vi om generate_text()
        print("No eligible posts found. Trying again...")
        return generate_text()
    else:
        post = min(eligible_posts, key=len) # Tar den kortaste posten eftersom de tenderar att vara mest sammanhängande
        return_title = post[0].replace("\\", "") # Filtrerar bort \\ eftersom de finns där en ' har använts
        return_body = post[1].replace("\\", "")
        return_dict = {"title": return_title, "body": return_body} # Lämnar tillbaka en godkänd post
        print("Generation done")
        return return_dict
