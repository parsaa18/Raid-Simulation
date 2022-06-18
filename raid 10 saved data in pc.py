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

 
