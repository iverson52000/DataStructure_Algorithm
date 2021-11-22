from hashlib import md5

arr = [1, 2, 3, 'a', 7]

for item in arr:
    try:
        if isinstance(item, str):
            raise Exception("string!")
        else:
            print(item)
    except Exception as err:
        print(err)

print(md5(b"testing!!!"))

root = "/home/airtable"
path1 = "/home/airtable/Backups/2017_bashrc"
print(path1.split(root+"/")[-1])
