import time
from telnetlib import EC

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from Functions.BetStake.BetSatke import BetStake
from Functions.BetStake.Betamount import Betamount1
from Functions.CommonFunction.CommonFunction import getBalance, getExposure, editStake, getExposureAfterbet,getBalanceAfterBet
from Functions.BetPlacing.SP_BetPlacing import SPOne_bet, SPtwo_bet, SPthree_bet, SPfour_bet, SPfive_bet, SPsix_bet, \
    SPseven_bet, SPeight_bet, SPnine_bet, SPzero_bet, SPAll_bet
from Functions.Result.Result import SP_Result, getresult
from driver import Base


class TestCase_SP(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_OneBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPOne_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 1:
            print("SP 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 1 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPtwo_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 2:
            print("SP 2 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 2 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPthree_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 3:
            print("SP 3 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 3 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPfour_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 4:
            print("SP 4 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 4 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPfive_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 5:
            print("SP 5 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 5 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPsix_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 6:
            print("SP 6 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 6 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPseven_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 7:
            print("SP 7 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 7 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPeight_bet(self.driver)
        getresult(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 8:
            print("SP 8 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 8 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPnine_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 9:
            print("SP 9 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 9 loss ")
            Automated_Balance = Balance - AlterExposure
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
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPzero_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case1" and value == 0:
            print("SP 0 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 0 loss ")
            Automated_Balance = Balance - AlterExposure
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")

    def test_ALLBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        SPAll_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = SP_Result(self.driver)
        if Case == "Case2":
            print("SP All won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("SP 1 Loss ")
            Automated_Balance = Balance - AlterExposure
            print("Automated Balance = " + str(Automated_Balance))
        time.sleep(1)
        Balance_After_Result = getBalanceAfterBet(self.driver)
        assert Balance_After_Result == Automated_Balance
        if Balance_After_Result == Automated_Balance:
            print(
                f"Successfully Completed All Scenarios are passed, BalanceOn Screen--> {Balance_After_Result} = {Automated_Balance} <--Automation Balance")
        else:
            print("Something wrong in payoff check it manually (or) Check the server speed ")


