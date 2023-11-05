class FollowList:
    def __init__(self):
        self.followers = []
    
    def load(self, path):
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
    
    def save(self):
        """Saves the list of followers to a more readable file with a date"""
        pass
        
    def print(self):
        """Prints the list of followers"""
        for i, follower in enumerate(self.followers, 1):
            print(f"{i}) {follower}")
        