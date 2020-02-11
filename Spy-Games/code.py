# --------------
##File path for the file 
file_path
#Code starts here
def read_file(path):
    file = open(file_path,mode = 'r')
    print(file)
    sentence = file.readline()
    file.close()
    return sentence
sample_message = read_file(file_path)
print(sample_message)



# --------------
#Code starts here
fd1 = open(file_path_1)
message_1 = fd1.read()
print(str(message_1))
fd2 = open(file_path_2)
message_2 = fd2.read()
print(str(message_2))

def fuse_msg(message_a,message_b):

    
   
    quotient = int(message_b)//int(message_a)
    return str(quotient)

secret_msg_1 = fuse_msg(message_1,message_2)
print(secret_msg_1)


    




# --------------
#Code starts here
fd = open(file_path_3)
message_3 = fd.read()
print('message sentences in variables = ',message_3)

#creating the function for substitute

def substitute_msg(message_c):
    global sub
    if message_c == 'Red':
        sub = 'Army General'
    elif message_c == 'Green':
        sub = 'Data Scientist'
    elif message_c == 'Blue':
        sub = 'Marine Biologist'
    return sub
        
secret_msg_2 = substitute_msg(message_3)
print('result = ',secret_msg_2)


# --------------
# File path for message 4  and message 5
file_path_4
file_path_5

fp4 = open(file_path_4)
message_4 =fp4.read()
print('4th text message = ',message_4)
fp5 = open(file_path_5)
message_5 = fp5.read()
print('5th text message = ',message_5)

#creating the fuction for compair the messages compare_msg()

def compare_msg(message_d,message_e):
    
    a_list = message_d.split()
    b_list = message_e.split()
    c_list = [x for x in a_list if x not in b_list]
    
        
    final_msg = " ".join(c_list)
    print(final_msg)
    return final_msg

secret_msg_3 =compare_msg(message_4,message_5) 
print('Secret text message = ', secret_msg_3)

    

#Code starts here







# --------------
#Code starts here
Fp6 = open(file_path_6)
message_6 = Fp6.read()
print('6th text message = ',message_6 )

def extract_msg(message_f):
    a_list = message_f.split()
    even_word = lambda x: (len(x)%2 == 0)
    b_list = list(filter(even_word , a_list))
    final_msg = " ".join(b_list)
    return final_msg

secret_msg_4 = extract_msg(message_6)
print('Secret text message = ', secret_msg_4)


# --------------
#Secret message parts in the correct order
message_parts=[secret_msg_3, secret_msg_1, secret_msg_4, secret_msg_2]


final_path= user_data_dir + '/secret_message.txt'
secret_msg =" ".join(message_parts)
print('Secret message before calling fuction = ', secret_msg)
#Code starts here

def write_file(secret_msg,path):
    f = open(path,mode = 'a+')
    f.write(secret_msg)
    f.close()

write_file(secret_msg,final_path)
print(secret_msg)


