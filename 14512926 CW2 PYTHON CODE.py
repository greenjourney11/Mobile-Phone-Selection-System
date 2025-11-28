import re
class Mobile:
    def __init__(self, name):
        self.name = name

    def gaming(self):
        return {
            "OPTION 1": "ASUS ROG PHONE 8 PRO",
            "OPTION 2": "NUBIA REDMAGIC 9 PRO"}

    def photography(self):
        return {
            "OPTION 1": "SAMSUNG S24 ULTRA",
            "OPTION 2": "IPHONE 15 PRO MAX"
        }

    def dailyuse(self):
        return {
            "OPTION 1": "BLACKPHONE 2",
            "OPTION 2": "KATIM RO1"
        }
    def get_details(self,device_name):
        details = {
            "ASUS ROG PHONE 8 PRO" :
                {"SPECIFICATION": "PROCESSOR--SNAPDRAGON 8 GEN 3,RAM--24GB,CAMERA--32MP,DISPLAY--AMOLED6.7INCH" ,
                 "PRICE": "1099GBP"
                 },
            "NUBIA REDMAGIC 9 PRO":
                {"SPECIFICATION": "PROCESSOR--SNAPDRAGON 8 GEN 3,RAM--16GB,CAMERA--50MP,DISPLAY--AMOLED6.81NCH" ,
                 "PRICE": "900GBP"
                 },
            "SAMSUNG S24 ULTRA":
                {"SPECIFICATION": "PROCESSOR--QUALCOMM SM8650AB,RAM--12GB,CAMERA--200MP,DISPLAY--6.8 QUAD HD+" ,
                 "PRICE": "1249GBP"
                },
            "IPHONE 15 PRO MAX":
                {"SPECIFICATION": "PROCESSOR-- A17PRO CHIP,RAM--8GB,CAMERA--48MP,DISPLAY--6.7 OLED SCREEN" ,
                 "PRICE": "1199GBP"
                 },
            "BLACKPHONE 2":
                {"SPECIFICATION": "PROCESSOR--SNAPDRAGON 1.7GHZ,RAM--3GB,CAMERA--13MP,DISPLAY--5.5INCH" ,
                 "PRICE": "562GBP"
                 },
            "KATIM RO1":
                {"SPECIFICATION": "PROCESSOR--QUALCOMM 765G,RAM--8GB,CAMERA--64MP,DISPLAY--POLED 6.47INCH" ,
                 "PRICE": "899GBP"
                }
        }
        return details.get(device_name, {"SPECIFICATION": "N/A", "PRICE": "N/A"})
    def card_payment(self,price):
        print("\nCARD PAYMENT:")
        card_holder_name = input("ENTER CARD HOLDER NAME: ")

        while True:
            card_number = input("ENTER CARD NUMBER (in format 1234 5678 1234 5678): ")
            if re.fullmatch(r"(\d{4} ){3}\d{4}", card_number):
                print("VALID CARD NUMBER",card_number)
                break
            else:
                print("INVALID CARD NUMBER. PLESE ENTRE 16-DIGITS CARD NUMBER.")
        while True:
            cvv = input("ENTRE CVV (3 DIGITS): ")
            if re.fullmatch(r"\d{3}", cvv):
                break
            else:
                print("INVALID CVV. PLESE ENTRE 3 DIGITS CVV.")
        while True:
            expire_date = input("ENTRE CARD EXPIRE DATE (MM/YY):")
            if re.fullmatch(r"(0[1-9]|1[0-2])\/\d{2}",expire_date):
                break
            else:
                print("INVALID EXPIRE DATE. PLESE ENTER IN MM/YY FORMAT.")
        while True:
            pin = input("ENTRE 4-DIGIT PIN: ")
            if re.fullmatch(r"\d{4}", pin):
                break
            else:
                print("INVALID PIN. PLESE ENTRE A 4-DIGIT PIN.")
        print("PAYMENT SUCCESSFULL!")
        self.restart_option()

    def installment_payment(self, price):
        print("\nINSTALLMENT PAYMENT:")
        print("CHOOSE AN INSTALLMENTS OPTION:")
        print("1. 12 MONTHS (5% installment rate)")
        print("2. 24 MONTHS (4.2% installment rate)")
        print("3. 36 MONTHS (3.5% installment rate)")

        installment_option = input("ENTRE A NUMBER OF YOUR CHOICE: ")

        if installment_option in ['1', '2', '3']:
            installment_rate = {'1': 0.05, '2': 0.042, '3': 0.035}[installment_option]
            total_price = price * (1 + installment_rate)
            print(f"TOTAL PRICE INCLUDING INSTALLMENT CHARGES: {total_price} GBP")
            print("PAYMENT SUCCESSFULL!")
            self.restart_option()
        else:
            print("INVALID OPTION. PAYMENT FAILED")
            self.restart_option()

    def restart_option(self):
        restart_choice = input("DO YOU WANT TO START FROM DEVICE SELECTION? (Y/N): ").upper()
        if restart_choice == 'Y':
            self.user_interface()
        else:
            print("THANK YOU FOR USING THE SERVICE!")
    def user_interface(self):
        print("CHOOSE A CATEGORY :")
        print("1. GAMING")
        print("2. PHOTOGRAPHY")
        print("3. DAILYUSE")

        category = input('ENTRE A NUMBER OF YOUR CHOICE:')

        if category == '1':
            option = self.gaming()
            print("\n GAMING OPTIONS:")
        elif category == '2':
            option = self.photography()
            print("\n PHOTOGRAPHY OPTIONS:")
        elif category == '3':
            option = self.dailyuse()
            print("\n DAILYUSE OPTIONS:")
        else:
            print("INVALID CHOICE, PLEASE SELECT VALID CATEGORY.")
            return
        for key, value in option.items():
            print(f"{key}: {value}")
        choice = input("ENTRE A NUMBER OF (1 or 2) THAT YOU PREFER: ")

        if choice == '1':
            selected_option = list(option.values())[0]
        elif choice == '2':
            selected_option = list(option.values())[1]
        else:
            print("INVALID OPTION. PLEASE SELECT A VALID OPTION.")
            return choice

        print(f"\nYou selected: {selected_option}")
        print("WHAT DO YOU WANT TO SEE")
        print("1. DEVICE SPECIFICATION")
        print("2. PRICE")

        detail_choice = input("ENTER A NUMBER OF YOUR CHOICE: ")
        details = self.get_details(selected_option)

        if detail_choice == '1':
            print(f"SPECIFICATION: {details['SPECIFICATION']}")

        elif detail_choice == '2':
            print(f"PRICE: {details['PRICE']}")

        payment_choice = input("WOULD YOU LIKE TO MAKE A PAYMENT? (Y/N): ").upper()
        if payment_choice == 'N':
            print("THANK YOU FOR USING THE SERVICE!")
            x = input("WOULD YOU LIKE TO SEE PRICE? (Y/N): ").upper()
            if x == 'Y':
                print(f"PRICE: {details['PRICE']}")
                payment_choice = input("WOULD YOU LIKE TO MAKE A PAYMENT? (Y/N): ").upper()
                if payment_choice == 'N':
                    print("THANK YOU FOR USING THE SERVICE!")
                    self.restart_option()
                elif payment_choice == 'Y':
                    pass
                else:
                    print("INVALID OPTION")
            elif x == 'N':
                print("NO PROBLEM")
            else:
                print("INVALID OPTION")
        elif payment_choice == 'Y':
            pass
        else:
            print("INVALID OPTION")
        if payment_choice == 'Y':
            print(f"PRICE: {details['PRICE']}")
            print("CHOOSE A PAYMENT METHOD:")
            print("1. CARD PAYMENT")
            print("2. INSTALLMENT PAYMENT")
            payment_method = input("ENTRE THE NUMBER OF YOUR CHOISE: ")
            price = float(details['PRICE'].replace('GBP', ''))
            if payment_method == '1':
                self.card_payment(price)
            elif payment_method == '2':
                self.installment_payment(price)
            else:
                print("INVALID PAYMENT OPTION")
                self.restart_option()
mobile = Mobile("MyMobile")
mobile.user_interface()