from followlist import FollowList    
import os

def main():
    
        
    # Initialize FollowList object
    listPath = "list.txt"
    following_list = FollowList()
    following_list.load_copypaste(listPath)
    following_list.save()
    
    # Initialize comparing object
    comparePath = "testlist.txt"
    compare_list = FollowList()
    compare_list.load_copypaste(comparePath)
    
    # Initialize
    following_list.compare(compare_list, printResults=True)

if __name__ == '__main__':
    main()