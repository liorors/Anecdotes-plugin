import json
from plugin.dummyjson_plugin import DummyJSONPlugin

def main():
    #create an instance of the plugin with correct username and password
    plugin = DummyJSONPlugin("emilys", "emilyspass")
    
    ##changed to invalid creds to test failure
    ##plugin = DummyJSONPlugin("emilys", "emilysnotpass")  
 


    #connectivity test (login)
    if plugin.login():
        print("E1 - User Details:")
        #collect and print authenticated user details
        print(json.dumps(plugin.collect_user_details(), indent=2))

        print("\nE2 - Posts (First 3):")
        #collect 60 posts, but print only the first 3
        posts = plugin.collect_posts().get("posts", [])[:3]
        print(json.dumps(posts, indent=2))

        print("\nE3 - Posts with Comments (First 3):")
        #collect 60 posts with comments, print the first 3
        posts_with_comments = plugin.collect_posts_with_comments()[:3]
        print(json.dumps(posts_with_comments, indent=2))

if __name__ == "__main__":
    main()
