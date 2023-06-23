import time

from Functions.BetStake.BetSatke import BetStake
from Functions.BetStake.Betamount import Betamount1
from Functions.CommonFunction.CommonFunction import getBalance, getExposure, editStake,getExposureAfterbet,getBalanceAfterBet
from Functions.BetPlacing.Trio_BetPlacing import TRIO_bet
from Functions.Result.Result import getresult,TRIO_REsult
from driver import Base


class TestCase_TRIO(Base):

    def test_getBalance_and_Exposure(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)

    def test_EditStake(self):
        EditStake = editStake(self.driver)

    def test_TRIO_Bet(self):
        Balance = getBalance(self.driver)
        Exposure = getExposure(self.driver)
        TRIO_bet(self.driver)
        time.sleep(1)
        Betodds1 = BetStake(self.driver)
        Betamount = Betamount1(self.driver)
        AlterExposure = getExposureAfterbet(self.driver)
        value = getresult(self.driver)
        Case = TRIO_REsult(self.driver)
        if Case == "Case1":
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





