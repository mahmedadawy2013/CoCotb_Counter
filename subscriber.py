from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue
from cocotb_coverage.coverage import *


@CoverPoint("top.up"      , vname="up"      , bins=[(0,1),(1,1)]  , bins_labels = ["up_0_to_1"   , "up_1_to_0", ]       ) 
@CoverPoint("top.down"    , vname="down"    , bins=[(0,1),(1,1)]  , bins_labels = ["down_0_to_1" , "down_1_to_0", ]     ) 
@CoverPoint("top.count"   , vname="count"   , bins=list(range(0, 16 ))) 
@CoverPoint("top.count"   , vname="count"   , bins=[(15,0),(0,15)], bins_labels = ["count_15_to_0" , "count_0_to_15", ] ) 
@CoverCross(
  "top.count",
  items = ["top.up", "top.down" ,"top.count"],
  ign_bins = [ ("up_0_to_1", "count_0_to_15"), ("up_1_to_0", "count_0_to_15") ,("down_0_to_1", "count_15_to_0"),\
               ("down_1_to_0", "count_15_to_0") , ("down_0_to_1" ,"up_0_to_1" ) ,("down_0_to_1" ,"up_1_to_0" ) , ]                                                          
)
def sample(up,down,count):
    pass

class subscriber() :
   
    def __init__(self ,name = "SUBSCRIBER"): 
       self.name               = name
       self.t_sub              = transactions()
       self.sub_mail           = cocotb.queue.Queue()

    async def run_subscriber (self) : 
        while(True):
            self.t_sub = transactions()
            cocotb.log.info("[subscriber] receiving from monitor..... ") 
            self.t_sub = await self.sub_mail.get() 
            self.t_sub.display("SUBSCRIBER")
            cocotb.log.info("[subscriber] receiving from monitor..... ") 
            sample(self.t_sub.up,self.t_sub.down,self.t_sub.count)

    def coverage_report(self):
        count       = coverage_db["top.count"].coverage          
        count_p     = coverage_db["top.count"].cover_percentage  
        cocotb.log.info("The count   coverage is : "+str(count))
        cocotb.log.info("The count_p coverage percentage is : "+str(count_p))


                