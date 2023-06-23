import time

from Functions.BetStake.BetSatke import BetStake
from Functions.BetStake.Betamount import Betamount1
from Functions.CommonFunction.CommonFunction import getBalance, getExposure, editStake, getExposureAfterbet, \
    getBalanceAfterBet
from Functions.BetPlacing.CommonDP_BetPlacing import CDPOne_bet, CDPtwo_bet, CDPthree_bet, CDPfour_bet, CDPfive_bet, CDPsix_bet, CDPseven_bet, CDPeight_bet, CDPnine_bet, CDPzero_bet
from Functions.Result.Result import getresult, CommonSP_Result, Cards_Result, CommonDP_Result
from driver import Base


class TestCase_CommonDP(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_OneBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        CDPOne_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 1 in Cards_Value:
            print("CDP 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 1 loss ")
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
        CDPtwo_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 2 in Cards_Value:
            print("CDP 2 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 2 loss ")
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
        CDPthree_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 3 in Cards_Value:
            print("CDP 3 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 3 loss ")
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
        CDPfour_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 4 in Cards_Value:
            print("CDP 4 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 4 loss ")
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
        CDPfive_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 5 in Cards_Value:
            print("CDP 5 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 5 loss ")
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
        CDPsix_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 6 in Cards_Value:
            print("CDP 6 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 6 loss ")
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
        CDPseven_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 7 in Cards_Value:
            print("CDP 7 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 7 loss ")
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
        CDPeight_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 8 in Cards_Value:
            print("CDP 8 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 8 loss ")
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
        CDPnine_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 9 in Cards_Value:
            print("CDP 9 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 9 loss ")
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
        CDPzero_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonDP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 0 in Cards_Value:
            print("CDP 0 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CDP 0 loss ")
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

