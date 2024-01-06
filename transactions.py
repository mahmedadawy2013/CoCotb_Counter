import cocotb 
import random
from cocotb_coverage.crv import *

"""***************************************************************************************************************
* Check This Important Link For Coverage And Constraints 
https://cocotb-coverage.readthedocs.io/en/latest/reference.html#cocotb_coverage.crv.Randomized.randomize_with

* This The Source Code With Examples 
https://cocotb-coverage.readthedocs.io/en/latest/_modules/cocotb_coverage/crv.html#Randomized.add_constraint

* Check This Link For Extra Information about Constraints 
https://cocotb-coverage.readthedocs.io/en/latest/introduc

tion.html#constrained-random-verification-features-in-systemverilog
* Another link but it is so important 
https://cocotb-coverage.readthedocs.io/en/latest/tutorials.html

*****************************************************************************************************************"""
class  transactions(Randomized):
    def __init__(self ,name = "TRANSACTIONS"):
        Randomized.__init__(self)
        self.name = name
        self.rst         =  0  
        self.load        =  0
        self.up          =  0
        self.down        =  0
        self.In          =  0
        self.high        =  0
        self.low         =  0
        self.count       =  0

        self.add_rand("rst"        , list(range(0,2)     )   ) 
        self.add_rand("load"       , list(range(0,2)     )   ) 
        self.add_rand("up"         , list(range(0,2)     )   )
        self.add_rand("down"       , list(range(0,2)     )   )
        self.add_rand("In"         , list(range(0,16)    )   )

    def display(self,name = "TRANSACTION"):
        cocotb.log.info("******************"+str(name)+"*******************")
        cocotb.log.info("the Value of rst        is   " + str(self.rst   ))
        cocotb.log.info("the Value of load       is   " + str(self.load  ))
        cocotb.log.info("the Value of up         is   " + str(self.up    ))
        cocotb.log.info("the Value of down       is   " + str(self.down  ))
        cocotb.log.info("the Value of In         is   " + str(self.In    ))
        cocotb.log.info("the Value of high       is   " + str(self.high  ))
        cocotb.log.info("the Value of low        is   " + str(self.low   ))
        cocotb.log.info("the Value of count      is   " + str(self.count ))
        cocotb.log.info("**************************************************")


