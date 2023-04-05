import view
import Database

def start():
    connection = Database.createConnection()
    Database.createTable(connection)
    view.printMenu()
    ch = view.inputСhoose()
    match ch:
        case 1:
            title = view.inputTitle()
            note = view.inputnote()
            Database.insertNote(connection,title,note)
            printAllData(connection)
        case 2:
           printAllData(connection)
           id = view.inputnoteID()
           title = view.inputTitle()
           note = view.inputnote()
           Database.updateNote(connection,title,note,id)
           Database.selectSpecificNote(connection,id)
        case 3:
            printAllData(connection)
        case 4:
            printAllData(connection)
            id = view.inputnoteID()
            Database.deleteNote(connection,id)
            printAllData(connection)

def printAllData(connection):
    data = Database.selectAllNotes(connection)
    view.print_data(data)




