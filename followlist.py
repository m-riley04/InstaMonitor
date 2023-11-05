import os
import datetime

class FollowList:
    def __init__(self):
        self.followers = []
    
    def load_copypaste(self, path):
        """
        Loads a list of followers from a copy-pasted text file of your following list.
        The file should contain followers in the following format:
            [username]'s profile picture
            [username]
            [name] (optional)
        """
        file = open(path, 'r', encoding='utf8')
        followerIndex = 0
        lines = file.readlines()
        for i, text in enumerate(lines):
            if ("'s profile picture" in text):
                followerIndex += 1
                follower = lines[i+1][:-1]
                self.followers.append(follower)
            else:
                continue
        file.close()
            
    def load(self, path):
        """Loads a list of followers from a 1:1 list of usernames in a text file"""
        file = open(path, 'r', encoding='utf8')
        lines = file.readlines()
        file.close()
        
    def compare(self, other, printResults=False):
        """Compares this FollowList with another FollowList, prints it's results, and returns a dictionary of it's results"""
        # Check if no changes have been made
        if (self == other):
            print("No follows or unfollows between these 2 following lists.")
            return None
        
        # Print disclaimer
        # TODO: save followers as their own datatype so past usernames/username changes can be stored
        print("DISCLAIMER: It is possible that those who changed their usernames between the 2 dates are labeled as 'unfollowed' or 'followed'. Please manually check this on your own.")
        
        # Init lists
        unfollowed = []
        followed = []
        
        # Check for follows 
        for follower in other.followers:
            if follower not in self.followers:
                followed.append(follower)
    
        # Check for unfollows
        for follower in self.followers:
            if follower not in other.followers:
                unfollowed.append(follower)
                
        # Print Results
        if (printResults):
            # Print New Follows
            print("--- FOLLOWS ---")
            for i, follower in enumerate(followed, 1):
                print(f"{i}) {follower}")
                
            # Print Unfollows
            print("--- UNFOLLOWS ---")
            for i, unfollower in enumerate(unfollowed, 1):
                print(f"{i}) {unfollower}")
                
        # Return dictionary
        return { "unfollowed": unfollowed, "followed": followed }
    
    def compare_newest():
        """Compares the followlist to the most recent previously saved list"""
        
    
    def save(self):
        """Saves the list of followers to a more readable file with a date"""
        # Check that we have a checks directory for storing saves
        if (not os.path.exists(f"{os.getcwd()}\\checks")):
            os.mkdir(f"{os.getcwd()}\\checks")
        date = datetime.datetime.now().strftime("%Y-%m-%d--%H-%M-%S")
        file = open(f"{os.getcwd()}\\checks\\{date}.txt", 'w', encoding='utf8')
        for follower in self.followers:
            file.write(f"{follower}\n")
        file.close()
        
    def print(self):
        """Prints the list of followers"""
        for i, follower in enumerate(self.followers, 1):
            print(f"{i}) {follower}")
    
    def __eq__(self, other):
        return self.followers == other.followers