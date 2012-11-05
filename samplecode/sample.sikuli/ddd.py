import javax.swing.JOptionPane as JOptionPane
import javax.swing.JPasswordField as JPasswordField

# ask user input his vpn password
jPasswordField = JPasswordField()
switchApp("Sikuli IDE")
result = JOptionPane.showConfirmDialog(None, jPasswordField, "Please input vpn password", JOptionPane.OK_CANCEL_OPTION);

if result == 0:
    # open app
    vpnapp = App("NetExtender")
    vpnapp.open()
    wait("SONICWALL.png", 60)
    type("Password.png", jPasswordField.text)
    click("Connect.png")

    sparrowApp = App("Sparrow")
    sparrowApp.open()

    wait("swnotlcSonic.png", 90)
    doubleClick("swnotlcSonic.png")
    wait("Sonlcwall.png", 90)
    re = find("OneTimePassw.png").offset(Location(100, 0)).nearby(5)
    doubleClick(re)
    type("c", KeyModifier.CMD)

    vpnapp.focus()
      
   

    click("AEmpOfHlYPHS.png")
    type("v", KeyModifier.CMD)

    click("1331268901918.png")