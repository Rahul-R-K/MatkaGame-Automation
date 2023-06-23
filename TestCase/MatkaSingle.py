from Functions.CommonFunction.CommonFunction import getBalance, getExposure, editStake, getExposureAfterbet,getBalanceAfterBet
from Functions.BetPlacing.Single_BetPlacing import One_bet, two_bet, three_bet, four_bet, five_bet, six_bet, seven_bet, eight_bet, nine_bet, zero_bet, Low_bet, High_bet, Odd_bet, Even_bet
from Functions.Result.Result import getresult
from Functions.BetStake.BetSatke import BetStake, BetStake2, BetStake3
from Functions.BetStake.Betamount import Betamount1
from driver import Base
import time


class TestCase_Single(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_OneBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        One_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 1 :
            print("Single 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value !=1:
            print("Single1 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_twoBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        two_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 2:
            print("Single 2 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 2:
            print("Single 2 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_threeBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        three_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 3:
            print("Single 3 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 3:
            print("Single 3 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_fourBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        four_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 4:
            print("Single 4 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 4:
            print("Single 4 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_fiveBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        five_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 5:
            print("Single 5 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 5:
            print("Single 5 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_sixBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        six_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 6:
            print("Single 6 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 6:
            print("Single 6 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_sevenBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        seven_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 7:
            print("Single 7 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 7:
            print("Single 7 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_eightBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        eight_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 8:
            print("Single 8 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 8:
            print("Single 8 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_nineBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        nine_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 9:
            print("Single 9 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 9:
            print("Single 9 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_zeroBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        zero_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value == 0:
            print("Single 0 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value != 0:
            print("Single 0 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_LowBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Low_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value in [1, 2, 3, 4, 5]:
            print("Single 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value not in [1, 2, 3, 4, 5]:
            print("Single1 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_HighBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        High_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value in [6, 7, 8, 9, 0]:
            print("Single 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value not in [6, 7, 8, 9, 0]:
            print("Single1 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_OddBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        One_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value in [1, 3, 5, 7, 9]:
            print("Single 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value not in [1, 3, 5, 7, 9]:
            print("Single1 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_EvenBet(self):
        global Automated_Balance
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        Even_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        value = getresult(self.driver)
        print(f'Value = {value}')
        if value in [2, 4, 6, 8, 0]:
            print("Single 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - Betamount)
            print("Automated Balance = " + str(Automated_Balance))
        elif value not in [2, 4, 6, 8, 0]:
            print("Single1 loss")
            Automated_Balance = Balance - Betamount
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")
















    '''def test_Combo1Bet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        One_bet(self.driver)
        time.sleep(.5)
        two_bet(self.driver)
        time.sleep(.5)
        Low_bet(self.driver)
        time.sleep(.5)
       

    def test_Combo2Bet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        One_bet(self.driver)
        time.sleep(.5)
        two_bet(self.driver)
        time.sleep(.5)
        five_bet(self.driver)
        time.sleep(.5)
        three_bet(self.driver)
        time.sleep(.5)
        Odd_bet(self.driver)
        time.sleep(.5)
        Even_bet(self.driver)
        getresult(self.driver)'''

