# Task 2

computer_beep = input("Does the computer beep when powered on? [Y/N]: ")

drive_spin = input("Does the drive spin when powered on? [Y/N]: ")

if (computer_beep == 'Y' and drive_spin == 'Y') :
    print("Contact Tech Support.")
else:
    if (computer_beep == 'Y' and drive_spin == 'N') :
        print("Check drive cables.")
    else:
          if (computer_beep == 'N' and drive_spin == 'N') :
              print("Bring computer to repair centre.")
          else:
              if (computer_beep == 'N' and drive_spin =='Y') :
                  print("Check the speaker contacts.")
                  
