from Parameter_Xref.update import update_main

def settings_menu():
    print("""Select an Option:
(1) Update Param Xref Database Notes
(2) More Settings To come
(3) Go back
          """)
    selection = input('>>> ')

    if selection == '1':
        update_main()
    elif selection == '2':
        print("Why did you go here?")
    elif selection == '3':
        return
