from cocotb.triggers import *
from transactions import *
import cocotb
import cocotb.queue

class monitor ():
   t_monitor    = transactions()
   mon_mail_s   = cocotb.queue.Queue()
   mon_mail_su  = cocotb.queue.Queue()
   def __int__(self,name = "MONITOR"):
        self.name= name
      
   async def run_monitor (self,dut_monitor):
      cocotb.log.info("[Monitor] STARTING.")
      await RisingEdge(dut_monitor.clk)
      while(True):
        cocotb.log.info("[Monitor] waiting for item ...")
        await RisingEdge(dut_monitor.clk)
        await ReadOnly()
        self.t_monitor.rst           =   int(dut_monitor.rst)
        self.t_monitor.load          =   int(dut_monitor.load)    
        self.t_monitor.up            =   int(dut_monitor.up.value)    
        self.t_monitor.down          =   int(dut_monitor.down.value)
        self.t_monitor.In            =   int(dut_monitor.In.value)
        self.t_monitor.high          =   int(dut_monitor.high.value)
        self.t_monitor.low           =   int(dut_monitor.low.value)
        self.t_monitor.count         =   int(dut_monitor.count.value)
        self.t_monitor.display("MONITOR")  
        await self.mon_mail_s.put(self.t_monitor)  
        await self.mon_mail_su.put(self.t_monitor)
