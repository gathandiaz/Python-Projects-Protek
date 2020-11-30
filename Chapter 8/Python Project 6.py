x = ['apel','rambutan','jeruk','mangga']
print('file sebelum diurutkan                                = ',x)

def sortStringByChar(file):
    file.sort(key = len, reverse = True)
    print('file setelah diurutkan berdasarkan dari yang terbesar = ',file)
    
sortStringByChar(x)
