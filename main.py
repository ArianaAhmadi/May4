#for i in range(4): #i=0,1,3
  #for j in range(4): #0,1,2,3
    #print(j)
  #print()         #skip a line
####################################
#s='Force'
#for i in range(5):
  #if s[i]=='r':
    #print('RRRRRR')
  #else:
    #print(s[i])
####################################
#s='May the Force be with you.'
#print(len(s)) #26 characters
#print(s[:])  #prints the string
#print(s[1:]) #commenting the frist letter out
#print(s[4:6+1])#print letter 4 to 6+1 because youhave to have an extra value at the end
#print(s[::1])  #1 is an argument, skip characters or change the direction of the strings
#print(s[::2]) #seeeee
#print(s[4:6+1:2])
#print(s[::-1])#string is printed backwards
####################################
s='abcdefghijklm'
print(s[0:10:2])
for i in range(0,10,2):
    print(i,s[i])