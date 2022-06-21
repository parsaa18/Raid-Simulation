
#با سلام و عرض خسته نباشید 

#پروژه( Raid )مبانی کامپیوتر استاد کاوه رضایی 

#با همکاری گروهی ( نام اعضای گروه )
#پارسا اقایی 
#مهدی قاسمی 
#مریم برزگر 

#این پروژه در گیت هاب انجام شده است 

#لینک گیت هاب :
#https://github.com/parsaa18/Raid-Simulation.git

from prettytable import PrettyTable

type_of_Raid = PrettyTable(['Raid 0','Raid 1','Raid  10'])

type_of_Raid.add_row(['inter number 0','inter number 1','inter number 10'])

print ('\n\nchoose type of Raid from under table : ','\n\n',type_of_Raid,'\n')

type_Raid = [0,1,10]

while True :
    type_Raid_choosen = int (input ('which type of Raid ? : '))
    
    if type_Raid_choosen in type_Raid :
        break
    else :
        print('\n\n'+'please inter a correct number ','\n\n')  

type_of_data =PrettyTable(['data matchtable','saved data in pc'])

type_of_data.add_row(['inter M','inter S '])

print ('\n'+'which type of data do you have ? : ','\n\n',type_of_data,'\n')

type_data = ['m','s']

while True :
    type_data_choosen = input('which type of data ? ')
    type_data_choosen = type_data_choosen.lower()
    if type_data_choosen in type_data :
        break 
    else :
        print ('\n\n'+'please inter a correct noune ','\n\n')

type_data_choosen = type_data_choosen.lower()

if type_data_choosen == 'm' :
    
    inp=input('\nenter the thing you want to save:')

    inp2=inp

    s1=''

    s2=''

#Raid 0 for data matchtable
    if type_Raid_choosen == 0 :
        for i in range(len(inp)):
            if i%2==0:
                s1+=inp[i]
            if i%2==1:
                s2+=inp[i]
        
        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s1)

        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s2)

        if (len(s1)+len(s2))<=100:
            Raid_0 = PrettyTable(['DISK 1','DISK 2'])

            Raid_0.add_row([s1,s2])

            print ('\nresult for Raid 0 : ','\n\n',Raid_0,'\n\n\n')
            
        else :
            
            print ('\nresult for Raid 0 : ','\n\n','DISK 1 : ',s1,'\n\n','DISK 2 : ',s2)

    s3=''
#Raid 1 for data matchtable
    if type_Raid_choosen == 1 :
        
        for i in range(len(inp)):
            if i%2==0:
                s1+=inp[i]
            if i%2==1:
                s2+=inp[i]
        
        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s1)

        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s2)
            
        for j in range(len(inp2)):
            if j<=(len(s1)-1):
                s3+=s1[j]
            if j<=(len(s2)-1):
                s3+=s2[j]

        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s3)
    
        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s3)

        if len(s3)<=50:
            Raid_1 = PrettyTable(['DISK 1','DISK 2'])

            Raid_1.add_row([s3,s3])

            print ('\nresult for Raid 1 : ','\n\n',Raid_1)

        else :
            
            print ('\nresult for Raid 0 : ','\n\n','DISK 1 : ',s3,'\n\n','DISK 2 : ',s3)

# Raid 10 for data matchtable            
    if type_Raid_choosen == 10 :

        for i in range(len(inp)):
            if i%2==0:
                s1+=inp[i]
            if i%2==1:
                s2+=inp[i]
        
        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s1)

        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s2)
            
        with open('Disk3.txt','w') as dsk3:
            dsk3.write(s1)

        with open('Disk4.txt','w') as dsk4:
            dsk4.write(s2)
            
        if (len(s1)+len(s2))<=100:
            Raid_0 = PrettyTable(['DISK 1','DISK 2','DISK 3','DISK 4',])

            Raid_0.add_row([s1,s2,s1,s2])

            print ('\nresult for Raid 10 : ','\n\n',Raid_0,'\n\n\n')
            
        else :
            
            print ('\nresult for Raid 10 : ','\n\n','DISK 1 : ',s1,'\n\n','DISK 2 : ',s2,'\n\n','DISK 3 : ',s1,'DISK 4 : ',s2)

                      
if type_data_choosen == 's' :
    
    data_storage_path = input ('\ninter your data_storage_path : ')

    data_storage_path = open (data_storage_path,'r')

    data_storage_path = data_storage_path.read()
    
    data_storage_path_2 = data_storage_path
    
    s1=''

    s2=''
#Raid 0 for saved data in pc
    if type_Raid_choosen == 0 :
        
        for i in range(len(data_storage_path)):
            if i%2==0:
                s1+=data_storage_path[i]
            if i%2==1:
                s2+=data_storage_path[i]
                
            with open('Disk1.txt','w') as dsk1:
                dsk1.write(s1)

            with open('Disk2.txt','w') as dsk2:
                dsk2.write(s2)

        if (len(s1)+len(s2))<=100:
            Raid_0 = PrettyTable(['DISK 1','DISK 2'])

            Raid_0.add_row([s1,s2])

            print ('\nresult for Raid 0 : ','\n\n',Raid_0,'\n\n\n')

        else:
            print ('\nresult for Raid 0 : ','\n\n','DISK 1 : ',s1,'\n\n','DISK 2 : ',s2)

    s3=''
#Raid 1 for saved data in pc
    if type_Raid_choosen == 1 :
        
        for i in range(len(data_storage_path)):
            if i%2==0:
                s1+=data_storage_path[i]
            if i%2==1:
                s2+=data_storage_path[i]
                
        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s1)

        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s2)

        for j in range(len(data_storage_path)):
            if j<=(len(s1)-1):
                s3+=s1[j]
            if j<=(len(s2)-1):
                s3+=s2[j]
                
        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s3)
    
        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s3)

        
        if len(s3)<=50:
            Raid_1 = PrettyTable(['DISK 1','DISK 2'])

            Raid_1.add_row([s3,s3])

            print ('\nresult for Raid 1 : ','\n\n',Raid_1)

        else :
            print ('\nresult for Raid 0 : ','\n\n','DISK 1 : ',s3,'\n\n','DISK 2 : ',s3)
            
#Raid 10 for saved data in pc
            
    if type_Raid_choosen == 10 :

        for i in range(len(data_storage_path)):
            if i%2==0:
                s1+=data_storage_path[i]
            if i%2==1:
                s2+=data_storage_path[i]
        
        with open('Disk1.txt','w') as dsk1:
            dsk1.write(s1)

        with open('Disk2.txt','w') as dsk2:
            dsk2.write(s2)
            
        with open('Disk3.txt','w') as dsk3:
            dsk3.write(s1)

        with open('Disk4.txt','w') as dsk4:
            dsk4.write(s2)
            
        if (len(s1)+len(s2))<=100:
            Raid_0 = PrettyTable(['DISK 1','DISK 2','DISK 3','DISK 4',])

            Raid_0.add_row([s1,s2,s1,s2])

            print ('\nresult for Raid 10 : ','\n\n',Raid_0,'\n\n\n')
            
        else :
            
            print ('\nresult for Raid 10 : ','\n\n','DISK 1 : ',s1,'\n\n','DISK 2 : ',s2,'\n\n','DISK 3 : ',s1,'\n\n','DISK 4 : ',s2)

 
            





