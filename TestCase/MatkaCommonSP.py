import time

from Functions.BetStake.BetSatke import BetStake
from Functions.BetStake.Betamount import Betamount1
from Functions.CommonFunction.CommonFunction import getBalance, getExposure, editStake, getBalanceAfterBet, \
    getExposureAfterbet
from Functions.BetPlacing.CommonSP_BetPlacing import CSPOne_bet, CSPtwo_bet, CSPthree_bet, CSPfour_bet, CSPfive_bet, CSPsix_bet, CSPseven_bet, CSPeight_bet, CSPnine_bet, CSPzero_bet
from Functions.Result.Result import getresult, CommonSP_Result, Cards_Result
from driver import Base


class TestCase_CommonSP(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_OneBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        CSPOne_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 1 in Cards_Value:
            print("CSP 1 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 1 loss ")
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
        CSPtwo_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 2 in Cards_Value:
            print("CSP 2 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 2 loss ")
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
        CSPthree_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 3 in Cards_Value:
            print("CSP 3 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 3 loss ")
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

    def test_FourBet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        CSPfour_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 4 in Cards_Value:
            print("CSP 4 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 4 loss ")
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
        CSPfive_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 5 in Cards_Value:
            print("CSP 5 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 5 loss ")
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
        CSPsix_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 6 in Cards_Value:
            print("CSP 6 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 6 loss ")
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
        CSPseven_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 7 in Cards_Value:
            print("CSP 7 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 7 loss ")
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
        CSPeight_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 8 in Cards_Value:
            print("CSP 8 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 8 loss ")
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
        CSPnine_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 9 in Cards_Value:
            print("CSP 9 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 9 loss ")
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
        CSPzero_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = CommonSP_Result(self.driver)
        Cards_Value = Cards_Result(self.driver)
        if Case == "Case1" and 0 in Cards_Value:
            print("CSP 0 won ")
            Automated_Balance = Balance + ((Betodds1 * Betamount) - AlterExposure)
            print("Automated Balance = " + str(Automated_Balance))
        else:
            print("CSP 0 loss ")
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

