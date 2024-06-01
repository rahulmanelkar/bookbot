from string import ascii_lowercase

def character_count(user_string):
    character_count_dict = {}
    #initialize dict keys as lowercase letters and set them to 0
    for i in ascii_lowercase:
        character_count_dict[i]=0
    
    #count characters
    for character in user_string:
        if character in character_count_dict:
            character_count_dict[character]+=1

    return character_count_dict


def sort_dict(dict_to_sort):
    """Take a dict , turn it into a dict of dicts, and sort it by num value. Return it as a list"""
    """ Eg: Take this dict
            vehicles = {"car":7,"plane":10,"boat":2}
            and return
            vehicles =  [
                            {"name": "car", "num": 7},
                            {"name": "plane", "num": 10},
                            {"name": "boat", "num": 2}
                        ]
            but sorted
    """
    dict_to_list = [{"character":key,"count":value} for key,value in dict_to_sort.items()]
    dict_to_list.sort(reverse=True, key=lambda d:d["count"])
    return dict_to_list

def report(chdict, file_name, total_words):
    print(f'--- Begin report of {file_name} ---')
    print(f'{total_words} words found in the document\n')
    for elem in chdict:
        print(f"The {elem['character']} was found {elem['count']} times")
    print("--- End report ---")


def main(file_name="books/frankenstein.txt"):
    try:
        with open(file_name) as f:
            file_contents = f.read()
            words = file_contents.split()            
    except FileNotFoundError:
        print("File Not Found")

    count_characters = character_count(file_contents.lower())
    #print(count_characters)
    sorted_counts = sort_dict(count_characters)
    
    report(sorted_counts, file_name, len(words))



if __name__=="__main__":
    main()
    

