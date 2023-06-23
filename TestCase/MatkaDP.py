import time

from Functions.BetStake.BetSatke import BetStake
from Functions.BetStake.Betamount import Betamount1
from Functions.CommonFunction.CommonFunction import getBalance, getExposure, editStake, getExposureAfterbet, \
    getBalanceAfterBet
from Functions.BetPlacing.DP_BetPlacing import DPOne_bet, DPtwo_bet, DPthree_bet, DPfour_bet, DPfive_bet, DPsix_bet, DPseven_bet, DPeight_bet,DPnine_bet,DPzero_bet,DPAll_bet
from Functions.Result.Result import getresult,DP_Result
from driver import Base


class TestCase_DP(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_OneBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        DPOne_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 1:
            print("DP 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 1 loss ")
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
        DPtwo_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 2:
            print("DP 2 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 2 loss ")
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
        DPthree_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 3:
            print("DP 3 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 3 loss ")
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

    def four_OneBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        DPfour_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 4:
            print("DP 4 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 4 loss ")
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
        DPfive_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 5:
            print("DP 5 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 5 loss ")
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
        DPsix_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 6:
            print("DP 6 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 6 loss ")
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
        DPseven_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 7:
            print("DP 7 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 7 loss ")
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
        DPeight_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 8:
            print("DP 8 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 8 loss ")
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
        DPnine_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 9:
            print("DP 9 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 9 loss ")
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
        DPzero_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case1" and value == 0:
            print("DP 0 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP 0 loss ")
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
        DPAll_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = DP_Result(self.driver)
        if Case == "Case2":
            print("DP All won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("DP All loss ")
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