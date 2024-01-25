print ("hallo"); print ('i love php')
print(True) 


# variable: 
name = 'hosam'
print('welcome,' +name+' in the game') # Var
age = '25'
print ('du bist ' +age+ ' geworden') # Var 

#Connet 2 Word: 
name1= 'Husameldin '
name2= 'Osman'
print (name1+name2)
# or 
#names = 'Husameldin Osman'
#print (names)

#Number
print (5+5)
print (5*5)

# 2 line zusammen: \ 
print ('Husameldin \
Osman'  )

# print one word: 
x = 'Husameldin Osman'
print (x[0])
print (x[-1]) # mn ala5r 
print (x[0:10]) # mn al 0 l7di 10 

#print (names)

# string function
# upper , lower , title 
print (name.upper()) # -> 3shan ykon capital 
print (name.isupper()) # 3shan tgi al Antwort eza true wla false 
print (name.lower())
print(name. islower())

print ('ich bin '+name1.upper()+name2.upper()+ ' und ich bin ' +age)
print ('ich bin ' +name1.title()+ name2.title()+' und ich bin '+age) # title bt5li awl 7rf mn kol klma capital

#split: 
program_lan= 'html css Javascript php python'
print (program_lan.split())

# len Function: 
x = 'ahmed'
print (len(x)) # 3shan a7sb fe km 7rf fe x 
print (x.index('ah')) # 3shan a3rf ah r8m km fe alklma 
print (x.replace('e', 'a')) # lw 3awz a3'yer 7aga mkan 7aga 
print (x.replace(x, 'Husam'))  # momkn a3'yer al variable klo 

# l7di 14 

Attendees = 'Husam Macha Robert Mariya Nouman Amir'
print (Attendees.split())
print(len(Attendees))
print (Attendees.index('sam'))
print(Attendees.replace('Ma','ma'))
print ('Die liste von den Attendees ' +Attendees.upper()+ 'Der Attendee ' +x.upper()+' konnte aber nicht daran nicht teilnehmen')
print(Attendees[4])

#**************************************************test****************test 
Attendees= ('Husam osman awad ')
a = 'Amir'
m= 'maria'
r= 'robert'
n= 'nouman'
ma= 'macha'
print (Attendees.split())
print (len(Attendees))
print (Attendees[-1])
print ('alle '+Attendees.title()+' werden teilnehmen. Warscheinlich ' +a.upper()+ ' kommt nicht')
print (m+ ' '+ a)
print (Attendees.index('H'))
print (r.replace('r','R'))
#***************************************************************************************************

# Number:
print (type(5)) # 3shan a3rf no3 al7aga. 
print (type (5.2)) # da no3o float
print (str(5*5) + ' Years') # 3shan agm3 number m3a string 
print (float (19) ) #3shan a7wel integer ly float
print (int(10.5)) # 3shan a7wel mn float ly Integer
print (round(5.3)) # 3shan a7wel float ly a8rb integer
from math import * # 3shan a8dr a3ml kol almo3amlat al7sabia
print (floor(5.9)) # 3shan ageeb a8la r8m mn al float ly al integer
print (ceil(5.1)) # 3shan ageeb a3la r8m mn l float ly al integer 
print ( max (432, 3244)) # 3shan ageeb a3la 8ema 
print ( min (3324, 2344))