

def remove_tags(name:str):
    curr_tags = name.split("__")[-1].split(".")[0].split("_")
    print(curr_tags)
    

def main(args):
    remove_tags(args.file)

if __name__ == "__main__":
    main(None)
