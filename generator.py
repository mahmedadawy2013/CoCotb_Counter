from transactions import * 
from cocotb.triggers import * 
import cocotb
import cocotb.queue


class generator() :
   
    def __init__(self ,join_any,name = "GENERATOR"): 
       self.name             = name
       self.t_gen            = transactions()
       self.gen_mail         = cocotb.queue.Queue()
       self.gen_handover     = Event(name=None) 
       self.join_any         = join_any

    async def run_generator (self,dut_generator) : 
        iteration_number = 1000 ; 
        for i in range(iteration_number): 
            self.gen_handover.clear() 
            if (i == 0 ) :
                await self.reset_sequence()

            elif (i == 1) :
                await self.overflow_up_sequence()

            elif (i == 2) :
               await self.overflow_down_sequence()
            
            else :
                await self.normal_sequence() 


        await FallingEdge(dut_generator.clk)
        self.join_any.set()

    """ ************* **************** Sequence Generation ****************** ***************"""
    async def reset_sequence (self):
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst: rst == 0  )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ") 
        await self.gen_mail.put(self.t_gen)  
        await self.gen_handover.wait()      

    async def overflow_up_sequence(self) :
        self.gen_handover.clear() 
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst :rst == 1 ,lambda load :load == 1,lambda In :In == 15 )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ")
        await self.gen_mail.put(self.t_gen) 
        await self.gen_handover.wait()

        self.gen_handover.clear() 
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst :rst == 1 ,lambda load :load == 0,lambda down :down == 0 ,lambda up :up == 1 )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ")
        await self.gen_mail.put(self.t_gen) 
        await self.gen_handover.wait()


    async def overflow_down_sequence(self) :
        self.gen_handover.clear() 
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst :rst == 1 , lambda load :load == 1 , lambda In :In == 0 )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ")
        await self.gen_mail.put(self.t_gen) 
        await self.gen_handover.wait()

        self.gen_handover.clear() 
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst :rst == 1 ,lambda load :load == 0,lambda down :down == 1 ,lambda up :up == 0 )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ")
        await self.gen_mail.put(self.t_gen) 
        await self.gen_handover.wait()
    
    async def normal_sequence (self):
        self.t_gen = transactions()
        self.t_gen.randomize_with(lambda rst: rst == 1  )
        self.t_gen.display("GENERATOR")
        cocotb.log.info("[Generator] Sending To The Driver..... ") 
        await self.gen_mail.put(self.t_gen)  
        await self.gen_handover.wait()    
