from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue


class Scoreboard() :
   
    def __init__(self ,name = "SCOREBOARD"): 
       self.name               = name
       self.t_score            = transactions()
       self.score_mail         = cocotb.queue.Queue()
       self.passed_test_cases  = 0
       self.failed_test_cases  = 0
       self.reset_test_cases   = 0
       self.load_test_cases    = 0
       self.down_test_cases    = 0 
       self.up_test_cases      = 0 
       self.idle_test_cases    = 0 
       self.golden_counter     = 0 
       self.golden_high        = 0
       self.golden_low         = 0 






    async def run_scoreboard (self) : 
        while(True):
            self.t_score = transactions()
            cocotb.log.info("[Scoreboard] receiving from monitor..... ") 
            self.t_score = await self.score_mail.get() 
            self.t_score.display("SCOREBOARD")
            """ ******************** *********** Test Cases *************** ************** """
            if self.t_score.rst == 0:
                self.reset_test_case() 
            elif self.t_score.load ==1:
                self.load_test_case()
            elif self.t_score.down == 1 :
                self.down_test_case()
            elif self.t_score.up == 1 :
                self.up_test_case()
            else :
                self.idle_test_case()


    def reset_test_case (self) :
        self.reset_test_cases += 1
        self.golden_high = 1 if self.golden_counter == 15 else 0
        self.golden_low  = 1 if self.golden_counter == 0  else 0

        if self.t_score.count == self.golden_counter and self.t_score.low == self.golden_low and self.t_score.high == self.golden_high:
            cocotb.log.info("Reset Test Case Passed ")
            self.passed_test_cases += 1
        else:
            cocotb.log.info("Reset Test Case Failed ")
            self.failed_test_cases += 1

    def load_test_case(self) :
        self.load_test_cases += 1 
        self.golden_counter = self.t_score.In
        self.golden_high = 1 if self.golden_counter == 15 else 0
        self.golden_low  = 1 if self.golden_counter == 0  else 0

        if self.t_score.count == self.golden_counter and self.t_score.low == self.golden_low and self.t_score.high == self.golden_high:
            cocotb.log.info("Load Test Case Passed ")
            self.passed_test_cases += 1
        else:
            cocotb.log.info("Load Test Case Failed ")
            self.failed_test_cases += 1


    def down_test_case(self):
        self.down_test_cases +=  1 
        if (self.golden_counter == 0):
            self.golden_counter = 15 
            self.golden_high = 1 if self.golden_counter == 15 else 0
            self.golden_low  = 1 if self.golden_counter == 0  else 0
        else :
            self.golden_counter -=1
            self.golden_high = 1 if self.golden_counter == 15 else 0
            self.golden_low  = 1 if self.golden_counter == 0  else 0

        if self.t_score.count == self.golden_counter and self.t_score.low == self.golden_low and self.t_score.high == self.golden_high:
            cocotb.log.info("Down Test Case Passed ")
            self.passed_test_cases += 1
        else:
            cocotb.log.info("Down Test Case Failed ")
            self.failed_test_cases += 1

    def up_test_case(self):
        self.up_test_cases += 1
        if (self.golden_counter == 15):
            self.golden_counter = 0 
            self.golden_high = 1 if self.golden_counter == 15 else 0
            self.golden_low  = 1 if self.golden_counter == 0  else 0
        else :
            self.golden_counter +=1
            self.golden_high = 1 if self.golden_counter == 15 else 0
            self.golden_low  = 1 if self.golden_counter == 0  else 0

        if self.t_score.count == self.golden_counter and self.t_score.low == self.golden_low and self.t_score.high == self.golden_high:
            cocotb.log.info("Down Test Case Passed ")
            self.passed_test_cases += 1
        else:
            cocotb.log.info("Down Test Case Failed ")
            self.failed_test_cases += 1

    def idle_test_case(self):
        self.idle_test_cases += 1 
        if self.t_score.count == self.golden_counter and self.t_score.low == self.golden_low and self.t_score.high == self.golden_high:
            cocotb.log.info("Down Test Case Passed ")
            self.passed_test_cases += 1
        else:
            cocotb.log.info("Down Test Case Failed ")
            self.failed_test_cases += 1
    
    
    def report_test_cases(self):
        self.total_test_cases = self.passed_test_cases + self.failed_test_cases
        cocotb.log.info("The Number Of Total  Test Cases is :  " + str(self.total_test_cases)) 
        cocotb.log.info("The Number Of Rest   Test Cases is :  " + str(self.reset_test_cases))    
        cocotb.log.info("The Number Of Load   Test Cases is :  " + str(self.load_test_cases))  
        cocotb.log.info("The Number Of up     Test Cases is :  " + str(self.up_test_cases)) 
        cocotb.log.info("The Number Of down   Test Cases is :  " + str(self.down_test_cases))  
        cocotb.log.info("The Number Of idle   Test Cases is :  " + str(self.idle_test_cases))     
        cocotb.log.info("The Number Of Passed Test Cases is :  " + str(self.passed_test_cases)) 
        cocotb.log.info("The Number Of Failed Test Cases is :  " + str(self.failed_test_cases))       


                