from prettytable import PrettyTable

type_of_Raid = PrettyTable(['Raid 0','Raid 1','Raid  10'])

type_of_Raid.add_row(['inter number 0','inter number 1','inter number 10'])

print ('\n\nchoose type of Raid from under table : ','\n\n',type_of_Raid,'\n')

type_Raid_choosen = int (input ('which type of Raid ? : '))

type_of_data =PrettyTable(['data matchtable','saved data in pc'])

type_of_data.add_row(['inter M','inter S '])

print ('\n'+'which type of data do you have ? : ','\n\n',type_of_data,'\n')

type_data_choosen = input('which type of data ? ')

type_data_choosen = type_data_choosen.lower()

if type_data_choosen == 'm' :
    
    inp=input('\nenter the thing you want to save:')

    inp2=inp

    s1=''

    s2=''
