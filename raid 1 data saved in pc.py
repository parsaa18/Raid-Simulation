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
            
